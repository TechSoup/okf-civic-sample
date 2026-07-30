---
type: volunteer-request
title: "Harvest and distribution reporting the farm managers don't have to retype"
description: "Replace paper notebooks and Sunday-night data entry with mobile capture and one dashboard that answers every funder's question."
tags: ["technical-volunteers", "request", "draft", "synthetic", "reporting"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: reporting-dashboard
---

# Volunteer project — Harvest & distribution reporting

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

Every farm site keeps a notebook. Pounds harvested by crop, crates out the door on distribution day, households through the line. On Sunday night a farm manager sits down and types the week into a spreadsheet, and once a quarter somebody spends two days turning six spreadsheets into a funder report. The numbers are real and hard-won, and by the time anyone can act on them they're eleven weeks old.

Three funders want three different cuts of the same data — one wants pounds by crop, one wants households served by month, one wants the ratio of food grown on site to food distributed. Nobody can answer any of them without a week's notice.

## What it would do

Capture harvest and distribution numbers **at the site, on a phone, in under a minute**, and roll them up into a single dashboard that answers the standing funder questions without anyone reformatting anything.

## Confirm first (dependencies)

The bundle records **Airtable** as the program-data home, but that's **sourced-directly and unverified** — it does not appear in the TechSoup history and a website scan wouldn't see it. See [inventory](../technology/inventory.md). Step zero:

1. **Confirm Airtable** — is it real, who administers it, what plan, and is the nonprofit discount already applied?
2. **Confirm which productivity suite is authoritative.** The bundle shows both **Microsoft 365** (donated, ~12 seats) and **Google Workspace** in use. A volunteer needs to know which identity system staff actually log into before building anything they have to sign into. This is a decision for the organization, and it may be worth making before this project rather than around it.
3. **Confirm what the three funders literally require** — the reporting formats, in writing. Building to a remembered version of a funder's ask is how dashboards get rebuilt.

If Airtable turns out to be aspirational, the project changes shape — the capture layer stays, the storage decision reopens.

## What a volunteer would do (roughly 3–5 weeks)

1. **Sit through one distribution day** before designing anything. Per [constraints](constraints.md), this is required, not optional — the notebooks make sense once you've seen the conditions.
2. Model the data: crop, weight, date, site, and destination for harvest; crates and household counts for distribution. **Aggregate counts only** — see the hard constraint below.
3. Build mobile capture that works **with cold hands, in sunlight, wearing gloves, on a cracked phone, possibly with no signal**. Offline-tolerant, syncing later. Big targets, few fields, defaults that are right most of the time.
4. Build one dashboard with the three funder cuts as saved views, plus a season-to-date total the staff actually want for themselves.
5. Handle the real edge cases: a site that skips a week, a crop weighed in crates rather than pounds, a distribution day cancelled for weather, a number entered wrong and noticed a month later.
6. Leave a **one-page runbook** so a staff member can add a site or a crop, or change a funder view, without a developer.

**Definition of done:** a farm manager records a harvest from the field in under a minute, the dashboard shows it the same day, and the quarterly funder report is produced by selecting a date range instead of by two days of spreadsheet work.

## What the volunteer should bring

- Comfort with a **low-code data platform** (Airtable, or whatever the confirmation step lands on) including forms and views.
- **Mobile-first form design** judgment, and the humility to design for gloves and glare rather than for a desk.
- Enough **reporting sense** to turn a funder's prose requirement into a saved view.
- Willingness to write **plain-language documentation** for non-technical staff.

Per [constraints](constraints.md): **no participant identification.** The distribution program is open-door by commitment, not by oversight — a volunteer must not build anything that starts collecting names, addresses, or status from the food line, no matter how much cleaner the data would be. Aggregate counts only. Anything touching the youth farm crew's employment records requires a background check and is better scoped out entirely. And remember the seasonal window: this is winter work, or it doesn't happen.

## Capacity gained

Farm managers get their Sunday nights back. The organization can answer a funder question in an afternoon instead of a week, and — more useful — can see mid-season that one site is behind and do something about it while there's still season left. The quarterly report stops being a two-day event.

## Data sensitivity

Deliberately **low**, and it should stay that way. Harvest weights and household counts are not sensitive, which is exactly why this project is a good first one for a volunteer with no relationship to the organization yet. The two sensitive things nearby — **minor-employee records** and **any identification of program participants** — are both explicitly walled off in [constraints](constraints.md). A volunteer who finds themselves reaching for either has drifted out of scope.
