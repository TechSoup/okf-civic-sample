---
type: situation
title: "Detroit, Michigan"
description: "Situation node for Detroit, Michigan. The place three organizations in this collection operate in — not the organizations."
aliases: ["US-MI-detroit", "Detroit", "Detroit, MI"]
tags: ["cskg", "hub", "situation", "united-states"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "situation/US-MI-Detroit"
country: "US"
subdivision: "US-MI"
locality: "Detroit, Wayne County, Michigan"
x-civic:
  profile: civic/0.6
---

# Detroit, Michigan (Wayne County)

**A shared situation node.** Organizations carry this place key in optional `x-civic.situation`; the Members list below is generated from that key by `scripts/build_hubs.py`.

A *situation* describes a **place, not an organization.** Community context — population, income, industrial permitting, land availability, labour market — is stored **here, once for the place**, so it is not copied into every organization operating in Detroit.

## Community indicators
<!-- STUB — the statistical layer attaches here. Deliberately not populated. -->

**Stub, and deliberately empty.** The organizations in this collection are fabricated and labelled as such. **Detroit is not.**

Its poverty rate, median household income, asthma hospitalization rates, land-bank inventory, and industrial permitting record are real, published, consequential numbers about a real city. Putting fabricated versions of them in this file would be a worse kind of fabrication than inventing a nonprofit — a synthetic organization cannot be mistaken for real, and **a synthetic statistic about Detroit can.**

What would populate this section, for the organizations that link here:

- **Population, income, and poverty** by neighbourhood — US Census Bureau, American Community Survey
- **Food access geography** — USDA food access research atlas; local food-system assessments
- **Land availability** — the city land bank's parcel inventory, which matters directly to one member
- **Air quality and industrial permitting** — EPA and state environmental agency monitoring and permit records
- **Asthma and respiratory outcomes** — state and county public health surveillance
- **Labour market and apprenticeship landscape** — Bureau of Labor Statistics; state workforce agency

**Data Commons** aggregates several of these and would be a plausible single access path — which is what the real Chapter 510 bundle's Oakland node pointed at. Note that the sources differ by country across this collection; see [index](index.md).

## Why three organizations, three program areas

Detroit hosts the largest cluster in this collection, and the three organizations here are in **three different program areas** — food security, environmental justice, and workforce training. That was arranged deliberately: if each program area occupied its own city, the graph would be five disconnected islands and the only answerable question would be *who else does what I do.*

Because places cross program areas, **"who else works here" is answerable**, and it turns up a food organization, an air-quality project, and a trades institute sharing a city and almost nothing else.

## Organizations here
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Eastside Harvest Collective](../../organizations/synthetic-eastside-harvest-collective/README.md) — Detroit urban-farming and food-distribution organization, with a deliberately unreconciled budget
- [synthetic-Motor City Trades Institute](../../organizations/synthetic-motor-city-trades-institute/README.md) — Detroit pre-apprenticeship and trades-training organization, mid-sized, with real technical debt
- [synthetic-Riverbend Air Alliance](../../organizations/synthetic-riverbend-air-alliance/README.md) — Detroit environmental-justice organization running a community air-monitoring network in an industrial corrido
<!-- /GENERATED -->

## Edges within this place

**One partnership:** Eastside Harvest ↔ Motor City Trades. Farm-crew members who finish a season and want a skilled trade are referred across, with a data-sharing agreement neither organization has ever exercised.

**One edge that leaves:** Riverbend Air holds `coalition_with` links to [New Orleans](US-LA-orleans.md) and [Cali, Colombia](CO-VAC-cali.md) — fenceline-monitoring peers who share methodology and no geography. It has no relationship with either of its Detroit neighbours.

**That asymmetry is the point.** The organization with the closest peers is the one whose peers are farthest away.

## Related

- [K30](../ntee/K30.md), [C20](../ntee/C20.md), [J22](../ntee/J22.md) — the three members' primary codes, all in different branches
- [SDG-11](../sdg/SDG-11.md) — sustainable cities. Two of the three members
