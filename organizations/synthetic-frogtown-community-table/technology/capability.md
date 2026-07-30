---
type: technology-capability
title: synthetic-Frogtown Community Table — Technology capability
description: The organization's standing on a digital-assessment rubric, and why a composite score would describe it wrongly. Mocked.
tags: [technology, capability, mock, synthetic]
resource: https://assessment.techsoup.org/
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Technology capability

> **MOCK, inside a SYNTHETIC bundle.** Two layers of unreality: the organization is fabricated, and even within the fabrication no assessment was run. The levels below are placeholders showing where a rubric plugs in. Do not read them as a measurement.

Note the frontmatter: `status: draft`. That is core OKF v0.2 §5.4 doing exactly what it is for — this record is not yet reviewed and possibly incomplete, and a consumer can tell without reading the warning banner. There is **no `verified` key**, so the record sits at the *unverified* trust tier, which is correct.

| Domain | Level (mock) | Note |
|---|---|---|
| Digital infrastructure | Developing | One suite, 6 seats, single identity, 3 ageing desktops. Small, coherent, adequate |
| Data & CRM | **Established** | Donor database used properly and reconciled monthly; shelf counts in two consistent sheets |
| Finance systems | Established | Accounting system right-sized, monthly reconciliation against the donor database |
| Cybersecurity & privacy | **At risk** | Endpoints fully covered — but the website taking $70K a year is unmaintained and unowned |
| Staff digital skills | Developing | 4.5 FTE who use their tools well; nobody's job is systems |
| Reporting & measurement | Developing | Reports what the food bank requires, accurately. Nothing beyond it |

## The scoring problem this record exposes

Look at the shape. **Established on data and finance. At risk on security. Developing elsewhere.** Any composite would land this organization around "developing" — a middling score for a middling organization, which is not what this is.

Two distortions are worth separating.

**Some of these scores are measuring budget, not practice.** "Digital infrastructure: Developing" reflects three ageing desktops and six seats. There is no version of this organization at $430K that scores Established on infrastructure, however well it is run. A $7.9M organization scores higher partly because it can afford contracted IT support. **That is a size difference presented as a maturity difference.**

**One At-risk is worth more than five Developings.** The single security item — an unmaintained, unowned donation form processing a sixth of the organization's revenue — is more consequential than everything else on this table combined. In a composite it becomes one-sixth of a number.

**The generalizable point:** this organization's actual profile is *excellent practice at small scale with one dangerous hole.* A flattened score says *unremarkable*. The specific, actionable finding disappears into the average, and what survives is a judgement that mostly reflects revenue.

## What the rubric gets right

The **Data & CRM: Established** score is correct and worth dwelling on, because it is the domain where comparable organizations are usually weakest. This one keeps donor records properly, reconciles them monthly against its accounting, keeps shelf data separate with a deliberate no-names policy, and has no shadow systems.

It is also exactly the domain a website fingerprint cannot see, which is why the automated tier in [inventory.md](inventory.md) came out "low."

*When real assessment data arrives it replaces this table, `status` moves to `stable`, and a `verified` entry gets added. The At-risk domain is the [volunteer project](../technical-volunteers/index.md), and it is genuinely the only thing here that needs doing.*
