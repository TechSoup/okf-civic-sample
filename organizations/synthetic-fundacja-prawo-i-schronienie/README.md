---
type: org
title: "synthetic-Fundacja Prawo i Schronienie"
description: "A fabricated Warsaw foundation providing legal aid to refugees and migrants — the collection's GDPR bundle, and the one with the most machine-readable registry."
resource: https://synthetic-prawo-schronienie.example.org
aliases: ["synthetic-Fundacja Prawo i Schronienie", "synthetic-Law and Shelter Foundation", "Fundacja Prawo i Schronienie"]
tags: ["org-bundle", "nonprofit", "synthetic", "legal-aid", "refugees", "poland", "international", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-prawo-schronienie.example.org"
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
  subject: ["SJ040000", "SS090300", "SR040100"]     # PCS Subject facet
  population: ["PG010400", "PG010000", "PG010200"]  # PCS Population facet
  org_type: EA030000                                # PCS OrgType facet
  registration_country: PL                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  classification_note: "No NTEE code — NTEE is a US IRS vocabulary. PCS Subject and Population apply everywhere and are assigned directly from the activity description. ICNPO/ICNP-TSO would be the international NTEE counterpart and is left unassigned rather than guessed."
  provides: legal-representation
  org_type_note: "Polish *fundacja*. PCS OrgType EA030000 (Foundations) is the closest equivalent."
  registration:
    scheme: "KRS"
    id: "0000000000"
    tax_status: "organizacja pożytku publicznego (OPP) — public benefit organization status"
    legal_form: "fundacja (foundation)"
  budget_currency: PLN
  sdg: ["10", "16"]        # optional global layer; reaches 15 of 15
  situation: PL-MZ-warszawa
  data_protection_regime: "GDPR / RODO"
  verifiable_by: [techsoup]
---

# synthetic-Fundacja Prawo i Schronienie

*(synthetic-Law and Shelter Foundation)*

> **⚠ SYNTHETIC.** This organization does not exist. Its name, registration numbers, address, website, budget figures, programs, technology, and eligibility determination are all invented. The KRS, NIP, and REGON numbers are **all zeros**, a pattern never assigned, so they cannot collide with a real entity. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Fundacja Prawo i Schronienie ("Prawo i Schronienie") provides legal representation and advice to refugees and migrants in Poland. In the organization's own words:

> Protection is a legal status, and a legal status is a procedure, and a procedure is a set of deadlines in a language you do not read. We are the part between a person and the procedure.

*Mission: **org-sourced**[^org-site] (simulated), translated. The Polish original would be the canonical text in a real bundle — see the note on language below.*

Beyond that statement the picture is **derived** and would need confirmation: it employs **nine lawyers** (*radcowie prawni* and *adwokaci*) and **eleven advisers and caseworkers**, handles roughly **2,400 matters a year**, and works across asylum procedure, temporary protection status, residence permits, and employment rights for migrant workers. It was established in **2015** and obtained **OPP status** in 2018. Its caseload changed shape sharply in **2022** and has not returned to what it was.

It is a **mid-sized** Polish NGO — annual revenue around **PLN 4,800,000**, assets around **PLN 890,000**. Funding is a mix of EU programme money, Polish public funds, international foundations, and the **1% tax designation** that OPP status allows. Its office is at **ul. Nadrzeczna 14/3, 00-312 Warszawa, Poland**. *(mechanical, simulated.)*

- **What it does →** no NTEE code. See the classification note below.
- **Who it serves →** [population](population.md) — refugees and migrants in Poland; see also [SDG-16](../../_shared/sdg/SDG-16.md) (peace, justice, strong institutions) and [SDG-10](../../_shared/sdg/SDG-10.md) (reduced inequalities).
- **Where →** [PL-MZ-warszawa](../../_shared/situations/PL-MZ-warszawa.md) (Warsaw, Mazowieckie, Poland).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, at 92% confidence, established through a **registry more machine-readable than the American one**.
- **What it runs →** [technology](technology/index.md). Where GDPR changes the answers.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).

## What breaks in the schema here

