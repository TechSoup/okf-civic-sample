---
type: situation
title: "Saint Paul, Minnesota"
description: "Situation node for Saint Paul, Minnesota. The place two organizations in this collection operate in — not the organizations."
aliases: ["US-MN-saint-paul", "Saint Paul", "St. Paul, MN"]
tags: ["cskg", "hub", "situation", "united-states", "urban"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "situation/US-MN-SaintPaul"
country: "US"
subdivision: "US-MN"
locality: "Saint Paul, Ramsey County, Minnesota"
x-civic:
  profile: civic/0.6
---

# Saint Paul, Minnesota (Ramsey County)

**A shared situation node.** Organizations carry this place key in optional `x-civic.situation`; the Members list below is generated from that key by `scripts/build_hubs.py`.

A *situation* describes a **place, not an organization.**

## Community indicators
<!-- STUB — the statistical layer attaches here. Deliberately not populated. -->

**Stub, and deliberately empty** — see [index](index.md).

What would populate it, for the organizations linking here:

- **Immigrant and refugee settlement patterns** by community of origin — US Census Bureau, ACS; state refugee resettlement records. Both members' work is organized around these communities
- **Languages spoken at home** — and note that census language categories **capture Karen, Oromo, and other communities poorly**, sometimes folding them into broader groupings, which matters for anyone using public data to size the populations either member serves
- **Neighbourhood income and poverty** — ACS at tract level
- **Food access** — regional food bank allocation data; USDA
- **Immigration court docket and backlog** for Minnesota cases — Executive Office for Immigration Review
- **Detention facilities used for Minnesota cases**, including out of state, which is central to one member's detained-representation work
- **Enforcement activity** — where published, and the gaps in what is published are themselves relevant

## Two organizations, one set of families, and the trust that connects them

The two members here serve substantially **the same households** from two directions — a culturally-specific food shelf and an immigration legal-defense practice — and the relationship between them is the most instructive thing at this node.

**North Star Defense holds monthly legal clinic hours in Frogtown Table's back room.**

That arrangement works for a reason worth stating: **people will raise an immigration question at a food shelf they already visit, and will not walk into a law office downtown.** Both organizations reached that conclusion independently, and so did [the Farmworker Law Center](../../organizations/synthetic-central-valley-farmworker-law-center/README.md) in California, which sends an advocate to ride mobile pantry routes.

**Three organizations in this collection, in two states, arriving at the same insight: legal intake happens where trust already is.** That pattern is only visible because the collection contains multiple places, and it is a stronger finding than anything either bundle states alone.

## What the pair also demonstrates about verification

These two organizations sit at opposite ends of the collection's legibility range, in the same city:

| | [Frogtown Table](../../organizations/synthetic-frogtown-community-table/README.md) | [North Star Defense](../../organizations/synthetic-north-star-immigrant-defense/README.md) |
|---|---|---|
| Revenue | $430K — smallest in the collection | $2.6M |
| Verification confidence | **0.88 — lowest clean score** | 0.93 |
| Technology stack | **Tidiest in the collection** | Grew 4× in four years; four systems that don't connect |

**The smaller, tidier organization scores lower**, because verification confidence measures how much of an organization has been written down in retrievable places. Frogtown Table's board minutes are in a folder. See [its eligibility file](../../organizations/synthetic-frogtown-community-table/verification.md), which sets the comparison out against a much messier organization scoring 0.96.

## Organizations here
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Frogtown Community Table](../../organizations/synthetic-frogtown-community-table/README.md) — culturally-specific food shelf in Saint Paul, Minnesota
- [synthetic-North Star Immigrant Defense](../../organizations/synthetic-north-star-immigrant-defense/README.md) — Saint Paul immigration legal-defense organization whose client data is a target, not merely confidential
<!-- /GENERATED -->

## Related

- [P84](../ntee/P84.md) — ethnic and immigrant services. **Both members**, which makes this the only place node whose two organizations share a code
- [K30](../ntee/K30.md) / [I80](../ntee/I80.md) — their differing primary codes
- [SDG-10](../sdg/SDG-10.md) — reduced inequalities. Both members
