# Bundle Update Log

Update history for this bundle (OKF v0.2 §9). Newest first. This log records **edits to the bundle**. A determination *about the organization* is a different thing and lives in [verification.md](verification.md).

## 2026-08-07

* **Addition**: Added `impact.md` (`type: impact`) and `what_i_need_funding_for.md` (`type: funding_need`) — outcomes and results, and funding priorities, both in the organization's own voice. Both are optional enrichment; neither is part of the published `civic/0.6` profile (see each file's own `description`).

## 2026-07-29

* **Update**: Migrated to **OKF v0.2** and **civic/0.6**. `timestamp` replaced by `generated`; provenance claims joined to a frontmatter `sources` list by footnote (§5.1); the simulated determination moved onto core `verified` and `stale_after` (§5.2, §5.5); `index.md` reduced to a listing carrying only `okf_version` (§8); this log reformatted to the §9 date-grouped shape.
* **Update**: Required frontmatter reduced to five `x-civic` keys. Assigned **Candid PCS** codes — Subject `SJ040000, SS090300, SR040100`, Population `PG010400, PG010000, PG010200`, OrgType `EA030000`. Assigned directly from the activity description; no NTEE to cross from.
* **Update**: `eligibility.md` renamed to `verification.md` (`type: verification`). The eligibility *facts* — organization type and registration country — are now required frontmatter on the organization record; what remains is an optional, dated, third-party determination.
* **Update**: Wikilinks that resolve to a file converted to ordinary markdown links (§6.1). Wikilinks retained only for **emergent terms** with no target file, which the spec explicitly permits and which is how vocabulary the controlled facets cannot carry becomes visible in the graph.

## 2026-07-28

* **Creation**: Bundle created, fabricated for the synthetic collection. Modeled file-for-file on the Chapter 510 Ink bundle. The **first of three international bundles**, and the one that breaks the most schema assumptions at once: no EIN (`ein: null`, explicit rather than omitted), no 501(c)(3) — a *fundacja* with KRS, NIP, REGON, and OPP status; **no NTEE**, because NTEE is a US IRS vocabulary, with ICNPO left unassigned rather than guessed; budget in **PLN**, unconverted; and **GDPR** as the data-protection regime, which makes a US-hosted service a legal question rather than a procurement preference. Deliberately cast to **correct the assumption that international means less verifiable** — Poland's KRS is a public court register with structured records and filed financials, so this organization verifies more easily than several US bundles here. Read against synthetic-Nyando Community Health Trust, which is genuinely hard to verify, the pair shows that verifiability tracks the information environment rather than the country. Also raises two schema gaps: no way to mark which language a field is authoritative in, and `privileged` as a US term of art that does not port. Classification and situation nodes point out to shared `_shared/`.

## 2026-05-28

* **Creation**: Simulated validation determination recorded (APPROVE, 0.92, via KRS/NIP/REGON/OPP rather than IRS records; GDPR compliance not assessed; case-level review out of scope as professional secrecy). Fabricated workspace `SYNTH-WORKSPACE-0013`.
