---
type: volunteer-constraints
title: "synthetic-Corporación Río Vivo — Volunteer constraints & security requirements"
description: "The org's rules for technology volunteers, where the failure mode is physical harm to community leaders. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic", "colombia", "security"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & security requirements

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**. It is the most serious file in this collection, and the reason is simple: the people we work with are among the most endangered human rights defenders in the world, and some plausible technology decisions would make that worse.

## What is actually at stake

We need to say this plainly rather than let it sit implied.

Colombia is one of the most dangerous countries on earth to defend land, water, or territory. Killings of defenders here are counted annually in large numbers, and the people at greatest risk are **rural community leaders** — which is exactly who the eleven organizations we accompany are made of.

**A document that links a named community monitor to a monitoring point and a sampling schedule tells someone where a specific person will be, at a predictable time, in an area where people have been killed for this work.**

That is not a privacy classification. It is not a compliance question. We are asking you to hold it as the first fact about any design.

## The hard rules

**1. Never assemble the linked dataset.** Monitor names, precise coordinates, and schedules must not exist together in any system, file, export, backup, or working copy — including yours, including temporarily, including on your own machine while you develop. If your design requires that join to exist even momentarily, the design is wrong and we need a different one.

**2. Never publish a map of monitoring points.** Our coalition partners in [Detroit](../../synthetic-riverbend-air-alliance/README.md) and [Louisiana](../../synthetic-gulf-corridor-justice-project/README.md) both publish theirs and they are right to. We are not them. If a benchmarking exercise says we are behind our peers on this, the benchmark is wrong.

**3. Reduced precision in anything that circulates.** Coordinates get truncated before they leave the accompaniment staff. Do not restore precision because a visualization would be better. Do not store the precise version "just in case."

**4. No schedules in any system.** When someone will be at a monitoring point is communicated verbally or over Signal, close to the date. It is not a calendar entry, not a task, not a field in a database.

**5. Never attribute a reading to a named person in anything that circulates.** Attribution is a normal, good data practice and here it is a hazard. Community organization level, at most, and only where that community has agreed.

## The data is not ours

**Monitoring data belongs to the eleven community organizations that produced it.** We hold it under agreements. We are stewards, not owners.

So:

- **We cannot authorize you to use it however you like**, because we cannot authorize ourselves to.
- **Publication, sharing, funder access, and research use each require the relevant community's decision**, through its own governance. A *consejo comunitario* has an assembly. The assembly decides. This takes time and that time is not an obstacle to be worked around.
- **If a community ends the relationship, its data goes with it.** Build so that is possible — data separable by community, extractable, and deletable. A system that cannot hand a community its own data and remove it from ours does not meet our obligations.
- **Do not design anything that requires pooling all eleven communities' data** to function. Some may not agree, and the design must survive that.

## Working securely with us

- **Signal for everything sensitive.** Not email. We will tell you what counts as sensitive, and when in doubt it does.
- **Full-disk encryption on your machine**, non-negotiable, and no organizational data in personal cloud storage or personal backups.
- **No screenshots.** Not for documentation, not for a bug report, not redacted.
- **Do not name us or our partner communities in a portfolio, blog post, talk, or code repository.** Not modesty — attribution creates a public link between you, us, and eleven communities. Ask before mentioning us anywhere.
- **Do not travel to the field areas** unless we arrange it, and do not go independently to "understand the context." Your presence is visible and it is not neutral.
- **Tell us immediately about any incident**, including a lost device or an accidental exposure. Immediately. Not after you have investigated.
- **Prefer local processing and local storage.** Every additional service is another party who might be compelled, breached, or simply careless with something that has these consequences.

## On AI

- **No community data, monitor identity, or location data into any AI service.** Any, ever, for any purpose. We cannot tell a community what happened to its data if it has gone to a model, and we have promised them we could.
- **Public documents — licences, agency resolutions, filings — are a reasonable place for extraction assistance**, and would help us. Output is a lead for a person to verify, never a fact.
- **Nothing generated presented as our analysis.** We defend our findings in front of authorities who would like them to be wrong.

## Language

- **Spanish is required** for anything community-facing, and community materials are written by us, not by you.
- **English is fine for working with our technical and administrative staff.**
- **Community monitors vary in literacy** and several are more comfortable with voice than text. Do not design a text-first interface for them.

## Practical

- **Confidentiality agreement and a security conversation with our operations coordinator** before any access. The second is substantive; if it goes badly we stop, and that is a reasonable outcome for both of us.
- **Bad connectivity is the normal case** in the field areas. Design for it.
- **Handover:** seventeen staff, no developer, and no prospect of one. Configuration over code, and anything needing maintenance needs an owner agreed in advance.
- **Our accompaniment staff are the scarce resource**, and they are usually in the territory.

## What we would say no to

- A map of monitoring points.
- A consolidated database joining monitors, locations, and schedules.
- Attribution of readings to named individuals.
- Anything that pools all eleven communities' data as a requirement.
- Community data in an AI service or a third-party analytics tool.
- A volunteer who wants to publicize the work.
- A volunteer who tells us our security practices are excessive. We have buried people.
