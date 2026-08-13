#!/usr/bin/env python3
"""Generate a JSON payload for an organization bundle, using a mapping file
and a JSON template file.

Usage:
    python3 scripts/generate_mapped_json.py <org_name> <mapping_name> [-o output.json]

Example:
    python3 scripts/generate_mapped_json.py synthetic-black-mountain-workforce-partnership pdc

`org_name` is an organization's folder name under `organizations/` — not
a path, just the name (e.g. "synthetic-black-mountain-workforce-partnership").

`mapping_name` is a folder name under `scripts/mappings/` (e.g. "pdc").
That folder must contain exactly two files:
    map.md          the mapping file
    definition.json the JSON template file
This command works the same whether run from the repository root or from
inside `scripts/` — paths are resolved relative to this script's own
location, not the current directory.

Without -o, the output defaults to
"organizations/<org_name>/<org_name>_<mapping_name>.json" — e.g. the
example above writes
organizations/synthetic-black-mountain-workforce-partnership/synthetic-black-mountain-workforce-partnership_pdc.json

There are two input files, with two different jobs:

- The **mapping file** says which piece of an organization's data goes
  into which output field, identified by a code. Lines look like:
      - `README.md#title`=organization_name
      - `README.md#x-civic.registration.id`=organization_tax_id
      - `README.md#sources[].resource`=organization_website
  The property after `#` may be a dotted path into nested YAML (objects
  via `.key`), not just a top-level key. Use `[]` (not a fixed index) to
  walk a list of objects — the mapping describes the array's *shape*,
  not how many items happen to exist in one file, so `[]` expands to
  one output field per item actually present, however many that is
  (0, 1, 3, ...). Lines with an empty value after `=` are skipped.

- The **JSON template file** is a plain JSON document that shapes the
  output, using `{{...}}` placeholders that get filled in with the
  values the mapping file pulled out. No network calls, no external
  service — everything the template needs comes from the mapping.

  The template must contain exactly one array holding a single object —
  that's the "repeat this" marker. It gets rendered once per mapped
  value and expanded into an array with one entry per value. Inside
  that one object, three placeholders are available:
      {{code}}    the code from the mapping file (e.g. "organization_name")
      {{value}}   the actual value pulled from the organization's data
      {{source}}  "<file>#<property>" the value came from

  Anywhere else in the template (outside that repeated object),
  `{{some_code}}` is filled in with the value mapped to the code
  `some_code` — e.g. `{{organization_name}}` pulls in whatever value
  the mapping file assigned to the code `organization_name`.

  A placeholder that is the *entire* string value (e.g. `"{{value}}"`)
  is replaced with the real value as-is, preserving its type (a list
  stays a list). A placeholder embedded in a longer string (e.g.
  `"id-{{value}}"`) is replaced as text.

This design is generic: `scripts/mappings/pdc/definition.json` shapes the
output to look like a Philanthropy Data Commons Application Form field
(https://philanthropydatacommons.org/base-fields-list/), but PDC is just
one example target — write a different template file to shape the same
mapped data into a different JSON format entirely.
"""

import argparse
import copy
import json
import os
import re
import sys

import yaml

MAPPING_LINE_RE = re.compile(r"^\s*-\s*`([^#`]+)#([^`]+)`\s*=\s*(\S.*)?\s*$")
FULL_PLACEHOLDER_RE = re.compile(r"^\{\{(\w+)\}\}$")
PARTIAL_PLACEHOLDER_RE = re.compile(r"\{\{(\w+)\}\}")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
ORGANIZATIONS_DIR = os.path.join(REPO_ROOT, "organizations")
MAPPINGS_DIR = os.path.join(SCRIPT_DIR, "mappings")


def parse_mapping_file(mapping_path):
    """Return an ordered list of (relative_md_path, property, code)."""
    mappings = []
    with open(mapping_path, "r", encoding="utf-8") as f:
        for line in f:
            match = MAPPING_LINE_RE.match(line.rstrip("\n"))
            if not match:
                continue
            rel_path, prop, code = match.groups()
            if not code:
                continue
            mappings.append((rel_path.strip(), prop.strip(), code.strip()))
    return mappings


PATH_TOKEN_RE = re.compile(r"([^.\[\]]+)|(\[\])|\[(\d+)\]")


def _tokenize_path(prop):
    """Split a path like "x-civic.relations[].target" into
    [('key', 'x-civic'), ('key', 'relations'), ('wildcard',), ('key', 'target')]."""
    tokens = []
    for name, wildcard, index in PATH_TOKEN_RE.findall(prop):
        if name:
            tokens.append(("key", name))
        elif wildcard:
            tokens.append(("wildcard", None))
        else:
            tokens.append(("index", int(index)))
    return tokens


def resolve_path(frontmatter, prop):
    """Resolve a path (dotted objects via ".key", list items via "[]" for
    every item or "[N]" for a fixed index) against a parsed frontmatter
    dict. Yields (concrete_path, value) for every match — zero matches
    means the path doesn't exist (or, for "[]", the list is empty)."""

    def walk(current, tokens, path_so_far):
        if not tokens:
            yield path_so_far, current
            return
        kind, arg = tokens[0]
        rest = tokens[1:]
        if kind == "key":
            if not isinstance(current, dict) or arg not in current:
                return
            next_path = f"{path_so_far}.{arg}" if path_so_far else arg
            yield from walk(current[arg], rest, next_path)
        elif kind == "index":
            if not isinstance(current, list) or arg >= len(current):
                return
            yield from walk(current[arg], rest, f"{path_so_far}[{arg}]")
        elif kind == "wildcard":
            if not isinstance(current, list):
                return
            for i, item in enumerate(current):
                yield from walk(item, rest, f"{path_so_far}[{i}]")

    yield from walk(frontmatter, _tokenize_path(prop), "")


