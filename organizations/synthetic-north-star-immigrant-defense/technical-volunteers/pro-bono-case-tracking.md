---
type: volunteer-request
title: "Connect 1,300 matters to the 90 attorneys carrying them"
description: "Close the seam between the case platform and the pro bono network spreadsheets — and establish what ninety outside attorneys are actually doing with client files."
tags: ["technical-volunteers", "request", "draft", "synthetic", "data-migration"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: data-migration-crm-consolidation
---

# Volunteer project — Pro bono network and case tracking

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

Ninety private-practice attorneys carry cases for us under supervision. They are the difference between us serving 1,300 matters and serving maybe 400.

Our matters are in our case platform. Our attorneys are in two spreadsheets — who we trained, when, who has capacity, who took what. Nothing connects them except people remembering.

So: a supervising attorney can't quickly see everything one pro bono attorney is holding. We can't reliably say who in the network is active this quarter. And a pro bono client sometimes calls our main line and reaches someone who cannot find their matter, which is a bad experience for a person who is already frightened.

## The thing we didn't ask about, which may matter more

Ninety outside attorneys hold our client files on their own firm infrastructure. **We have no visibility into what any of them does with that data and no standard we ask them to meet.**

Given [constraints](constraints.md) — our threat model, the fact that a list of our clients is the most dangerous artefact we hold — that is arguably our largest exposure, and it sits almost entirely outside our control. We have not addressed it because we do not know how to without straining relationships we depend on.

A volunteer who helped us think through a **minimum standard we could ask of network attorneys**, and a way to ask for it that ninety busy lawyers would actually accept, would be doing something more valuable than the tracking work. We would like both. If we could only have one, it might be this.

## Confirm first (dependencies)

1. **What the case management platform can do about a supervising-attorney relationship.** Can a matter carry an external attorney reference natively? If yes this project is mostly configuration. If no, it is an integration and a harder conversation about where the join lives. Nobody has asked the vendor.
2. **What the two pro bono spreadsheets actually contain**, including how much of the useful information is in a notes column. Expect the answer to be "a lot."
3. **What the vendor would do with a records demand.** Per [constraints](constraints.md), the question we ask about any service holding client data. It applies to the platform we already use, and nobody has asked it.
4. **Whether network attorneys would tolerate any new obligation.** They volunteer. A system that adds a login and a monthly update will be ignored, and then we will have worse data than we do now plus a system. Talk to five of them before designing anything.
5. **What "active" means.** We use the word and we do not define it. Trained ever? Took a case this year? Available now? The definition determines what any report means.

## What a volunteer would do (roughly 8–12 weeks)

### The tracking half

1. **Talk to network attorneys first** — five or six, per the dependency above. This determines whether the design is viable and it is the step most likely to be skipped.
2. **Define the pro bono attorney record** and its relationship to a matter: who supervises, who carries, what state the case is in, when it was placed. Define **active** explicitly.
3. **Put the relationship where the matters already are**, if the platform allows it. Per [constraints](constraints.md), configuration over code, and per the same file, resist creating a new store of client information — a second system holding a client-to-attorney mapping is a new copy of the most dangerous artefact the organization has. **Prefer extending what exists over building alongside it.**
4. **Migrate the spreadsheets**, including the notes columns, and document what could not be structured rather than dropping it.
5. **Build the three views that matter:** everything one attorney is carrying, who is active and has capacity, and — for whoever answers the main line — a fast lookup that finds a pro bono client's matter and says who to route them to.
6. **Add nothing for the attorneys to maintain** unless step 1 says they will. Placement and status should be updatable by North Star staff as a side effect of work they already do.
7. **Set a deletion schedule** for anything new before it holds its first record. Per [constraints](constraints.md), non-negotiable.

### The security half

8. **Draft a minimum standard** for network attorneys handling North Star client files. Realistic, short, and achievable by a solo practitioner: device encryption, no client files in personal cloud storage, a named person responsible, what to do if a device is lost, what to do if they receive a records demand. **Per [constraints](constraints.md), that last one matters — a network attorney served instead of North Star is a real path in and nobody has told them what to do.**
9. **Design how to ask.** Ninety volunteers, no leverage, relationships the organization needs. Probably part of training rather than a compliance exercise; probably an attestation rather than an audit. This is a design problem about people, and it is the hard part.
10. Leave a **runbook**: place a case with a network attorney, mark someone inactive, onboard a new network member including the standard, and respond to a lost-device report.

**Definition of done:** a supervising attorney can see one network attorney's full load in one place; the person answering the main line can find a pro bono client's matter in under a minute; "active this quarter" is a defined term with a number behind it; nothing new holds client data without a deletion schedule; and there is a written minimum standard that network attorneys have been asked to meet in a way most of them accepted.

## What the volunteer should bring

- **Configuration-first instincts.** The best outcome here is that most of this happens inside the existing platform. A volunteer eager to build something new is the wrong fit, and per [constraints](constraints.md) a new client-data store is a risk rather than a feature.
- **Integration experience** against a sector legal platform, and patience with a product not built for extension.
- **Genuine security thinking, calibrated to an adversarial threat model.** Not checklist security. The organization needs someone who can reason about compelled disclosure and device seizure, and who will not reflexively recommend more logging.
- **The people skills for the security half.** Persuading ninety volunteer lawyers to adopt a practice is not a technical problem and it is most of the value.
- Willingness to write documentation for non-technical operations staff.

Per [constraints](constraints.md): confidentiality agreement, background check, **and a conversation with the operations director about the threat model** before access. Develop against the synthetic caseload the organization provides. **No screenshots, nothing on personal devices, no client data into any AI service, no case or client scoring, no new logging without asking, and no writing about this work publicly.** If you receive any request for the organization's data, refer it and respond to nothing.

## Capacity gained

Supervision gets better, which in a pro bono model is the thing that protects clients — a supervising attorney who can see a network member's whole load can tell when someone is overcommitted before a deadline is missed. The main line stops failing pro bono clients. And the organization can finally answer how large its network actually is, which is the number every funder asks and nobody can currently produce.

From the security half: the organization's widest exposure gets a floor under it. Not closed — ninety independent practices will never be uniform — but a stated standard and a known procedure for a served or lost device is a large improvement over nothing.

## Data sensitivity

**Privileged, and adversarially targeted.** Both, which is the combination that makes this bundle different from every other in the collection.

The specific hazard to hold throughout: **a clean, structured mapping of clients to attorneys is a better version of the most dangerous artefact this organization holds.** Right now that mapping is fragmented across spreadsheets and people's memories, which is inconvenient and is also a form of protection. **Making it tidy makes it more valuable to anyone who obtains it.**

That is not a reason to abandon the project — the supervision benefit is real and protects clients. It is a reason to build it inside the existing platform under existing controls rather than as a new system, to set retention before the first record, and to think about who can see the whole picture at once. Per [constraints](constraints.md), the organization would rather have a slightly less convenient tool than a comprehensive one.

A volunteer whose instinct is that consolidating scattered data into one clean place is self-evidently an improvement should sit with that instinct for a while before acting on it here.
