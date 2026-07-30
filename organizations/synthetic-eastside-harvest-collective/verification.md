---
type: verification
title: "synthetic-Eastside Harvest Collective — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved, with an open flag."
tags: ["eligibility", "verification", "determination", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-06-11T00:00:00Z }
stale_after: 2027-06-11
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0001"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-06-11
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

## Current status: **ELIGIBLE — with one open flag**

Note the status value: `ELIGIBLE_WITH_OPEN_FLAG`, not `ELIGIBLE`. The organization qualifies. There is also something unresolved about it. Both are true, and code that flattens this to a boolean loses the second half.

## Determination v1 — 2026-06-11

**APPROVE**, 91% confidence (HIGH). The registration ID matched the simulated registry exactly, 501(c)(3) status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches.

**Open flag — financial figures do not reconcile.** The budget stated on the application ($1,400,000) and the total revenue on the filed return ($2,064,880, FY ending September 2025) differ by 47% with no explanatory note. The determination approves the organization anyway — the discrepancy affects *sizing*, not *eligibility* — but records the gap as unresolved rather than choosing a number. See [README](README.md).

**Second flag — site tenure partially unverifiable.** Legal interest could be established for one of four growing sites. The others appear to be short-term city land-bank licenses or informal stewardship. Not disqualifying; material to any decision about multi-year support.

- **Next re-validation due:** 2027-06-11.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. The full screening battery is not copied here; in a real bundle it would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0001`.*

> There is no long-form report behind this determination, because there was no determination. In a real bundle this is where the pointer to the internal report host would go, along with a note about whether it's reachable.

<!-- Next re-validation (due 2027-06-11) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
