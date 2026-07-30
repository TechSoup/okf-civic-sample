---
type: population
title: "synthetic-Motor City Trades Institute — Who it serves"
description: "The adults entering the trades that the organization serves. Fabricated."
tags: ["population", "beneficiaries", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: program-reporting
    resource: "simulated programme and funder reporting"
    title: "Programme and funder reporting (simulated)"
    author: process:program-reporting
    last_modified: 2026-02-28
x-civic:
  profile: civic/0.6
  population: ["PA020000", "PG040000", "PJ020000"]
---

# Who Motor City Trades serves

**⚠ Synthetic — fabricated data.**

Motor City Trades serves **adults entering the skilled trades** — about **340 enrollments a year**, ages 18 to 54 with a median in the low thirties, roughly 70% Detroit residents and the rest from surrounding Wayne County. Most arrive without a trade credential and with a work history in retail, warehouse, or gig work. *(**corroborated**, simulated — enrollment counts are reported to the state and independently held, unlike the outcome figures.)*

Three sub-populations matter enough to name, because each brings different requirements:

**Returning citizens** — roughly **a third of enrollment**, arriving through a county reentry contract. This is the group that shapes the most about how the organization operates: which employers will interview a graduate, which trades have licensing barriers tied to conviction history, and how the organization thinks about background checks — including for its own volunteers. See [constraints](technical-volunteers/constraints.md), where that reasoning is written out.

**Adults needing a math bridge** — about 40% place below the arithmetic level the apprenticeship entrance exams require. The bridge program exists because the trade training is useless to someone who cannot pass the test at the end of it.

**Young adults referred from partner organizations** — a smaller stream, including farm-crew graduates from [synthetic-Eastside Harvest Collective](../synthetic-eastside-harvest-collective/README.md). Younger, less work history, higher completion rates.

## Data on this population is unusually sensitive, and unusually fragmented

Two things are true at once. This organization holds the **most sensitive participant data in the collection** — conviction histories, income verification, benefits status, drug-screen results required by employer partners, and in some cases immigration documentation. And it holds that data across **three systems that do not agree with each other**, none of which is authoritative. See [inventory](technology/inventory.md).

Anything reading this bundle should register that combination. The consolidation project in [technical-volunteers](technical-volunteers/index.md) is not a tidiness exercise; it is a project that touches conviction records, which is why its constraints are the tightest in the collection.

*Provenance: **corroborated**[^program-reporting] for enrollment (simulated state reporting); **derived** for demographic detail. Retention and placement figures are **organization-held and single-source** — see [README](README.md).*

Community context for Detroit — labor market, wage levels, transit access to job sites, the regional apprenticeship landscape — belongs to the place, not here: see [US-MI-detroit](../../_shared/situations/US-MI-detroit.md). This file says *who*; the situation node says *the conditions around them*.

[^program-reporting]: Programme and funder reporting (simulated)
