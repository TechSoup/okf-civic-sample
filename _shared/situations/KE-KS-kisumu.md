---
type: situation
title: "Kisumu County, Kenya"
description: "Situation node for Kisumu County, Kenya. The place one organization in this collection operates in — not the organization."
aliases: ["KE-KS-kisumu", "Kisumu County", "Kisumu", "Nyando"]
tags: ["cskg", "hub", "situation", "kenya", "international", "rural"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "situation/KE-KS-Kisumu"
country: "KE"
subdivision: "KE-KS"
locality: "Kisumu County (Nyando sub-county), Kenya"
x-civic:
  profile: civic/0.6
---

# Kisumu County, Kenya (Nyando sub-county)

**A shared situation node.** Organizations carry this place key in optional `x-civic.situation`; the Members list below is generated from that key by `scripts/build_hubs.py`.

A *situation* describes a **place, not an organization.**

## Community indicators
<!-- STUB — the statistical layer attaches here. Deliberately not populated. -->

**Stub, and deliberately empty** — see [index](index.md). Kisumu County is a real place and fabricating health statistics about it would be worse than fabricating a nonprofit.

**Sources are Kenyan, and one of them is unusual for this collection:**

- **Population and households** — **KNBS** (Kenya National Bureau of Statistics), census and surveys
- **Health indicators** — the **national health information system**, which is the same system the organization linking here reports into monthly. Note what that means: **the organization is a producer of this node's indicators**, not only a consumer of them
- **Maternal, newborn, and child health** — KNBS Demographic and Health Survey; county health records
- **Malaria burden** — national malaria programme surveillance
- **Water access and treatment** — KNBS; county water authority
- **Flooding in the lower Nyando** — county disaster management; Kenya Meteorological Department. Recurring, seasonal, and it moves households
- **Community health strategy implementation** — national and county policy documents, which define the programme structure the organization operates inside
- **Mobile coverage and electrification** — Communications Authority; rural electrification data

**World Bank** and **Data Commons** carry some KNBS-derived series, which makes this node partly reachable through the same path as the US nodes — and the indicators are not identically defined, so a cross-country comparison built on that convenience will be comparing near-neighbours rather than the same thing.

## The organization here is a producer of this place's data

Worth pulling out, because it does not happen at any other node in this collection.

Every US situation node above would be populated from sources the organizations link to but do not create. Here, **the organization's 142 community health promoters generate household-level data that flows monthly into the national system**, and that system is one of the authoritative sources for this county's health indicators.

**The bundle schema has no way to express that an organization contributes to its own situation node's evidence base.** The `x-civic.situation` edge points one direction and describes the organization as an occupant of a place. In this case it is also a measurement instrument for it.

## The inversion this node holds

The organization linking here has **the best program data in the collection and the worst verifiability.**

9,600 registered households. Structured offline capture. Twelve years of continuous monthly reporting into a national system. It can tell you which promoter catchments had which antenatal completion rates last quarter — a level of routine externally-reported data that no US bundle here approaches.

**And verification returned `INSUFFICIENT_EVIDENCE`.** Not a rejection. Six of seven checks failed on **retrievability, not substance** — the audit exists but is not publicly filed; the trust deed exists but is paper; the trustees are named on it. And the process **had no step for the strongest available evidence**, because it was built to check registries, filings, and web presence.

Its automated technology tier came out **"very low," the lowest of the fifteen bundles**, because a web scan cannot see 142 people walking between households.

## Read this node against Poland

**This is the collection's argument, and it needs both nodes to work.**

| Node | Registry | Outcome |
|---|---|---|
| [Warsaw](PL-MZ-warszawa.md) | Public court register, filed financials, named boards | **APPROVE 0.92 — easier than the US** |
| [Cali](CO-VAC-cali.md) | Real public registry, less depth | APPROVE 0.89 — comparable to the US |
| **Kisumu County** | Paper deed, framework in transition, audits not publicly filed | **No determination — method failure** |

**Verifiability tracks the information environment.** Not the country's wealth, not the organization's competence, and not the quality of its data. If this were the only international node in the collection, the lesson would have been "the global South is hard to verify," which is both wrong and the kind of wrong that gets built into a pipeline.

## And the learning runs uphill

The organization here holds a reciprocal **`learn_with`** edge to [Fresno County, California](US-CA-fresno.md) — the collection's only one, joining two clinics with almost nothing else in common.

The Californian organization has **twenty times the budget** and its mobile unit **charts on paper**, because it never solved the offline field-data problem. The Kenyan organization solved it years ago out of necessity.

**Traverse that edge assuming expertise follows money and you get it backwards.**

## What the place costs the workforce

One more thing that belongs to the place rather than the organization: **mobile data and airtime are a real household expense here**, and the 142 community health promoters — community members on stipends, mostly women — **pay for the data bundles that submit the organization's required reporting.**

That is a transfer from the poorest people in the operation to the organization's donor deliverables, it is unmeasured, and it is a live harm rather than a design constraint. It appears in the bundle's [constraints](../../organizations/synthetic-nyando-community-health-trust/technical-volunteers/constraints.md) as a hard test on any project: does this increase or decrease what a promoter spends?

## Organizations here
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Nyando Community Health Trust](../../organizations/synthetic-nyando-community-health-trust/README.md) — community health organization in Kisumu County, Kenya — technically the most sophisticated field operation in 
<!-- /GENERATED -->

## Related

- [SDG-03](../sdg/SDG-03.md) — good health. Where this organization is reachable, since [E32](../ntee/E32.md) cannot reach it
- [SDG-06](../sdg/SDG-06.md) — clean water
- [PL-MZ-warszawa](PL-MZ-warszawa.md) — the contrasting international case, and the reason this node's lesson is about registries rather than countries
- [US-CA-fresno](US-CA-fresno.md) — the `learn_with` partner
