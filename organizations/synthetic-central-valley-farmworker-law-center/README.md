---
type: org
title: "synthetic-Central Valley Farmworker Law Center"
description: "A fabricated Central Valley legal-aid organization representing farmworkers in wage, housing, and immigration matters."
resource: https://synthetic-cv-farmworker-law.example.org
aliases: ["synthetic-Farmworker Law Center", "Central Valley Farmworker Law Center"]
tags: ["org-bundle", "nonprofit", "synthetic", "legal-aid", "immigration", "farmworker", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-cv-farmworker-law.example.org"
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
  subject: ["SJ040000", "SS090300"]                 # PCS Subject facet
  population: ["PJ130000", "PG010200", "PG010000"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: legal-representation
  registration:
    scheme: "IRS-EIN"
    id: "00-1000005"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["I80", "P84"]      # optional US-only layer; reaches 12 of 15
  sdg: ["8", "10", "16"]        # optional global layer; reaches 15 of 15
  situation: US-CA-fresno
  relations:
    - { target: synthetic-valle-verde-food-network, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-Central Valley Farmworker Law Center

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Central Valley Farmworker Law Center ("the Law Center") represents farmworkers in Fresno and adjacent counties in wage claims, housing-condition cases, workplace-safety matters, and immigration proceedings. In the organization's own words:

> Most of what is done to a farmworker is legal until somebody makes it a case. Our job is to make it a case.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it employs **seven attorneys and nine non-attorney advocates**, opens roughly **900 matters a year**, holds **know-your-rights sessions** in the communities where its clients live, and maintains a small **removal-defense** practice that is chronically oversubscribed. It was founded in **1998** and received IRS exemption the same year.

It is a **mid-sized** nonprofit — annual revenue around **$1,800,000**, assets around **$610,000**. Funding is a mix of state legal-services allocation, foundations, court-awarded fees, and a small individual-donor base. Its office is at **2255 Calle Justicia, Fresno, CA 93721**. *(mechanical, simulated.)*

- **What it does →** classified as [I80](../../_shared/ntee/I80.md) (legal services); also [P84](../../_shared/ntee/P84.md) (ethnic and immigrant services).
- **Who it serves →** [population](population.md) — farmworkers and their households; see also [SDG-16](../../_shared/sdg/SDG-16.md) (peace, justice, strong institutions), [SDG-08](../../_shared/sdg/SDG-08.md) (decent work), and [SDG-10](../../_shared/sdg/SDG-10.md) (reduced inequalities).
- **Where →** [US-CA-fresno](../../_shared/situations/US-CA-fresno.md) (Fresno County, California).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, validated at high confidence (0.95), with an unusual limitation on what verification could examine.
- **What it runs →** [technology](technology/index.md). Notable for what it deliberately does *not* run.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md). The collection's hardest project, and the one where the interesting work was deciding what **not** to build.
- **Who it works with →** [synthetic-Valle Verde Food Network](../synthetic-valle-verde-food-network/README.md), also in Fresno County. An advocate rides two mobile-pantry routes a month and takes intakes at the tailgate. It is the Law Center's single most productive intake channel, because a food line is a place people already trust and a law office is not.

## Why the pantry line is the intake channel

Worth stating plainly, because it explains the shape of this organization's technology problem. **People do not walk into a law office to report their employer.** They especially do not do so if their status is precarious, if the employer also owns their housing, or if the last person who complained was let go the following week.

They will, however, mention it while waiting for a box of food, to an advocate they have seen at the same place every month, in their own language. That is where the Law Center's cases come from. Any system that assumes intake happens at an office, on a website, or through a form has misunderstood the organization.

## One thing verification could not establish

**Case outcomes could not be examined, and should not have been.** The Law Center's substantive work is protected by attorney-client privilege, so verification could confirm that the organization is real, in good standing, and staffed by licensed attorneys — and could go no further. It could not review case files, outcomes, or client information, and no amount of diligence would change that.

This is a genuinely different kind of gap from the ones in the other bundles. Elsewhere in this collection, unverifiable means *nobody documented it*. Here it means **the information is privileged and asking would be improper.** Anything reading these bundles to build a scoring or comparison system should treat those two situations differently: one is a weakness, the other is a legal boundary that a well-behaved system respects rather than penalizes.

*(mechanical[^registry]: the simulated determination labels case-level data "Not examined — privileged.")*

The consequence is that **this organization's effectiveness cannot be assessed from outside**, and any metric that appears to do so is measuring something else — grant reports, press coverage, or self-description.

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials
[^registry]: Registry record (simulated)
