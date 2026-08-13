---
type: org
title: "synthetic-Eastside Harvest Collective"
description: "A fabricated Detroit urban-farming and food-distribution organization, with a deliberately unreconciled budget."
resource: https://synthetic-eastside-harvest.example.org
aliases: ["synthetic-Eastside Harvest", "Eastside Harvest Collective"]
tags: ["org-bundle", "nonprofit", "synthetic", "food-security", "urban-agriculture", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-eastside-harvest.example.org"
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
  subject: ["SS030600", "SM010000"]                 # PCS Subject facet
  population: ["PG100000", "PG030000", "PA010000"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: food-distribution
  registration:
    scheme: "IRS-EIN"
    id: "00-1000001"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["K30", "K20"]      # optional US-only layer; reaches 12 of 15
  sdg: ["2", "11"]        # optional global layer; reaches 15 of 15
  situation: US-MI-detroit
  relations:
    - { target: synthetic-motor-city-trades-institute, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-Eastside Harvest Collective

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns, so it cannot collide with a real one. Provenance labels below are simulated — a line marked *org-sourced* was not sourced from any organization. See the [collection README](../../README.md).

synthetic-Eastside Harvest Collective ("Eastside Harvest") grows food on vacant land on Detroit's east side and moves it to the neighbors around it. In the organization's own words:

> We farm the land that's already here, with the people who already live here. Food should not have to travel across a county to reach a block that has been growing it all along.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation from the org: it runs **four farm sites** across roughly six acres of city-owned and land-bank parcels, reaches about **4,200 households a year** through weekly produce distribution, and employs a **paid youth farm crew** of 16-to-24-year-olds who cycle through a season of growing work. It began as a single block-club garden in **2011**, incorporated in **2012**, and received IRS exemption in **2013**.

It is a **mid-small** nonprofit. Its address is **1440 Sunrise Row, Detroit, MI 48214**. *(mechanical, from a simulated Business Master File record.)*

- **What it does →** classified as [K30](../../_shared/ntee/K30.md) (Food service, free food distribution); also [K20](../../_shared/ntee/K20.md) (agricultural programs).
- **Who it serves →** [population](population.md) — east-side Detroit households; see also [SDG-02](../../_shared/sdg/SDG-02.md) (zero hunger).
- **Where →** [US-MI-detroit](../../_shared/situations/US-MI-detroit.md) (Detroit, Wayne County, Michigan).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, but with an open flag. Read it before you use the budget number.
- **What it runs →** [technology](technology/index.md).
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).
- **Who it works with →** [synthetic-Motor City Trades Institute](../synthetic-motor-city-trades-institute/README.md), also in Detroit. Farm-crew members who finish a season and want a trade go there; the two organizations share an intake referral and, on paper, a data-sharing agreement nobody has ever tested.

## The budget does not reconcile, and nobody reconciled it

**This is the deliberate defect in this bundle.** Two budget figures are on file and they are far apart:

| Source | Figure | Period |
|---|---|---|
| Self-reported on its TechSoup application | **$1,400,000** | stated as "current annual budget," undated |
| Filed annual return | **$2,064,880** in total revenue | fiscal year ending September 2025 |

That's a **47% gap**, and there is no note anywhere explaining it. The plausible explanations are ordinary — the application figure might be an operating budget excluding a one-time capital grant for land acquisition, or it might just be stale by two years, or someone might have typed the wrong number. **None of them is recorded, so none of them is known.**

Reported assets are **$1,180,000**. *(mechanical, simulated.)*

The bundle deliberately **does not pick a number**. Anything that consumes this record has to decide what to do with two, and that decision should be visible rather than buried in a default. If your code silently takes the first figure it finds, this bundle is how you find that out.

## One thing verification could not establish

**Land tenure is unverifiable.** The organization farms four sites, and available sources establish clear tenure on only one of them. Two appear to be held on short-term licenses from the city land bank, and one is described in the org's own materials as "in stewardship," which is not a legal interest in anything. For a food-production organization, whether it will have its growing sites in three years is a bigger question than most things that *were* verified. It is not a disqualifier and it is not the org hiding anything — it is a genuinely hard thing to document. See [eligibility](verification.md).

*(mechanical[^registry]: the simulated determination labels site tenure "Partially unverifiable.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials
[^registry]: Registry record (simulated)
