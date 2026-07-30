---
type: population
title: "synthetic-Sierra Foothills Community Health — Who it serves"
description: "The rural patients the organization serves. Fabricated."
tags: ["population", "beneficiaries", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: registry
    resource: "simulated registry extract"
    title: "Registry record (simulated)"
    author: process:registry-import
    last_modified: 2026-01-15
x-civic:
  profile: civic/0.6
  population: ["PG090000", "PG030000", "PJ130000"]
---

# Who Sierra Foothills serves

**⚠ Synthetic — fabricated data.**

Sierra Foothills serves **rural eastern Fresno County** — about **14,000 distinct patients** a year across roughly **51,000 visits**, drawn from foothill towns and unincorporated communities spread over a service area with no other primary care and no hospital. Roughly **62% are on public insurance**, **19% uninsured** and seen on a sliding scale, the remainder commercially insured or self-pay. *(**mechanical**, simulated — patient counts are reported to the federal health-center program annually and are among the most rigorously audited numbers in this collection.)*

**Note the provenance contrast with the rest of the collection.** Most bundles here carry *derived* population figures — reconstructed, estimated, or unverifiable. This organization's counts are **mechanical and externally audited**, because a federal reporting requirement compels them annually in a defined format. Same field, same apparent shape, radically different evidentiary weight. If you are comparing organizations across this collection, that difference matters more than the numbers do.

## Sub-populations that change how the organization operates

**Migrant and seasonal agricultural worker households** — a dedicated program and roughly a fifth of patients. Care is episodic by necessity: a patient may be in the service area for four months, and a treatment plan that assumes twelve months of continuity fails. The organization's records show the same patient reappearing after eighteen-month gaps, sometimes under a slightly different name spelling, which is the root of a real data problem — see [inventory](technology/inventory.md).

**Patients with no reliable transport** — the reason the mobile unit exists. A ninety-minute drive to a clinic is not a barrier that a reminder text solves.

**Patients seen at the absorbed site** — about 2,600 people whose records live in a **second, older electronic health record system** following a 2023 absorption that was never completed. From the patient's point of view they are patients of one organization. From the data's point of view they are somewhere else. This is the subject of the [volunteer project](technical-volunteers/index.md) and it has clinical consequences, not just administrative ones.

**Spanish-speaking patients** — a majority of the agricultural worker program and a large share overall. The organization staffs bilingually rather than relying on interpretation, which is both better care and a hiring constraint. **Mixtec and Triqui** speakers are served through the interpretation line, with the same limits [the Law Center describes](../synthetic-central-valley-farmworker-law-center/population.md).

## The record-matching problem, stated plainly

An episodic patient population, two clinical systems, name variation across records, and no shared identifier produces a specific hazard: **the same person can exist as two patients, and a clinician may see half a history.** Allergies, medications, and prenatal history are the fields where that matters most.

This is not a reporting inconvenience. It is the reason the migration project in this bundle is scoped as a clinical-safety issue rather than an efficiency one.

*Provenance: **mechanical**[^registry] (simulated) for patient counts and payer mix, from federal program reporting. **Derived** for the sub-population estimates. The duplicate-record estimate is **sourced-directly** and acknowledged by the organization as approximate.*

Community context for Fresno County — rural health-professional shortage designations, transport, agricultural employment, water and air conditions that show up as patient presentations — belongs to the place, not here: see [US-CA-fresno](../../_shared/situations/US-CA-fresno.md). This file says *who*; the situation node says *the conditions around them*. Three organizations in this collection share that node; this one sees the health consequences of what the other two address directly.

[^registry]: Registry record (simulated)
