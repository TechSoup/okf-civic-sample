# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SE050100, SE050000`, Population `PG090000, PG030000, PJ130000`, OrgType `EA040000`. Subject crosswalked from NTEE E32, E30 via the taxonomy's own former-code column.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. Cast as the collection's **largest organization** ($7.9M, 88 staff) and its **heavily-regulated** case, where most of what is known about the organization is held by regulators and invisible in the bundle. Carries the collection's only **`learn_with`** edge — to synthetic-Nyando Community Health Trust in Kisumu County, Kenya. Its volunteer project is the only one in the collection requiring a **Business Associate Agreement** before work can begin, and it involves PHI in two unmerged electronic health record systems. Classification and situation nodes point out to shared `_shared/`.

## 2026-01-22

* **Creation**: Simulated validation determination recorded (APPROVE, 0.94; clinical quality out of scope, separately regulated). Fabricated workspace `SYNTH-WORKSPACE-0006`.
