#!/usr/bin/env python3
"""Generate the shared hub nodes in `_shared/` from the organization records.

Every hub's membership list is derived, never hand-maintained: this script reads
the `x-civic` frontmatter of each `organizations/synthetic-*/README.md` and rewrites

  * `_shared/pcs/<CODE>.md`  — one node per PCS code in a REQUIRED facet
                               (subject, population, org_type), created if absent
  * the `<!-- GENERATED -->` block in each `_shared/ntee/`, `_shared/sdg/`
    and `_shared/situations/` node — the OPTIONAL enrichment layers
  * the `index.md` listing in `_shared/` and each of its subdirectories

PCS titles and scope notes come from `_shared/pcs/pcs-codes.json`, an attributed
subset vendored by `scripts/extract_pcs.py`. Nothing here reaches the network.

    python3 scripts/build_hubs.py            # rewrite the hubs
    python3 scripts/build_hubs.py --check    # fail if anything is out of date
"""
import glob
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit('PyYAML is required: pip install -r requirements.txt')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARED = os.path.join(ROOT, '_shared')
# Every org bundle lives under this one directory.
ORGS_DIR = 'organizations'
PCS_JSON = os.path.join(SHARED, 'pcs', 'pcs-codes.json')
FM = re.compile(r'^---\n(.*?)\n---\n?(.*)$', re.S)
GEN = re.compile(r'(<!-- GENERATED[^>]*-->\n)(.*?)(\n<!-- /GENERATED -->)', re.S)

FACET_LABEL = {'subject': 'Subject', 'population': 'Population', 'org_type': 'OrgType'}
FACET_MEANS = {
    'subject': 'what an organization does',
    'population': 'who an organization serves',
    'org_type': 'what kind of organization it is',
}
ATTRIB = ('*Title and scope note (c) [Candid](https://taxonomy.candid.org), from the Philanthropy '
          'Classification System, used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) '
          'and unmodified.*')


def split(text):
    m = FM.match(text)
    return (m.group(1), m.group(2)) if m else (None, text)


def load_orgs():
    orgs = []
    for p in sorted(glob.glob(os.path.join(ROOT, ORGS_DIR, 'synthetic-*', 'README.md'))):
        fm, _ = split(open(p, encoding='utf-8').read())
        d = yaml.safe_load(fm) or {}
        xc = d.get('x-civic') or {}
        orgs.append({
            'slug': os.path.basename(os.path.dirname(p)),
            'title': d.get('title', ''),
            'description': d.get('description', ''),
            'subject': xc.get('subject') or [],
            'population': xc.get('population') or [],
            'org_type': [xc['org_type']] if xc.get('org_type') else [],
            'country': xc.get('registration_country', ''),
            'ntee': [str(x) for x in (xc.get('ntee') or [])],
            'sdg': [str(x) for x in (xc.get('sdg') or [])],
            'situation': xc.get('situation'),
        })
    return orgs


def short(org):
    """A one-line member description: place if known, else the org description."""
    d = org['description'] or ''
    d = re.sub(r'^A fabricated\s*', '', d).rstrip('.')
    return d[:110]


def member_lines(orgs, depth=2):
    up = '../' * depth
    out = []
    for o in sorted(orgs, key=lambda x: x['title']):
        out.append(f'- [{o["title"]}]({up}{ORGS_DIR}/{o["slug"]}/README.md) — {short(o)}')
    return '\n'.join(out) if out else '*No organization in this collection carries this code.*'


# --------------------------------------------------------------------------- #
def parent_chain(code):
    """PCS codes nest in the digits: SS030601 -> SS030600 -> SS030000 -> SS000000."""
    prefix, digits = code[:2], code[2:]
    out = []
    for keep in (4, 2, 0):
        p = prefix + digits[:keep] + '0' * (6 - keep)
        if p != code and p not in out:
            out.append(p)
    return out


