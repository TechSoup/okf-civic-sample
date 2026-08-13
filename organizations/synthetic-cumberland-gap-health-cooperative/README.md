---
type: org
title: "synthetic-Cumberland Gap Health Cooperative"
description: "A fabricated small rural clinic in Letcher County, Kentucky, where the broadband problem belongs to the patients as much as to the organization."
resource: https://synthetic-cumberland-gap-health.example.org
aliases: ["synthetic-Cumberland Gap Health", "Cumberland Gap Health Cooperative"]
tags: ["org-bundle", "nonprofit", "synthetic", "rural-health", "appalachia", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-cumberland-gap-health.example.org"
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
  subject: ["SE050100", "SE040200"]                 # PCS Subject facet
  population: ["PG090000", "PG030000", "PA020300"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: primary-care
  registration:
    scheme: "IRS-EIN"
    id: "00-1000007"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["E32"]      # optional US-only layer; reaches 12 of 15
  sdg: ["3"]        # optional global layer; reaches 15 of 15
  situation: US-KY-letcher
  relations:
    - { target: synthetic-black-mountain-workforce-partnership, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-Cumberland Gap Health Cooperative

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Cumberland Gap Health Cooperative ("Cumberland Gap Health") is a small clinic in Letcher County, Kentucky, serving hollows and ridge communities across a county with no hospital of its own. In the organization's own words:

> We have one nurse practitioner, one doctor two days a week, and a truck. Forty percent of our patients cannot get here on their own and about the same number cannot use a video visit. So we go, or we don't see them.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it runs **one clinic site** plus **home and community visits**, sees roughly **3,100 distinct patients** a year, and carries a caseload weighted toward **diabetes, hypertension, chronic respiratory disease, and substance-use recovery**. Its respiratory caseload includes a significant number of former miners with occupational lung disease, which shapes both its clinical work and its benefits-advocacy work. It was founded in **1978** and has operated continuously since.

It is a **small** nonprofit — annual revenue around **$1,100,000**, assets around **$390,000**, and about **14 staff** including one physician at 0.4 FTE, two nurse practitioners, and a community health worker. Revenue is a mix of public insurance reimbursement, a state rural-health allocation, foundation grants, and patient fees. Its address is **210 Cutshin Ridge Road, Whitesburg, KY 41858**. *(mechanical, simulated.)*

- **What it does →** classified as [E32](../../_shared/ntee/E32.md) (ambulatory health center / community clinic).
- **Who it serves →** [population](population.md) — Letcher County residents; see also [SDG-03](../../_shared/sdg/SDG-03.md) (good health).
- **Where →** [US-KY-letcher](../../_shared/situations/US-KY-letcher.md) (Letcher County, Kentucky).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, at 90% confidence, the lowest of the clean US determinations.
- **What it runs →** [technology](technology/index.md). Read it for the failed telehealth programme, which failed for the right reason.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).
- **Who it works with →** [synthetic-Black Mountain Workforce Partnership](../synthetic-black-mountain-workforce-partnership/README.md), also in Letcher County. The two organizations run a **health-careers pathway** together: Black Mountain trains people for medical assistant, phlebotomy, and CNA roles, and Cumberland Gap Health provides the clinical placements and hires some of the graduates. It is the most reciprocal partnership in this collection — each organization is the other's supplier.

## It is called a cooperative and it is not one

**A small, genuine data-quality problem, preserved deliberately.**

The organization has been called Cumberland Gap Health Cooperative since 1978, when it was founded as a membership health cooperative by a group of miners' families. It reorganized as a **nonprofit corporation** in the 1980s and has been a 501(c)(3) ever since. It kept the name because the name is what people in the county call it.

So: **its legal form does not match its name**, and any process that infers organizational type from a name string will classify it wrongly. It is not a cooperative, it has no members in the legal sense, and it would tell you so if you asked — but nobody asks, because the name is right there.

This is worth having in a sample corpus because the failure is silent. There is no error, no missing field, no low-confidence score. Just a confident wrong answer produced from a legitimate signal. The required `org_type: EA040000` (public charities) is the only thing in the record that contradicts the name, and it contradicts it silently — a consumer has to notice the disagreement rather than being told about it. There is **no field anywhere in the profile for the note itself**, which is this bundle's schema suggestion: **the schema needs a place to say "the obvious inference is wrong."**

## One thing verification could not establish

**Whether the organization can continue at its current staffing.** Verification confirmed that it exists, is in good standing, and is properly governed. It could not resolve the thing that actually determines this organization's future, which is that its physician coverage is 0.4 FTE, held by someone who drives in from another county, and there is no identified successor.

That is not a verifiable fact and it is not a compliance question. It is the most important thing about this organization's next three years, and no verification process is built to see it. The organization is candid about it; the bundle records it; nothing else can be said with confidence.

*(mechanical[^registry]: the simulated determination labels organizational continuity "Not assessed — out of scope.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials
[^registry]: Registry record (simulated)
