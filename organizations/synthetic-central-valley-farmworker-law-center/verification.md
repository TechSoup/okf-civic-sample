---
type: verification
title: "synthetic-Central Valley Farmworker Law Center — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved, with a privilege limitation on scope."
tags: ["eligibility", "verification", "determination", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-02-27T00:00:00Z }
stale_after: 2027-02-27
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0005"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-02-27
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

## Determination v1 — 2026-02-27

**APPROVE**, 95% confidence (HIGH). The registration ID matched the simulated registry exactly, 501(c)(3) status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches. Governance is documented — a thirteen-member board including three named attorney members and a client-community representative seat. Attorney licensure was confirmed against the state bar for all seven attorneys.

## A scope limitation that is not a deficiency

**Case-level information was not examined, because it is privileged.**

This determination establishes that the organization exists, is legitimately constituted, is in good standing, and is staffed by licensed attorneys. It does **not** establish anything about the quality, outcomes, or conduct of its legal work, because reviewing that would require access to privileged client information that the organization cannot lawfully provide and that a verification process has no business requesting.

**This should be read as a boundary, not a gap.** The distinction matters for anything built against this collection:

| | Example | How a system should treat it |
|---|---|---|
| **Undocumented** | [Motor City Trades](../synthetic-motor-city-trades-institute/verification.md)' three-year retention claim — organization-held, single-source, could have been better evidenced | A weakness. Worth flagging |
| **Absent by policy** | [Valle Verde](../synthetic-valle-verde-food-network/verification.md)'s individual-participant counts — deliberately not collected, protectively | Neither a strength nor a weakness. Record the policy |
| **Privileged** | This organization's case outcomes | A legal boundary. A system that penalizes it is badly designed |

Three superficially similar absences, three different meanings, and **none of them distinguishable from the shape of the data alone**. Only a statement like this one carries the difference. If you are building eligibility logic, scoring, or a completeness metric across this collection, these three bundles together are the test set.

**Also noted:** the organization holds a **state legal-services allocation** and receives **court-awarded fees**, an unusual revenue mix that a general-purpose nonprofit financial model may not handle. Not an eligibility question.

- **Next re-validation due:** 2027-02-27.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0005`.*

<!-- Next re-validation (due 2027-02-27) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