**This is the first of three international bundles, and the reason they exist in the collection.** Four assumptions that hold across all twelve US bundles fail here.

**1. There is no EIN and no 501(c)(3).** This organization is a **fundacja** — a foundation under Polish law — registered in the **KRS** (*Krajowy Rejestr Sądowy*, the National Court Register), with a **NIP** tax identifier and a **REGON** statistical identifier. Its charitable standing is **OPP status** (*organizacja pożytku publicznego*), which is a designation with its own criteria, its own reporting, and one distinctive feature: it entitles the organization to receive **1% of an individual taxpayer's income tax** by designation, which is a funding mechanism with no US analogue.

The bundle carries `ein: null` explicitly rather than omitting the field. **Any script requiring `ein` will drop this organization**, and a null is easier to notice than an absence.

**2. There is no NTEE code, and there cannot be.** NTEE is maintained by the US Internal Revenue Service. It does not apply to Polish entities and assigning one would be inventing a fact. The international counterpart would be **ICNPO** (or the newer **ICNP-TSO**), and this bundle **leaves it unassigned rather than guessing** — the same rule that keeps PCS codes out of the whole collection.

Consequence: **SDG is the only classification vocabulary that reaches all fifteen organizations here.** See [the SDG hubs](../../_shared/sdg/index.md).

**3. Money is in złoty, and it is not converted.** `budget_currency: PLN`. PLN 4,800,000 is not translated into dollars anywhere in this bundle, because a converted figure is an exchange rate on an unstated date wearing the costume of a fact about an organization. If a downstream view wants USD, it converts at read time with a rate it can cite.

**4. The data-protection regime is GDPR, and it is not a stricter version of American privacy practice — it is a different structure.** Lawful basis, data-subject rights, records of processing, data-protection-by-design, and restrictions on transfers outside the EEA. That last one is the sharp edge: **a US-hosted cloud service is a legal question for this organization**, not a procurement preference. See [inventory](technology/inventory.md) — it is the substance of the [volunteer project](technical-volunteers/index.md).

## A correction to the obvious assumption

**It would be easy to assume international means less verifiable. For Poland the opposite is true.**

The KRS is a **public court register** with a searchable online interface, structured entity records, filed financial statements, and named board members. The OPP list is public and current. Establishing this organization's legal existence, governance, and financial reporting is **more straightforward and more machine-readable** than the equivalent for several of the US bundles, where the strongest evidence is a paper minute book in an office.

Compare [Frogtown Table](../synthetic-frogtown-community-table/verification.md) at 0.88 — a US organization whose governance records are in a folder. This Polish organization scores higher partly because Poland writes more of this down in retrievable public form.

**The collection's third international bundle, [Nyando in Kenya](../synthetic-nyando-community-health-trust/README.md), is genuinely hard to verify.** The point is that this is a fact about registries and information environments, **not about countries being more or less legible in general**, and a collection with only one international example would have taught the wrong lesson.

## A note on language

This bundle is written in English because the collection is. In a real Polish bundle **the Polish text would be canonical** and the English a translation, which raises a structural question the current schema has no answer for: there is no way to mark which language a field is authoritative in, or to carry both.

That is a genuine gap. An organization's own description of itself in its own language is the `org-sourced` record; a translation is `derived`, and the current provenance vocabulary cannot express that distinction.

## One thing verification could not establish

**Case outcomes are confidential**, the same boundary as at both US legal-aid bundles in this collection, though it arrives through a different door: Polish professional-secrecy obligations for *radcowie prawni* and *adwokaci* rather than the American attorney-client privilege doctrine. Different legal architecture, functionally the same limit — the information cannot be provided and a verification process should not ask.

Worth noting for anyone building comparison logic: **"privileged" is not a portable concept.** It is a US term of art. The underlying protection exists in most jurisdictions under different names with different scope, and a field that records `privileged: true` is quietly asserting an American legal framework.

*(mechanical[^registry]: the simulated determination labels case-level data "Not examined — professional secrecy.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials
[^registry]: Registry record (simulated)
