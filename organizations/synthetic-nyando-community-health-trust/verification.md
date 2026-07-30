---
type: verification
title: "synthetic-Nyando Community Health Trust — Eligibility & verification"
description: "The organization's simulated verification determination — INSUFFICIENT EVIDENCE. Not a rejection; a method failure."
tags: ["eligibility", "verification", "determination", "synthetic", "kenya", "insufficient-evidence"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0015"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
x-civic:
  profile: civic/0.6
---

# Eligibility & verification

**⚠ Synthetic — this determination was never made. It is fabricated to give the record a realistic shape.**

A **log**, written by the validation system. Each re-validation appends a new entry; nothing is overwritten. Everyone else reads this file; only the validation system writes it. Edit history for the *bundle* is separate — see [log](log.md).

## Current status: **INSUFFICIENT EVIDENCE — no determination reached**

> **This is not a rejection.** Nothing adverse was found. No screening hit, no allegation, no inconsistency, no refusal to cooperate. The process could not assemble enough externally-retrievable documentation to responsibly approve **or** decline, and it stopped rather than guess.
>
> **The correct reading is "we do not know."** A system that renders this as ineligible has converted a limitation of its own method into a finding against an organization.

## Attempt v1 — 2026-07-09 — no determination

**What was checked, and what happened:**

| Check | Result |
|---|---|
| **Registration** | The organization is registered and produced its documentation on request. Its **2011 trust deed is a paper instrument** in a registry office, and Kenya's transition to the current public-benefit-organization framework adds ambiguity about which record is authoritative. **Not confirmable through an external search.** |
| **KRA PIN and tax exemption** | Exists; exemption held. **Not externally verifiable** — the organization holds correspondence, the authority does not publish a searchable list. |
| **Governance** | Trustees are **named in the trust deed**. The deed is paper. **No public record retrievable.** |
| **Financial statements** | **Audited annually.** Audits go to donors and the regulator. **Not publicly filed anywhere.** |
| **Compliance screening** (OFAC, PEP, debarment, adverse media, FATF, sanctions) | **Cleared — no matches.** The one part that worked, because it depends on international lists rather than local records. |
| **Web presence corroboration** | A minimal website and a Facebook page. **Nothing to cross-reference.** |
| **Independent third-party evaluation** | None retrievable. |

**Six of seven checks failed on retrievability rather than on substance.** In every case, the document exists. In no case could this process obtain it independently.

## What the process could not see, and what it says about the process

Here is the part worth dwelling on.

**The organization reports monthly into a national health information system, in a defined format, with data of a quality no other bundle in this collection approaches.** 142 promoters, 9,600 registered households, structured indicators, offline capture, monthly supervision. See [population](population.md) and [inventory](technology/inventory.md).

That reporting is:

- **Continuous** — twelve years of monthly submissions.
- **Externally held** — by a national health authority, not by the organization.
- **Structured and auditable**.
- **A far stronger signal of institutional function** than a filed 990 or a set of published board minutes.

**The verification process did not look at it, because it has no step for it.** It was built to check registries, filings, and web presence — the artefacts a US nonprofit produces. It has no notion that an organization's most rigorous external accountability might run through a sectoral government reporting system in another country.

So: **the best available evidence about this organization was invisible to a process that concluded it could not find enough evidence.**

## Compare across the three international bundles

| | Registry | Financials | Verifiability | Outcome |
|---|---|---|---|---|
| [Poland](../synthetic-fundacja-prawo-i-schronienie/verification.md) | Public court register, structured, named boards | Filed publicly in a repository | **Better than the US** | APPROVE 0.92 |
| [Colombia](../synthetic-corporacion-rio-vivo/verification.md) | Real public registry, less depth | Partially public | **Comparable to the US** | APPROVE 0.89 |
| **Kenya (this bundle)** | Paper deed, framework in transition | Audited, not publicly filed | **Method failure** | **No determination** |

**Verifiability tracks the information environment.** Not the country's wealth, not the organization's competence. Poland is easier than America. Kenya is a method failure. If this collection contained only one international bundle it would have taught something false; with three, the actual pattern is visible.

And note the ordering against the US bundles: [Motor City Trades](../synthetic-motor-city-trades-institute/verification.md) scored **0.96** with three participant systems that disagree and an abandoned CRM. This organization cannot be scored at all and knows exactly which of 9,600 households received a fourth antenatal visit last quarter.

## What this bundle tests

- **Can your model represent three states?** Eligible, not eligible, **and not determinable**. A boolean cannot. Collapsing to `false` penalizes an organization for its registry's filing practices; collapsing to `true` waves through anything unverifiable.
- **Does "insufficient evidence" propagate correctly?** This organization holds a `learn_with` edge to [Sierra Foothills](../synthetic-sierra-foothills-community-health/verification.md), which is approved. Neither status should affect the other.
- **Does your process have a path forward?** An undetermined organization needs a next step — a documented alternative evidence route — not permanent limbo. See below.
- **Does your pipeline distinguish "no evidence found" from "adverse evidence found"?** They produce the same absence of a positive determination and mean opposite things.
- **Would your process have looked at the national health reporting?** Almost certainly not. That is the finding.

## What should happen next

The organization is verifiable. Not through this method.

An alternative evidence route would include: **the audited financial statements** (the organization will provide them; they are simply not public), **the trust deed** (a paper document that can be obtained or attested), **a reference from the county health department** it works alongside, **confirmation from the two international donors** who fund it and who have conducted their own due diligence, and **its national health information system reporting record**.

Every one of those is stronger than what was searched for. **All of them require asking rather than searching**, and a process designed to scale by searching has no step for asking.

That is the general lesson: **automated verification scales by looking in places where records are published, and it systematically fails organizations whose records are real, rigorous, and elsewhere.** The failure is not random — it correlates with jurisdiction, with organization size, and with proximity to institutions that publish. A system that treats its own reach as the boundary of what exists will keep drawing that conclusion, at scale, about the same kinds of organizations.

<!-- No determination reached. A v2 attempt should use the alternative evidence route above rather than repeating v1. -->

[^determination]: Validation determination (simulated)
