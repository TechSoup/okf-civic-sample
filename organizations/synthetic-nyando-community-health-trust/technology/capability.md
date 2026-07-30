---
type: technology-capability
title: "synthetic-Nyando Community Health Trust — Technology capability"
description: "The org's standing on the TechSoup digital-assessment rubric — the collection's largest gap between automated and informed readings. Mocked."
resource: https://assessment.techsoup.org/
tags: ["technology", "capability", "mock", "synthetic", "kenya"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Technology capability

> **MOCK, inside a SYNTHETIC bundle.** The organization is fabricated, and even within the fabrication no assessment was run. The levels below are placeholders showing where the [assessment.techsoup.org](https://assessment.techsoup.org/) rubric plugs in. Do not read them as a measurement.

## The two readings, and the gap between them is the widest in this collection

### As an automated assessment scores it

| Domain | Level (automated) | What the signal said |
|---|---|---|
| Digital infrastructure | **At risk** | Basic site builder; nothing detected |
| Data & CRM | **Unknown** | No CRM, no platform, nothing detected |
| Finance systems | **Unknown** | Nothing detected |
| Cybersecurity & privacy | **At risk** | No privacy policy, no protection layer, no TLS best practice |
| Staff digital skills | **Unknown** | Not assessed |
| Reporting & measurement | **At risk** | No analytics, no dashboards, nothing detected |

**Overall: very low digital maturity — the lowest of the fifteen bundles.** Generated recommendations would include implementing a CRM, adopting cloud tools, adding analytics, and building digital capacity among staff.

### As it should be scored, with the sourced-directly lane

| Domain | Level (informed) | Reality |
|---|---|---|
| Digital infrastructure | Developing | Modest office IT; **solar charging and a device fleet that functions in a place with unreliable power** |
| Data & CRM | **Established — best in the collection** | 142 offline-first mobile collectors, structured household registers for 9,600 households, twelve years of continuous monthly submissions to a national system |
| Finance systems | Developing | Commercial local accounting; **annually audited** |
| Cybersecurity & privacy | Developing | Endpoint coverage on office machines; household data on ~30 promoter-owned handsets is a real gap; Kenyan Data Protection Act obligations unassessed |
| Staff digital skills | **Established** | 23 staff running monthly data-quality supervision for 142 field workers. This is the capability |
| Reporting & measurement | **Established** | More rigorous, more continuous, and more externally accountable than any other bundle here |

## Four domains went from At risk or Unknown to Established

That is not a calibration error. It is a **category error**, and the mechanism is worth stating precisely:

**The automated assessment measures how much an organization talks to the internet.** Website, CRM, cloud services, analytics — these are the observable traces of an organization whose operations pass through the public web. This organization's operations pass through **142 people walking between households in a rural sub-county, and a government reporting system.** Neither leaves a trace a web scan can find.

The scan is not returning a wrong measurement. **It is returning a correct measurement of the wrong thing**, and then a maturity label is attached to it.

## Why this matters more than the other mis-scorings in this collection

Several bundles here show a rubric getting an organization wrong. [The Law Center](../../synthetic-central-valley-farmworker-law-center/technology/capability.md) loses points for deliberate privacy choices. [The Polish bundle](../../synthetic-fundacja-prawo-i-schronienie/technology/capability.md) gets a reassuring score while in legal breach. [The Colombian bundle](../../synthetic-corporacion-rio-vivo/technology/capability.md) would receive advice that endangers people.

**This one is the systematic case.** The others are individual mismatches between an instrument and a context. This is a bias with a **direction**: web-observable signal under-measures organizations that are rural, offline, non-Anglophone, or operating outside high-income countries. Those characteristics correlate. **The same organizations get under-scored, consistently, at scale, for structural reasons.**

Three consequences worth carrying past this bundle:

1. **A maturity score built on observable web signal should not be published as a maturity score.** It is a measure of digital surface area. Naming it accurately would prevent most of the harm.
2. **"Unknown" must not decay into "weak."** Three domains here scored Unknown purely because nothing was detected, and the composite fell accordingly. An honest pipeline would refuse to produce a composite from this much absence.
3. **The `sourced-directly` lane is not an enrichment. For some organizations it is the only lane that contains anything true.** Asking does not scale, and the organizations for which it is indispensable are precisely the ones a scaled process will describe worst.

## And the genuine weaknesses, none of which the automated table found

- **Household data on ~30 promoter-owned handsets**, with no documented policy for what happens when a device is sold, shared, or lost.
- **Kenyan Data Protection Act 2019 obligations unassessed** — the same jurisdictional blind spot as [GDPR in the Polish bundle](../../synthetic-fundacja-prawo-i-schronienie/technology/capability.md).
- **Promoters absorbing data and airtime costs** for the organization's reporting. An equity failure rather than a technical one, and unmeasured.
- **No documented continuity** for the mobile platform's hosting, or for household registers when a promoter leaves.
- **Data flows up and does not come back** — the organization cannot easily use its own data for management. The [volunteer project](../technical-volunteers/index.md).

*When real assessment data arrives it replaces this table and the warning comes off.*
