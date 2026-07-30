---
type: verification
title: "synthetic-Valle Verde Food Network — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved."
tags: ["eligibility", "verification", "determination", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-03-14T00:00:00Z }
stale_after: 2027-03-14
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0004"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-03-14
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

## Determination v1 — 2026-03-14

**APPROVE**, 93% confidence (HIGH). The registration ID matched the simulated registry exactly, 501(c)(3) status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches. Governance is documented — a nine-member board, five of whom are named as community members from the service area.

**Noted, not flagged — and this is the interesting part of this determination.** The organization cannot produce an unduplicated-individuals-served count, because **it does not collect individual identifiers as a matter of policy**. The determination records this as a **policy position, not a deficiency**, and approves accordingly.

That distinction is worth preserving deliberately. A verification process that treated every absent field as a data-quality problem would have marked this organization down for the single most protective decision it makes. The organization declines to hold names, addresses, or immigration status for a population where such a list is a hazard. See [README](README.md) and [population](population.md).

If you are building eligibility or scoring logic against this collection, **this bundle is the test for whether your rules can distinguish a deliberate absence from a missing value.** They should not be handled the same way, and the difference cannot be detected from the shape of the data — only from a statement like this one.

**Also noted:** the organization holds **state food-bank allocation funding** whose formula is defined per-individual. It reports estimates, labeled as estimates, derived from household counts. No funder has objected; the determination records that the mismatch exists.

- **Next re-validation due:** 2027-03-14.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0004`.*

<!-- Next re-validation (due 2027-03-14) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
