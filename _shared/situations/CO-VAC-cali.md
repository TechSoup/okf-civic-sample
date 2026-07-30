---
type: situation
title: "Cali and the Cauca basin, Valle del Cauca, Colombia"
description: "Situation node for Cali and the Cauca basin. The place one organization in this collection operates in — not the organization."
aliases: ["CO-VAC-cali", "Cali", "Valle del Cauca", "Cauca basin"]
tags: ["cskg", "hub", "situation", "colombia", "international"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "situation/CO-VAC-Cali"
country: "CO"
subdivision: "CO-VAC"
locality: "Cali and the lower Cauca basin, Valle del Cauca, Colombia"
x-civic:
  profile: civic/0.6
---

# Cali and the Cauca basin (Valle del Cauca, Colombia)

**A shared situation node.** Organizations carry this place key in optional `x-civic.situation`; the Members list below is generated from that key by `scripts/build_hubs.py`.

A *situation* describes a **place, not an organization.**

## Community indicators
<!-- STUB — the statistical layer attaches here. Deliberately not populated, and here the reason is stronger than elsewhere. -->

**Stub, and deliberately empty.** Two reasons, and the second one is specific to this node.

**First, the general reason** — see [index](index.md). Real places get real statistics or none.

**Second, and more serious: some data about this place is dangerous.** Community-level detail about collective territories in a contested area — populations, locations, leadership — is information with uses. The organization linking here **reduces the precision of coordinates in anything that circulates**, and a situation node stuffed with fine-grained territorial data would undo that at the level above.

So this stub stays a stub, and any future population of it should carry the same precision discipline the organization applies to its own records.

**Sources, when populated, are Colombian:**

- **Population, income, and poverty** — **DANE** (*Departamento Administrativo Nacional de Estadística*)
- **Collective territories** — *consejos comunitarios* and *resguardos* registries, at a deliberately coarse level
- **Water quality in the Cauca basin** — regional environmental authority (CVC) and national monitoring
- **Mining titles, licences, and agro-industrial discharge permits** — ANLA and mining authority records
- **Security situation for defenders** — Defensoría del Pueblo; UN human rights office reporting; and note that **the numbers here are contested and lag**

**Not** US Census, not ACS. See [index](index.md) for why treating community context as one uniform layer across three continents produces incomparable comparisons.

## The place fact that dominates everything

**Colombia is among the most dangerous countries in the world to defend land, water, or territory**, and the people at greatest risk are rural community leaders — precisely the eleven community organizations that the organization linking here accompanies.

This belongs at the situation level rather than inside the bundle, because **it is a property of the place** and it would apply to any organization doing this work here. Its consequences run through every part of the bundle:

- A dataset linking a named community monitor to a monitoring point and a schedule is **a targeting package**, not a privacy concern.
- **No map of monitoring points is published**, though both of this organization's coalition partners in [Detroit](US-MI-detroit.md) and [New Orleans](US-LA-orleans.md) publish theirs and are right to.
- Encryption, compartmentalization, and paper-for-sensitive-matters are **protective measures**, and an [automated assessment recommends removing all four](../../organizations/synthetic-corporacion-rio-vivo/technology/capability.md).
- Adverse-media screening returns heavy results because **stigmatizing defenders is a documented tactic that has preceded violence** — which means an automated screen can convert an attack campaign into a compliance finding.

**A situation node is the right place for this** precisely because it is not about one organization. Anyone building tooling for this region needs it before they see a single bundle.

## Collective rights change what a place is

Much of the territory here is held under **collective title** — Afro-Colombian *consejos comunitarios* and Indigenous *resguardos*, with recognized governance institutions and real authority, including the constitutional right to **prior consultation** (*consulta previa*) before projects affecting their territory.

That has a modelling consequence the schema does not handle: **the community organizations here are governance bodies, not beneficiary populations.** They decide. The organization linking here describes its relationship as *acompañamiento* — accompaniment — and **the monitoring data belongs to them, not to the NGO holding it.**

There is no way in the current bundle structure to say "we hold this dataset, we do not own it, and here is who decides about it." That gap affects every organization working with communities that assert data sovereignty, which is not an exotic case.

## The third information environment

Colombia's **RUES** and Cámara de Comercio registration is a genuine public registry — less detailed than [Poland's KRS](PL-MZ-warszawa.md), considerably more retrievable than what was available for [Kisumu County](KE-KS-kisumu.md). The organization verified at **0.89**, roughly comparable to the US bundles.

Three international nodes, three positions: **better than the US, comparable to the US, and a method failure.** That range is the collection's argument.

Data protection here is **Ley 1581 de 2012** (*habeas data*) with the Superintendencia de Industria y Comercio as authority — a third structure, neither GDPR nor the US absence of a general law.

## Organizations here
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Corporación Río Vivo](../../organizations/synthetic-corporacion-rio-vivo/README.md) — Colombian watershed-defense organization where digital security is physical security, and where the communitie
<!-- /GENERATED -->

## Related

- [SDG-06](../sdg/SDG-06.md) — clean water. No US member in that hub
- [SDG-13](../sdg/SDG-13.md) — climate action. The coalition triangle
- [SDG-16](../sdg/SDG-16.md) — peace, justice, strong institutions
- [C20](../ntee/C20.md) — the code this organization's work fits and cannot carry
- [US-MI-detroit](US-MI-detroit.md) / [US-LA-orleans](US-LA-orleans.md) — its coalition partners, and the same method requiring incompatible practice
