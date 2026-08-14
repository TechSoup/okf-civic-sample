---
type: org
title: "synthetic-Sierra Foothills Community Health"
description: "A fabricated federally-supported community health center network in rural Fresno County — the largest organization in this collection."
resource: https://synthetic-sierra-foothills-health.example.org
aliases: ["synthetic-Sierra Foothills Health", "Sierra Foothills Community Health"]
tags: ["org-bundle", "nonprofit", "synthetic", "rural-health", "community-clinic", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-sierra-foothills-health.example.org"
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
  subject: ["SE050100", "SE050000"]                 # PCS Subject facet
  population: ["PG090000", "PG030000", "PJ130000"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: primary-care
  registration:
    scheme: "IRS-EIN"
    id: "00-1000006"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["E32", "E30"]      # optional US-only layer; reaches 12 of 15
  sdg: ["3", "10"]        # optional global layer; reaches 15 of 15
  situation: US-CA-fresno
  relations:
    - { target: synthetic-nyando-community-health-trust, type: learn_with }
  verifiable_by: [techsoup]
---

# synthetic-Sierra Foothills Community Health

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Sierra Foothills Community Health ("Sierra Foothills") runs three clinic sites and a mobile unit serving rural eastern Fresno County, on a sliding scale, regardless of insurance status. In the organization's own words:

> Nobody in this county should drive ninety minutes to be seen. That's the whole idea, and everything else we do is logistics in service of it.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it operates **three fixed sites and one mobile unit**, provides primary care, dental, behavioral health, and prenatal services, records roughly **51,000 patient visits a year** across about **14,000 distinct patients**, and runs a dedicated **migrant and seasonal agricultural worker health program**. It was founded in **1979** and has held federal health-center program support since the mid-1980s.

It is the **largest organization in this collection** — annual revenue around **$7,900,000**, assets around **$6,200,000** including two owned buildings and the mobile unit, and about **88 staff** including 6 physicians, 11 mid-levels, and 3 dentists. Revenue is majority **public insurance reimbursement**, plus federal health-center funding, sliding-scale patient fees, and foundation support. Its administrative office is at **40 Foothill Clinic Way, Sanger, CA 93657**. *(mechanical[^registry], simulated.)*

- **What it does →** classified as [E32](../../_shared/ntee/E32.md) (ambulatory health center / community clinic); also [E30](../../_shared/ntee/E30.md) (health treatment facilities).
- **Who it serves →** [population](population.md) — rural eastern Fresno County, including agricultural worker households; see also [SDG-03](../../_shared/sdg/SDG-03.md) (good health) and [SDG-10](../../_shared/sdg/SDG-10.md) (reduced inequalities).
- **Where →** [US-CA-fresno](../../_shared/situations/US-CA-fresno.md) (Fresno County, California).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, validated at high confidence (0.94).
- **What it runs →** [technology](technology/index.md). Two electronic health record systems, because of an absorption that never finished.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md). The only project in this collection that requires a Business Associate Agreement before a volunteer can start.

## A peer relationship across a border

Sierra Foothills carries a **`learn_with`** edge to [synthetic-Nyando Community Health Trust](../synthetic-nyando-community-health-trust/README.md) in Kisumu County, Kenya — the two organizations exchange practice on community health worker models and on delivering care where patients are, twice-yearly, informally.

Two things about this edge are deliberate in the collection's design:

**It crosses a border and a wealth gradient, and the learning runs both directions.** Sierra Foothills has more money and more equipment. Nyando has a considerably more mature community-health-worker model and years of hard-won practice in operating without reliable connectivity, which is a problem Sierra Foothills' mobile unit has too and has solved worse. Anyone traversing this edge assuming the direction of expertise follows the direction of budget will get it backwards.

**This is the collection's only `learn_with` edge**, and it is the clearest case for why asserted edges exist at all. `civic/0.6` carries three optional relation types — `partners_with`, `coalition_with`, `learn_with` — for relationships that **cannot be computed**. Nothing in the required frontmatter would ever pair a $7.9M California clinic network with a Kenyan community health trust: different countries, different currencies, different `org_type`, wildly different scale. Substitution and complementarity are derivable from `provides` plus place; *peer learning across a 15,000-kilometre gap* is a fact about the world that somebody had to write down. See the [collection README](../../README.md).

## One thing verification could not establish

**Clinical quality was not assessed, and eligibility verification is the wrong instrument for it.** The determination confirmed that the organization exists, is properly constituted, holds its licences, and is in good standing. It did not evaluate care quality, patient outcomes, or clinical safety.

Those things *are* assessed, rigorously, by an entirely different apparatus — federal health-center program review, state licensing, accreditation, payer audits, and the organization's own quality committee. That apparatus is far more demanding than anything in this bundle. But **none of it is visible here**, and a reader who takes this bundle as a complete account of what is known about this organization would badly underestimate how much scrutiny it operates under.

Worth stating because it generalizes: for a regulated organization, **an org bundle is a thin slice of the available evidence**, and the interesting question is often not what the bundle says but which regulator holds the rest. *(mechanical: the simulated determination labels clinical quality "Not assessed — out of scope; separately regulated.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials

[^registry]: Registry record (simulated)
