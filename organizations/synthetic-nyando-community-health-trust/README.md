---
type: org
title: "synthetic-Nyando Community Health Trust"
description: "A fabricated community health organization in Kisumu County, Kenya — technically the most sophisticated field operation in this collection, and the one a verification process could not confirm."
resource: https://synthetic-nyando-health.example.org
aliases: ["synthetic-Nyando Community Health Trust", "Nyando Community Health Trust"]
tags: ["org-bundle", "nonprofit", "synthetic", "rural-health", "community-health", "kenya", "international", "cskg", "insufficient-evidence"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-nyando-health.example.org"
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
  subject: ["SE040200", "SE130700"]                 # PCS Subject facet
  population: ["PG090000", "PH040000", "PA010000"]  # PCS Population facet
  org_type: EA000000                                # PCS OrgType facet
  registration_country: KE                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  classification_note: "No NTEE code — NTEE is a US IRS vocabulary. PCS Subject and Population apply everywhere and are assigned directly from the activity description. ICNPO/ICNP-TSO would be the international NTEE counterpart and is left unassigned rather than guessed."
  provides: community-health-outreach
  org_type_note: "Kenyan registered trust operating under the public-benefit-organization framework. No PCS OrgType level-2 code matches, so the level-1 parent EA000000 is used deliberately."
  registration:
    scheme: "Kenya public-benefit-organization framework"
    id: "PBO/0000/0000"
    tax_status: "Income tax exemption held; subject to periodic renewal with the Kenya Revenue Authority"
    legal_form: "Trust"
  budget_currency: KES
  sdg: ["3", "6"]        # optional global layer; reaches 15 of 15
  situation: KE-KS-kisumu
  relations:
    - { target: synthetic-sierra-foothills-community-health, type: learn_with }
  data_protection_regime: "Data Protection Act, 2019 (Kenya)"
  verifiable_by: [techsoup]
---

# synthetic-Nyando Community Health Trust

> **⚠ SYNTHETIC.** This organization does not exist. Its name, registration identifiers, address, website, budget figures, programs, technology, and eligibility determination are all invented. Identifiers are all zeros, a pattern not assigned, so they cannot collide with a real entity. Provenance labels below are simulated. See the [collection README](../../README.md).

> ## ⚠ VERIFICATION RETURNED INSUFFICIENT EVIDENCE
>
> [verification.md](verification.md) carries **no `verified` key at all** — which under OKF §5.3 is the *unverified* tier, and is the point of this bundle. This is **not a rejection.** A verification process designed around publicly-filed records and web presence could not assemble enough external documentation to reach a determination either way, so there is no determination to record.
>
> **The organization functions well. Its own records are among the best in this collection.** The failure is in the method, and [eligibility](verification.md) explains exactly where — it is the most useful file in this bundle.

synthetic-Nyando Community Health Trust ("Nyando Health") supports community health promoters across a rural sub-county of Kisumu County, in western Kenya. In the organization's own words:

> The clinic is real but it is far, and a mother deciding at midnight whether to walk there is making a medical decision with no medical information. We put a trained neighbour within twenty minutes of every household. That is the whole strategy.

*Mission: **org-sourced**[^org-site] (simulated), translated in part — the organization works in Dholuo, Kiswahili, and English.*

Beyond that statement the picture is **derived** and would need confirmation: it supports **142 community health promoters** attached to four link health facilities, covering roughly **9,600 households**; its work centres on **maternal and child health, malaria, and household water treatment**; and it reports into Kenya's **national health information system** monthly. It was established by **trust deed in 2011** by a group of local health workers and community elders.

By Kenyan standards it is a **mid-sized** community organization — annual revenue around **KES 62,000,000**, assets around **KES 9,400,000**, and about **23 paid staff** supporting the 142 promoters, who receive stipends rather than salaries. Funding is international foundations, a bilateral donor programme, county government contribution in kind, and a small amount of local giving. Its address is **P.O. Box 0000, Ahero, Kisumu County, Kenya**. *(mechanical, simulated.)*

- **What it does →** no NTEE code. See the classification note in the frontmatter.
- **Who it serves →** [population](population.md) — rural households in Nyando; see also [SDG-03](../../_shared/sdg/SDG-03.md) (good health) and [SDG-06](../../_shared/sdg/SDG-06.md) (clean water).
- **Where →** [KE-KS-kisumu](../../_shared/situations/KE-KS-kisumu.md) (Kisumu County, Kenya).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — **undetermined. Read that file; it is the point of this bundle.**
- **What it runs →** [technology](technology/index.md). **The best field data operation in this collection.**
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).
- **Who it learns with →** [synthetic-Sierra Foothills Community Health](../synthetic-sierra-foothills-community-health/README.md) in Fresno County, California — a reciprocal **`learn_with`** edge, and the collection's only one. No required field would ever have paired these two organizations; that is precisely why the edge had to be asserted rather than computed.

