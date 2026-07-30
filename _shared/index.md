# Shared nodes

**⚠ Part of a synthetic collection. Every organization listed in these nodes is fabricated** — see the [collection README](../README.md). The classification codes and the places are real.

Classification and place nodes that the fifteen organization bundles link to. Authored once here and shared across every bundle, so a hub's membership list has real entries and a place node hosts organizations from different program areas.

## One required layer, two optional ones

| Folder | Status | Reaches | What it is |
|---|---|---|---|
| [pcs/](pcs/index.md) | **required** | 15 of 15 | Candid PCS — the vocabulary `civic/0.6` requires, 19 subject + 17 population + 3 org-type nodes |
| [sdg/](sdg/index.md) | optional | 15 of 15 | UN Sustainable Development Goals — global but coarse |
| [ntee/](ntee/index.md) | optional | 12 of 15 | US IRS classification — cannot reach the three non-US organizations |
| [situations/](situations/index.md) | optional | 15 of 15 | Places. Community context lives here, once per place |

**A bundle is conformant carrying only the PCS codes.** Everything else in this folder is enrichment that makes the graph worth querying.

## The membership lists are generated

Every `<!-- GENERATED -->` block in this folder is rebuilt from the organizations' own frontmatter by `scripts/build_hubs.py`. Earlier versions of this collection maintained them by hand and documented the drift as a known problem; `scripts/validate.py` now runs `--check` and fails if a list is stale, so the two directions cannot disagree.

## What a situation node is for

A **situation** describes a place, not an organization. Community context — population, income, health outcomes, connectivity — is stored once for the place, so it is not copied into every organization operating there. See [situations/](situations/index.md) for the clearest demonstration this collection contains.
