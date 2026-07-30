---
type: volunteer-request
title: "Field intakes into the case system in a day, not two weeks"
description: "Structured capture and narrowly-scoped transcription assistance for tailgate intakes, with deterministic deadline flagging — and an explicit account of the AI features that were declined."
tags: ["technical-volunteers", "request", "draft", "synthetic", "ai-assisted", "intake"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: ai-assisted-intake-triage
---

# Volunteer project — Intake capture & triage assistance

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

An advocate takes eleven intakes at a pantry tailgate on a Tuesday morning. Spanish, mostly, two in Mixtec through a family member. She writes on a legal pad and records voice memos for the ones where writing while listening would break the conversation.

Those eleven intakes reach our case-management system somewhere between four days and two weeks later, depending on what else that week holds. In that window: nobody has run a conflicts check, nobody has looked at whether a wage claim is about to run out of time, and if the person was an H-2A worker who left the county, we may never reach them again.

Twice last year a wage claim came to us in time and was filed late because the intake sat in a notebook.

## What was declined, and why

**Read this section before the scope.** The obvious project here is not the one being requested, and the reasons are specific.

**Declined: a model that assesses whether an intake is a viable case.** The organization is oversubscribed and rations, so a merit score sounds like exactly the help it needs. It is the most harmful thing that could be built here. A score becomes the decision within a month — that is what scores do — and it would encode assumptions about which accounts sound credible. The accounts that sound least tidy come from people who are frightened, speaking through an interpreter, describing something that happened over eight months to an employer who is also their landlord. **Those are the clients who most need representation and the ones a scoring model would quietly move down the queue.** Rationing decisions here stay with people who can be asked to justify them. See [constraints](constraints.md).

**Declined: a client-facing intake chatbot.** Two independent problems. It would constitute the unauthorized practice of law the moment it said anything useful, and a correct answer from a machine is still advice. And separately — a person deciding whether it is safe to contact a legal-aid office about their employer, with their status in question, does not need a bot. That first contact is a carefully weighed decision and a human being should be on the other end of it.

**Declined: machine translation of clients' own accounts as the intake record.** A model can render Spanish to English well and Mixtec to English badly, and in both cases the output is not a record of what the person said. A mistranslated fact becomes a false statement in a filing and the client bears the cost. Interpretation for legal meaning is a professional skill; the organization pays for a line that provides it.

**Declined: anything that touches privileged case files.** Not a volunteer's to access, and not the organization's to grant. See [constraints](constraints.md).

## What is actually being asked for

Two pieces. **The first needs no AI and delivers most of the value** — worth saying plainly, since the request is framed as an AI project.

### Piece one — structured field capture and deterministic deadline flagging (no AI)

- **Offline-capable structured intake** on the advocate's phone or tablet: who (as much as they'll give), what happened, when it happened, where, employer, and whether they expect to be in the county in six months. Works with no signal — parts of the service area have none, the same constraint [Valle Verde](../../synthetic-valle-verde-food-network/technology/inventory.md) documents.
- **Conflicts-check-first workflow.** Per [constraints](constraints.md), nothing may create a matter or contact a person before conflicts screening. The capture tool produces a *pending inquiry*, clearly not a matter, that queues for screening.
- **Deadline flagging by rule, not by model.** Given a date of harm and a claim type, the applicable limitation period is arithmetic. A rules table maintained by an attorney, flagging anything approaching a threshold, **failing loudly** and treating uncertainty as "not captured." Per [constraints](constraints.md), this is malpractice-risk territory and must never fail quietly.
- **Sync into the case-management platform** so an intake taken Tuesday morning is screenable Tuesday evening.

That is the project's core value, and there is no machine learning in it.

### Piece two — narrowly scoped transcription assistance (AI, tightly bounded)

The advocate's **own voice memos** — her professional summary of an intake, spoken in her own words after the conversation — transcribed and structured into a draft the tool pre-fills for her review.

The boundaries, all of which come from [constraints](constraints.md):

- **The advocate's summary only.** Never a recording of the client speaking. Different thing, different risks, out of scope.
- **Draft only, always reviewed.** The transcription pre-fills fields; the advocate corrects and confirms before anything is submitted. Nothing reaches the case system without her approval.
- **No inference beyond transcription and field-mapping.** No summarizing what it means, no suggesting a claim type, no flagging anything as promising. Speech to text, text to fields, stop.
- **Processing arrangement with no training on inputs, no retention beyond processing, documented handling, signed agreement.** If that isn't available on acceptable terms, piece two is dropped and piece one still works. It should be built so that dropping it is easy.
- **Spanish and English only.** Mixtec and Triqui transcription is not reliable and the organization will not pretend otherwise — those intakes stay with the interpretation line and human notes.

