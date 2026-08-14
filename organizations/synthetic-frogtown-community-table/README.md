---
type: org
title: synthetic-Frogtown Community Table
description: A fabricated culturally-specific food shelf in Saint Paul, Minnesota.
resource: https://synthetic-frogtown-table.example.org
tags: [org-bundle, nonprofit, synthetic, food-security, immigrant-serving]
aliases: ["synthetic-Frogtown Table", "Frogtown Community Table"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: https://synthetic-frogtown-table.example.org
    title: The organization's own website and published materials
    author: human:org-staff
    last_modified: 2026-03-02
  - id: registry
    resource: "simulated registry extract"
    title: Registry record (simulated)
    author: process:registry-import
    last_modified: 2026-01-15
  - id: program-reporting
    resource: "simulated programme and funder reporting"
    title: Programme and funder reporting (simulated)
    author: process:program-reporting
    last_modified: 2026-02-28
x-civic:
  # ---- REQUIRED by civic/0.6. These five keys are the whole profile. ----
  profile: civic/0.6
  subject: [SS030601, SS030600, SS090300]           # PCS Subject facet — what it does
  population: [PG010000, PG010400, PG030000]        # PCS Population facet — who it serves
  org_type: EA040000                                # PCS OrgType facet — what kind of organization
  registration_country: US                          # ISO 3166-1 alpha-2

  # ---- OPTIONAL below. Every key here makes the bundle more useful and ----
  # ---- none of it affects conformance. Omit any of it freely.          ----
  provides: food-shelf
  registration:
    scheme: IRS-EIN
    id: "00-1000009"
    tax_status: "501(c)(3)"
  operating_locations:
    - country: US
      subdivision: US-MN
      locality: "Frogtown, Saint Paul, Ramsey County, Minnesota"
  budget:
    amount: 430000
    currency: USD
    period: FY2025
    basis: annual-revenue
  ntee: ["K30", "K31", "P84"]                       # optional US-only layer; reaches 12 of 15
  sdg: ["2", "10"]                                  # optional global layer; reaches 15 of 15
  situation: US-MN-saint-paul
  relations:
    - { target: synthetic-north-star-immigrant-defense, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-Frogtown Community Table

> **⚠ SYNTHETIC.** This organization does not exist. Its name, registration number, address, website, budget figures, programs, technology, and determination are all invented. The registration ID uses the prefix `00-`, which the IRS never assigns, so it cannot collide with a real one. Sources listed in the frontmatter are simulated: a claim attributed to `org-site` was not sourced from any organization.

synthetic-Frogtown Community Table ("Frogtown Table") runs a food shelf in Saint Paul stocked for the people who actually shop there. In the organization's own words:

> A box of food nobody in the household knows how to cook is not food assistance, it is a disposal problem we have handed to somebody who is already tired. We stock what our neighbours eat.[^org-site]

It operates **one food shelf** open four days a week, serving roughly **1,900 households a year**[^program-reporting] across the [[Hmong]], [[Karen]], [[Somali]], [[Oromo]], and [[Latino]] communities of the surrounding neighbourhoods. It runs a community kitchen, maintains garden plots, and delivers to homebound elders.[^org-site] It was founded in **2009** by a group of neighbourhood congregations and received exemption in **2010**.[^registry]

It is a very small organization — annual revenue around **$430,000**, assets around **$95,000**, and **4.5 FTE** staff plus about 60 volunteers.[^registry] Funding is regional food-bank allocation, a city grant, congregational giving, and individual donors. Its address is **615 Como Crossing, Saint Paul, MN 55103**.[^registry]

## Reading this bundle

- **Who it serves →** [population.md](population.md)
- **What it runs →** [programs.md](programs.md)
- **What it accomplished →** [impact.md](impact.md)
- **What it needs funding for →** [what_i_need_funding_for.md](what_i_need_funding_for.md)
- **Has anyone verified this? →** [verification.md](verification.md)
- **What technology it has →** [technology/](technology/index.md)
- **Volunteer rules and one scoped project →** [technical-volunteers/](technical-volunteers/index.md)

## The two kinds of link in this bundle, and why it matters

This is the design idea worth copying, so it is stated at the top rather than buried.

**Structural links are ordinary markdown links.** `[population.md](population.md)` points at a file that exists. These are the bundle's navigable spine and they work in a GitHub view, in an editor, and in Obsidian.

**Emergent terms are wikilinks.** `[[Hmong]]`, `[[Karen]]`, `[[Somali]]`, `[[Oromo]]` above point at nothing. There is no `Hmong.md` in this bundle and there does not need to be — OKF v0.2 §6.1 says a consumer must tolerate a link whose target does not exist, because "it may simply represent not-yet-written knowledge."

That tolerance is load-bearing here. The required `population` field says `PG010000` (Immigrants and migrants), `PG010400` (Refugees and displaced people), `PG030000` (Economically disadvantaged people). Those three PCS codes are what make this organization **comparable** to any other bundle in the world that uses the same facet. They are also the least interesting true thing about who shops at this shelf.

The wikilinks carry what the organization itself says: five specific communities, which are not interchangeable, and whose differences drive procurement, storage, volunteer recruitment, and shelf layout — see [population.md](population.md). Nobody had to ratify `[[Karen]]` as a term for it to be usable. If a hundred organizations write `[[Karen]]` in their own bundles, that shape becomes visible in the graph, and at that point somebody can write the page and it becomes a real node.

**The controlled vocabulary makes bundles comparable. The emergent one makes them true.** A bundle needs both, and only one of them is required.

## One thing verification could not establish

**Whether the organization can survive the loss of its executive director.** She has been there since 2011, speaks Hmong and some Somali, is known personally to a large share of the households that use the shelf, and holds the relationships with all four congregational funders. There is no deputy.[^org-site]

For a 4.5-FTE organization this is neither unusual nor a failing — it is what a small organization looks like. But it is the material fact about this organization's next five years, and it is not a compliance question, so no verification process examines it. The bundle records it because a reader deciding whether to invest in this organization should know that the investment is substantially in one person.

## Where this sits in the collection

This bundle is the **worked reference** for the set: it is the one to read first, and it carries the fullest explanation of why the frontmatter looks the way it does.

It is also conformant **on its own**. The collection around it adds shared classification hubs in [`_shared/pcs/`](../../_shared/pcs/index.md), place nodes in [`_shared/situations/`](../../_shared/situations/index.md), the optional NTEE and SDG layers, and edges to fourteen peer organizations. All of that makes the graph worth querying and **none of it is required**. If you are building your own, the honest minimum is the five `x-civic` keys in the frontmatter above plus core OKF's `type`.

- **Who it works with →** [synthetic-North Star Immigrant Defense](../synthetic-north-star-immigrant-defense/README.md), also in Saint Paul. Same families, two needs — an immigration question surfaces at a food shelf long before it reaches a law office. North Star holds monthly clinic hours in this organization's back room, which is a considerably lower-friction referral than a phone number.
- **Where →** [Saint Paul, Minnesota](../../_shared/situations/US-MN-saint-paul.md).

[^org-site]: The organization's own website and published materials
[^registry]: Registry record (simulated)
[^program-reporting]: Programme and funder reporting (simulated)
