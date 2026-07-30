---
type: verification
title: "synthetic-Corporación Río Vivo — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved — and a serious caution about automated adverse-media screening."
tags: ["eligibility", "verification", "determination", "synthetic", "colombia"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-06-18T00:00:00Z }
stale_after: 2027-06-18
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0014"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-06-18
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

## Determination v1 — 2026-06-18

**APPROVE**, 89% confidence (MODERATE-HIGH).

**What was checked — again, no IRS records:**

- **NIT confirmed** with the tax authority's identifier structure.
- **Registration confirmed** in the Cámara de Comercio and the RUES public business and social registry — entity existence, legal form (*corporación*, an ESAL), registered address, statutory purpose, and legal representative.
- **RTE status confirmed** — *Régimen Tributario Especial*, the Colombian special tax regime for non-profit entities, which carries its own annual qualification and reporting obligations.
- **Filed annual reporting reviewed** to the extent publicly available.
- **Compliance screening** (OFAC, PEP, debarment, FATF, sanctions) cleared with no matches.
- **Adverse media: see below.** This is the substance of this determination.

**Legibility sits between the collection's two other international cases.** Colombia's RUES is a genuine public registry and better than nothing by a wide margin; it carries less detail than [Poland's KRS](../synthetic-fundacja-prawo-i-schronienie/verification.md), which publishes filed financial statements and full board composition, and far more than what was available for [Nyando in Kenya](../synthetic-nyando-community-health-trust/verification.md). Three countries, three information environments, and the confidence scores track the registries rather than the organizations.

## The adverse-media problem, and it is the most serious note in this collection

**Adverse-media screening on this organization returns a great deal of material, and an automated process could easily convert a campaign against human rights defenders into a compliance finding.**

What the screen surfaces:

- Trade and regional press characterizing the organization as **an obstacle to development and investment** in the region.
- Material alleging it is **externally funded and foreign-directed**, a standard framing used against internationally-supported NGOs.
- At least one piece implying **links to armed groups** — an allegation with no substantiation, which in the Colombian context is among the most dangerous things that can be said about a person or organization, because it can precede violence.
- Records of **legal complaints filed against the organization by companies** it has taken action against.
- A significant volume of **social media activity** attacking named staff.

The determination assessed all of it and cleared it. Here is why that assessment required human judgement:

**Stigmatization of defenders is a documented tactic, not incidental coverage.** Publicly recasting land and environmental defenders as obstacles to progress, as foreign agents, or as guerrilla-linked is a recognized pattern that international human rights bodies have repeatedly identified as a precursor to violence against them. It is produced deliberately, sometimes in volume, and it is designed to look like ordinary controversy.

**An automated screen cannot tell the difference**, and it fails in the worst possible direction. Its inputs are text about an organization; the text is genuinely adverse; the sources are genuinely publications. A model scoring "adverse media volume" will find a great deal, and a rule that lowers confidence or requires escalation will penalize the organization **for having been targeted**.

**The consequence is not a wrong score. It is a mechanism.** If an automated verification system reduces an organization's standing because it is smeared, then **smearing an organization becomes a way to cut off its access to support** — funding, donated software, partnerships, anything gated on verification. The attack acquires a new payload, and the verifying system becomes the delivery vehicle.

That is the strongest reason in this collection for a **human decision point on adverse media for advocacy organizations**, and for treating a high volume of hostile coverage as **a signal requiring interpretation rather than a negative finding**. [The Louisiana bundle](../synthetic-gulf-corridor-justice-project/verification.md) raises a milder version of the same problem; here the stakes include people's lives.

If you are building or evaluating automated screening, **this bundle is the case to test against**, and the correct behaviour is not a cleverer classifier. It is a refusal to decide.

## Scope limitations

**Monitoring methodology: not assessed.** Field instruments with periodic accredited-laboratory verification — a reasonable design under real budget constraints, and not a defensible regulatory monitoring regime. The organization frames its data as establishing a pattern that obliges investigation, which is correct and is not how the numbers read once quoted. See [README](README.md).

**Community-held data: not examined, and correctly so.** Monitoring data belongs to the eleven community organizations, not to Río Vivo. Verification did not request it. **A verification process has no standing to ask an organization for data it does not own**, and one that pressed the point would be asking the organization to breach its agreements. This is a fourth category of unexaminable, alongside undocumented, absent-by-policy, and privileged — and the collection now contains all four.

**Ley 1581 compliance: not assessed.** The organization's obligations under Colombian data protection law were not evaluated. A gap rather than a boundary, and one a US-shaped verification process has no step for — the same structural blind spot as [GDPR in the Polish bundle](../synthetic-fundacja-prawo-i-schronienie/verification.md).

**Noted, not flagged:** the organization's staff receive threats and its office location is known. Security expenditure appears in its budget. Not an eligibility question; material to understanding its cost structure, and a reason to be careful what any downstream system publishes about it.

- **Next re-validation due:** 2027-06-18.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0014`.*

<!-- Next re-validation (due 2027-06-18) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
