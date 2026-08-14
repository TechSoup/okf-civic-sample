---
type: org
title: "synthetic-Corporación Río Vivo"
description: "A fabricated Colombian watershed-defense organization where digital security is physical security, and where the communities own their own data."
resource: https://synthetic-rio-vivo.example.org
aliases: ["synthetic-Corporación Río Vivo", "synthetic-Living River Corporation", "Corporación Río Vivo"]
tags: ["org-bundle", "nonprofit", "synthetic", "environmental-justice", "water", "colombia", "international", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-rio-vivo.example.org"
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
  subject: ["SC030400", "SC030407", "SJ040700"]     # PCS Subject facet
  population: ["PE030000", "PG090000", "PJ080000"]  # PCS Population facet
  org_type: EA000000                                # PCS OrgType facet
  registration_country: CO                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  classification_note: "No NTEE code — NTEE is a US IRS vocabulary. PCS Subject and Population apply everywhere and are assigned directly from the activity description. ICNPO/ICNP-TSO would be the international NTEE counterpart and is left unassigned rather than guessed."
  provides: watershed-defense
  org_type_note: "Colombian *corporación* (ESAL). No PCS OrgType level-2 code matches the form, so the level-1 parent EA000000 is used deliberately rather than forcing a closer-looking child."
  registration:
    scheme: "NIT"
    id: "900.000.000-0"
    tax_status: "Régimen Tributario Especial (RTE)"
    legal_form: "ESAL — entidad sin ánimo de lucro (corporación)"
  budget_currency: COP
  sdg: ["6", "13", "16"]        # optional global layer; reaches 15 of 15
  situation: CO-VAC-cali
  relations:
    - { target: synthetic-riverbend-air-alliance, type: coalition_with }
    - { target: synthetic-gulf-corridor-justice-project, type: coalition_with }
  data_protection_regime: "Ley 1581 de 2012 (habeas data)"
  verifiable_by: [techsoup]
---

# synthetic-Corporación Río Vivo

*(synthetic-Living River Corporation)*

> **⚠ SYNTHETIC.** This organization does not exist. Its name, NIT, address, website, budget figures, programs, technology, and eligibility determination are all invented. The NIT's check digit does not validate, so it cannot be a real one. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Corporación Río Vivo ("Río Vivo") works with river communities in the Cauca basin of Valle del Cauca to document and contest what is being discharged into their water. In the organization's own words:

> The river is not a resource here. It is where people bathe, fish, wash, and bury. When a company obtains a licence to discharge into it, somebody has decided that those things matter less than the licence. We are the argument that they don't.

*Mission: **org-sourced**[^org-site] (simulated), translated. The Spanish original would be canonical in a real bundle — see the language note.*

Beyond that statement the picture is **derived** and would need confirmation: it accompanies **eleven community organizations** — including Afro-Colombian *consejos comunitarios* and campesino associations — supports **community water monitoring** at some thirty points along two tributaries, brings **administrative and legal actions** including *acciones populares* and *tutelas*, and provides technical support in **consulta previa** processes. It was founded in **2009**.

It is a **mid-sized** Colombian ESAL — annual revenue around **COP 1,900 million**, assets around **COP 340 million**, and about **17 staff**. Funding is European and North American foundations, some EU cooperation money, a small national contribution, and modest local giving. Its office is at **Calle 118 Norte # 0-00, Cali, Valle del Cauca, Colombia**. *(mechanical[^registry], simulated.)*

- **What it does →** no NTEE code. See the classification note in the frontmatter.
- **Who it serves →** [population](population.md) — river communities with collective territorial rights; see also [SDG-06](../../_shared/sdg/SDG-06.md) (clean water), [SDG-13](../../_shared/sdg/SDG-13.md) (climate action), and [SDG-16](../../_shared/sdg/SDG-16.md) (peace, justice, strong institutions).
- **Where →** [CO-VAC-cali](../../_shared/situations/CO-VAC-cali.md) (Cali and the Cauca basin, Valle del Cauca, Colombia).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, at 89% confidence, and **read the note on adverse-media screening**, which is the most important thing in that file.
- **What it runs →** [technology](technology/index.md). Where a location dataset is a safety question.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).

