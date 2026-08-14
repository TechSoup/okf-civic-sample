# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SE050100, SE040200`, Population `PG090000, PG030000, PA020300`, OrgType `EA040000`. Subject crosswalked from NTEE E32 via the taxonomy's own former-code column.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. Cast as the collection's **legibility** case: a careful, 48-year-old organization that scores lower on verification confidence than a much messier one, purely because less of it has been written down in retrievable places. Also carries two deliberate traps — a **name/legal-form mismatch** (called a cooperative, incorporated as a nonprofit corporation) that produces a confident wrong classification with no error, and a **telehealth capability its patients largely cannot use**, so the capability flag misleads. The first is recorded only in prose — the profile has no field for it, and this bundle's README notes that absence as a schema suggestion. Reciprocal partnership edge to synthetic-Black Mountain Workforce Partnership established. Classification and situation nodes point out to shared `_shared/`.

## 2026-05-06

* **Creation**: Simulated validation determination recorded (APPROVE, 0.90 — lowest of the clean US determinations, for legibility reasons rather than quality). Fabricated workspace `SYNTH-WORKSPACE-0007`.
