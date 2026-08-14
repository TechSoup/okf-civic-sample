# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SE040200, SE130700`, Population `PG090000, PH040000, PA010000`, OrgType `EA000000`. Assigned directly from the activity description; no NTEE to cross from.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. The **third of three international bundles** and the collection's **insufficient-evidence** case, carrying a fourth registration framework (Kenyan trust deed plus public-benefit-organization registration, KRA PIN), a fourth data-protection regime (Data Protection Act 2019), a fourth catalogue, and budget in **KES**, unconverted. Built around a deliberate inversion: **the best program data in the collection and the worst verifiability** — 142 community health promoters capturing structured household data offline and reporting monthly into a national health information system, in an organization a verification process could not confirm exists, because six of seven checks failed on retrievability rather than substance and the process had no step for the strongest available evidence. Positioned explicitly against the Polish bundle (easier to verify than the US) and the Colombian one (comparable), so the collection teaches that **verifiability tracks the information environment** rather than the country or the organization. Carries the reciprocal **`learn_with`** edge to synthetic-Sierra Foothills Community Health, where the learning runs uphill — the Californian organization with 20× the budget charts on paper in its mobile unit because it has not solved what this organization solved years ago. Also surfaces the promoter equity problem (community health workers absorbing mobile data costs for the organization's donor reporting) as a live harm rather than a design constraint. Classification and situation nodes point out to shared `_shared/`.

## 2026-07-09

* **Creation**: Simulated verification attempted. **No determination reached — insufficient evidence.** Nothing adverse found; compliance screening cleared. Registration, governance, and financial checks all failed on external retrievability. An alternative evidence route is documented in [eligibility.md](verification.md). Fabricated workspace `SYNTH-WORKSPACE-0015`.
