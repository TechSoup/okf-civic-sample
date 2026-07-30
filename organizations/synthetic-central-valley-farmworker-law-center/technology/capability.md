---
type: technology-capability
title: "synthetic-Central Valley Farmworker Law Center — Technology capability"
description: "The org's standing on the TechSoup digital-assessment rubric. Mocked, and a demonstration of how the rubric mis-scores this org."
resource: https://assessment.techsoup.org/
tags: ["technology", "capability", "mock", "synthetic"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Technology capability

> **MOCK, inside a SYNTHETIC bundle.** The organization is fabricated, and even within the fabrication no assessment was run. The levels below are placeholders showing where the [assessment.techsoup.org](https://assessment.techsoup.org/) rubric plugs in. Do not read them as a measurement.

## Two scorings of the same organization

This bundle carries the rubric **twice**, because the gap between the two is the point.

### As an automated assessment would score it

| Domain | Level (automated) | What the signal said |
|---|---|---|
| Digital infrastructure | Developing | WordPress, nothing notable detected |
| Data & CRM | Unknown | No CRM detected on the website |
| Finance systems | Unknown | Nothing detected |
| Cybersecurity & privacy | Developing | Cloudflare present; no privacy policy detected |
| Staff digital skills | Unknown | Not assessed |
| Reporting & measurement | **At risk** | **No analytics of any kind** |

Overall: **low digital maturity.** Recommended actions would include installing web analytics, adding a chat widget to improve intake conversion, and implementing a CRM.

### As it should be scored, with the sourced-directly lane

| Domain | Level (informed) | Reality |
|---|---|---|
| Digital infrastructure | Established | Microsoft 365, ~19 seats, managed endpoints including travelling laptops |
| Data & CRM | Established | Sector-standard legal-aid case management running the whole practice |
| Finance systems | Established | QuickBooks Online Plus, handles court-awarded fee accounting |
| Cybersecurity & privacy | **Established with one real gap** | Deliberate no-tracker posture, Signal for sensitive comms, endpoint coverage — but the M365 tenancy has never been reviewed |
| Staff digital skills | Established | A legal practice runs on documents and deadlines; this staff is fluent in both |
| Reporting & measurement | Developing | Strong on case reporting; deliberately blind on web, by choice |

Overall: **a well-run small legal practice with one unexamined platform configuration.**

## Why the first table exists in this bundle

Because that is the table a pipeline produces, and someone will act on it. The recommended actions it generates are not merely useless here — **installing analytics and a chat widget on an immigration legal-aid site would create a hazard for the organization's clients.** The advice is confident, standard, and wrong in a way that has consequences for real people.

Three things follow, and they generalize past this bundle:

1. **Automated assessment cannot distinguish absence-by-choice from absence-by-inability.** Not a tuning problem — the information is not in the signal. Only asking recovers it.
2. **"Unknown" is being treated as "weak."** Four domains here scored Unknown or Developing purely because nothing was detected, and the composite score dropped accordingly. An honest pipeline would refuse to produce a composite at all from this much missing data.
3. **The one real gap doesn't appear in the automated table.** The unreviewed Microsoft 365 tenancy holding privileged client material is the organization's actual exposure, and it is invisible from outside. The automated assessment flagged the deliberate privacy protections and missed the genuine risk — precisely inverted.

*When real assessment data arrives it replaces this table and the warning comes off. Compare [Motor City Trades](../../synthetic-motor-city-trades-institute/technology/capability.md) (high verification confidence, worst internal hygiene) and [Riverbend Air](../../synthetic-riverbend-air-alliance/technology/capability.md) (high skill, low stewardship) — the collection deliberately contains several organizations whose maturity score would describe them badly.*
