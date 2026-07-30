---
type: classification
title: "SDG 3 — Good health and well-being"
description: "UN Sustainable Development Goal 3 — ensure healthy lives and promote well-being for all at all ages."
resource: https://sdgs.un.org/goals
aliases: ["SDG-03", "sdg:3", "SDG 3", "Good health and well-being"]
tags: ["cskg", "hub", "sdg", "classification", "health"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "sdg:3"
scheme: "SDG"
scheme_authority: "United Nations"
scheme_uri: "https://sdgs.un.org/goals"
x-civic:
  profile: civic/0.6
---

# SDG 3 — Good health and well-being

**A shared classification node.** Organizations carry this goal number in optional `x-civic.sdg`; the Members list below is generated from that key by `scripts/build_hubs.py`.

**Ensure healthy lives and promote well-being for all at all ages.**

## The largest hub in the collection, and the one that shows what SDG is for

**Five members, on two continents, in two different program areas** — three clinical organizations and two environmental-justice organizations that frame their work as health work.

**No NTEE hub can do this.** The clinics are in [E32](../ntee/E32.md) (two of three — the Kenyan one cannot be), the environmental organizations are in [C20](../ntee/C20.md) (two of three — the Colombian one cannot be), and nothing in the NTEE layer connects a rural clinic to an air-quality monitoring project even though both are about whether people get sick.

Here is the coverage arithmetic across the two vocabularies for these same organizations:

| | NTEE reaches | SDG reaches |
|---|---|---|
| Clinics | 2 of 3 | **3 of 3** |
| Environmental-justice organizations | 2 of 3 | **3 of 3** |
| Both groups together, in one hub | **Not possible** | **Yes** |

**This is the payoff for SDG's coarseness.** [SDG-02](SDG-02.md) shows the cost — one goal where NTEE offers three useful distinctions. This hub shows the benefit: five organizations that genuinely share a purpose, across borders and across sector boundaries, reachable in one edge.

## Two organizations here are worth reading against each other

[Sierra Foothills](../../organizations/synthetic-sierra-foothills-community-health/README.md) ($7.9M, California) and [Nyando](../../organizations/synthetic-nyando-community-health-trust/README.md) (KES 62M, Kenya) hold a reciprocal **`learn_with`** edge — the collection's only one, and an edge no required field would have produced.

The Californian organization has twenty times the budget and **charts on paper in its mobile unit.** The Kenyan organization solved offline field data collection years ago out of necessity and runs 142 promoters on it. **Verification could not confirm the Kenyan organization exists**, and its program data is the best in the collection.

Traverse that edge assuming expertise flows from the larger budget and you get it backwards.

## Members
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Cumberland Gap Health Cooperative](../../organizations/synthetic-cumberland-gap-health-cooperative/README.md) — small rural clinic in Letcher County, Kentucky, where the broadband problem belongs to the patients as much as
- [synthetic-Gulf Corridor Justice Project](../../organizations/synthetic-gulf-corridor-justice-project/README.md) — Louisiana environmental-justice organization whose public evidence archive is contested by a well-resourced ad
- [synthetic-Nyando Community Health Trust](../../organizations/synthetic-nyando-community-health-trust/README.md) — community health organization in Kisumu County, Kenya — technically the most sophisticated field operation in 
- [synthetic-Riverbend Air Alliance](../../organizations/synthetic-riverbend-air-alliance/README.md) — Detroit environmental-justice organization running a community air-monitoring network in an industrial corrido
- [synthetic-Sierra Foothills Community Health](../../organizations/synthetic-sierra-foothills-community-health/README.md) — federally-supported community health center network in rural Fresno County — the largest organization in this 
<!-- /GENERATED -->

## Related

- [E32](../ntee/E32.md) — community clinics. Two of the three clinics here
- [C20](../ntee/C20.md) — pollution abatement. Two of the environmental organizations here
- [SDG-06](SDG-06.md) — clean water. Shares the Kenyan member
- [SDG-13](SDG-13.md) — climate action. Shares both environmental members