def pcs_hub(code, meta, members, existing):
    facet = meta['facet']
    title = meta['title']
    chain = ' › '.join(meta['path']) if meta.get('path') else title
    former = meta.get('former_ntee')
    note = (meta.get('scope_note') or '').strip()

    fm = [
        'type: classification',
        f'title: {json.dumps(f"{code} — {title}", ensure_ascii=False)}',
        f'description: {json.dumps(f"Candid PCS {FACET_LABEL[facet]} code {code} — {title}.", ensure_ascii=False)}',
        'resource: https://taxonomy.candid.org',
        f'aliases: {json.dumps([code, f"pcs:{code}", title], ensure_ascii=False)}',
        f'tags: ["hub", "pcs", "classification", "{facet}"]',
        'synthetic: false',
        'status: stable',
        'generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }',
        f'id: pcs:{code}',
        'scheme: PCS',
        'scheme_authority: Candid',
        'scheme_uri: https://taxonomy.candid.org',
        f'facet: {FACET_LABEL[facet]}',
    ]
    if former:
        fm.append(f'former_ntee: {json.dumps(former)}')
    fm += ['x-civic:', '  profile: civic/0.6']
    fm.append(f'  {facet}: {code}' if facet == 'org_type' else f'  {facet}: ["{code}"]')

    body = [f'# {code} — {title}', '']
    body.append('> **The code on this page is real.** It is a genuine Candid PCS code, unaltered. '
                '**Every organization listed under Members is fabricated** — see the '
                '[collection README](../../README.md).')
    body.append('')
    body.append(f'A **shared classification node**. Organizations carry `x-civic.{facet}: [{code}]` in their '
                f'required frontmatter; the description lives here once; **the Members list below is generated '
                f'from those edges** by `scripts/build_hubs.py`.')
    body.append('')
    body.append(f'## What this code means')
    body.append('')
    if note:
        body.append(note)
        body.append('')
    body.append(f'**Facet:** {FACET_LABEL[facet]} — *{FACET_MEANS[facet]}*.')
    parents = parent_chain(code)
    if parents:
        body.append('  \n**Broader codes:** ' + ' ← '.join(f'`{c}`' for c in parents) +
                    ' — PCS codes nest structurally, so a query can roll a leaf up to its parent.')
    if former:
        body.append(f'  \n**Former NTEE/GCS code:** `{former}` — this profile crosswalked the US organizations\' '
                    f'NTEE codes to PCS through the taxonomy\'s own former-code column rather than by hand.')
    body.append('')
    body.append(ATTRIB)
    body.append('')
    body.append('## Members')
    body.append(f'<!-- GENERATED from x-civic.{facet} — do not edit by hand; run scripts/build_hubs.py -->')
    body.append(members)
    body.append('<!-- /GENERATED -->')
    body.append('')
    return '---\n' + '\n'.join(fm) + '\n---\n\n' + '\n'.join(body)


def upgrade_frontmatter(fm_text, kind):
    """Bring an existing _shared node's frontmatter to OKF v0.2 + civic/0.6."""
    d = yaml.safe_load(fm_text) or {}
    d.pop('okf_version', None)
    d.pop('synthetic_collection', None)
    lines = [f'type: {d.get("type", "classification")}']
    for k in ('title', 'description'):
        if d.get(k):
            lines.append(f'{k}: {json.dumps(d[k], ensure_ascii=False)}')
    if d.get('scheme_uri'):
        lines.append(f'resource: {d["scheme_uri"]}')
    if d.get('aliases'):
        lines.append(f'aliases: {json.dumps(d["aliases"], ensure_ascii=False)}')
    if d.get('tags'):
        lines.append(f'tags: {json.dumps([t for t in d["tags"] if t], ensure_ascii=False)}')
    lines.append('synthetic: false')
    lines.append('status: stable')
    lines.append('generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }')
    for k in ('id', 'scheme', 'scheme_authority', 'scheme_uri',
              'country', 'subdivision', 'locality'):
        if d.get(k):
            lines.append(f'{k}: {json.dumps(d[k], ensure_ascii=False)}')
    lines += ['x-civic:', '  profile: civic/0.6']
    return '\n'.join(lines)


