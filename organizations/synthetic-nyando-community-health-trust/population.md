---
type: population
title: "synthetic-Nyando Community Health Trust — Who it serves"
description: "The rural households in Nyando the organization serves. Fabricated."
tags: ["population", "beneficiaries", "synthetic", "kenya"]
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
  population: ["PG090000", "PH040000", "PA010000"]
---

# Who Nyando Health serves

**⚠ Synthetic — fabricated data. And note that this bundle's [verification returned insufficient evidence](verification.md).**

Nyando Health serves **rural households in a sub-county of Kisumu County**, western Kenya — roughly **9,600 households**, something over **44,000 people**, in an area of smallholder farming, fishing, and seasonal flooding along the lower Nyando. Coverage is organized around **142 community health promoters**, each responsible for a defined catchment of about 65–70 households. *(**mechanical**, simulated — household registers are maintained by the promoters and reported into the national health information system, which makes these the most precisely enumerated figures in this collection.)*

## Note the provenance, because it contradicts the bundle's verification status

Look at the label on that paragraph: **mechanical**, from a structured register reported into a national system. Not *derived*, not an estimate.

**This organization knows exactly who it serves.** Every household in its coverage area is registered, assigned to a named promoter's catchment, and visited on a schedule. It can produce household-level counts by catchment, by month, by indicator.

Set that against the twelve US bundles. [Eastside Harvest](../synthetic-eastside-harvest-collective/population.md) counts households at a distribution and knows nothing else. [Riverbend Air](../synthetic-riverbend-air-alliance/population.md) cannot say how many people it served. [Black Mountain](../synthetic-black-mountain-workforce-partnership/population.md) does not know if its graduates are still employed. **This organization's population data is better than any of them**, and it is the bundle a verification process could not confirm exists.

That gap — **excellent program data, unretrievable institutional documentation** — is the whole argument of this bundle. They are different kinds of evidence and a process that measures one will draw the wrong conclusion about the other.

## Sub-populations the programme is organized around

**Pregnant women and mothers of children under five** — the core of the community health strategy. Antenatal visit completion, facility delivery, immunization, and growth monitoring. The indicators the national system asks for and the ones the promoters are trained around.

**Households without treated water** — the majority, seasonally. Household water treatment and safe storage, which is health work and also flood-response work.

**Households displaced by seasonal flooding** — recurring rather than exceptional. The lower Nyando floods, households move, and a promoter's register has to follow people who are not where they were. **The organization tracks households through displacement**, which is genuinely difficult and is the sort of thing no external evaluation ever sees.

**Community health promoters themselves** — 142 people, predominantly women, who are community members with stipends rather than salaried staff. They are simultaneously the workforce and part of the population, and their situation is the organization's central equity problem. See below.

## The promoters are the ethical crux and it belongs in this file

Community health promoters here are **not volunteers in the way a Western organization means it, and not employees either.** They are community members, mostly women, doing structured health work for a stipend, and:

- They **absorb costs the organization does not fully cover** — most consequentially **mobile data and airtime** for the reporting the organization requires of them, and sometimes transport. A promoter paying for the data bundle that submits her own reporting is subsidizing the organization's donor deliverables out of a stipend.
- **The stipend model's sustainability is contested nationally**, and has been for years. Who should pay community health workers is a live policy question, not a settled one.
- Their **status is ambiguous** in a way that would not be tolerated for salaried staff, and the organization knows it.

The organization is candid about this and describes it as the thing it would fix first with unrestricted money. **Anything reading this bundle to design something for the promoters should treat their unpaid costs as a live harm rather than a design constraint** — and note that the [volunteer project](technical-volunteers/index.md) is scoped partly around not increasing them.

## Language

**[[Dholuo]]** is the language of the work — promoters visit households in Dholuo. **Kiswahili** is used in mixed settings. **English** is the language of reporting, funders, and the national health information system.

That layering has a consequence worth stating: **the people who produce the data work in one language and the system that receives it operates in another.** Training materials, form labels, and indicator definitions cross that boundary, and meaning is lost in both directions. Several promoters have limited written English and are recording into English-labelled forms.

*Provenance: **mechanical**[^registry] (simulated) for household and coverage figures, from promoter registers reported into the national system. **Sourced-directly** for the promoter cost and status detail.*

Community context for Kisumu County and the Nyando basin — population, health indicators, flooding, water access, the county health system and its facilities — belongs to the place, not here: see [KE-KS-kisumu](../../_shared/situations/KE-KS-kisumu.md). This file says *who*; the situation node says *the conditions around them*.

[^registry]: Registry record (simulated)
