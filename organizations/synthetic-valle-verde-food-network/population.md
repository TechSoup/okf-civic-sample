---
type: population
title: "synthetic-Valle Verde Food Network — Who it serves"
description: "The farmworker households the organization serves. Fabricated."
tags: ["population", "beneficiaries", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: program-reporting
    resource: "simulated programme and funder reporting"
    title: "Programme and funder reporting (simulated)"
    author: process:program-reporting
    last_modified: 2026-02-28
x-civic:
  profile: civic/0.6
  population: ["PJ130000", "PG090000", "PG030000"]
---

# Who Valle Verde serves

**⚠ Synthetic — fabricated data.**

Valle Verde serves **farmworker households in 17 unincorporated communities** across Fresno County — settlements of a few hundred to a few thousand people, most without a grocery store, several without reliable domestic water. Roughly **3,800 households** come through the mobile pantry in a typical month, with sharp seasonal variation. *(**corroborated** at the household level, simulated; individual counts do not exist — see below.)*

## Seasonality is the defining feature

This population's need moves with the agricultural calendar, and it moves in the opposite direction from what people expect. Demand is **highest between harvests**, not during them — the weeks when there is no work are the weeks the food runs out. There is a hard peak in **late winter** before the first pruning and thinning work, and a second in **midsummer** between stone fruit and grapes.

Anything reading this bundle for capacity planning should note that a monthly average describes this organization badly. The February load is roughly double the September load, and the organization's whole operational design — vehicle scheduling, volunteer recruitment, warehouse holding — is built around that curve.

## What is deliberately not collected

**No names. No addresses. No immigration status. Ever.** Valle Verde counts households and boxes, and asks nothing else.

This is a **protective policy, not a data gap**, and the reasoning is straightforward: in this service population, a list of names and addresses is a hazard to the people on it. The organization has declined a funder requirement to collect individual identifiers, and would decline again.

Consequences worth being explicit about, because they will surface in anything built against this bundle:

- The **unduplicated-individuals count** that a state food-bank allocation formula asks for **does not exist and cannot be derived**. The organization estimates from household counts and average household size. The estimate is labeled as an estimate.
- **Demographics are absent** — no age, no household composition, no income verification.
- **Repeat visits are invisible.** A household coming every cycle and a household coming once are the same record, which is to say neither is a record.

*Provenance: **corroborated**[^program-reporting] for household and box counts (simulated, cross-checked against warehouse throughput); **derived** for community-level population; **absent by policy** for everything individual.*

## Language

The service population speaks **Spanish**, **Mixtec**, and **[[Triqui]]**, and the last two are in this context primarily **oral** languages with variation between communities of origin. A meaningful share of adults have limited literacy in any written language.

The practical effect is that **the eleven promotoras are the interface** — not a channel to the interface, the interface itself. Information moves through people who are known in the community and speak the right variant. See [README](README.md) and, for what this means when designing anything, [constraints](technical-volunteers/constraints.md).

Community context for Fresno County — agricultural employment, unincorporated-community water systems, transit, the geography of food access — belongs to the place, not here: see [US-CA-fresno](../../_shared/situations/US-CA-fresno.md). This file says *who*; the situation node says *the conditions around them*. Two organizations in this collection share that situation node and serve overlapping populations from different angles — see [the Law Center's population file](../synthetic-central-valley-farmworker-law-center/population.md).

[^program-reporting]: Programme and funder reporting (simulated)
