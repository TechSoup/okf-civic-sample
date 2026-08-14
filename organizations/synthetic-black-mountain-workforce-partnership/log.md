# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SN020302, SB040000`, Population `PG090000, PJ020000, PG030000`, OrgType `EA040000`. Subject crosswalked from NTEE J22 via the taxonomy's own former-code column.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. Paired deliberately with synthetic-Cumberland Gap Health Cooperative to demonstrate **one community-level infrastructure gap defeating two organizations' programs in two different sectors** — the county's broadband availability killed the clinic's telehealth and undermines this organization's remote-work track. The shared cause lives in the situation node, not in either bundle, which is the collection's argument for storing community conditions with the place. Also carries the **most reciprocal partnership edge** in the collection (each organization is the other's supplier and customer) and, read against synthetic-Motor City Trades Institute, the collection's **honest-absence-versus-flattering-estimate** comparison. Classification and situation nodes point out to shared `_shared/`.

## 2026-06-30

* **Creation**: Simulated validation determination recorded (APPROVE, 0.92; long-term retention recorded as not collected, stated explicitly). Fabricated workspace `SYNTH-WORKSPACE-0008`.