def extract_frontmatter(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}
    yaml_text = "\n".join(lines[1:end_idx])
    data = yaml.safe_load(yaml_text)
    return data if isinstance(data, dict) else {}


def find_repeat_marker(node, path=()):
    """Find the array-of-one-object "repeat this" marker in the template.
    Returns a list of paths (tuples of keys/indices) to every marker
    found; a well-formed template has exactly one."""
    found = []
    if isinstance(node, dict):
        for key, value in node.items():
            found.extend(find_repeat_marker(value, path + (key,)))
    elif isinstance(node, list):
        if len(node) == 1 and isinstance(node[0], dict):
            found.append(path)
        else:
            for i, item in enumerate(node):
                found.extend(find_repeat_marker(item, path + (i,)))
    return found


def get_at_path(node, path):
    for step in path:
        node = node[step]
    return node


def set_at_path(node, path, value):
    target = node
    for step in path[:-1]:
        target = target[step]
    target[path[-1]] = value


def render(node, context):
    """Recursively substitute {{token}} placeholders using `context`
    (token -> value). A placeholder that's the whole string is replaced
    with the value as-is (keeping its type); embedded placeholders are
    stringified. Tokens with no match in `context` are left untouched."""
    if isinstance(node, dict):
        return {k: render(v, context) for k, v in node.items()}
    if isinstance(node, list):
        return [render(item, context) for item in node]
    if isinstance(node, str):
        full_match = FULL_PLACEHOLDER_RE.match(node)
        if full_match:
            token = full_match.group(1)
            return context[token] if token in context else node

        def replace_partial(m):
            token = m.group(1)
            return str(context[token]) if token in context else m.group(0)

        return PARTIAL_PLACEHOLDER_RE.sub(replace_partial, node)
    return node


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("org_name", help="Organization folder name under organizations/")
    parser.add_argument("mapping_name", help="Mapping folder name under scripts/mappings/")
    parser.add_argument("-o", "--output", help="Output JSON file path")
    args = parser.parse_args()

    org_name_default = os.path.basename(args.org_name.rstrip("/"))
    org_path = os.path.join(ORGANIZATIONS_DIR, org_name_default)
    if not os.path.isdir(org_path):
        print(f"Error: {org_path} is not a directory.", file=sys.stderr)
        sys.exit(1)

    mapping_name = os.path.basename(args.mapping_name.rstrip("/"))
    mapping_dir = os.path.join(MAPPINGS_DIR, mapping_name)
    mapping_file = os.path.join(mapping_dir, "map.md")
    json_template_file = os.path.join(mapping_dir, "definition.json")
    if not os.path.isfile(mapping_file):
        print(f"Error: {mapping_file} is not a file.", file=sys.stderr)
        sys.exit(1)
    if not os.path.isfile(json_template_file):
        print(f"Error: {json_template_file} is not a file.", file=sys.stderr)
        sys.exit(1)

    output_path = args.output or os.path.join(
        org_path, f"{org_name_default}_{mapping_name}.json"
    )

    with open(json_template_file, "r", encoding="utf-8") as f:
        try:
            template = json.load(f)
        except json.JSONDecodeError as exc:
            print(f"Error: {json_template_file} is not valid JSON: {exc}",
                  file=sys.stderr)
            sys.exit(1)

    marker_paths = find_repeat_marker(template)
    if len(marker_paths) != 1:
        print(f"Error: {json_template_file} must contain exactly one "
              f"array holding a single object (found {len(marker_paths)}).",
              file=sys.stderr)
        sys.exit(1)
    marker_path = marker_paths[0]
    field_template = get_at_path(template, marker_path)[0]

    mappings = parse_mapping_file(mapping_file)
    if not mappings:
        print("No mapped fields found in mapping file.", file=sys.stderr)

    frontmatter_cache = {}
    mapped = []  # list of (code, value, source)
    global_lookup = {}  # code -> first value seen for that code

    for rel_path, prop, code in mappings:
        md_path = os.path.join(org_path, rel_path)
        if rel_path not in frontmatter_cache:
            if not os.path.isfile(md_path):
                print(f"Warning: {md_path} not found, skipping.", file=sys.stderr)
                frontmatter_cache[rel_path] = {}
            else:
                frontmatter_cache[rel_path] = extract_frontmatter(md_path)
        frontmatter = frontmatter_cache[rel_path]

        matches = list(resolve_path(frontmatter, prop))
        if not matches:
            print(f"Warning: {rel_path}#{prop} not present in frontmatter, skipping.",
                  file=sys.stderr)
            continue

        for concrete_path, value in matches:
            source = f"{org_name_default}/{rel_path}#{concrete_path}"
            mapped.append((code, value, source))
            if code not in global_lookup:
                global_lookup[code] = value

    rendered_items = [
        render(field_template, {"code": code, "value": value, "source": source})
        for code, value, source in mapped
    ]

    output = render(copy.deepcopy(template), global_lookup)
    set_at_path(output, marker_path, rendered_items)

    text = json.dumps(output, indent=2, ensure_ascii=False, default=str)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {output_path} ({len(rendered_items)} mapped fields)", file=sys.stderr)


if __name__ == "__main__":
    main()
