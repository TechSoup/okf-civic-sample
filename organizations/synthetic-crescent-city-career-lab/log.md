# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SN020302, SN020300`, Population `PJ020000, PG030000, PG100000`, OrgType `EA040000`. Subject crosswalked from NTEE J22, J20 via the taxonomy's own former-code column.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. Assigned the collection's **lapsed-determination** defect: an APPROVE at 0.94 issued 2024-02-14 on a two-year term, expired 2026-02-14, not renewed, 165 days out of date at creation. Chosen as the *quiet* defect — nothing else in the bundle is wrong, nothing looks like a problem, and the only field that changed did so by the calendar advancing. The eligibility file documents the mundane mechanics (a departing staff member's deactivated email address as the single point of failure) because that failure mode is far more common than fraud or loss of standing. Partnership edge to synthetic-Gulf Corridor Justice Project, which holds a current determination, so the pair tests whether status propagates along edges. Classification and situation nodes point out to shared `_shared/`.

## 2026-02-14

* **Creation**: **Determination expired.** No re-validation performed. No entry was made in the determination log at the time, because an expiry is the absence of an event and nothing was arranged to notice it. This line was added retrospectively when the bundle was built.

## 2024-02-14

* **Creation**: Simulated validation determination recorded (APPROVE, 0.94, two-year term). Fabricated workspace `SYNTH-WORKSPACE-0012`.
