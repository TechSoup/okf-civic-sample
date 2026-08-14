---
type: org
title: "synthetic-Riverbend Air Alliance"
description: "A fabricated Detroit environmental-justice organization running a community air-monitoring network in an industrial corridor."
resource: https://synthetic-riverbend-air.example.org
aliases: ["synthetic-Riverbend Air", "Riverbend Air Alliance"]
tags: ["org-bundle", "nonprofit", "synthetic", "environmental-justice", "air-quality", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-riverbend-air.example.org"
    title: "The organization's own website and published materials"
    author: human:org-staff
    last_modified: 2026-03-02
  - id: registry
    resource: "simulated registry extract"
    title: "Registry record (simulated)"
    author: process:registry-import
    last_modified: 2026-01-15
x-civic:
  # ---- REQUIRED by civic/0.6. These five keys are the whole profile. ----
  profile: civic/0.6
  subject: ["SC030100", "SC030000"]                 # PCS Subject facet
  population: ["PG100000", "PG030000"]              # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: community-air-monitoring
  registration:
    scheme: "IRS-EIN"
    id: "00-1000002"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["C20", "C30"]      # optional US-only layer; reaches 12 of 15
  sdg: ["3", "11", "13"]        # optional global layer; reaches 15 of 15
  situation: US-MI-detroit
  relations:
    - { target: synthetic-gulf-corridor-justice-project, type: coalition_with }
    - { target: synthetic-corporacion-rio-vivo, type: coalition_with }
  verifiable_by: [techsoup]
---

# synthetic-Riverbend Air Alliance

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Riverbend Air Alliance ("Riverbend Air") monitors air quality in a heavy-industrial corridor of southwest Detroit and puts the resulting numbers in front of regulators. In the organization's own words:

> We are not waiting for the state to tell us what we're breathing. Thirty-one sensors on thirty-one neighbors' houses, reading every two minutes, and the data belongs to the block it was collected on.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it operates a network of **31 low-cost particulate sensors** hosted on residents' homes and porches, files technical comments on **air-permit applications**, runs an **asthma-outreach partnership** with two neighborhood clinics, and trains a small **youth science corps** in reading and presenting the data. It formed in **2016** out of a block-club campaign against a truck-routing decision, and received IRS exemption in **2017**.

It is a **small** nonprofit — annual revenue around **$680,000**, assets around **$240,000**, most of it foundation-funded with one significant government subaward. Its address is **3300 Foundry Line Road, Detroit, MI 48217**. *(mechanical[^registry], simulated.)*

- **What it does →** classified as [C20](../../_shared/ntee/C20.md) (pollution abatement and control); also [C30](../../_shared/ntee/C30.md) (natural resources conservation).
- **Who it serves →** [population](population.md) — the residents of the corridor; see also [SDG-03](../../_shared/sdg/SDG-03.md) (good health) and [SDG-11](../../_shared/sdg/SDG-11.md) (sustainable cities).
- **Where →** [US-MI-detroit](../../_shared/situations/US-MI-detroit.md) (Detroit, Wayne County, Michigan).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, validated at high confidence (0.94).
- **What it runs →** [technology](technology/index.md). Note that this organization's technology *is* its program, which is unusual in this collection.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).

## A coalition that ignores geography

Riverbend Air is one of three organizations in this collection tied together by a **fenceline-monitoring coalition** rather than by a shared place:

- [synthetic-Gulf Corridor Justice Project](../synthetic-gulf-corridor-justice-project/README.md) — New Orleans, Louisiana
- [synthetic-Corporación Río Vivo](../synthetic-corporacion-rio-vivo/README.md) — Cali, Colombia

They share monitoring methodology, a common data format, and an annual convening; they share no funder, no staff, and no watershed. **This edge exists in the collection on purpose.** A graph that only connects organizations to their neighbors is a map. The interesting question — *who else is doing this, anywhere* — is only answerable if some edges cross geography. If you are testing traversal logic, this triangle is the case that catches a query which assumed proximity.

## One thing verification could not establish

**The organization's own data has never been externally validated.** Riverbend Air's sensor network is the substance of its advocacy, and no independent party has ever calibrated it against a reference monitor. The sensors are a well-understood commodity type with known limitations — humidity sensitivity, drift, a wide confidence interval at low concentrations — and the organization is candid about this in its materials. But "candid about the limitation" and "the limitation is addressed" are different things.

This matters more than a governance gap would, because the data is the point. An opposing expert at a permit hearing will go here first. The verification could confirm that the network exists and is maintained; it could not confirm that its readings are defensible. *(mechanical: the simulated determination labels data validation "Unverifiable — out of scope.")*

That gap is also the reason the [volunteer project](technical-volunteers/index.md) in this bundle is about the integrity of the pipeline rather than about anything more visible.

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials

[^registry]: Registry record (simulated)
