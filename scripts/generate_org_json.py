#!/usr/bin/env python3
"""Generate a single JSON file summarizing the YAML frontmatter of every
markdown file in an organization's bundle folder.

Usage:
    python3 scripts/generate_org_json.py <org_name> [-o output.json]

Example:
    python3 scripts/generate_org_json.py synthetic-black-mountain-workforce-partnership

`org_name` is an organization's folder name under `organizations/` — not
a path, just the name. This command works the same whether run from the
repository root or from inside `scripts/`; the organization folder is
resolved relative to this script's own location, not the current
directory.

Without -o, the output defaults to
"organizations/<org_name>/<org_name>.json" (e.g.
organizations/synthetic-black-mountain-workforce-partnership/synthetic-black-mountain-workforce-partnership.json),
matching the existing per-organization JSON files in this repo.

The output JSON is a mapping from each markdown file's path (relative to
the organization folder, e.g. "technology/inventory.md") to that file's
YAML frontmatter properties. Markdown files with no frontmatter (or no
leading "---" block) are omitted.
"""

import argparse
import json
import os
import sys

import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
ORGANIZATIONS_DIR = os.path.join(REPO_ROOT, "organizations")


def extract_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None
    yaml_text = "\n".join(lines[1:end_idx])
    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        print(f"YAML parse error in {path}: {e}", file=sys.stderr)
        return None
    return data


def build_org_json(org_path):
    result = {}
    md_files = []
    for dirpath, _dirnames, filenames in os.walk(org_path):
        for fn in filenames:
            if fn.endswith(".md"):
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, org_path)
                md_files.append(rel)
    md_files.sort()

    for rel in md_files:
        full = os.path.join(org_path, rel)
        fm = extract_frontmatter(full)
        if fm is not None:
            result[rel] = fm

    return result, len(md_files)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("org_name", help="Organization folder name under organizations/")
    parser.add_argument("-o", "--output", help="Output JSON file path")
    args = parser.parse_args()

    org_name = os.path.basename(args.org_name.rstrip("/"))
    org_path = os.path.join(ORGANIZATIONS_DIR, org_name)
    if not os.path.isdir(org_path):
        print(f"Error: {org_path} is not a directory.", file=sys.stderr)
        sys.exit(1)

    output_path = args.output or os.path.join(org_path, f"{org_name}.json")

    result, total_files = build_org_json(org_path)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")

    print(
        f"Wrote {output_path} ({len(result)} files with frontmatter, "
        f"{total_files} total md files)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
