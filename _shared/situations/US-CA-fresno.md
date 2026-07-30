---
type: situation
title: "Fresno County, California"
description: "Situation node for Fresno County, California. The place three organizations in this collection operate in — not the organizations."
aliases: ["US-CA-fresno", "Fresno County", "Fresno, CA"]
tags: ["cskg", "hub", "situation", "united-states", "rural"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "situation/US-CA-Fresno"
country: "US"
subdivision: "US-CA"
locality: "Fresno County, California"
x-civic:
  profile: civic/0.6
---

# Fresno County, California

**A shared situation node.** Organizations carry this place key in optional `x-civic.situation`; the Members list below is generated from that key by `scripts/build_hubs.py`.

A *situation* describes a **place, not an organization.**

## Community indicators
<!-- STUB — the statistical layer attaches here. Deliberately not populated. -->

**Stub, and deliberately empty** — see [index](index.md) for why real statistics about real places are not fabricated in this collection.

What would populate it, for the organizations linking here:

- **Population, income, and poverty**, including the unincorporated communities — US Census Bureau, ACS
- **Agricultural employment**, seasonality, and H-2A usage — USDA; state labour agency
- **Domestic well water quality** — state water board records for nitrate and arsenic exceedance in unincorporated communities. Directly relevant to one member's bottled-water programme
- **Health professional shortage designations** and clinic coverage — HRSA
- **Broadband and mobile coverage** in the unincorporated county — FCC, and note that FCC coverage maps have historically overstated rural availability, which matters here
- **Language spoken at home**, including Indigenous Mexican languages that census categories capture poorly
- **Transit availability** — effectively none across much of the service area

## Three organizations, three program areas, one population

Fresno County hosts three of the fifteen — food security, legal aid, and rural health — and unlike the [Detroit](US-MI-detroit.md) cluster, **they substantially serve the same people.** Farmworker households appear in all three bundles: at a mobile pantry, in a wage claim, and in a clinic's migrant and seasonal agricultural worker programme.

That makes this the collection's best cluster for a specific question: **what does it look like when three organizations hold different fragments of the same household's situation, and none of them can see the others' fragment?**

Each holds what its own work requires and no more. The pantry deliberately holds nothing identifying. The Law Center's case files are privileged. The clinic's records are PHI. **Three organizations, one family, three information silos that all exist for good reasons** — and no amount of goodwill or interoperability work should collapse them.

## The shared constraint that belongs to the county

**Connectivity.** Parts of the service area have no reliable mobile coverage, and it defeats things at two members independently:

- [Valle Verde](../../organizations/synthetic-valle-verde-food-network/README.md) acquired four tablets for route data capture in 2021 and abandoned them in six weeks, because the software required a connection to save.
- [Sierra Foothills](../../organizations/synthetic-sierra-foothills-community-health/README.md)' mobile unit **charts on paper** and clinicians write up notes hours later back at base.

Same roads. Same gap. Two organizations, two paper workarounds, and it belongs here rather than in either bundle. [Letcher County](US-KY-letcher.md) carries the strongest version of this argument.

## Organizations here
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Central Valley Farmworker Law Center](../../organizations/synthetic-central-valley-farmworker-law-center/README.md) — Central Valley legal-aid organization representing farmworkers in wage, housing, and immigration matters
- [synthetic-Sierra Foothills Community Health](../../organizations/synthetic-sierra-foothills-community-health/README.md) — federally-supported community health center network in rural Fresno County — the largest organization in this 
- [synthetic-Valle Verde Food Network](../../organizations/synthetic-valle-verde-food-network/README.md) — Central Valley food-security organization serving farmworker communities across unincorporated Fresno County
<!-- /GENERATED -->

## Edges

**One partnership:** Valle Verde ↔ the Law Center. An advocate rides two pantry routes a month and takes intakes at the tailgate — the Law Center's most productive intake channel, because a food line is a place people already trust and a law office is not.

**One edge that leaves the country:** Sierra Foothills holds a `learn_with` link to [Kisumu County, Kenya](KE-KS-kisumu.md), where a much smaller organization solved the offline field-data problem this county's roads created.

## Related

- [K30](../ntee/K30.md), [I80](../ntee/I80.md), [E32](../ntee/E32.md) — the three members' primary codes
- [SDG-10](../sdg/SDG-10.md) — reduced inequalities. Two of the three members
