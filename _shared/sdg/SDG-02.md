---
type: classification
title: "SDG 2 — Zero hunger"
description: "UN Sustainable Development Goal 2 — end hunger, achieve food security and improved nutrition, and promote sustainable agriculture."
resource: https://sdgs.un.org/goals
aliases: ["SDG-02", "sdg:2", "SDG 2", "Zero hunger"]
tags: ["cskg", "hub", "sdg", "classification", "food"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "sdg:2"
scheme: "SDG"
scheme_authority: "United Nations"
scheme_uri: "https://sdgs.un.org/goals"
x-civic:
  profile: civic/0.6
---

# SDG 2 — Zero hunger

**A shared classification node.** Organizations carry this goal number in optional `x-civic.sdg`; the Members list below is generated from that key by `scripts/build_hubs.py`.

**End hunger, achieve food security and improved nutrition, and promote sustainable agriculture.**

## The same three organizations as [K30](../ntee/K30.md), and a lesson about granularity

This hub and the NTEE food-service hub contain exactly the same three organizations. Comparing the two is the clearest way to see what the two vocabularies each give up.

**NTEE distinguishes** food service ([K30](../ntee/K30.md)) from food banking ([K31](../ntee/K31.md)) from agricultural production ([K20](../ntee/K20.md)). Three codes, and the differences are real: one of these organizations grows food and the other two source it.

**SDG puts all of that in one goal**, along with global agricultural policy, nutrition science, and famine response.

Neither is wrong. **SDG's coverage is complete and its granularity is coarse; NTEE's granularity is useful and its coverage stops at the US border.** In this collection the food organizations happen to all be American, so nothing is lost here — but see [SDG-03](SDG-03.md) or [SDG-16](SDG-16.md), where SDG reaches organizations NTEE cannot, and the trade pays off.

The practical answer is to carry both and let the query choose, which is what these bundles do.

## Members
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Eastside Harvest Collective](../../organizations/synthetic-eastside-harvest-collective/README.md) — Detroit urban-farming and food-distribution organization, with a deliberately unreconciled budget
- [synthetic-Frogtown Community Table](../../organizations/synthetic-frogtown-community-table/README.md) — culturally-specific food shelf in Saint Paul, Minnesota
- [synthetic-Valle Verde Food Network](../../organizations/synthetic-valle-verde-food-network/README.md) — Central Valley food-security organization serving farmworker communities across unincorporated Fresno County
<!-- /GENERATED -->

**All three deliberately collect no individual identifiers**, for overlapping but distinct reasons — a protective policy at two of them, and at the third a commitment to open-door distribution. Their reasons are recorded in their [population](../../organizations/synthetic-valle-verde-food-network/population.md) files, and the reasons are the only thing distinguishing a policy from a data gap.

## Related

- [K30](../ntee/K30.md) / [K31](../ntee/K31.md) / [K20](../ntee/K20.md) — the same organizations, three ways
- [SDG-01](SDG-01.md) — no poverty. One member claims it; arguably all three could
- [SDG-11](SDG-11.md) — sustainable cities. One member, for its urban agriculture
