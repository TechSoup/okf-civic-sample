---
type: verification
title: "synthetic-Gulf Corridor Justice Project — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved."
tags: ["eligibility", "verification", "determination", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-02-12T00:00:00Z }
stale_after: 2027-02-12
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0011"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-02-12
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

## Determination v1 — 2026-02-12

**APPROVE**, 91% confidence (HIGH). The registration ID matched the simulated registry exactly, 501(c)(3) status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches. Governance is documented — an eleven-member board, six of whom are corridor residents, with published minutes.

## A note on adverse-media screening for advocacy organizations

Worth recording because it is a general problem this bundle happens to illustrate.

Adverse-media screening on this organization returns **a substantial volume of critical coverage** — trade-press articles disputing its findings, opinion pieces characterizing it as an obstacle to regional investment, and at least one industry-funded report questioning its survey methodology by name.

None of it constitutes adverse media in the sense the screen is designed to detect. It is **an organization being publicly opposed by the interests it opposes**, which for an advocacy organization is evidence that the work is landing rather than evidence of a problem.

The determination assessed the coverage and cleared it. **But a screening process tuned for fraud and misconduct will surface this material, and a less careful reading of the same results would produce a finding against an organization for having effective opponents.** Any automated adverse-media step applied to advocacy organizations needs to handle this deliberately, and this bundle is a reasonable test for whether yours does.

**Out of scope:** the **health survey's methodology** was not assessed. Verification confirmed the survey exists and is administered consistently; whether it withstands expert challenge is a scientific question outside eligibility verification. See [README](README.md) — it is also the question an opposing expert will focus on.

**Noted, not flagged:** the organization holds **respondent-level health information without HIPAA coverage and without privilege**, meaning it is discoverable in litigation. Its 2023 consent revision tells respondents so. Not an eligibility question; a significant ethical and operational fact. See [population](population.md).

**Noted:** this organization's `partners_with` edge points to [synthetic-Crescent City Career Lab](../synthetic-crescent-city-career-lab/verification.md), whose own determination has **lapsed** and whose status is `PENDING_REVALIDATION`. This has no bearing on Gulf Corridor's eligibility — an organization's status does not propagate along partnership edges — and it is recorded because anything traversing this graph will encounter the pairing.

- **Next re-validation due:** 2027-02-12.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0011`.*

<!-- Next re-validation (due 2027-02-12) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
