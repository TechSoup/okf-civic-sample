#!/usr/bin/env python3
"""Validate this collection against OKF v0.2 and the civic/0.6 profile.

Two independent conformance levels, checked separately, because they are not the
same claim:

  CORE OKF v0.2 (§11) — the only hard requirements the format itself makes:
    1. every non-reserved `.md` file has a parseable YAML frontmatter block;
    2. every frontmatter block has a non-empty `type`;
    3. `index.md` and `log.md` follow §8 and §9 when present.
  Plus the v0.2 field families where used: `generated`/`verified` (§5.2),
  `status` (§5.4), `sources` (§5.1), and the retirement of `timestamp` (§13.1).

  civic/0.6 — a promise a record opts into by declaring `x-civic.profile`.
  A record with `type: org` must carry five keys and no more:
    profile, subject, population, org_type, registration_country
  `subject`/`population`/`org_type` must resolve against the vendored Candid PCS
  subset; `registration_country` must be an ISO 3166-1 alpha-2 code.

Nothing under `x-civic` can make a bundle non-conformant with core OKF: §11
requires a consumer to tolerate unknown keys. Everything optional is reported,
never failed.

    python3 scripts/validate.py             # validate the collection
    python3 scripts/validate.py --terms     # list the emergent (unresolved) terms
    python3 scripts/validate.py --self-test # confirm the fixtures are rejected
"""
import argparse
import datetime
import glob
import json
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.exit('PyYAML is required: pip install -r requirements.txt')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = 'civic/0.6'
REQUIRED_ORG_KEYS = ['profile', 'subject', 'population', 'org_type', 'registration_country']
STATUS_VALUES = {'draft', 'stable', 'deprecated'}
# The only asserted org-to-org edges civic/0.6 defines. Kept in step with
# schemas/civic_schema.json and docs/civic-profile.md.
RELATION_TYPES = {'partners_with', 'coalition_with', 'learn_with'}
# Every org bundle lives under this one directory. Relation targets are slugs
# relative to it, not paths.
ORGS_DIR = 'organizations'
RESERVED = {'index.md', 'log.md'}
PCS_JSON = os.path.join(ROOT, '_shared', 'pcs', 'pcs-codes.json')
FIXTURE_DIR = os.path.join(ROOT, 'schemas', 'fixtures')
# Repo-level project files, not knowledge concepts. OKF only reserves index.md
# and log.md; these are excluded because they document the repository rather
# than describing anything in it.
NOT_CONCEPTS = {'CONTRIBUTING.md', 'NOTICE.md', 'CHANGELOG.md'}

FM = re.compile(r'^---\n(.*?)\n---\n?(.*)$', re.S)
MD_LINK = re.compile(r'(?<!\!)\[[^\]]*\]\(([^)\s]+?)(?:\s+"[^"]*")?\)')
WIKILINK = re.compile(r'\[\[([^\]]+)\]\]')
CODE_SPAN = re.compile(r'`[^`\n]*`')
CODE_FENCE = re.compile(r'^```.*?^```', re.S | re.M)
FOOTNOTE_USE = re.compile(r'\[\^([^\]]+)\]')
FOOTNOTE_DEF = re.compile(r'^\[\^([^\]]+)\]:', re.M)

# ISO 3166-1 alpha-2, current assignments.
ISO_3166_1 = set("""AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ
BL BM BN BO BQ BR BS BT BV BW BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ
DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT
GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY
KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX
MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS
RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN
TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW""".split())


def split(text):
    m = FM.match(text)
    return (m.group(1), m.group(2)) if m else (None, text)


def strip_code(body):
    """Remove fenced blocks and inline spans before scanning for links or
    footnotes. Documentation quotes regexes and YAML that would otherwise be
    read as markup."""
    return CODE_SPAN.sub('', CODE_FENCE.sub('', body))


def rel(p):
    return os.path.relpath(p, ROOT)


