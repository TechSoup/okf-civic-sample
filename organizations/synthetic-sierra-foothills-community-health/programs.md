---
type: programs
title: "synthetic-Sierra Foothills Community Health — Programs & services"
description: "What the organization runs. Fabricated."
tags: ["programs", "services", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  subject: ["SE050100", "SE050000"]
---

# Programs & services

**⚠ Synthetic — fabricated data.**

*The list below is **derived** (simulated) from public materials; a real organization would confirm and replace it with its own description.*

Sierra Foothills is a clinical organization, so its "programs" are service lines plus the logistics that get them to people.

- **Primary care** — three fixed sites, the core of the organization. Sliding scale, all payers, no one turned away.
- **Dental** — two of the three sites. Chronically oversubscribed; the organization describes dental as the service where its waiting list is longest and the consequences of waiting are most visible.
- **Behavioral health** — integrated into primary care rather than referred out, which the organization considers the most important change it has made in a decade and the hardest to staff.
- **Prenatal care** — a service line that matters disproportionately in a county where the alternative is a ninety-minute drive.
- **Mobile unit** — one vehicle on a fixed weekly rotation to communities with no site. Runs into the same connectivity problem as [Valle Verde's](../synthetic-valle-verde-food-network/programs.md) pantry routes, on some of the same roads.
- **Migrant and seasonal agricultural worker health program** — a dedicated program with its own outreach, extended hours during harvest, and a care model built around episodic presence.
- **Community health worker outreach** — a small team doing follow-up, navigation, and home contact. The practice area where the organization actively learns from [synthetic-Nyando Community Health Trust](../synthetic-nyando-community-health-trust/README.md), whose model is further along.

*(Ambulatory clinical care is the activity behind its [E32](../../_shared/ntee/E32.md) classification; the facility-based services are why it also carries [E30](../../_shared/ntee/E30.md).)*

## What "program" means differently here

Everything above is **separately regulated, separately reimbursed, and separately reported**, in ways that no other bundle in this collection has to contend with. A dental visit and a behavioral health visit have different documentation requirements, different payer rules, and different federal reporting lines.

The practical consequence for anyone reading this bundle: **program boundaries in a clinical organization are not descriptive choices, they are compliance structures.** Splitting or merging them in a data model is not a modelling preference — it can break a reimbursement claim. Any tooling that treats `programs` as free-form organizational self-description will handle this bundle wrong.

## Which of these should become its own file first

**The migrant and seasonal agricultural worker program.** It has its own funding, its own outreach staff, its own hours, its own care model, and — most importantly — the **episodic-presence problem** that drives the organization's hardest data question. It is currently one bullet and it is the reason the record-matching issue exists at all.

**The mobile unit** is the second candidate, because it is currently described as a delivery mechanism and functions as a distinct site with its own constraints, its own connectivity failures, and its own patient relationships.
