---
type: verification
title: "synthetic-North Star Immigrant Defense — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved, with privilege and adversarial-risk limitations on scope."
tags: ["eligibility", "verification", "determination", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-03-05T00:00:00Z }
stale_after: 2027-03-05
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0010"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-03-05
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

## Determination v1 — 2026-03-05

**APPROVE**, 93% confidence (HIGH). The registration ID matched the simulated registry exactly, 501(c)(3) status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches. Governance is documented — a seventeen-member board including four attorney members and two seats reserved for people with lived experience of the immigration system. Bar licensure confirmed for all fourteen attorneys and accreditation confirmed for the nine accredited representatives.

**Debarment screening is materially significant.** The organization holds a county contract for detained representation.

## Two scope limitations, of different kinds

**One: case-level information is privileged and was not examined.** Same boundary as at [the Law Center](../synthetic-central-valley-farmworker-law-center/verification.md) — the information cannot lawfully be provided and requesting it would be improper. A boundary, not a gap.

**Two, and specific to this organization: the verification process itself had to be conducted carefully.** This is worth recording because it is a consideration no other bundle in this collection raises.

Ordinary verification collects and retains documentation about an organization. For an organization whose client list is a target, **the verification record itself becomes a small piece of the attack surface** — a compiled, structured, externally-held file about an organization that expects to be looked for. The determination notes that it deliberately did not request, and does not retain, anything that would identify a client, a pro bono attorney, or the organization's operational security arrangements.

The general point for anyone building verification or bundle infrastructure: **the act of documenting an organization is not neutral for every organization.** Most of the time, more documentation is straightforwardly good — it improves legibility, and this collection's own [discussion of legibility](../synthetic-frogtown-community-table/verification.md) treats that as the desirable direction. For a small number of organizations doing adversarial work, more documentation held in more places is a cost, and a system designed only around the first case will impose it without noticing.

## What is deliberately absent from every public record

The organization tracks **how many rapid-response callers it cannot help** and does not publish the figure, on the grounds that a public number showing most callers get no lawyer would deter calls — and a call that doesn't happen is a person who certainly gets no representation. See [README](README.md) and [population](population.md).

Recorded here as **"Organization-held, not published"** rather than as a gap. It is the most meaningful measure of unmet need this organization has, and it is withheld by a considered judgement of the people closest to the harm.

For anyone building need models from published nonprofit data: this is a case where the missing number is missing for a reason, and imputing it would be substituting an estimate for a decision.

- **Next re-validation due:** 2027-03-05.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0010`.*

<!-- Next re-validation (due 2027-03-05) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
