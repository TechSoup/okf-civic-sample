---
type: org
title: "synthetic-Gulf Corridor Justice Project"
description: "A fabricated Louisiana environmental-justice organization whose public evidence archive is contested by a well-resourced adversary."
resource: https://synthetic-gulf-corridor.example.org
aliases: ["synthetic-Gulf Corridor", "Gulf Corridor Justice Project"]
tags: ["org-bundle", "nonprofit", "synthetic", "environmental-justice", "petrochemical", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-gulf-corridor.example.org"
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
  subject: ["SC030100", "SE130200"]                 # PCS Subject facet
  population: ["PG030000", "PG100000"]              # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: environmental-evidence-archive
  registration:
    scheme: "IRS-EIN"
    id: "00-1000011"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["C20", "C30"]      # optional US-only layer; reaches 12 of 15
  sdg: ["3", "11", "13", "16"]        # optional global layer; reaches 15 of 15
  situation: US-LA-orleans
  relations:
    - { target: synthetic-crescent-city-career-lab, type: partners_with }
    - { target: synthetic-riverbend-air-alliance, type: coalition_with }
    - { target: synthetic-corporacion-rio-vivo, type: coalition_with }
  verifiable_by: [techsoup]
---

# synthetic-Gulf Corridor Justice Project

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Gulf Corridor Justice Project ("Gulf Corridor") documents the health and environmental burden carried by communities along a stretch of the Louisiana industrial river corridor, and intervenes in the permitting decisions that add to it. In the organization's own words:

> Every facility here was permitted. Every permit had a public comment period. The comments were filed by people who had thirty days to respond to four hundred pages of dispersion modelling, without a scientist. We are the scientist now.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it maintains a **community sampling programme** for air and water, runs a **door-to-door health survey** covering several thousand households, files **technical interventions in permitting proceedings**, and publishes a **public document archive** of permits, monitoring reports, and its own sampling results. It was founded in **2008** after a facility expansion the surrounding neighbourhoods learned about from a newspaper.

It is a **mid-sized** nonprofit — annual revenue around **$1,500,000**, assets around **$420,000**, and about **16 staff** including two people with graduate training in environmental science and a community-organizing team of five. Funding is foundation-heavy with a small individual base and occasional cost recovery from litigation. Its address is **3820 Corridor Reach Road, New Orleans, LA 70117**. *(mechanical[^registry], simulated.)*

- **What it does →** classified as [C20](../../_shared/ntee/C20.md) (pollution abatement and control); also [C30](../../_shared/ntee/C30.md) (natural resources conservation).
- **Who it serves →** [population](population.md) — corridor residents; see also [SDG-03](../../_shared/sdg/SDG-03.md) (good health), [SDG-13](../../_shared/sdg/SDG-13.md) (climate action), and [SDG-16](../../_shared/sdg/SDG-16.md) (peace, justice, strong institutions).
- **Where →** [US-LA-orleans](../../_shared/situations/US-LA-orleans.md) (New Orleans and the adjacent river parishes, Louisiana).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, validated at 91% confidence.
- **What it runs →** [technology](technology/index.md). A public archive that is somebody's target.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).
- **Who it works with →** [synthetic-Crescent City Career Lab](../synthetic-crescent-city-career-lab/README.md), also in New Orleans, on **green-infrastructure and remediation job placement** — Gulf Corridor knows which work is coming and which employers are credible; Career Lab trains and places. Note that Career Lab's [verification determination has lapsed](../synthetic-crescent-city-career-lab/verification.md), which is worth seeing from this side of a partnership edge.

## A coalition that crosses two borders

Gulf Corridor is one of three organizations in this collection tied together by a **fenceline-monitoring coalition** rather than by geography:

- [synthetic-Riverbend Air Alliance](../synthetic-riverbend-air-alliance/README.md) — Detroit, Michigan
- [synthetic-Corporación Río Vivo](../synthetic-corporacion-rio-vivo/README.md) — Cali, Colombia

Shared methodology, a common data format, an annual convening. No shared funder, staff, or watershed. **The edge exists in the collection on purpose** — a graph where organizations only connect to their neighbours is a map, and the question *who else does this work anywhere* is only answerable if some edges ignore proximity. If you are testing traversal, this triangle catches a query that assumed adjacency.

## The adversary is well-resourced, and it changes the technology problem

Most organizations in this collection worry about accidental exposure. [One](../synthetic-north-star-immigrant-defense/README.md) worries about a hostile state. This one has a different situation again: **its opponents are industrial facilities and their counsel, who are competent, patient, funded, and operating entirely within the law.**

What that looks like in practice:

- **Every number the organization publishes will be contested by a paid expert.** Not dismissed — contested, in a proceeding, with a rebuttal report.
- **The document archive is the organization's asset and its vulnerability.** If someone can cast doubt on whether a posted document is authentic or unaltered, they do not need to rebut its contents.
- **Public-records battles run both ways.** The organization uses records requests; it also receives them, and discovery in litigation reaches its own files.
- **The site has been attacked.** Once defaced, repeatedly scraped, and subject to traffic events that coincide with hearing dates. See [inventory](technology/inventory.md).

The consequence for anything reading this bundle: **integrity and availability matter more here than confidentiality.** That inverts the usual priority order, and a security recommendation set built around protecting secrets will miss what this organization actually needs — which is proof that its evidence has not been altered, and a site that stays up on the day of a hearing.

## One thing verification could not establish

**Whether the health survey data would survive expert challenge.** The organization's door-to-door survey is its most distinctive evidence and its most contestable: administered by trained community members rather than clinicians, self-reported, without a matched control population, and collected by an organization with an obvious interest in the result.

The organization is candid about all of this and describes the survey as documenting a pattern that warrants investigation rather than as proving causation. That is the correct framing and it is not the framing its results are quoted in once they reach a newspaper.

Verification could confirm the survey exists and is administered consistently. It could not assess whether its methodology holds up, and that is the question an opposing expert will build a career moment on. *(mechanical: the simulated determination labels survey methodology "Not assessed — out of scope.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials

[^registry]: Registry record (simulated)
