#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# OKF Civic Sample — a tiny starter validator/linter.
# Checks two things, with no third-party dependencies:
#   1. Every markdown doc has YAML frontmatter with a non-empty `type` (OKF's one hard rule).
#   2. Internal markdown links resolve to files that exist (link health).
# It intentionally does NOT reject unknown fields, missing optional fields, or
# external links — OKF says consumers MUST be permissive.
#
# Usage: python3 validate.py [root_dir]

import sys
import re
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def frontmatter_type(text: str):
    """Return the `type` value from leading YAML frontmatter, or None."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    for line in block.splitlines():
        if line.strip().startswith("type:"):
            return line.split("type:", 1)[1].strip().strip('"').strip("'")
    return None


def main(root="."):
    root = Path(root)
    md_files = sorted(root.rglob("*.md"))
    problems = []
    checked = 0

    for f in md_files:
        if ".obsidian" in f.parts:
            continue
        if f.name in ("README.md", "CONTRIBUTING.md") or f.name.startswith("LICENSE"):
            continue  # repo scaffolding, not OKF concept documents
        checked += 1
        text = f.read_text(encoding="utf-8", errors="ignore")

        t = frontmatter_type(text)
        if not t:
            problems.append(f"{f}: missing or empty `type` (OKF requires it)")

        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            if not (f.parent / target).resolve().exists():
                problems.append(f"{f}: broken internal link -> {target}")

    print(f"Checked {checked} markdown file(s).")
    if problems:
        print(f"\n{len(problems)} issue(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("All good: every doc has a `type`, and internal links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
