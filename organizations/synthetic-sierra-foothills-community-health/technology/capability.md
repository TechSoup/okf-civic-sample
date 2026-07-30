---
type: technology-capability
title: "synthetic-Sierra Foothills Community Health — Technology capability"
description: "The org's standing on the TechSoup digital-assessment rubric. Mocked."
resource: https://assessment.techsoup.org/
tags: ["technology", "capability", "mock", "synthetic"]
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
| Digital infrastructure | Established | ~95 seats, managed identity, professional IT support under contract |
| Data & CRM | **At risk** | Two unmerged EHRs, a third dental island, quarterly reporting hand-merged from two exports |
| Finance systems | Established | Fund-accounting platform, annual audit, revenue-cycle integration |
| Cybersecurity & privacy | Developing | Strong on clinical systems; administrative tenancy never audited against PHI assumptions |
| Staff digital skills | Established | Clinical staff are fluent in their systems; that is a licensure-adjacent expectation |
| Reporting & measurement | Developing | Federal reporting is rigorous and produced; the process to produce it is a spreadsheet merge |

## The rubric doesn't have a place for the thing that matters

Every domain above is scored on the *administrative* organization, because that is what the rubric is built for. The organization's actual technology risk is **clinical**: a patient can have two records and a clinician can see one of them.

There is no domain on this rubric where "a clinician may be looking at half a medication list" is expressible. It shows up faintly as Data & CRM: At risk, alongside things like a duplicate mailing list.

That is not a criticism of the rubric — it was designed for organizations where the worst data outcome is a bad report. But it means that for a clinical organization, **the rubric's output should be read as a partial assessment of the back office**, and anyone using it to characterize overall technology risk here will understate it substantially.

## Scale changes what the domains mean

Two domains score Established for reasons that have nothing to do with organizational virtue:

- **Digital infrastructure** — this organization can afford contracted IT support. That is a budget fact, not a maturity achievement, and a $430K organization doing everything right would still score lower.
- **Staff digital skills** — clinical staff are fluent in clinical systems because licensure and employment require it. Also not a choice the organization made.

Compare [Frogtown Table](../../synthetic-frogtown-community-table/technology/capability.md) at $430K, which is genuinely well-run and will score lower on both. **Some of what this rubric measures is size.** Worth knowing before comparing scores across a corpus with a twenty-fold budget range.

*When real assessment data arrives it replaces this table and the warning comes off. The At-risk domain here — the unmerged clinical systems — is the [volunteer project](../technical-volunteers/index.md), and unlike most projects in this collection it is a patient-safety issue rather than an efficiency one.*
