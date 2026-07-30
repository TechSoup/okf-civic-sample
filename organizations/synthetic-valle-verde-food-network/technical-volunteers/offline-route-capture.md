---
type: volunteer-request
title: "Route data capture that survives a day with no signal"
description: "Replace paper route sheets with offline-first capture that works in dead zones, so a seasonal demand spike is visible in days instead of two weeks."
tags: ["technical-volunteers", "request", "draft", "synthetic", "offline-first", "infrastructure"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: hardware-network-infrastructure
---

# Volunteer project — Offline route capture

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

Nine routes, two-week cycle, clipboard on the dash. The coordinator tallies households at each stop, the sheets come back to the warehouse, and somebody keys them in when they get to it — which is sometimes ten days later.

In February we ran out of boxes on two routes three cycles in a row before anyone realized demand had jumped. The information was sitting in a stack of paper on a desk. By the time we could see the spike, it was over and we'd missed it.

## We already tried the obvious version of this

**This matters more than anything else in this request.** In 2021 we got four tablets through TechSoup for exactly this. We used them for six weeks and stopped.

They failed because the software needed a connection to save. A coordinator would enter twenty households, drive into a dead zone, and lose the entries. Twice was enough. The coordinators went back to paper and they were right — paper does not lose your afternoon.

The tablets are in a drawer in the warehouse office. If your proposal is a tablet with a form on it, we have done that. See [inventory](../technology/inventory.md).

## What it would do

Capture household and box counts **at the tailgate, on a device, with no network**, hold them safely for a whole working day, and sync when the truck comes back into coverage — so the warehouse sees a route's numbers the same evening instead of ten days later.

## Confirm first (dependencies)

1. **Actual coverage, measured.** Nobody has mapped where the dead zones are on the nine routes. Do this first, on a route, with a logging app. It's the difference between "offline sometimes" and "offline for five hours," and the design depends on which.
2. **Whether the four tablets still work.** Five years in a drawer. If they charge and hold a battery through a route day, the hardware question is already answered and the money goes into software.
3. **The client-management platform** that runs warehouse inventory — its name, plan, and crucially whether it has an API or an import path. The route data has to land somewhere it can be reconciled against inventory.
4. **Whether the state reporting export actually works**, or whether someone is re-keying. If it's being re-keyed, that's a second, smaller win available in this project.
5. **What the coordinators want.** Ride a route first — per [constraints](constraints.md) this is required, not suggested. Ask them what they'd want on a screen. They have opinions and nobody has asked.

## What a volunteer would do (roughly 6–10 weeks, scheduled April–May or October–November)

1. **Ride a route.** Full day, on the truck. Per [constraints](constraints.md). Everything below will be wrong if this step is skipped.
2. **Map coverage** across all nine routes so the offline requirement is a measured number rather than an assumption.
3. **Build offline-first capture.** The non-negotiable properties, in order:
   - **Writes locally first, always.** The record is safe on the device before anything else happens.
   - **Visibly safe.** The coordinator can see, without understanding anything about sync, that today's numbers are recorded. Per [constraints](constraints.md), a spinner is not reassurance — a count of saved stops is.
   - **Survives a dead battery, a dropped device, and a force-quit.** A route day's data must not depend on the app closing cleanly.
   - **Learnable in five minutes** by someone with twenty minutes at the warehouse before they leave, and no follow-up training.
   - **Big targets, few fields, sensible defaults.** Household count and box count per stop. Nothing else unless a coordinator asks for it.
4. **Sync on return** — automatic when coverage returns, with a clear indicator of what has and hasn't gone through, and no silent failures.
5. **Reconcile into the warehouse platform** so route counts and inventory can be compared, and the state report can be produced without hand-keying.
6. **Build the one view the organization actually needs:** current cycle against the same cycle last year, per route, visible the day after a route runs. That single view is what makes February visible in February.
7. **Keep paper as the fallback, permanently.** Not a transition plan — a standing fallback. A device fails on a route someday and the route still has to run.
8. Leave a **runbook**: add a stop, add a route, recover unsynced data, and produce the state report.

**Definition of done:** a coordinator completes a full route through measured dead zones, loses nothing, and the warehouse sees the numbers that evening. A demand spike is visible within one cycle. Paper still works if the device doesn't.

## What the volunteer should bring

- Genuine **offline-first** experience. This is the whole job. Local-first storage, conflict-free sync, and the instinct to distrust anything that assumes a request will succeed.
- **Mobile design for field conditions** — sunlight, dust, gloves, a tailgate, someone waiting. Not phone-app polish; field ergonomics.
- Ability to **integrate with a food-bank client-management platform**, or the patience to work out that it can't be integrated with and design around that.
- **Respect for a working paper process.** The paper is not the problem — the ten-day lag is. A volunteer who treats the clipboard as backwardness will design something worse than it.
- Willingness to write **plain-language documentation**, per [constraints](constraints.md).

Per [constraints](constraints.md), the two hard rules apply absolutely: **no field for a participant's name, address, or immigration status** — not even optional, because an optional identity field is an identity field once someone starts using it. And **assume no network as the normal case**. The promotoras are the interface for anything community-facing; this project is coordinator-facing, which is why it's tractable. Spanish is not required for this work, though it will make the route day go better.

## Capacity gained

The organization can see its own demand while it can still act on it. February stops being a surprise. Boxes get allocated to the routes that need them in the cycle that needs them, rather than in hindsight. And nine coordinators stop carrying a stack of paper that represents ten days of invisible information.

Second-order: if the state export works, someone stops re-keying data for a compliance report, which is a few hours a month back for a staff of eight.

## Data sensitivity

**Deliberately very low, and it must stay that way** — which is what makes this a good project for a volunteer with no prior relationship to the organization. Household counts and box counts, per stop, with no identifiers. There is nothing here that could harm anyone if it leaked, and that is a design achievement rather than an accident.

The pressure to change that will come later and from a reasonable direction: someone will point out that unduplicated counts would unlock a better funding formula, and that all it needs is a small identifier. [constraints](constraints.md) answers that question in advance, and the answer is no. A volunteer should build a system where saying yes later would require real work, not a checkbox.
