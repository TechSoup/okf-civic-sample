---
type: population
title: "synthetic-Corporación Río Vivo — Who it works with"
description: "The river communities the organization accompanies. Fabricated."
tags: ["population", "beneficiaries", "synthetic", "colombia"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-rio-vivo.example.org"
    title: "The organization's own website and published materials"
    author: human:org-staff
    last_modified: 2026-03-02
x-civic:
  profile: civic/0.6
  population: ["PE030000", "PG090000", "PJ080000"]
---

# Who Río Vivo works with

**⚠ Synthetic — fabricated data.**

Note the verb. **Río Vivo does not describe itself as serving these communities; it describes itself as accompanying them** — *acompañamiento*, a word with real weight in Latin American organizing that means the community leads and the organization supports. That distinction is not decoration, and it shapes what this file can and cannot say.

The organization accompanies **eleven community organizations** along two tributaries of the Cauca in Valle del Cauca — Afro-Colombian *[[consejos comunitarios]]*, two [[campesino]] associations, and one Indigenous *cabildo*. Together these represent something over **9,000 people**. *(**derived**, simulated, and see the caution below about why even this number is not straightforwardly the organization's to state.)*

## Collective rights change what a population is

The people here are not individuals receiving a service. Most hold **collective territorial rights** — Afro-Colombian community councils and Indigenous *cabildos* have legally recognized collective title and their own governance institutions, with real authority.

Consequences that a US-shaped population model cannot represent:

- **The unit is the community, not the person.** An *asamblea* decides. There is no meaningful sense in which this organization has 9,000 individual beneficiaries.
- **Consultation is a legal right.** *Consulta previa* — prior consultation — is a constitutional requirement before projects affecting collective territory. The organization provides technical support in those processes; it does not conduct them and does not speak for anyone in them.
- **The community can direct the organization**, and does. This is not a service relationship with the power running the usual way.
- **Even a population count is not the NGO's to publish freely.** The eleven organizations have views about how they are described and counted, and some have specific reasons — a census figure attached to a named territory in a contested area is information with uses.

**The current bundle schema assumes an organization serves individuals it can count.** Here the accurate answer is "eleven organizations, who represent their own members, and who decide what we may say about them." There is no field for that.

## What the organization holds, and why it is dangerous

The monitoring programme generates, unavoidably:

- **Monitoring point locations** — geographic coordinates, in rural territory.
- **Sampling schedules** — when someone will be at a specific place.
- **Names of community monitors** — the people trained to take samples.
- **Community meeting records** — who attended, who spoke, what was decided.

Put together, that is a document describing **where specific named people, in a contested rural area, can be found at predictable times.** See [README](README.md). In a country where killings of land and environmental defenders are documented annually in large numbers, this is not a privacy classification exercise.

The organization's practices follow from that: **monitor identities are compartmentalized**, coordinates are held at reduced precision in anything that circulates, schedules are not written down in shared systems, and published outputs are aggregated to a level the communities have agreed to.

**A well-intentioned volunteer wanting to build a nice map of monitoring points with contributor attribution would be building the single most dangerous artefact this organization could possess.** That sentence is in [constraints](technical-volunteers/constraints.md) too, because it is the specific mistake this bundle exists to prevent.

## Language

**Spanish** is the working language throughout. Some elder members of the Indigenous *cabildo* speak an Indigenous language as a first language, and community meetings in that territory are conducted accordingly with interpretation the community arranges itself — not the NGO.

Literacy varies considerably among community monitors, and several are more comfortable with voice than with written forms. Anything designed for them needs to work that way, the same practical constraint [the California farmworker bundle](../synthetic-valle-verde-food-network/population.md) documents.

## Data protection in Colombia

Colombia has its own regime — **Ley 1581 de 2012**, the *habeas data* law, with the Superintendencia de Industria y Comercio as the authority. It requires authorization for processing, has a category of sensitive data, provides data-subject rights, and requires registration of databases in certain circumstances.

**It is not GDPR and it is not the US absence of a general law.** A third structure, and a corpus with only US bundles plus one European one would leave anyone believing there are two models. See [the Polish bundle](../synthetic-fundacja-prawo-i-schronienie/population.md) for the second.

*Provenance: **derived**[^org-site] (simulated) throughout, and constrained: much of what could be said about these communities is **not the organization's to disclose**. That is a governance fact, not a data gap.*

Community context for Cali and the Cauca basin — the watershed, mining and agro-industrial activity, collective territories, the security situation for defenders — belongs to the place, not here: see [CO-VAC-cali](../../_shared/situations/CO-VAC-cali.md). This file says *who*; the situation node says *the conditions around them*.

[^org-site]: The organization's own website and published materials
