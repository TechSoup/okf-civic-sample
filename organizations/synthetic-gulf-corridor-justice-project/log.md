# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SC030100, SE130200`, Population `PG030000, PG100000`, OrgType `EA040000`. Subject crosswalked from NTEE C20, C30 via the taxonomy's own former-code column.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. Cast as the collection's **integrity-over-confidentiality** case: the organization's data is meant to be public, so its security problem is proving nothing has been altered and staying available on hearing days — the third distinct threat model in the collection, after North Star's hostile-state model and the Law Center's professional-responsibility one. Its adversary is competent, funded, and entirely lawful. Also carries two notes intended as tests: **adverse-media screening on an advocacy organization** returns heavy critical coverage that is evidence of effectiveness rather than misconduct, and its `partners_with` edge points at an organization whose **determination has lapsed**, so status does not propagate along edges. Coalition edges to Detroit and to Cali, Colombia. Classification and situation nodes point out to shared `_shared/`.

## 2026-02-12

* **Creation**: Simulated validation determination recorded (APPROVE, 0.91; survey methodology out of scope; adverse-media volume assessed and cleared). Fabricated workspace `SYNTH-WORKSPACE-0011`.