def write(path, content, check, changed):
    old = open(path, encoding='utf-8').read() if os.path.exists(path) else None
    if old == content:
        return
    changed.append(os.path.relpath(path, ROOT))
    if not check:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(content)


# --------------------------------------------------------------------------- #
def main():
    check = '--check' in sys.argv
    changed = []
    orgs = load_orgs()
    pcs = json.load(open(PCS_JSON, encoding='utf-8'))['codes']

    # ---- required layer: one PCS node per code in use ----
    used = {'subject': set(), 'population': set(), 'org_type': set()}
    for o in orgs:
        for facet in used:
            used[facet].update(o[facet])

    for facet, codes in used.items():
        for code in sorted(codes):
            meta = pcs.get(code)
            if meta is None:
                print(f'WARNING: {code} missing from pcs-codes.json; run scripts/extract_pcs.py')
                continue
            members = member_lines([o for o in orgs if code in o[facet]])
            p = os.path.join(SHARED, 'pcs', f'{code}.md')
            existing = open(p, encoding='utf-8').read() if os.path.exists(p) else None
            write(p, pcs_hub(code, meta, members, existing), check, changed)

    # ---- optional layers: refresh the GENERATED block in place ----
    for kind, field in (('ntee', 'ntee'), ('sdg', 'sdg'), ('situations', 'situation')):
        for p in sorted(glob.glob(os.path.join(SHARED, kind, '*.md'))):
            if os.path.basename(p) == 'index.md':
                continue
            text = open(p, encoding='utf-8').read()
            fm_text, body = split(text)
            if fm_text is None:
                continue
            d = yaml.safe_load(fm_text) or {}
            key = os.path.basename(p)[:-3]
            if kind == 'ntee':
                mine = [o for o in orgs if key in o['ntee']]
            elif kind == 'sdg':
                num = str(int(key.split('-')[1]))
                mine = [o for o in orgs if num in o['sdg']]
            else:
                mine = [o for o in orgs if o['situation'] == key]
            block = member_lines(mine)
            header = ('<!-- GENERATED from the organizations\' x-civic frontmatter '
                      '— do not edit by hand; run scripts/build_hubs.py -->\n')
            new_body = GEN.sub(lambda m: header + block + m.group(3), body, count=1)
            new_fm = upgrade_frontmatter(fm_text, kind)
            write(p, '---\n' + new_fm + '\n---\n\n' + new_body.lstrip('\n'), check, changed)

    # ---- index listings (reserved: no frontmatter, OKF §8) ----
    write(os.path.join(SHARED, 'pcs', 'index.md'), pcs_index(used, pcs, orgs), check, changed)
    for kind, heading, blurb in (
        ('ntee', 'NTEE classification hubs',
         'US IRS classification. An **optional** enrichment layer that reaches only the US organizations.'),
        ('sdg', 'SDG classification hubs',
         'UN Sustainable Development Goals. An **optional** enrichment layer that reaches every organization.'),
        ('situations', 'Situations (places)',
         'Place nodes. Community context attaches **here, once for the place**, not inside each organization.'),
    ):
        write(os.path.join(SHARED, kind, 'index.md'),
              simple_index(kind, heading, blurb, orgs), check, changed)
    write(os.path.join(SHARED, 'index.md'), shared_index(used, orgs), check, changed)

    if check:
        if changed:
            print(f'{len(changed)} hub file(s) out of date:')
            for c in changed:
                print('  -', c)
            return 1
        print('hubs are up to date.')
        return 0
    print(f'wrote {len(changed)} hub file(s).' if changed else 'hubs already up to date.')
    return 0


