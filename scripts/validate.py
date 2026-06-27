#!/usr/bin/env python3
"""Validate okf-civic-sample records against the civic/0.4 profile.

Checks, per record:
  1. Frontmatter is present and parseable.
  2. Frontmatter conforms to schemas/civic_schema.json (core OKF + x-civic 0.4).
  3. Every record carrying an x-civic block declares profile == civic/0.4.
  4. Edge equivalence: the typed link-title edges in the prose (e.g.
     `"complements: ..."`, `"requires: ..."`) match x-civic.relations exactly.
  5. Reciprocity: if A links to B with a SYMMETRIC edge type, B links back to A
     with the same type. Directional edges (e.g. `requires`) are exempt — only
     the target's existence is checked.

Link titles per OKF issue #101 are the authoritative, human-edited source of
edges; x-civic.relations is a generated projection of them.

Usage:
    python3 scripts/validate.py            # validate every record (exit 1 on failure)
    python3 scripts/validate.py --write    # regenerate profile + relations in place
    python3 scripts/validate.py --self-test  # confirm the validator rejects the broken fixture
"""
import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install -r requirements.txt")

try:
    import json
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("jsonschema is required: pip install -r requirements.txt")

PROFILE = "civic/0.4"
EDGE_TYPES = {"alternative", "complements", "conflicts", "requires", "related", "learn-with"}
# Symmetric edges must be reciprocated (A->B implies B->A). Directional edges
# are one-way by nature (A requires B does not mean B requires A), so the
# reciprocity check is skipped for them — only target existence is verified.
DIRECTIONAL_EDGE_TYPES = {"requires"}
RELATION_TYPES = {"offer", "meal-site", "course"}  # types that carry a relations list

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORD_DIRS = ["offers", "resources", "docs"]
ROOT_RECORDS = ["index.md"]
SCHEMA_PATH = os.path.join(ROOT, "schemas", "civic_schema.json")
FIXTURE_DIR = os.path.join(ROOT, "schemas", "fixtures")

FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
# A markdown link that carries a title: [text](href "title")
TITLED_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\s+\"([^\"]*)\"\)")


# --------------------------------------------------------------------------- #
# discovery & parsing
# --------------------------------------------------------------------------- #
def discover_records():
    paths = [os.path.join(ROOT, p) for p in ROOT_RECORDS]
    for d in RECORD_DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            for f in sorted(files):
                if f.endswith(".md"):
                    paths.append(os.path.join(dirpath, f))
    return [p for p in paths if os.path.exists(p)]


def split_frontmatter(text):
    """Return (frontmatter_text, body) or (None, None) if no frontmatter."""
    m = FM_RE.match(text)
    if not m:
        return None, None
    return m.group(1), m.group(2)


def extract_edges(body):
    """Typed edges from prose link titles, in order of appearance.

    Only links whose title begins with a recognized edge token count;
    incidental links (no title, or an unrecognized token) are ignored.
    Returns a list of dicts: {target, type, note}.
    """
    edges = []
    for href, title in TITLED_LINK_RE.findall(body):
        if ":" not in title:
            continue
        token, _, note = title.partition(":")
        token = token.strip()
        if token not in EDGE_TYPES:
            continue
        edges.append({"target": href, "type": token, "note": note.strip()})
    return edges


def rel(path):
    return os.path.relpath(path, ROOT)


# --------------------------------------------------------------------------- #
# validation
# --------------------------------------------------------------------------- #
def load_records(paths):
    """Parse every record once. Returns (records, parse_errors).

    records: list of dicts {path, data, body, edges}.
    """
    records, errors = [], []
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        fm_text, body = split_frontmatter(text)
        if fm_text is None:
            errors.append((rel(p), "no YAML frontmatter found"))
            continue
        try:
            data = yaml.safe_load(fm_text)
        except yaml.YAMLError as e:
            errors.append((rel(p), f"unparseable frontmatter: {e}"))
            continue
        if not isinstance(data, dict):
            errors.append((rel(p), "frontmatter is not a mapping"))
            continue
        records.append({"path": p, "data": data, "body": body, "edges": extract_edges(body)})
    return records, errors