def discover():
    """Every markdown file in the collection, excluding tooling directories."""
    out = []
    for dp, dns, fs in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in ('.git', 'venv', '.obsidian', 'fixtures')]
        for f in sorted(fs):
            if f.endswith('.md') and not (dp == ROOT and f in NOT_CONCEPTS):
                out.append(os.path.join(dp, f))
    return sorted(out)


def load_pcs():
    if not os.path.exists(PCS_JSON):
        return None
    return json.load(open(PCS_JSON, encoding='utf-8'))['codes']


# --------------------------------------------------------------------------- #
def as_date(value):
    """A YAML date, a datetime, or an ISO string. None if it is none of those."""
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    try:
        return datetime.date.fromisoformat(str(value))
    except ValueError:
        return None


def check_file(p, pcs, terms, stale=None):
    """Return (core_errors, profile_errors)."""
    core, prof = [], []
    base = os.path.basename(p)
    text = open(p, encoding='utf-8').read()
    fm_text, body = split(text)

    # ---------- reserved files (OKF §8, §9; §11 rule 3) ----------
    if base == 'index.md':
        is_bundle_root = os.path.dirname(p) != ROOT and os.path.exists(
            os.path.join(os.path.dirname(p), 'README.md'))
        if fm_text is not None:
            d = yaml.safe_load(fm_text) or {}
            extra = [k for k in d if k != 'okf_version']
            if extra:
                core.append(f'index.md may carry only `okf_version` (§8); found {extra}')
            elif d.get('okf_version') != '0.2':
                core.append(f'okf_version is {d.get("okf_version")!r}, expected "0.2"')
        elif is_bundle_root:
            core.append('bundle-root index.md should declare okf_version: "0.2" (§12)')
        check_links(p, body, core, terms)
        return core, prof

    if base == 'log.md':
        if fm_text is not None:
            core.append('log.md is a reserved file and carries no frontmatter (§3.1, §9)')
        heads = re.findall(r'^## (.+)$', body, re.M)
        if not heads:
            core.append('log.md needs at least one `## YYYY-MM-DD` heading (§9)')
        bad = [h.strip() for h in heads if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', h.strip())]
        if bad:
            core.append(f'log.md headings must be ISO 8601 dates (§9); found {bad}')
        check_links(p, body, core, terms)
        return core, prof

    # ---------- concept documents (§11 rules 1 and 2) ----------
    if fm_text is None:
        core.append('no parseable YAML frontmatter (§11.1)')
        return core, prof
    try:
        d = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        core.append(f'unparseable frontmatter: {e}')
        return core, prof
    if not isinstance(d, dict):
        core.append('frontmatter is not a mapping')
        return core, prof
    if not d.get('type'):
        core.append('missing non-empty `type` (§11.2)')

    # ---------- v0.2 field families ----------
    if 'timestamp' in d:
        core.append('`timestamp` is superseded by `generated.at` (§13.1)')
    if 'status' in d and d['status'] not in STATUS_VALUES:
        core.append(f'status {d["status"]!r} is not draft|stable|deprecated (§5.4)')
    g = d.get('generated')
    if g is not None:
        if not isinstance(g, dict) or not g.get('by'):
            core.append('`generated.by` is required within `generated` (§5.2)')
        elif not re.match(r'^(human:|process:)\S+|^\S+/\S+$', str(g['by'])):
            core.append(f'generated.by {g["by"]!r} does not follow the actor convention (§7)')
    v = d.get('verified')
    if v is not None:
        events = v if isinstance(v, list) else [v]
        for ev in events:
            if not isinstance(ev, dict) or not ev.get('by') or not ev.get('at'):
                core.append('each `verified` entry needs `by` and `at` (§5.2)')
        # A determination with no term cannot be aged, so freshness becomes
        # unanswerable rather than false. §5.5 pairs the two keys.
        if 'stale_after' not in d:
            core.append('`verified` without `stale_after` — a determination with no term '
                        'cannot be checked for freshness (§5.5)')

    # `stale_after` must be a real date. Whether it has *passed* is deliberately
    # not an error: this collection ships one deliberately-expired determination,
    # and expiry is a fact about today, not a defect in the record.
    if 'stale_after' in d:
        day = as_date(d['stale_after'])
        if day is None:
            core.append(f'stale_after {d["stale_after"]!r} is not an ISO 8601 date (§5.5)')
        elif stale is not None and day < datetime.date.today():
            stale[rel(p)] = day

    source_ids = set()
    for s in d.get('sources') or []:
        if not isinstance(s, dict):
            core.append('a `sources` entry is not a mapping (§5.1)')
            continue
        if not s.get('resource'):
            core.append('a `sources` entry lacks the required `resource` (§5.1)')
        if s.get('id'):
            source_ids.add(s['id'])

    used = set(FOOTNOTE_USE.findall(strip_code(body))) - set(FOOTNOTE_DEF.findall(body))
    used |= set(FOOTNOTE_USE.findall(strip_code(body)))
    for u in sorted(set(FOOTNOTE_USE.findall(strip_code(body)))):
        if u not in source_ids:
            core.append(f'footnote [^{u}] has no matching `sources[].id` (§5.1)')
    for u in sorted(set(FOOTNOTE_USE.findall(strip_code(body)))):
        if u not in set(FOOTNOTE_DEF.findall(body)):
            core.append(f'footnote [^{u}] is used but never defined')

    # ---------- civic/0.6 ----------
    xc = d.get('x-civic')
    if xc is not None:
        if not isinstance(xc, dict):
            prof.append('`x-civic` is not a mapping')
        else:
            if xc.get('profile') != PROFILE:
                prof.append(f'x-civic.profile must be {PROFILE!r} (found {xc.get("profile")!r})')
            if d.get('type') == 'org':
                for k in REQUIRED_ORG_KEYS:
                    if k not in xc:
                        prof.append(f'REQUIRED x-civic.{k} is missing from a `type: org` record')
            for key in ('subject', 'population'):
                val = xc.get(key)
                if val is None:
                    continue
                if not isinstance(val, list):
                    prof.append(f'x-civic.{key} must be a list of PCS codes')
                    continue
                for code in val:
                    verdict = check_pcs(code, key, pcs)
                    if verdict:
                        prof.append(verdict)
            if 'org_type' in xc:
                verdict = check_pcs(xc['org_type'], 'org_type', pcs)
                if verdict:
                    prof.append(verdict)
            rc = xc.get('registration_country')
            if rc is not None and str(rc) not in ISO_3166_1:
                prof.append(f'registration_country {rc!r} is not an ISO 3166-1 alpha-2 code')
            # Asserted edges only, and only the three types the profile defines.
            # Unenforced, this drifted once already: `learn-with` against its two
            # underscored siblings, in the data and the profile doc both.
            rels = xc.get('relations')
            if rels is not None:
                if not isinstance(rels, list):
                    prof.append('x-civic.relations must be a list')
                else:
                    for r in rels:
                        if not isinstance(r, dict) or not r.get('target') or not r.get('type'):
                            prof.append('each x-civic.relations entry needs `target` and `type`')
                            continue
                        if r['type'] not in RELATION_TYPES:
                            prof.append(f'relation type {r["type"]!r} is not '
                                        f'{"|".join(sorted(RELATION_TYPES))}')
                        target = os.path.join(ROOT, ORGS_DIR, str(r['target']), 'README.md')
                        if not os.path.exists(target):
                            prof.append(f'relation target {r["target"]!r} has no bundle README '
                                        f'under {ORGS_DIR}/')

    check_links(p, body, core, terms)
    return core, prof


def check_pcs(code, facet, pcs):
    if pcs is None:
        return None  # snapshot absent; skip rather than fail
    meta = pcs.get(str(code))
    if meta is None:
        return (f'{code} is not in the vendored Candid PCS subset — '
                f'run scripts/extract_pcs.py, or the code does not exist')
    if meta['facet'] != facet:
        return f'{code} is a PCS {meta["facet"]} code, used as {facet}'
    return None


def check_links(p, body, core, terms):
    """Markdown links must resolve. Unresolved wikilinks are emergent terms, not errors."""
    clean = strip_code(body)
    for href in MD_LINK.findall(clean):
        if href.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        target = href.split('#')[0]
        if not target:
            continue
        cand = os.path.normpath(os.path.join(os.path.dirname(p), target))
        if not os.path.exists(cand):
            core.append(f'markdown link does not resolve: {href}')
    for w in WIKILINK.findall(clean):
        term = w.split('|')[0].replace('\\', '').strip()
        cand = os.path.normpath(os.path.join(os.path.dirname(p), term + '.md'))
        if os.path.exists(cand):
            core.append(f'wikilink [[{term}]] resolves to a file; use a markdown link (§6.1)')
        else:
            terms.setdefault(term, set()).add(rel(p))


# --------------------------------------------------------------------------- #
def self_test():
    fixtures = sorted(glob.glob(os.path.join(FIXTURE_DIR, '*.md')))
    if not fixtures:
        print('self-test: no fixtures found under schemas/fixtures/')
        return False
    pcs = load_pcs()
    ok = True
    for p in fixtures:
        core, prof = check_file(p, pcs, {})
        n = len(core) + len(prof)
        if n:
            print(f'[rejected as expected] {rel(p)} — {n} error(s)')
            for e in (core + prof)[:4]:
                print(f'       - {e}')
        else:
            print(f'[UNEXPECTED PASS] {rel(p)} — fixture should have failed')
            ok = False
    print()
    print('self-test passed.' if ok else 'self-test FAILED.')
    return ok


def main():
    ap = argparse.ArgumentParser(description='Validate the collection.')
    ap.add_argument('--terms', action='store_true', help='list emergent (unresolved) terms')
    ap.add_argument('--self-test', action='store_true', help='confirm the fixtures are rejected')
    ap.add_argument('--quiet', action='store_true', help='only report failures')
    args = ap.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    pcs = load_pcs()
    if pcs is None:
        print('note: _shared/pcs/pcs-codes.json is absent; PCS codes will not be checked.\n')

    terms = {}
    stale = {}
    files = discover()
    core_fail, prof_fail = {}, {}
    for p in files:
        core, prof = check_file(p, pcs, terms, stale)
        if core:
            core_fail[rel(p)] = core
        if prof:
            prof_fail[rel(p)] = prof

    for p in sorted(map(rel, files)):
        mark = 'FAIL' if (p in core_fail or p in prof_fail) else 'ok'
        if not (args.quiet and mark == 'ok'):
            print(f'[{mark}] {p}')
            for e in core_fail.get(p, []):
                print(f'       - core: {e}')
            for e in prof_fail.get(p, []):
                print(f'       - civic/0.6: {e}')

    # hubs must be derived from current frontmatter, not stale
    hub = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'build_hubs.py'), '--check'],
                         capture_output=True, text=True)
    hubs_ok = hub.returncode == 0

    print()
    print(f'{len(files) - len(set(core_fail) | set(prof_fail))}/{len(files)} records passed.')
    print(f'  core OKF v0.2 : {len(files) - len(core_fail)}/{len(files)}')
    print(f'  civic/0.6     : {len(files) - len(prof_fail)}/{len(files)}')
    print(f'  generated hubs: {"up to date" if hubs_ok else "STALE — run scripts/build_hubs.py"}')
    if not hubs_ok:
        print(hub.stdout.strip())
    print(f'  emergent terms: {len(terms)} unresolved wikilink term(s) — informational, not errors')
    if stale:
        today = datetime.date.today()
        print(f'  expired determinations: {len(stale)} record(s) past `stale_after` '
              f'as of {today} — informational, not errors')
        for path, day in sorted(stale.items()):
            print(f'       - {path} — stale_after {day} ({(today - day).days} days ago)')
    else:
        print('  expired determinations: none past `stale_after`')

    if args.terms:
        print()
        print('Emergent terms (vocabulary the controlled facets do not carry):')
        for t, where in sorted(terms.items()):
            print(f'  [[{t}]] — {len(where)} record(s)')

    sys.exit(0 if (not core_fail and not prof_fail and hubs_ok) else 1)


if __name__ == '__main__':
    main()
