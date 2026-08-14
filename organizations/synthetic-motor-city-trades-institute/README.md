---
type: org
title: "synthetic-Motor City Trades Institute"
description: "A fabricated Detroit pre-apprenticeship and trades-training organization, mid-sized, with real technical debt."
resource: https://synthetic-motor-city-trades.example.org
aliases: ["synthetic-Motor City Trades", "Motor City Trades Institute"]
tags: ["org-bundle", "nonprofit", "synthetic", "workforce-training", "apprenticeship", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-motor-city-trades.example.org"
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
  subject: ["SN020302", "SN020300"]                 # PCS Subject facet
  population: ["PA020000", "PG040000", "PJ020000"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: trades-training
  registration:
    scheme: "IRS-EIN"
    id: "00-1000003"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["J22", "J20"]      # optional US-only layer; reaches 12 of 15
  sdg: ["4", "8"]        # optional global layer; reaches 15 of 15
  situation: US-MI-detroit
  relations:
    - { target: synthetic-eastside-harvest-collective, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-Motor City Trades Institute

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Motor City Trades Institute ("Motor City Trades") runs pre-apprenticeship training in the electrical, HVAC, and welding trades and places graduates into registered apprenticeships and jobs. In the organization's own words:

> A pre-apprenticeship is only worth what it opens. We measure ourselves on who is still in the trade three years later, not on who finished our course.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it enrolls about **340 adults a year** across three trade tracks, maintains placement agreements with **two union halls and eleven employers**, and runs a **second-chance track** for people returning from incarceration that accounts for roughly a third of enrollment. It opened in **2008** as a program of a larger community-development corporation, spun out and received IRS exemption in **2009**.

It is the **second-largest organization in this collection** — annual revenue around **$3,200,000**, assets around **$2,750,000** including a building, and about **34 staff**. Roughly 60% of revenue is government: state workforce funding, a federal apprenticeship grant, and a county reentry contract. Its address is **1900 Kestrel Works Avenue, Detroit, MI 48208**. *(mechanical[^registry], simulated.)*

- **What it does →** classified as [J22](../../_shared/ntee/J22.md) (job training and employment); also [J20](../../_shared/ntee/J20.md) (employment procurement assistance).
- **Who it serves →** [population](population.md) — adults entering the trades, including returning citizens; see also [SDG-08](../../_shared/sdg/SDG-08.md) (decent work) and [SDG-04](../../_shared/sdg/SDG-04.md) (quality education).
- **Where →** [US-MI-detroit](../../_shared/situations/US-MI-detroit.md) (Detroit, Wayne County, Michigan).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, validated at high confidence (0.96).
- **What it runs →** [technology](technology/index.md). Three overlapping systems and a Salesforce implementation that stopped halfway.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).
- **Who it works with →** [synthetic-Eastside Harvest Collective](../synthetic-eastside-harvest-collective/README.md), also in Detroit. Young people who finish a season on Eastside Harvest's farm crew and want a skilled trade come here; the two organizations share a referral pathway and a data-sharing agreement neither has ever exercised.

## What makes this bundle useful: a mature organization with a mess inside it

Most small-nonprofit technology stories are about scarcity. This one is about **accumulation**. A $3.2M organization with 34 staff and heavy government reporting obligations has bought, been given, and been mandated into more systems than it can maintain, and the result is that the single number it cares most about — *is this graduate still in the trade three years later* — is the number it can least reliably produce.

Three systems hold pieces of the same person's record, and none of them is authoritative. The detail is in [inventory](technology/inventory.md), and it is the reason the [volunteer project](technical-volunteers/index.md) here is a consolidation rather than a build.

## One thing verification could not establish

**Long-term placement outcomes cannot be substantiated.** The organization states a three-year trade-retention rate in its materials and in at least one grant report. Verification could confirm the *completion* figures — those are reported to the state and independently held — but could not substantiate the retention claim, because the data behind it lives in a spreadsheet maintained by one staff member and reconstructed partly from personal follow-up and social media.

That is not a fabrication and it is probably roughly right. But an organization that has deliberately staked its identity on a long-term outcome measure is measuring it with the least rigorous instrument it owns, and it is the claim most likely to be challenged in a competitive federal application. *(mechanical: the simulated determination labels outcome data "Unverifiable — organization-held, single-source.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials

[^registry]: Registry record (simulated)