def pcs_index(used, pcs, orgs):
    out = ['# PCS classification hubs — the required layer', '',
           '**⚠ Part of a synthetic collection. Every organization listed in these hubs is fabricated** — '
           'see the [collection README](../../README.md). **The codes themselves are real.**', '',
           "Candid's **Philanthropy Classification System** is the controlled vocabulary that `civic/0.6` "
           'requires. Three of its five facets carry the profile\'s three required classification keys:', '',
           '| Facet | `x-civic` key | Answers | Nodes here |', '|---|---|---|---|',
           f'| Subject | `subject` | what an organization does | {len(used["subject"])} |',
           f'| Population | `population` | who it serves | {len(used["population"])} |',
           f'| OrgType | `org_type` | what kind of organization it is | {len(used["org_type"])} |', '',
           'PCS also has **Strategy** and **Transaction** facets, which this collection does not yet use; they are '
           'the natural vocabulary for describing how support and money flow between organizations.', '',
           '## This folder used to be empty, and the reason it no longer is', '',
           'Earlier versions of this collection shipped `_shared/pcs/` deliberately empty, because assigning codes '
           'from memory would have put invented identifiers into a real vocabulary\'s namespace. That reasoning was '
           'right and it has been satisfied rather than abandoned: every code below was read out of Candid\'s '
           'published 2024 taxonomy, and the US organizations\' codes were **crosswalked mechanically** through the '
           'taxonomy\'s own former-NTEE column rather than guessed. Titles and scope notes are Candid\'s, unmodified. '
           'The subset in use is vendored as [`pcs-codes.json`](pcs-codes.json) so nothing here needs the network.', '',
           '**Nothing was fabricated to fill this folder.** Where a code genuinely did not fit — the Colombian '
           '*corporación* and the Kenyan trust have no PCS OrgType level-2 equivalent — the level-1 parent is used '
           'deliberately and the record says so, which is still better than forcing a closer-looking child.', '',
           '## PCS reaches all fifteen; NTEE reaches twelve', '',
           'This is the finding that made PCS the required layer. NTEE is maintained by the US IRS and cannot apply '
           'to the Polish, Colombian, or Kenyan organizations — an NTEE rollup silently covers 80% of this '
           'collection, with no error and no null. PCS Subject and Population classify *activity and people* rather '
           'than tax status, so they apply everywhere.', '',
           'One honest caveat: **PCS is not uniformly jurisdiction-neutral.** Candid\'s own scope note for '
           '`EA040000` (Public charities) describes US 501(c) organizations specifically. The generic parents are '
           'neutral, which is why the two non-US organizations without a matching form sit at `EA000000`.', '']
    for facet in ('subject', 'population', 'org_type'):
        out.append(f'## {FACET_LABEL[facet]} — `{facet}`')
        out.append('')
        for code in sorted(used[facet]):
            meta = pcs.get(code)
            if not meta:
                continue
            n = sum(1 for o in orgs if code in o[facet])
            former = f' *(← NTEE {meta["former_ntee"]})*' if meta.get('former_ntee') else ''
            out.append(f'* [{code} — {meta["title"]}]({code}.md) - {n} member(s){former}')
        out.append('')
    out.append('*Every Members list in this folder is generated by `scripts/build_hubs.py` from the organizations\' '
               'required frontmatter. Do not edit them by hand.*')
    out.append('')
    return '\n'.join(out)