## Confirm first (dependencies)

1. **Is the case-management platform's deadline module configured**, or are deadlines in a parallel calendar? Determines whether piece one integrates or rebuilds. See [inventory](../technology/inventory.md).
2. **Does the platform have an API or import path** that can accept a pending inquiry without creating a matter? If not, the conflicts-first requirement gets harder and needs an attorney in the design conversation.
3. **The limitation-period rules table** — an attorney has to author it. This is the dependency most likely to stall the project, and it should start on day one.
4. **Where the voice memos currently live.** They are probably on a staff member's phone, probably retained indefinitely, possibly containing privileged content in an uncontrolled place. This is a live exposure independent of the project and worth flagging even if nothing else proceeds.
5. **Whether an acceptable transcription arrangement exists** on the organization's terms. Establish before building piece two, not after.

## What a volunteer would do (roughly 8–12 weeks)

1. Sit through **one tailgate intake session** — with client consent, or observing from outside earshot. The pace, the interruptions, and why she uses voice memos are not conveyable secondhand.
2. Design the **pending-inquiry** record with an attorney, keeping the conflicts boundary intact.
3. Build **offline-first structured capture**, per the same constraints as the Valle Verde route work: local write first, visibly safe, survives a dead battery, learnable in five minutes.
4. Build the **deadline rules engine** from the attorney-authored table. Loud failure, no silent gaps, uncertainty treated as not-captured.
5. Integrate into the case-management platform for screening.
6. **Then, and only if the arrangement is acceptable**, add transcription of advocate voice memos as a pre-fill.
7. Write the **retention story** — what the tool keeps, where, for how long, and how it's deleted. For an organization holding privileged material with no retention schedule, this may be the most durable thing the project produces.
8. Leave a **runbook**: add a claim type, update the limitation table, recover unsynced intakes, respond to a deadline flag.

**Definition of done:** an intake taken at a Tuesday tailgate is conflicts-screened Tuesday evening, an approaching limitation period is flagged before it matters, and no advocate loses an afternoon's intakes to a dead zone. Piece two, if it exists, saves her an hour a session and changes nothing about who decides what.

## What the volunteer should bring

- **Offline-first mobile** experience. Same hard requirement as elsewhere in this county.
- **Integration** work against a sector case-management platform, and patience with a product not designed for extension.
- **Rules-engine discipline** — this is deadline logic where being right matters more than being clever.
- If piece two proceeds: **applied-AI judgment specifically about bounding a model**, plus enough contract literacy to read a data-processing agreement. The skill needed here is knowing what to refuse.
- Willingness to write **plain-language documentation**, per [constraints](constraints.md).
- **Spanish** for the intake observation; not required for the build.

Per [constraints](constraints.md): **signed confidentiality agreement and background check before anything**, **no access to privileged case files**, **develop against synthetic data the organization provides**, and **no merit scoring, no chatbot, no client-facing AI**. A volunteer who arrives wanting to build a prioritization model will be turned down, and the organization would rather say so here than after a month of work.

## Capacity gained

The gap between an intake happening and the organization knowing about it closes from two weeks to a day. Conflicts screening happens while the person is still reachable. A limitation period gets noticed while there is time to file. An advocate stops spending Sunday evenings transcribing her own notebook.

What does **not** change: how many cases the organization can take, and who gets one. That is a capacity and funding question, and the honest thing about this project is that it does not touch it. A project that claimed to would be the merit-scoring model, and that is the thing being declined.

## Data sensitivity

**As high as it gets in this collection, and structurally different from the rest.** The material is not merely sensitive, it is **privileged** — a category with legal weight, professional-responsibility consequences, and no volunteer access under any agreement.

The project is deliberately designed to sit at the boundary: **pending inquiries, not matters.** Pre-screening information, from a person who is not yet a client, captured with their knowledge, moving into a system where a licensed attorney takes over. That framing is what makes any of this doable by a volunteer, and it should not be eroded for convenience — the first time a pending inquiry becomes a de-facto matter file, the whole arrangement is void.

Two exposures worth naming even though they sit outside the project: the **voice memos on a staff phone**, and the **never-reviewed Microsoft 365 tenancy holding privileged client material** (see [inventory](../technology/inventory.md)). Either may matter more than what is being requested. A good volunteer will say so.
