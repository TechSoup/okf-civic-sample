---
type: population
title: synthetic-Frogtown Community Table — Who it serves
description: The immigrant and refugee households the organization serves, and why a demographic list is the least useful half of it.
tags: [population, beneficiaries, synthetic]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: program-reporting
    resource: "simulated programme and funder reporting"
    title: Programme and funder reporting (simulated)
    author: process:program-reporting
    last_modified: 2026-02-28
  - id: org-staff
    resource: "simulated conversation with organization staff"
    title: Organization staff, directly (simulated)
    author: human:org-staff
    last_modified: 2026-03-02
x-civic:
  profile: civic/0.6
  population: [PG010000, PG010400, PG030000]
---

# Who Frogtown Table serves

**⚠ Synthetic — fabricated data.**

Frogtown Table serves **immigrant and refugee households** in Frogtown and adjacent Saint Paul neighbourhoods — roughly **1,900 households a year**, with about 700 using the shelf regularly.[^program-reporting] The five largest communities are [[Hmong]], [[Karen]], [[Somali]], [[Oromo]], and [[Latino]], alongside longer-settled Black and white households in the same blocks.[^org-staff]

The required frontmatter says `PG010000`, `PG010400`, `PG030000` — immigrants and migrants, refugees and displaced people, economically disadvantaged people. That is correct, it is queryable, and it is comparable to every other bundle using the PCS Population facet. It is also three codes doing the work of five communities that do not consider themselves interchangeable, which is why the specific terms are carried as wikilinks in the prose. See [README.md](README.md) on why both layers exist.

## Culturally-specific service is a program design, not a demographic

**The most useful modelling observation in this bundle.**

It would be easy to record this organization's distinctiveness as a population attribute — a list of ethnic groups in a field. That misses what is actually going on. Stocking for these five communities changes:

- **Procurement.** Rice by the fifty-pound bag, not the two-pound box. Fresh herbs and greens that a standard food-bank pallet does not carry. Halal meat, sourced separately, with certification that has to be real. Whole fish. Dried beans in varieties a general pantry does not stock.
- **Storage.** More cold and more dry-goods volume per household served than a conventional shelf needs, in a building that was not designed for it.
- **Volunteer recruitment.** Volunteers who can talk to shoppers, which means recruiting from the communities rather than for general goodwill.
- **The shelf layout itself** — organized so that someone who reads no English can shop it.
- **What counts as success.** A household taking food it will actually cook, rather than a box distributed.

None of that is expressible as a demographic tag. **It is a set of operational commitments that follow from who the neighbours are**, and a schema that only offers a population list will record the least consequential half of it.

Worth stating as an open gap rather than pretending it is solved: there is no field in `civic/0.6` for "the way we do this is shaped by who we serve." Right now it lives in this document's prose, which is where OKF puts things that resist frontmatter. That may be the right answer. It may also be the next field.

## Language

Five languages before English: **Hmong, Karen, Somali, Oromo, Spanish**.[^org-staff] Practical realities:

- **Karen** is the smallest and least-resourced of the five for translation purposes, and the community includes households with limited literacy in any written language.
- **Oromo and Somali** are distinct languages and distinct communities, and treating them as one because both are "East African" is an error the organization sees made about it regularly.
- The organization staffs and recruits volunteers **from the communities**, which is why its language access works. It does not run on translation services.
- **Written translation is a partial answer.** Signage helps; the shelf is navigable by anyone because it is organized visually.

## What is collected, and the deliberate limits

The shelf records **household counts, household size, and neighbourhood** — enough for the regional food bank's allocation formula.[^program-reporting] It records a household's community affiliation **only if the household volunteers it**, because it is used for procurement planning and for nothing else.[^org-staff]

**It does not record immigration status, and it does not record names for shelf visits.** The households using this shelf include people for whom a list is a hazard.

Donor records are a different matter and are kept properly, in a donor database. **Donors are named; shoppers are counted.** That distinction is deliberate and clean, and it is one of the reasons this organization's data practice is the tidiest thing about it.

Note what the frontmatter does *not* carry: there is no field here recording immigration status, and there should not be one. An absence maintained on purpose is different from a gap, and the difference is only visible because this paragraph says so.

[^program-reporting]: Programme and funder reporting (simulated)
[^org-staff]: Organization staff, directly (simulated)