def simple_index(kind, heading, blurb, orgs):
    out = [f'# {heading}', '',
           '**⚠ Part of a synthetic collection. Every organization listed in these nodes is fabricated** — '
           'see the [collection README](../../README.md).', '', blurb, '']
    if kind == 'ntee':
        out += ['Superseded as the primary classification by [PCS](../pcs/index.md), which is what `civic/0.6` '
                'requires and which reaches all fifteen organizations. These nodes are kept because the '
                'NTEE→PCS crosswalk is worth being able to see from both ends.', '']
    if kind == 'sdg':
        out += ['SDG reaches every organization, including the three outside the United States, but it is **coarse** '
                '— a neighbourhood food shelf and national agricultural policy both sit under Goal 2. Complete '
                'coverage and useful granularity are in tension, which is why the required layer is '
                '[PCS](../pcs/index.md) and this one is optional.', '']
    if kind == 'situations':
        out += ['### The strongest argument in this collection', '',
                '[Letcher County, Kentucky](US-KY-letcher.md) hosts two organizations in unrelated sectors — a rural '
                'clinic and a workforce training organization — and **the same community-level fact defeated a '
                'program at each of them.** The county\'s broadband availability killed the clinic\'s telehealth and '
                'undermines the workforce organization\'s remote-work track.', '',
                '**One cause. Two sectors. Two organizations. One address.** Store connectivity as an '
                'organizational attribute and you record two independent technology weaknesses and miss that there '
                'is a single problem belonging to the county.', '',
                '### Why the indicator sections are stubs', '',
                'Every node carries a stub for community indicators rather than fabricated statistics, and names the '
                'authoritative source that would populate it. The organizations here are invented and labelled as '
                'such; **the places are real.** A synthetic organization cannot be mistaken for real. A synthetic '
                'statistic about a real county can. Note that the source authority differs by country — US Census '
                'ACS, GUS in Poland, DANE in Colombia, KNBS in Kenya — so "community context" is not one uniform '
                'comparable layer.', '']
    out += ['## Contents', '']
    files = sorted(glob.glob(os.path.join(SHARED, kind, '*.md')))
    for p in files:
        b = os.path.basename(p)
        if b == 'index.md':
            continue
        fm, _ = split(open(p, encoding='utf-8').read())
        d = yaml.safe_load(fm) if fm else {}
        key = b[:-3]
        if kind == 'ntee':
            n = sum(1 for o in orgs if key in o['ntee'])
        elif kind == 'sdg':
            num = str(int(key.split('-')[1]))
            n = sum(1 for o in orgs if num in o['sdg'])
        else:
            n = sum(1 for o in orgs if o['situation'] == key)
        out.append(f'* [{(d or {}).get("title", key)}]({b}) - {n} organization(s)')
    out += ['', '*Membership lists are generated by `scripts/build_hubs.py` from the organizations\' frontmatter.*', '']
    return '\n'.join(out)


def shared_index(used, orgs):
    return '\n'.join([
        '# Shared nodes', '',
        '**⚠ Part of a synthetic collection. Every organization listed in these nodes is fabricated** — '
        'see the [collection README](../README.md). The classification codes and the places are real.', '',
        'Classification and place nodes that the fifteen organization bundles link to. Authored once here and '
        'shared across every bundle, so a hub\'s membership list has real entries and a place node hosts '
        'organizations from different program areas.', '',
        '## One required layer, two optional ones', '',
        '| Folder | Status | Reaches | What it is |', '|---|---|---|---|',
        f'| [pcs/](pcs/index.md) | **required** | 15 of 15 | Candid PCS — the vocabulary `civic/0.6` requires, '
        f'{len(used["subject"])} subject + {len(used["population"])} population + {len(used["org_type"])} org-type nodes |',
        '| [sdg/](sdg/index.md) | optional | 15 of 15 | UN Sustainable Development Goals — global but coarse |',
        '| [ntee/](ntee/index.md) | optional | 12 of 15 | US IRS classification — cannot reach the three '
        'non-US organizations |',
        '| [situations/](situations/index.md) | optional | 15 of 15 | Places. Community context lives here, '
        'once per place |', '',
        '**A bundle is conformant carrying only the PCS codes.** Everything else in this folder is enrichment that '
        'makes the graph worth querying.', '',
        '## The membership lists are generated', '',
        'Every `<!-- GENERATED -->` block in this folder is rebuilt from the organizations\' own frontmatter by '
        '`scripts/build_hubs.py`. Earlier versions of this collection maintained them by hand and documented the '
        'drift as a known problem; `scripts/validate.py` now runs `--check` and fails if a list is stale, so the '
        'two directions cannot disagree.', '',
        '## What a situation node is for', '',
        'A **situation** describes a place, not an organization. Community context — population, income, health '
        'outcomes, connectivity — is stored once for the place, so it is not copied into every organization '
        'operating there. See [situations/](situations/index.md) for the clearest demonstration this collection '
        'contains.', '',
    ])


if __name__ == '__main__':
    sys.exit(main())
