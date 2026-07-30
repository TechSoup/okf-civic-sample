---
type: volunteer-request
title: "Let each community see its own water data — and nobody see all of it"
description: "A low-bandwidth Spanish dashboard giving eleven community organizations access to their own monitoring findings, designed so the dataset that would endanger monitors is never assembled."
tags: ["technical-volunteers", "request", "draft", "synthetic", "reporting", "security"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: reporting-dashboard
---

# Volunteer project — Community findings dashboard

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

A community monitor takes a reading, tells us by phone or over Signal when she reaches a signal, and we write it down. Then we analyse it, and months later we present findings at an *asamblea* on paper, or in a filing.

The communities have asked us, reasonably, why they cannot see their own numbers. They collected them. They own them. And when they are sitting in a meeting with a company or an environmental authority, the person who took the samples should be able to say what the river has been doing for the last eight months without waiting for us to prepare something.

So: give each community access to its own data. In Spanish. On a phone, over a connection that barely works.

## The constraint that makes this hard, and interesting

**We are not asking you to build a database of our monitoring programme.** That is the thing we must never have. See [constraints](constraints.md).

A monitoring database that joins **who took the sample**, **exactly where**, and **when** is a document telling someone where a named community leader will be at a predictable time, in a country where people doing this work are killed. Our data is currently fragmented across paper, Signal messages, and compartmentalized staff knowledge, and **that fragmentation is a protective measure rather than a mess.**

So the design problem is genuinely unusual: **give eleven communities useful access to their own readings, while ensuring the dangerous linked dataset never exists — not in the system, not in a backup, not in an export, not on your laptop during development.**

That is possible. It requires deciding what not to store before deciding what to build.

## Confirm first (dependencies)

1. **What each community actually wants to see.** Eleven organizations, each with its own assembly, and they will not all want the same thing. Ask through our accompaniment staff — **do not approach communities directly**, per [constraints](constraints.md).
2. **What the agreements say.** Our data-stewardship agreements with the eleven organizations govern what we may do. Some may be partly informal. Establishing what each one permits is prerequisite work and may be the most valuable thing this project produces.
3. **Real connectivity where monitors and community leaders are.** Not what a coverage map claims. Measured.
4. **What devices they actually have.** Assume older Android phones, limited storage, metered data, and shared handsets.
5. **Whether our precision-reduction practice is documented** or is one staff member's habit. Per [inventory](../technology/inventory.md) this is the most tractable unknown in the bundle, and this project should not proceed on an undocumented control.

## The design, stated as constraints before features

Per [constraints](constraints.md), these come first:

- **Readings carry a monitoring point and a date. They do not carry who took them.** Attribution stops at the community organization, and only where that community agreed.
- **Coordinates are reduced precision, everywhere in the system.** There is no full-precision field. Not hidden, not admin-only — **absent**.
- **No schedules.** The system records that a reading happened, never that one is going to.
- **Each community sees only its own data.** No cross-community view exists — not for communities, not for staff, not for funders. Per [constraints](constraints.md), do not build anything that requires pooling all eleven.
- **Data is separable, extractable, and deletable by community.** If a community ends the relationship, it takes its data and we remove it. This has to be a one-command operation, not a project.
- **Aggregation levels are set by each community's agreement**, carried in the system rather than left to whoever runs a query.

Only then:

## What a volunteer would do (roughly 8–12 weeks)

1. **Work through the agreements with our operations coordinator** before designing. Dependency 2, and it bounds everything.
2. **Design the data model as a subtraction exercise.** Start from what a monitoring system would normally hold and remove every field that contributes to the linked dataset. Write down what was removed and why — that document is a deliverable and it is what lets the next person avoid re-adding a field for a good-sounding reason.
3. **Build for a bad connection on an old phone.** Small payloads, works over 2G, degrades to a static view, no map tiles pulled unnecessarily, readable on a cracked screen in sunlight. Spanish only in the interface; per [constraints](constraints.md) we write the text.
4. **Build the trend view that matters** — this monitoring point, these readings, over time, against the relevant standard, with our uncertainty language intact. Per [constraints](constraints.md), do not strip the caveats because a chart is cleaner without them, and do not present field-instrument readings with laboratory confidence.
5. **Make it usable in an assembly.** The realistic use is someone holding a phone in a meeting with a company representative. That means large type, few taps, and something printable, because a printed sheet works in a room with no signal.
6. **Handle intake without creating a schedule.** Monitors report by phone or Signal to accompaniment staff, who enter readings. **Do not build monitor-facing data entry** — a monitor entering a reading from a location at a time creates exactly the record we are avoiding.
7. **Per-community export and deletion**, tested by actually doing it.
8. **Document the protective controls** — precision limits, no-attribution, no-schedules, per-community isolation — as requirements with reasons, in Spanish and English. Per [inventory](../technology/inventory.md), our security practice currently lives in a few people's habits. **Turning it into documentation may outlast the dashboard.**
9. Leave a **runbook** our operations coordinator can follow, and confirm per [constraints](constraints.md) who maintains this after you go.

**Definition of done:** a community leader opens a phone in an assembly and shows eight months of her river's readings, in Spanish, over a bad connection; no view anywhere in the system attributes a reading to a person or reveals a precise location or any schedule; each community's data can be exported and deleted in one operation; and the protective controls are written down as requirements rather than habits.

## What the volunteer should bring

- **Low-bandwidth, low-end-device engineering.** Genuine skill, not a responsive layout. Old Android, 2G, metered data, offline-tolerant.
- **Data minimization as a design discipline** — the ability to build by subtraction, and to argue against your own instinct to store more. **This is the core competence for this project.**
- **Security thinking calibrated to physical risk.** Not compliance security. If your threat model tops out at reputational damage, this is not the right project for you.
- **Spanish** — required for working with our staff on anything user-facing, and for the documentation.
- **The temperament to accept constraints you cannot fully verify.** We are not going to explain every operational detail of how we protect people, and you will have to build within limits whose full reasoning you are not given. Some volunteers find that intolerable, which is fair, and better discovered now.
- Willingness to write documentation that will be read by non-technical staff in two languages.

Per [constraints](constraints.md): **never assemble the linked dataset**, no map of monitoring points, reduced precision only, no schedules anywhere, no individual attribution, no pooling requirement, **no community data in any AI service or third-party analytics**, Signal for sensitive communication, encrypted machine, no screenshots, no publicizing this work, and **no independent travel to the field areas**.

## Capacity gained

Eleven community organizations get access to evidence they produced and own. That is a shift in who holds the knowledge, which for an organization built on *acompañamiento* is the point rather than a side benefit — the community stops depending on us to tell it what its own river is doing.

Practically: a leader can answer a company's claim in the room instead of two months later.

And underneath: **our protective practice becomes documented.** Right now the most important security controls in this organization are habits held by a handful of people who could leave. Writing them down as system requirements, with reasons, is arguably worth more than the dashboard.

What this does not do: improve the science. Field instruments with periodic laboratory verification remain what they are, and per [README](../../../README.md) we are careful about what we claim from them. A dashboard that made the data look more authoritative than it is would be a step backwards.

## Data sensitivity

**The highest-consequence data in this collection, and the consequence is physical.**

Elsewhere in these fifteen bundles the worst outcome of a data failure is serious: a criminal record disclosed, an asylum account exposed, a client list reaching immigration enforcement. Here the worst outcome is that **someone is killed** — and the mechanism is not exotic. It is a well-organized dataset, in a country where this work carries that risk, reaching someone who wanted it.

Two things follow that are worth stating for anyone reading this collection as a whole:

**The safest system is the one that never holds the dangerous thing.** Not the one with the best access controls on it. Access controls fail, get misconfigured, get compelled, and get inherited by whoever comes next. A field that does not exist cannot be exposed. That is why this project is specified as a subtraction.

**"More data, better integrated, more accessible" is a default, not a law.** It is right most of the time, which is why it is a default, and it is wrong here in a way that has a body count. A volunteer, a rubric, or a model that cannot recognize the exception will do harm while following best practice — and that, more than anything else, is what this bundle is in the collection to demonstrate.
