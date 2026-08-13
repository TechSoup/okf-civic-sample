---
type: org
title: "synthetic-Valle Verde Food Network"
description: "A fabricated Central Valley food-security organization serving farmworker communities across unincorporated Fresno County."
resource: https://synthetic-valle-verde.example.org
aliases: ["synthetic-Valle Verde", "Valle Verde Food Network"]
tags: ["org-bundle", "nonprofit", "synthetic", "food-security", "rural", "farmworker", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-valle-verde.example.org"
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
  subject: ["SS030600", "SS030601"]                 # PCS Subject facet
  population: ["PJ130000", "PG090000", "PG030000"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: food-distribution
  registration:
    scheme: "IRS-EIN"
    id: "00-1000004"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["K30", "K31"]      # optional US-only layer; reaches 12 of 15
  sdg: ["1", "2"]        # optional global layer; reaches 15 of 15
  situation: US-CA-fresno
  relations:
    - { target: synthetic-central-valley-farmworker-law-center, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-Valle Verde Food Network

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Valle Verde Food Network ("Valle Verde") moves food to farmworker households in the unincorporated communities of Fresno County — places with no grocery store, sometimes no safe tap water, and a bus that comes twice a day if it comes. In the organization's own words:

> The food is grown here. Fourteen miles from the field, a family that picked it is deciding between groceries and the water bill. We drive the difference.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it runs **nine mobile pantry routes** on a two-week cycle reaching **17 unincorporated communities**, recovers produce from **regional packing houses** that would otherwise be culled, employs **eleven promotoras** who are from the communities they serve, and distributes bottled water in communities where domestic wells fail nitrate or arsenic standards. It began in **2004** as a church-basement operation and received IRS exemption in **2006**.

It is a **mid-sized** nonprofit — annual revenue around **$2,100,000**, assets around **$1,340,000** including four vehicles and a small warehouse. Funding is a mix of state food-bank allocations, foundations, and agricultural-sector giving. Its office is at **1180 Camino del Norte, Fresno, CA 93725**, though the organization's actual operating footprint is the county. *(mechanical, simulated.)*

- **What it does →** classified as [K30](../../_shared/ntee/K30.md) (food service, free food distribution); also [K31](../../_shared/ntee/K31.md) (food banks and pantries).
- **Who it serves →** [population](population.md) — farmworker households across unincorporated Fresno County; see also [SDG-02](../../_shared/sdg/SDG-02.md) (zero hunger) and [SDG-01](../../_shared/sdg/SDG-01.md) (no poverty).
- **Where →** [US-CA-fresno](../../_shared/situations/US-CA-fresno.md) (Fresno County, California).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, validated at high confidence (0.93).
- **What it runs →** [technology](technology/index.md). Read this one for what happens when your service area has no cell coverage.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).
- **Who it works with →** [synthetic-Central Valley Farmworker Law Center](../synthetic-central-valley-farmworker-law-center/README.md), also in Fresno County. The pantry line is where wage-theft and housing-condition problems surface first; a Law Center advocate rides two routes a month and takes intakes on the tailgate. It is the most-used referral pathway either organization has.

## Three languages, and one of them is mostly spoken

Valle Verde's communities speak **Spanish**, **Mixtec**, and **Triqui**. That is not a translation line item, it is a design constraint that touches everything:

- **Mixtec and Triqui are primarily oral languages** in this context, with variation between communities. Written translation is often not the answer; a recorded voice message from someone speaking the right variant is.
- A meaningful share of adults in the service population have **limited literacy in any language**, which rules out text-first interfaces regardless of which language the text is in.
- The **promotoras are the interface** — eleven people who speak the languages, are known in the communities, and carry the information. Any system that routes around them fails, and any system that adds to their load fails differently.

Anything reading this bundle to design something should register that a form is not a neutral choice here. See [constraints](technical-volunteers/constraints.md), where the organization states this more firmly than the collection's other bundles state anything.

## One thing verification could not establish

**The size of the population served cannot be established, and the organization would rather it stayed that way.** Valle Verde does not record names, addresses, or immigration status at distribution. It counts households and boxes. It does not and will not ask who someone is.

That is a deliberate protective choice in a service population where a list of names and addresses is a hazard, and the organization is explicit that it would refuse a funder requirement to collect it. The consequence is that the "unduplicated individuals served" figure that a state food-bank allocation formula wants does not exist and cannot be derived. The organization estimates; the estimate is honest and it is an estimate.

*(mechanical[^registry]: the simulated determination labels service-volume figures "Corroborated at household level; individual counts unverifiable by organizational policy.")*

That last phrase is the useful bit. **The gap is a policy, not a failure**, and a bundle that records it as a data-quality problem would be describing the organization wrongly.

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials
[^registry]: Registry record (simulated)
