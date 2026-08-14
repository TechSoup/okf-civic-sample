# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; per-claim provenance moved from prose parentheticals to `sources` entries with footnote attribution (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to the five `x-civic` keys — `profile`, `subject`, `population`, `org_type`, `registration_country`. NTEE and SDG codes replaced by **Candid PCS** facets, crosswalked from the 2024 PCS taxonomy: NTEE K31 → `SS030601`, K30 → `SS030600`, P84 → `SS090300`; population assigned directly from the PCS Population facet.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains here is an optional, dated, third-party determination.
* **Update**: Structural links converted to ordinary markdown links. Wikilinks retained **only** for emergent terms with no target file (`[[Hmong]]`, `[[Karen]]`, `[[Somali]]`, `[[Oromo]]`, `[[Latino]]`), which OKF §6.1 explicitly permits and which is the bundle's demonstration of vocabulary emerging from below.
* **Update**: Hand-maintained membership lists pointing out to the classification hubs and the place node were removed from the body. Those memberships are now **derived** from this bundle's frontmatter — `subject`, `population`, `org_type`, `ntee`, `sdg`, `situation` — and the hub Members lists are generated from them by `scripts/build_hubs.py`. Asserted peer edges, which cannot be derived, stay in `x-civic.relations`; this bundle keeps one, to synthetic-North Star Immigrant Defense. As the worked reference it carries the smallest set of asserted edges in the collection on purpose.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection, modeled file-for-file on a real organization bundle held elsewhere. Cast as the collection's counterexample: smallest budget of the fifteen, lowest clean verification confidence, and the tidiest technology stack — built to demonstrate that verification confidence measures legibility rather than competence and can run opposite to it.
* **Creation**: Simulated validation determination recorded (APPROVE, 0.88 — the lowest clean score in the collection, for legibility reasons rather than quality). Fabricated workspace `SYNTH-WORKSPACE-0009`.
