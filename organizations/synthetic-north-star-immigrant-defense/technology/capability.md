---
type: technology-capability
title: "synthetic-North Star Immigrant Defense — Technology capability"
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
| Digital infrastructure | **Established** | ~30 seats, conditional access and device policy actually configured and reviewed |
| Data & CRM | Developing | Case platform is solid; four systems that don't connect; pro bono network in spreadsheets |
| Finance systems | Established | Appropriate for size; audited |
| Cybersecurity & privacy | **Established — and the rubric can't see why** | See below |
| Staff digital skills | Established | Litigation practice at volume; genuine document and deadline fluency |
| Reporting & measurement | Developing | Reports what funders require; the number that matters is deliberately unpublished |

## The security score needs an explanation the rubric has no room for

**Cybersecurity & privacy: Established** — but almost none of the evidence for that score is the kind of thing a rubric asks about.

What a rubric typically looks for: endpoint protection, MFA, backup, a privacy policy, staff training. This organization has most of those, and they are not what makes it secure.

What actually makes it secure:

- **A threat model it can state**, including lawful compulsion, device seizure at borders, and targeted harassment.
- **Deliberately short retention**, because data not held cannot be compelled.
- **Deliberately minimal logging**, because an access log is a document about staff and clients that a hostile party would value.
- **No client portal**, because an account is a durable record of who is a client.
- **A clean-device travel protocol**, which appears in no inventory and no scan.

Four of those five would be scored as **deficiencies** by an automated assessment: missing analytics, missing audit logging, missing client portal, short retention. The fifth is invisible.

So this organization would likely score **worse** on an automated cybersecurity assessment than an organization with comprehensive logging, long retention, and a convenient portal — while being considerably harder to compromise and considerably better prepared for the specific things that actually threaten it.

**This is the strongest version of a claim this collection makes repeatedly:** maturity rubrics measure the presence of practices, and some practices are context-dependent in a way that inverts their sign. Compare [the Law Center](../../synthetic-central-valley-farmworker-law-center/technology/capability.md), which carries the same rubric twice to show the gap between the automated and informed readings.

## Where the organization is genuinely weak

Not in the places the rubric would flag. Two real weaknesses, both invisible from outside:

**The pro bono network's security posture is unknown and unmanaged.** Ninety outside attorneys hold North Star client files on their own firm infrastructure. The organization has no visibility and no standard. Given the threat model, this is the largest single exposure in the bundle, and it is not on any domain of this rubric because it concerns people who are not the organization's staff using systems that are not the organization's systems.

**Concentration in the rapid-response arrangement.** A phone tree and a shared log providing 24-hour coverage for the organization's most urgent function. Chosen deliberately over an answering service, and still fragile.

*When real assessment data arrives it replaces this table and the warning comes off. The [volunteer project](../technical-volunteers/index.md) addresses the pro bono seam — both the tracking gap and, more importantly, the security question underneath it.*
