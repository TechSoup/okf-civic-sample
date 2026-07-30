---
type: classification
title: "SDG 6 — Clean water and sanitation"
description: "UN Sustainable Development Goal 6 — ensure availability and sustainable management of water and sanitation for all."
resource: https://sdgs.un.org/goals
aliases: ["SDG-06", "sdg:6", "SDG 6", "Clean water and sanitation"]
tags: ["cskg", "hub", "sdg", "classification", "water"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "sdg:6"
scheme: "SDG"
scheme_authority: "United Nations"
scheme_uri: "https://sdgs.un.org/goals"
x-civic:
  profile: civic/0.6
---

# SDG 6 — Clean water and sanitation

**A shared classification node.** Organizations carry this goal number in optional `x-civic.sdg`; the Members list below is generated from that key by `scripts/build_hubs.py`.

**Ensure availability and sustainable management of water and sanitation for all.**

## The hub a US-only corpus would not have

**Two members, both international, no US organization.** This is the only hub in the collection with that shape, and it is worth sitting with.

- **Colombia** — [Río Vivo](../../organizations/synthetic-corporacion-rio-vivo/README.md) does watershed defense as its entire purpose: community monitoring of two Cauca tributaries, and legal action about what is discharged into them.
- **Kenya** — [Nyando](../../organizations/synthetic-nyando-community-health-trust/README.md) runs household water treatment and safe storage as core community health work, which becomes flood response for part of every year.

**And a US organization does water work and does not claim the goal.** [Valle Verde](../../organizations/synthetic-valle-verde-food-network/README.md) distributes bottled water to unincorporated Fresno County communities whose domestic wells fail nitrate or arsenic standards. Its own bundle is explicit that this is a stopgap for a drinking-water infrastructure failure it did not cause and cannot fix — and it classifies itself entirely under food codes, because it thinks of itself as a food organization.

So the honest membership of this hub is **three organizations, and one of them does not know it belongs here.** Its water programme is described in its [programs file](../../organizations/synthetic-valle-verde-food-network/programs.md) as the first candidate to become its own file, precisely because calling it food work obscures what it is.

**That is a general pattern worth watching for in any self-classified corpus: a programme that does not fit an organization's identity gets filed under the identity rather than under the programme.**

## Members
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Corporación Río Vivo](../../organizations/synthetic-corporacion-rio-vivo/README.md) — Colombian watershed-defense organization where digital security is physical security, and where the communitie
- [synthetic-Nyando Community Health Trust](../../organizations/synthetic-nyando-community-health-trust/README.md) — community health organization in Kisumu County, Kenya — technically the most sophisticated field operation in 
<!-- /GENERATED -->

## Related

- [SDG-03](SDG-03.md) — good health. Shares the Kenyan member; water and health are one programme there
- [SDG-13](SDG-13.md) — climate action. Shares the Colombian member
- [SDG-16](SDG-16.md) — peace, justice, strong institutions. Shares the Colombian member, whose work is largely legal
- [C30](../ntee/C30.md) — natural resources conservation. The code that most literally describes the Colombian organization's work, and which it cannot carry