## Digital security is physical security here

**This has to come before anything else in the bundle, because it changes how every other section should be read.**

Colombia is, by a substantial margin, among the most dangerous countries in the world to be an environmental or land defender. Killings of defenders are documented annually in the dozens to hundreds, and the people most at risk are **community leaders in rural territories** — precisely the eleven organizations Río Vivo accompanies.

The consequence for a data bundle is direct and unsentimental:

- **A dataset linking a named community leader to a monitoring point and a schedule is a targeting package.** Not a privacy concern. A targeting package.
- **Publishing where sampling happens, when, and by whom** is a risk decision that belongs to the community taking the risk, not to the NGO holding the spreadsheet.
- **The organization's own staff receive threats.** Its office location is known and its litigation makes enemies with resources.
- **Encryption, device discipline, and compartmentalization are not compliance measures.** They are the reason specific people are still alive, and the organization treats them that way.

Anything reading this bundle — a person, a script, or a model — should register that the ordinary cost/benefit of "more data is better, published data is better" **inverts here**. [Constraints](technical-volunteers/constraints.md) is written accordingly, and it is the most serious file in this collection.

Compare the two coalition partners. [Gulf Corridor](../synthetic-gulf-corridor-justice-project/README.md) in Louisiana faces a lawful, funded, competent adversary and its problem is proving its evidence. [Riverbend Air](../synthetic-riverbend-air-alliance/README.md) in Detroit mainly needs its data to survive. **Same methodology, same coalition, and here the same practice can get someone killed.** That is why the coalition edge exists in this collection.

## The communities own the data, and the organization is explicit that it does not

Río Vivo's position — stated in its own agreements with the eleven organizations — is that **community monitoring data belongs to the communities that produced it.** Río Vivo holds it, analyses it, and helps present it, under agreements that specify what it may do.

This is not a courtesy. In practice it means:

- **The organization cannot unilaterally publish**, share with a funder, contribute to a research dataset, or hand to a journalist. Each requires the relevant community's decision, through its own governance — a *consejo comunitario* has an assembly, and that assembly decides.
- **A funder asking for the underlying data may be told no**, and has been.
- **If a community ends the relationship, the data goes with it.**

**The current bundle structure has no way to express this.** Every schema in this collection assumes the organization described is the owner and controller of the data in its bundle. Here the bundle's most important dataset is held under a stewardship arrangement with eleven separate owners, each with its own decision-making body.

That is a real modelling gap, and it is not exotic — it is the ordinary situation for any organization working with Indigenous, Afro-descendant, or other communities that assert data sovereignty. A bundle format that cannot say "we hold this, we do not own it, and here is who decides" will quietly misrepresent every one of them.

## A note on language and currency

The Spanish text would be canonical in a real bundle; this English is a translation, and the schema has no way to mark which language a field is authoritative in — the same gap [the Polish bundle](../synthetic-fundacja-prawo-i-schronienie/README.md) raises.

**Budget figures are in Colombian pesos and are not converted.** `budget_currency: COP`. COP 1,900 million is a meaningful figure to anyone who works in Colombia and a conversion would be an exchange rate on an unstated date pretending to be a fact.

## One thing verification could not establish

**Whether the water quality findings would survive technical challenge.** The community monitoring programme uses field instruments and a periodic accredited-laboratory check, which is a reasonable design under real budget constraints and is not the same thing as a defensible monitoring regime. The organization says so plainly and describes its data as establishing a pattern that obliges the authorities to investigate.

That framing is correct and it is not the framing the numbers appear in once they reach a court filing or a press release. Verification confirmed the programme exists and is run consistently; it did not assess the science. *(mechanical: the simulated determination labels monitoring methodology "Not assessed — out of scope.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials

[^registry]: Registry record (simulated)
