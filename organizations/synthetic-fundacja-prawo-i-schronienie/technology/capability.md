---
type: technology-capability
title: "synthetic-Fundacja Prawo i Schronienie — Technology capability"
description: "The org's standing on the TechSoup digital-assessment rubric — a US-designed instrument applied to an EU organization. Mocked."
resource: https://assessment.techsoup.org/
tags: ["technology", "capability", "mock", "synthetic", "poland", "gdpr"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Technology capability

> **MOCK, inside a SYNTHETIC bundle.** The organization is fabricated, and even within the fabrication no assessment was run. The levels below are placeholders showing where the [assessment.techsoup.org](https://assessment.techsoup.org/) rubric plugs in. Do not read them as a measurement. This is the slot the **digital-assessment team** fills.

| Domain (assessment.techsoup.org) | Level (mock) | Note |
|---|---|---|
| Digital infrastructure | Established | ~24 seats, managed identity, EU data residency configured deliberately |
| Data & CRM | Established | EU-hosted case management with a DPA; runs the practice |
| Finance systems | Established | Commercial Polish accounting software handling VAT, ZUS, and OPP reporting |
| Cybersecurity & privacy | **Established — and this score is wrong** | See below |
| Staff digital skills | Established | Legal practice at volume in four languages |
| Reporting & measurement | Developing | Reports to EU and Polish funders adequately |

## The rubric cannot see this organization's biggest problem

**Cybersecurity & privacy scores Established, and the organization is in ongoing breach of data protection law.**

What the rubric asks about, and this organization has: endpoint encryption, managed identity, EU data residency on its productivity suite, a data-processing agreement with its case management vendor, a designated data protection officer, Signal for sensitive communication. By every question the instrument poses, this organization is doing well — better than most of the US bundles in this collection.

What the rubric does not ask about, because it was designed in a jurisdiction where these are not obligations:

- **A record of processing activities.** Required. Absent.
- **Lawful basis documented per data category.** Required. Not documented.
- **A data protection impact assessment** for high-risk processing. Required for what this organization plainly does. Absent.
- **A valid mechanism for transfers outside the EEA.** Required. Apparently absent — and personal data including special category data about asylum applicants is transferred to US processors by the organization's own website, daily. See [inventory](inventory.md).
- **Special category data assessment.** Required at a higher bar. Not done.
- **Retention defined per category.** Required. Only broadly defined.

**Five documented legal obligations, unmet, and a live unlawful transfer — none of which appears anywhere on this table.**

## Why this is the collection's strongest argument about assessment instruments

Several bundles here show a rubric mis-scoring an organization: [the Law Center](../../synthetic-central-valley-farmworker-law-center/technology/capability.md), where deliberate privacy choices scan as gaps; [Gulf Corridor](../../synthetic-gulf-corridor-justice-project/technology/capability.md), where the integrity problem has no domain; [North Star](../../synthetic-north-star-immigrant-defense/technology/capability.md), where good practice under an adversarial threat model reads as deficiency.

This one is different and worse. In those cases the instrument produced a **wrong score**. Here it produces a **confidently reassuring score for an organization with an active legal exposure** — and it does so while asking every question it was designed to ask, correctly.

The cause is structural: **a maturity rubric encodes the compliance environment of the place it was written.** Applied across jurisdictions, it does not become less accurate gradually — it becomes silently blind to whole categories of obligation. There is no partial credit and no warning.

Two implications for anyone extending an assessment beyond the US:

1. **The instrument needs a jurisdiction parameter**, and a set of questions that only apply in some jurisdictions. GDPR, and the equivalents in other countries, are not "extra privacy" — they are a different structure with documented artefacts that either exist or don't.
2. **Until then, an assessment of a non-US organization should decline to score privacy at all** rather than score it on US assumptions. A refusal is more honest than an Established.

## And a note on what the rubric got right

The **Established scores on infrastructure, data, and finance are fair and earned.** This is a well-run organization. The EU data residency configuration in particular was a deliberate decision that several better-resourced US organizations in this collection never made about their own donated tenancies.

The compliance gaps are documentation and one contractor's default choices, not competence. That distinction is worth preserving: **the organization is capable and non-compliant**, and those are not the same axis.

*When real assessment data arrives it replaces this table and the warning comes off. The GDPR remediation is the [volunteer project](../technical-volunteers/index.md).*
