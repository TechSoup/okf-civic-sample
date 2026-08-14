# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SS030600, SS030601`, Population `PJ130000, PG090000, PG030000`, OrgType `EA040000`. Subject crosswalked from NTEE K30, K31 via the taxonomy's own former-code column.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. Cast as the collection's **no-connectivity** case: a service area where cell coverage cannot be assumed, which invalidates the default mobile-data-capture assumptions and shapes the volunteer project. Also carries the collection's example of **absence-by-policy** — the organization refuses to collect individual identifiers, so a funder-required count genuinely does not exist. Partnership edge to synthetic-Central Valley Farmworker Law Center established, with a shared situation node. Classification and situation nodes point out to shared `_shared/`.

## 2026-03-14

* **Creation**: Simulated validation determination recorded (APPROVE, 0.93; policy-based data absence noted as a policy, not a deficiency). Fabricated workspace `SYNTH-WORKSPACE-0004`.