## The inversion this bundle exists to demonstrate

**This organization has better program data than almost any other bundle in this collection, and the worst verifiability.**

Its community health promoters collect structured household data on mobile devices, offline, and sync when they reach connectivity. It reports monthly into a national health information system in a defined format. It can tell you how many pregnant women in its coverage area received a fourth antenatal visit last quarter, by promoter catchment. That is a level of routine, structured, externally-reported program data that [Motor City Trades](../synthetic-motor-city-trades-institute/README.md) — verification confidence 0.96 — cannot approach.

And a verification process could not establish enough about it to reach any determination at all.

The reason is not that the organization is opaque. **It is that the evidence a verification process looks for lives somewhere else here:**

| What verification wanted | Where it is |
|---|---|
| Publicly filed annual financial statements | Not publicly filed. Audited annually; audits go to donors and the regulator, not a public repository |
| A searchable public registry entry with named trustees | The register exists; the organization's original 2011 trust deed predates digitization, and the framework transition adds ambiguity |
| Independent web presence to corroborate | A minimal site and a Facebook page. The organization's reputation is entirely local and offline |
| Press coverage, directory listings, third-party evaluation | Almost none in retrievable form |
| Named governance in a public record | Trustees are named in the deed, which is a paper document in a registry office |

**None of that means the documents do not exist.** The audit exists. The trust deed exists. The trustees are named on it. The organization's reporting into the national health system is more rigorous than anything most of the US bundles produce. **It is all real and none of it is retrievable by an external process looking in the places that process was built to look.**

## Read this against Poland, or the lesson goes wrong

If this were the collection's only international bundle, the obvious and incorrect conclusion would be that **organizations outside wealthy countries are harder to verify.**

[The Polish bundle](../synthetic-fundacja-prawo-i-schronienie/README.md) is there to prevent that. Poland's KRS is a public court register with structured entity records, named board members, and filed financial statements in an online repository — **more machine-readable than the American equivalent.** That organization verified more easily than several US bundles here, at 0.92.

So the collection contains three information environments:

- **Poland** — a public court register with filed financials. **Easier than the US.**
- **Colombia** — a real public registry with less depth. **Comparable to the US.**
- **Kenya** — records that exist and are not externally retrievable. **A method failure.**

**Verifiability tracks the information environment, not the competence of the organization and not the wealth of the country.** One international bundle would have taught a simpler and wronger lesson; three teach the actual one.

## The learning runs uphill

The `learn_with` edge to [Sierra Foothills](../synthetic-sierra-foothills-community-health/README.md) in California is reciprocal, and the direction of expertise is worth being explicit about.

Sierra Foothills has **$7.9M**, contracted IT support, an EHR vendor, and a compliance officer. Nyando Health has roughly **KES 62M** and no developer.

**Sierra Foothills' mobile unit charts on paper**, because its clinicians lose connectivity on rural roads and there is no offline workflow. Nyando Health solved that problem years ago out of necessity, and its 142 promoters capture structured data offline as a matter of routine. **On the specific question of delivering and documenting care where the network is not, the Kenyan organization is years ahead of the Californian one.**

Anyone traversing this edge and assuming expertise flows from the larger budget to the smaller will get it exactly backwards. That is why the edge is in the collection.

## A note on language and currency

The organization works in **Dholuo**, **Kiswahili**, and **English**. Community health promoters work in Dholuo; reporting is in English; training happens in a mix. There is no way in the current schema to mark which language a field is authoritative in — the same gap [Poland](../synthetic-fundacja-prawo-i-schronienie/README.md) and [Colombia](../synthetic-corporacion-rio-vivo/README.md) raise.

**Figures are in Kenyan shillings and are not converted.** `budget_currency: KES`.

## One thing verification could not establish

Nearly everything — see [eligibility](verification.md). But the substantive gap, separate from the documentary one: **whether the promoter stipend model is financially sustainable.** 142 promoters on stipends funded largely by two international donors, in a national policy environment where the question of who pays community health workers has been contested for years. The organization is candid that a change in either donor's priorities would be existential.

*(mechanical[^registry]: the simulated determination labels essentially all standard fields "Unverifiable — records not externally retrievable"; sustainability "Not assessed — out of scope.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials
[^registry]: Registry record (simulated)
