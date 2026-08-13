---
type: org
title: "synthetic-Crescent City Career Lab"
description: "A fabricated New Orleans workforce organization whose verification determination has expired — an organization in good standing with an invalid record."
resource: https://synthetic-crescent-city-career-lab.example.org
aliases: ["synthetic-Crescent City Career Lab", "Crescent City Career Lab"]
tags: ["org-bundle", "nonprofit", "synthetic", "workforce-training", "cskg", "lapsed-determination"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-crescent-city-career-lab.example.org"
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
  population: ["PJ020000", "PG030000", "PG100000"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: workforce-training
  registration:
    scheme: "IRS-EIN"
    id: "00-1000012"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["J22", "J20"]      # optional US-only layer; reaches 12 of 15
  sdg: ["4", "8"]        # optional global layer; reaches 15 of 15
  situation: US-LA-orleans
  relations:
    - { target: synthetic-gulf-corridor-justice-project, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-Crescent City Career Lab

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

> ## ⏰ THIS BUNDLE'S VERIFICATION DETERMINATION HAS EXPIRED
>
> [verification.md](verification.md) carries `verified: { at: 2024-02-14 }` and `stale_after: 2026-02-14`. The determination on file was an **APPROVE at 94% confidence**, issued with a two-year term. It expired **2026-02-14** and has not been renewed. As of the date of this bundle it is **five and a half months out of date**. No field says "expired" — you get there by comparing `stale_after` to today.
>
> **The organization is almost certainly still fine.** Nothing suggests otherwise. But *almost certainly still fine* is not a determination, and anything that reads this bundle should treat it as **unverified**, not as approved. See [eligibility](verification.md) for how the lapse happened, which is the most useful part of this bundle.

synthetic-Crescent City Career Lab ("Career Lab") moves adults in New Orleans from hospitality and service work into technical roles that pay more and survive a storm season. In the organization's own words:

> This city's economy has been one industry deep for a long time, and that industry closes when the weather turns or the tourists stop. We are not against hospitality. We are against a household having only one door.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it enrolls roughly **260 adults a year** across IT support, data, and green-infrastructure tracks, most of them 10 to 20 weeks; it maintains employer relationships with about **thirty regional employers**; and it runs an evening-and-weekend schedule because most participants are working while they train. It was founded in **2014** and received IRS exemption the same year.

It is a **mid-sized** nonprofit — annual revenue around **$1,700,000**, assets around **$480,000**, and about **19 staff**. Funding is a state workforce allocation, city economic-development funds, foundations, and modest employer contributions. Its address is **2450 Bywater Exchange, New Orleans, LA 70117**. *(mechanical[^registry], simulated.)*

- **What it does →** classified as [J22](../../_shared/ntee/J22.md) (job training and employment); also [J20](../../_shared/ntee/J20.md) (employment procurement assistance).
- **Who it serves →** [population](population.md) — working adults changing careers; see also [SDG-08](../../_shared/sdg/SDG-08.md) (decent work) and [SDG-04](../../_shared/sdg/SDG-04.md) (quality education).
- **Where →** [US-LA-orleans](../../_shared/situations/US-LA-orleans.md) (New Orleans, Orleans Parish, Louisiana).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — **its determination has lapsed.** Read that file before using this bundle for anything.
- **What it runs →** [technology](technology/index.md).
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md). The only AI project in the collection that touches no personal data at all.
- **Who it works with →** [synthetic-Gulf Corridor Justice Project](../synthetic-gulf-corridor-justice-project/README.md), also in New Orleans, on **remediation and coastal-infrastructure placement**. Gulf Corridor knows which work is actually coming to the corridor and which employers are credible; Career Lab trains and places. The principle both organizations state: people who live with the pollution should get the jobs cleaning it up.

## What this bundle is for

This is one of three deliberately imperfect bundles in the collection, and its defect is the **most mundane and the most likely to bite in practice**: a record that was valid and quietly stopped being valid, with no drama, no red flag, and no change to anything else in the bundle.

Everything here still looks fine. The programs are running, the partnership is active, the technology inventory is unremarkable, the organization is in good standing with every actual regulator. **Only one field changed**, and it changed by the passage of time rather than by an event.

Things worth testing against it:

- **Does your code compare `stale_after` to the current date, or does it treat the presence of a determination as approval?** The determination on file says APPROVE in large friendly letters. It is expired, and only the date arithmetic tells you so.
- **Does an expiry surface anywhere a person would see it?** In this bundle it is in the frontmatter, in a banner, and in the eligibility file. In a real corpus it may be in one field nobody renders.
- **How does a valid organization connected to an unverified one behave in your graph?** [Gulf Corridor](../synthetic-gulf-corridor-justice-project/verification.md) is current and points at this bundle. Status should not propagate along partnership edges, and it is worth confirming yours doesn't.
- **Can your system express "we don't know" as distinct from "no"?** This organization is not ineligible. It is unverified. Those are different and a boolean cannot hold the difference.

## One thing verification could not establish

Beyond the fact that the verification is out of date: **whether the organization's employer relationships are as deep as its materials suggest.** It reports about thirty employer partners. That number appears to include employers who have taken one graduate in three years alongside those who hire from every cohort, with no distinction drawn.

That is not dishonesty — it is what happens when "employer partner" has no definition and a grant application asks for a count. But it means the most important thing about a workforce organization, which is whether anyone will actually hire its graduates, is recorded as a single number that mixes a standing relationship with a one-off. *(mechanical: the simulated determination labels employer-partnership depth "Not assessed.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials

[^registry]: Registry record (simulated)