def validate(paths):
    """Return a dict path -> list of error strings (empty list == passed)."""
    with open(SCHEMA_PATH, encoding="utf-8") as fh:
        schema = json.load(fh)
    validator = Draft202012Validator(schema)

    records, parse_errors = load_records(paths)
    results = {rel(p): [] for p in paths}
    for path_rel, msg in parse_errors:
        results[path_rel].append(msg)

    # index records by repo-relative path for reciprocity lookups
    by_path = {rel(r["path"]): r for r in records}

    for r in records:
        path_rel = rel(r["path"])
        errs = results[path_rel]
        data, xc = r["data"], r["data"].get("x-civic")

        # 2. schema conformance
        for e in sorted(validator.iter_errors(data), key=lambda e: e.path):
            loc = "/".join(str(x) for x in e.path) or "(root)"
            errs.append(f"schema: {loc}: {e.message}")

        # 3. profile presence/value (clearer message than the schema alone)
        if isinstance(xc, dict) and xc.get("profile") != PROFILE:
            errs.append(f"x-civic.profile must be '{PROFILE}' (found {xc.get('profile')!r})")

        # 4. edge equivalence (prose link titles vs x-civic.relations)
        if isinstance(xc, dict) and data.get("type") in RELATION_TYPES:
            prose = {(e["target"], e["type"]) for e in r["edges"]}
            relations = xc.get("relations") or []
            declared = {(rl.get("target"), rl.get("type")) for rl in relations if isinstance(rl, dict)}
            for missing in sorted(prose - declared):
                errs.append(f"relation in prose but not in x-civic.relations: {missing[1]} -> {missing[0]}")
            for extra in sorted(declared - prose):
                errs.append(f"x-civic.relations has no matching prose link: {extra[1]} -> {extra[0]}")

        # 5. reciprocity
        if isinstance(xc, dict):
            src_dir = os.path.dirname(r["path"])
            for e in r["edges"]:
                target_path = rel(os.path.normpath(os.path.join(src_dir, e["target"])))
                target = by_path.get(target_path)
                if target is None:
                    errs.append(f"edge target not found: {e['type']} -> {e['target']}")
                    continue
                if e["type"] in DIRECTIONAL_EDGE_TYPES:
                    continue  # one-way edge: target exists, no reciprocity expected
                back = {(b["target"], b["type"]) for b in target["edges"]}
                expected = (os.path.basename(r["path"]), e["type"])
                if expected not in back:
                    errs.append(
                        f"non-reciprocal {e['type']} edge to {e['target']}: "
                        f"{rel(target['path'])} does not link back"
                    )

    return results


# --------------------------------------------------------------------------- #
# --write: regenerate profile + relations from prose edges
# --------------------------------------------------------------------------- #
def render_relations(edges):
    if not edges:
        return ["  relations: []"]
    out = ["  relations:"]
    for e in edges:
        out.append(f"    - target: {e['target']}")
        out.append(f"      type: {e['type']}")
        if e["note"]:
            note = e["note"].replace("\\", "\\\\").replace('"', '\\"')
            out.append(f'      note: "{note}"')
    return out


def rewrite_text(text):
    """Set x-civic.profile and regenerate relations without disturbing other lines."""
    fm_text, body = split_frontmatter(text)
    if fm_text is None:
        return text
    data = yaml.safe_load(fm_text)
    if not isinstance(data, dict) or "x-civic" not in data:
        return text

    lines = fm_text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.rstrip() == "x-civic:"), None)
    if start is None:
        return text
    end = start + 1
    while end < len(lines) and (lines[end] == "" or lines[end].startswith(" ")):
        end += 1
    inner = lines[start + 1:end]

    # strip any existing profile line and relations block
    cleaned, i = [], 0
    while i < len(inner):
        line = inner[i]
        if re.match(r"^  profile:", line):
            i += 1
            continue
        if re.match(r"^  relations:", line):
            i += 1
            while i < len(inner) and inner[i].strip() != "" and not re.match(r"^  \S", inner[i]):
                i += 1
            continue
        cleaned.append(line)
        i += 1

    new_inner = [f"  profile: {PROFILE}"] + cleaned
    if data.get("type") in RELATION_TYPES:
        new_inner += render_relations(extract_edges(body))

    new_lines = lines[:start + 1] + new_inner + lines[end:]
    return "---\n" + "\n".join(new_lines) + "\n---\n" + body


def write_all(paths):
    changed = []
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        new = rewrite_text(text)
        if new != text:
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(new)
            changed.append(rel(p))
    return changed


# --------------------------------------------------------------------------- #
# reporting / entry point
# --------------------------------------------------------------------------- #
def report(results):
    failed = {p: errs for p, errs in results.items() if errs}
    for p in sorted(results):
        errs = results[p]
        mark = "FAIL" if errs else "ok"
        print(f"[{mark}] {p}")
        for e in errs:
            print(f"       - {e}")
    print()
    total = len(results)
    print(f"{total - len(failed)}/{total} records passed.")
    return not failed


def self_test():
    """The validator must REJECT every fixture under schemas/fixtures/."""
    fixtures = [
        os.path.join(FIXTURE_DIR, f)
        for f in sorted(os.listdir(FIXTURE_DIR))
        if f.endswith(".md")
    ] if os.path.isdir(FIXTURE_DIR) else []
    if not fixtures:
        print("self-test: no fixtures found under schemas/fixtures/")
        return False
    results = validate(fixtures)
    ok = True
    for p in sorted(results):
        errs = results[p]
        if errs:
            print(f"[rejected as expected] {p} ({len(errs)} error(s))")
        else:
            print(f"[UNEXPECTED PASS] {p} — fixture should have failed")
            ok = False
    print()
    print("self-test passed." if ok else "self-test FAILED.")
    return ok


def main():
    ap = argparse.ArgumentParser(description="Validate the okf-civic-sample bundle.")
    ap.add_argument("--write", action="store_true", help="regenerate profile + relations in place")
    ap.add_argument("--self-test", action="store_true", help="confirm fixtures are rejected")
    args = ap.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    paths = discover_records()
    if args.write:
        changed = write_all(paths)
        if changed:
            print("Rewrote:")
            for c in changed:
                print(f"  - {c}")
        else:
            print("No changes (relations already up to date).")
        sys.exit(0)

    sys.exit(0 if report(validate(paths)) else 1)


if __name__ == "__main__":
    main()
