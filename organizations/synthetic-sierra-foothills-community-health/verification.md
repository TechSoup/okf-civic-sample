---
type: verification
title: "synthetic-Sierra Foothills Community Health — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved."
tags: ["eligibility", "verification", "determination", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-01-22T00:00:00Z }
stale_after: 2027-01-22
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0006"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-01-22
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

## Determination v1 — 2026-01-22

**APPROVE**, 94% confidence (HIGH). The registration ID matched the simulated registry exactly, 501(c)(3) status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches. Governance is documented and unusually well — a fifteen-member board with a majority-patient composition requirement attached to its federal health-center support, published minutes, audited financials.

**Debarment screening is materially significant here.** This organization bills public insurance and holds federal program funding; exclusion would be existential rather than inconvenient. It cleared.

## What this determination did not look at, and why that's the interesting part

**Clinical quality: not assessed.** Out of scope, and eligibility verification is the wrong instrument.

The point worth recording is not that the assessment was incomplete — it is that **this organization is the most heavily scrutinized in the collection, and almost none of that scrutiny appears here.** Federal health-center program review, state clinic licensing, payer audits, an annual financial audit, a standing internal quality committee, and mandatory annual reporting in a defined federal format all examine this organization more rigorously than any bundle-level process could.

So the 94% score is a statement about a narrow question — *is this organization real, legitimate, and in good standing* — and it happens to be the least informative thing anyone knows about this organization.

Compare across the collection:

| Organization | Verification confidence | What else is known about it |
|---|---|---|
| This one | 0.94 | An enormous amount, held by regulators, invisible here |
| [Motor City Trades](../synthetic-motor-city-trades-institute/verification.md) | 0.96 | A fair amount — audited, government-contracted — and the worst internal data hygiene in the collection |
| [Nyando](../synthetic-nyando-community-health-trust/verification.md) | insufficient evidence | Very little, and the sources to establish more may not exist |

**Three organizations, three verification outcomes, and the score ordering does not track anything about capability, quality, or trustworthiness.** It tracks how legible each organization is to a particular verification method. If you are building anything that consumes these scores, that is the thing to internalize.

**Also noted:** revenue is majority third-party reimbursement, which a general-purpose nonprofit financial model will likely mishandle — it looks like earned revenue, behaves like a receivable cycle, and carries clawback risk. Not an eligibility question.

- **Next re-validation due:** 2027-01-22.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0006`.*

<!-- Next re-validation (due 2027-01-22) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
