---
type: verification
title: "synthetic-Motor City Trades Institute — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved at high confidence."
tags: ["eligibility", "verification", "determination", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-04-02T00:00:00Z }
stale_after: 2027-04-02
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0003"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-04-02
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

## Determination v1 — 2026-04-02

**APPROVE**, 96% confidence (HIGH) — the highest confidence in this collection. The registration ID matched the simulated registry exactly, 501(c)(3) status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches.

The confidence is high for a straightforward reason: this organization is **heavily audited by other people**. A single audit, a state workforce contract, a federal apprenticeship grant, and a county contract all impose independent verification, and the resulting paper trail is deep. Governance is fully documented — an eleven-member board with named officers, published minutes, a conflict-of-interest policy on file.

**Worth noting explicitly:** the organization holds a **federal grant and a county reentry contract**, which means debarment screening matters here in a way it does not for a foundation-funded organization. It cleared. That's the finding, and it is more meaningful for this organization than for most.

**Out of scope:** the determination verified status and standing. It did **not** substantiate the organization's **three-year trade-retention claim**, which is organization-held and single-source. Verification confirmed completion figures (state-reported, independently held) and stopped there. See [README](README.md) — this gap is the organization's most exposed claim, not because anyone doubts it but because nothing outside the organization corroborates it.

- **Next re-validation due:** 2027-04-02.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0003`.*

## A note on what "high confidence" measured

96% is the highest score in this collection, and it went to the organization with the **worst internal data hygiene** of the twelve US bundles — three non-agreeing systems and an abandoned CRM implementation. Both things are correct. Eligibility verification asks whether an organization is real, legitimate, and in good standing. It does not ask whether the organization can find its own records.

If you are building anything that treats a verification score as a proxy for organizational capability, this bundle is the counterexample. Compare it against [synthetic-Frogtown Community Table](../synthetic-frogtown-community-table/verification.md) — a much smaller organization, a lower score, and a considerably tidier stack.

<!-- Next re-validation (due 2027-04-02) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
