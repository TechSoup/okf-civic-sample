---
type: volunteer-constraints
title: "synthetic-Valle Verde Food Network — Volunteer constraints & preferences"
description: "The org's own rules for technology volunteers. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & preferences

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**, and it starts from sensible defaults and diverges as the org fills it in. An agent scoping a project must treat these as non-negotiable.

*Pre-seeded with defaults appropriate to a rural food organization serving farmworker communities, then revised by the organization where the defaults didn't fit.*

## The two hard rules

**1. We do not collect names, addresses, or immigration status. This is not negotiable and it is not a preference.**

Nothing a volunteer builds may create a place to put a participant's identity, even an optional field, even one nobody is required to fill in. An optional field for a name is a name field, and the first time a well-meaning volunteer coordinator starts using it we have created a list that endangers the people on it. Household counts and box counts only. If a funder's requirement conflicts with this, that is a conversation we will have with the funder, and we have had it before.

**2. Assume there is no network, because on most of our routes there isn't one.**

We have already learned this the expensive way. Four tablets, 2021, abandoned in six weeks because the software wanted a connection to save a record. Anything built for route use must work **fully offline for a whole working day** and sync when it gets back to a signal — and it must be obvious to the coordinator that the data is safe before the signal exists. A spinner is not reassurance. Design for the dead zone as the normal case, not the exception.

## Language and literacy

- Our communities speak **Spanish, Mixtec, and Triqui**. The last two are, for our purposes, **spoken languages** — written translation is often not a usable answer, and there is variation between communities. A recorded voice message from the right person beats a perfect written translation.
- A meaningful share of the adults we serve have **limited literacy in any language**. Text-first design excludes them regardless of which language the text is in. Icons, voice, and demonstration carry more than words do.
- **A translate widget is not language access.** We have one on our website and it does almost nothing for our population. Don't propose it as a solution.
- **The promotoras are the interface.** Anything that routes around them will not reach anyone. Anything that adds work to their day will be quietly abandoned, and they will be right to abandon it. Build for them, with them, or don't.

## Working with our field staff

- **Seasonality is the schedule.** Late winter and midsummer are peak load and nobody has time. The workable windows are **April–May and October–November**. A volunteer who plans February design sessions with route coordinators is planning a project that doesn't happen.
- **Ride a route before you design anything.** Not optional. A full day, on the truck, at the tailgate. Everything about why the paper works and the tablet didn't is obvious after one route and invisible before it.
- **Route coordinators are drivers, not desk staff.** They have twenty minutes at the warehouse before they leave and they are tired when they get back. Training that requires a sit-down session will not land; the tool has to be learnable in five minutes.

## WhatsApp

We know. It's on personal phones, there's no retention policy, and if a group admin leaves we have a problem. **Do not propose replacing it.** Everything else is worse at voice messages, worse in bad coverage, and not already installed on everyone's phone. If you want to help here, help us make it more robust — more than one admin per group, important decisions written down somewhere else too — not migrate it.

## Everything else

- **Water-distribution logs are our only compliance record** for that program. Treat them as records, not spreadsheets to be tidied.
- **Volunteers who don't speak Spanish are welcome** for backend and technical work. Anything involving direct contact with community members needs Spanish at minimum, and honesty about what you can't say.
- **Handover:** no IT staff. Prefer configuration over code, managed services over anything we'd have to host, and documentation in plain language. If it needs a developer to change a field, it will stop being changed.
- **Eligibility limits:** background check required for anything involving contact with families or with the promotora program's records. Not required for backend-only work.
