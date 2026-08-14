# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SJ040000, SJ040700, SS090300`, Population `PG010000, PG010700, PG040300`, OrgType `EA040000`. Subject crosswalked from NTEE I80, I83, P84 via the taxonomy's own former-code column.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. Cast as the collection's **adversarial-risk** case: the only organization whose data somebody actively wants, so its `constraints.md` is a threat model rather than a privacy policy and argues that several ordinary good practices (comprehensive logging, long retention, cloud convenience, analytics) are wrong here. Written to be read against synthetic-Central Valley Farmworker Law Center — two legal-aid organizations whose failure modes barely overlap, one bounded by privilege and unauthorized-practice rules, the other by hostile interest. Its eligibility file raises the collection's one argument **against** legibility: documenting an organization is not neutral when the organization expects to be looked for. Also carries a deliberately **unpublished capacity figure** (rapid-response turnaways), as a caution for need models built from public data. Partnership edge to synthetic-Frogtown Community Table established, in whose back room it holds monthly clinic hours. Classification and situation nodes point out to shared `_shared/`.

## 2026-03-05

* **Creation**: Simulated validation determination recorded (APPROVE, 0.93; case-level review out of scope as privileged; verification record itself deliberately minimized). Fabricated workspace `SYNTH-WORKSPACE-0010`.
