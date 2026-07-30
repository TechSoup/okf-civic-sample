---
type: verification
title: "synthetic-Cumberland Gap Health Cooperative — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved at the lowest confidence of the clean US bundles."
tags: ["eligibility", "verification", "determination", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-05-06T00:00:00Z }
stale_after: 2027-05-06
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0007"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-05-06
  - id: registry
    resource: "simulated registry extract"
    title: "Registry record (simulated)"
    author: process:registry-import
    last_modified: 2026-01-15
x-civic:
  profile: civic/0.6
---

# Eligibility & verification

**⚠ Synthetic — this determination was never made. It is fabricated to give the record a realistic shape.**

A **log**, written by the validation system. Each re-validation appends a new entry; nothing is overwritten. Everyone else reads this file; only the validation system writes it. Edit history for the *bundle* is separate — see [log](log.md).

## Current status: **ELIGIBLE**

## Determination v1 — 2026-05-06

**APPROVE**, 90% confidence (MODERATE-HIGH) — the lowest of the eleven clean US determinations in this collection. The registration ID matched the simulated registry exactly, 501(c)(3) status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches. Governance is documented — a seven-member board, all county residents, minutes kept on paper.

## Why the confidence is lower, and why it should not be read as a concern

Nothing was wrong. The score is lower because **there is less of this organization written down anywhere**, and confidence is a function of corroborating sources rather than of organizational quality.

Specifically:

- **Minutes are on paper.** They exist, they are kept, they were describable. They are not retrievable by anyone outside the building.
- **No independent audit.** At $1.1M the organization is below the threshold that would compel one, so it has a financial review rather than an audit. Entirely appropriate and correspondingly less external documentation.
- **Almost no web presence to corroborate against.** A small site, no press coverage, no directory listings beyond the basics. Everything a verification process likes to cross-reference is thin.
- **A 48-year history in a county of 21,000** is the strongest evidence about this organization and is essentially unusable as a verification signal, because it is local knowledge rather than a record.

**The pattern generalizes and it matters for the whole collection.** Verification confidence measures **legibility** — how much of an organization has been written down in retrievable places. That correlates with size, with regulatory burden, and with proximity to institutions that generate paperwork. It does not correlate with quality, competence, or trustworthiness.

Ranked by confidence, this collection puts [Motor City Trades](../synthetic-motor-city-trades-institute/verification.md) (0.96) — which has the worst internal data hygiene of the twelve US bundles — above this organization (0.90), which is small, careful, and has run continuously since 1978. Both scores are correct. Neither means what a ranking implies.

The extreme case is [Nyando](../synthetic-nyando-community-health-trust/verification.md), where the same legibility problem is severe enough to produce a determination of insufficient evidence.

**Noted, not flagged:** the organization is named a *cooperative* and is incorporated as a nonprofit corporation. See [README](README.md) — recorded because an automated classifier will get it wrong and there will be no error to alert anyone.

**Out of scope:** clinical quality (separately regulated) and organizational continuity. The second is the material question about this organization's future — 0.4 FTE physician coverage with no identified successor — and no verification process is built to see it.

- **Next re-validation due:** 2027-05-06.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0007`.*

<!-- Next re-validation (due 2027-05-06) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
