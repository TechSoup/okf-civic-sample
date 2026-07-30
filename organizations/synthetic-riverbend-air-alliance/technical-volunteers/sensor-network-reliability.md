---
type: volunteer-request
title: "Know when a sensor dies, and own the seven years of data behind it"
description: "Failure alerting for a 31-sensor community air network, plus getting the historical archive out of a vendor platform and into storage the organization controls."
tags: ["technical-volunteers", "request", "draft", "synthetic", "infrastructure"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: hardware-network-infrastructure
---

# Volunteer project — Sensor network reliability & data custody

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

We found out in April that a sensor on Foundry Line had been dead since February. Six weeks of readings gone, from the block closest to the rail yard, during the exact period we were preparing comments on a permit renewal. Nobody did anything wrong — we noticed because someone happened to look at the map and see a flat line.

And when we went to pull the historical data for that comment, it took nine days and two emails to the sensor vendor's support desk, because we don't actually know where our own seven years of readings live. We have a program that is entirely made of data, and no control over it.

## What it would do

Two things, in this order of importance:

1. **Alert us within an hour when a sensor stops reporting**, so a gap is a maintenance ticket instead of a hole in the record.
2. **Get the full historical archive into storage the organization owns**, with a documented export path that runs continuously from now on.

## Confirm first (dependencies)

The whole sensor stack is **sourced-directly and unverified** in this bundle — see [inventory](../technology/inventory.md). Step zero:

1. **The vendor platform and the contract terms.** Which platform, what plan, what the terms say about data export and ownership, and whether an API exists. Everything downstream depends on the answer, and this is a question for the organization's ED, not something a volunteer can discover from outside.
2. **Where the archive actually is.** "Roughly 2019 onward, with gaps" is what the bundle records. Establish what exists, at what resolution, and whether the gaps are known or merely suspected.
3. **The 31 host records** — where they live, who has access, and whether a confidentiality agreement is already in place. Per [constraints](constraints.md) these are the most sensitive records the organization holds.
4. **Whether the four gateways are doing anything.** They were installed for hosts with unreliable wifi; nobody has confirmed they still function.

If the vendor platform has no export API, the project changes shape considerably — the alerting half still works, the custody half becomes a negotiation rather than an integration.

## What a volunteer would do (roughly 4–8 weeks)

1. **Inventory the fleet properly.** 31 sensors, 4 gateways, last-seen timestamp for each, firmware state, host site. There is no current authoritative list; produce one.
2. **Build failure detection.** Poll the platform (or ingest its feed), and alert when a sensor's last reading exceeds a threshold — with sensible handling for the ordinary case of a host's wifi dropping for twenty minutes. Alert to somewhere staff already look, not a dashboard nobody opens.
3. **Set up continuous export** to storage the organization controls, running in parallel with the vendor platform. Per [constraints](constraints.md) this must be **additive** — the vendor path stays live, the new path proves itself over weeks, and no cutover happens during this project.
4. **Backfill the history** as completely as the platform allows, and — importantly — **document what could not be recovered**. A known gap is usable in a hearing; an unknown gap is a liability.
5. **Write down the chain of custody.** A one-page account of how a reading gets from a sensor to a chart, in language the ED can read aloud at a permit hearing. Per [constraints](constraints.md) this is a deliverable, not documentation of a deliverable.
6. **Check the published map's spatial precision** against the host-privacy commitment, and flag — not fix — anything that narrows a sensor toward a household.
7. Leave a **runbook** covering: adding a sensor, retiring a sensor, responding to an alert, and pulling a date range for a filing.

**Definition of done:** a sensor unplugged as a test produces an alert within the hour; the organization can pull any date range from storage it controls, without emailing a vendor; and the recovered archive's gaps are documented rather than discovered later.

## What the volunteer should bring

- **Data pipeline and integration** experience — APIs, scheduled jobs, object storage. This is plumbing, and good plumbing is the point.
- **Monitoring and alerting** judgment, especially about false positives. An alerting system that cries wolf twice a week will be muted in a month, and then the organization is back where it started with an extra system to maintain.
- Enough **IoT familiarity** to reason about a commodity sensor fleet: intermittent connectivity, power loss, firmware drift.
- Preference for **managed services over bespoke code**, per [constraints](constraints.md) — this organization has no developer to inherit a custom application.
- Willingness to write **plain-language documentation**, including the custody note that has to survive being read into a public record.

Per [constraints](constraints.md): the time series is **evidence**, so all work is additive and reversible and nothing is the only copy. **Host addresses are confidential** — a confidentiality agreement and least-privilege access are required, and nothing built here may increase the precision of what's published. And do not "improve" the interface by removing the organization's uncertainty language: the network is uncalibrated, the organization is careful about saying so, and that carefulness is an asset.

## Capacity gained

The organization stops losing evidence it can't get back. A dead sensor becomes a Tuesday errand instead of a discovery in April. Preparing a permit comment stops involving a vendor support ticket. And for the first time the organization can answer the question an opposing expert will eventually ask — *where did this number come from* — with a document instead of an explanation.

## Data sensitivity

**Mixed, and the two halves need different handling.** The readings themselves are low-sensitivity and meant to be public; that's the whole point of the program. The **31 host records are high-sensitivity** — residential addresses volunteered in confidence, tied to environmental data, held by an organization with no privacy policy. A volunteer should expect to touch the first freely and the second only under agreement, and may well find that the most valuable hour of this project is the one spent telling the organization that its host spreadsheet needs to move somewhere with access control.

No youth-corps data is involved. If the project expands to include corps members in the maintenance rotation — which the organization would welcome — the background-check requirement in [constraints](constraints.md) applies.
