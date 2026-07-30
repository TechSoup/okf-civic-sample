---
type: volunteer-request
title: "One participant record that is actually authoritative"
description: "Consolidate three overlapping participant systems into one, starting by getting conviction histories off a single desktop machine with no confirmed backup."
tags: ["technical-volunteers", "request", "draft", "synthetic", "data-migration"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: data-migration-crm-consolidation
---

# Volunteer project — Participant record consolidation

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

We can tell you how many people enrolled last year three different ways, because three funders define it differently and we keep the answer in three places. What we cannot easily tell you is whether the man who finished welding in 2022 is still working as a welder, even though that is the only number we actually care about — and it's the one that lives in a spreadsheet one person maintains from phone calls.

Meanwhile the intake system we've run since 2009 sits on one desktop machine in the back office. Everything sensitive we hold is in it.

## Something more urgent than what we asked for

The organization's stated need is consolidation. Scoping against this bundle surfaces a bigger problem, and the honest thing is to name it rather than bury it in a later phase.

**Thousands of conviction histories sit in a seventeen-year-old single-machine database that is outside the organization's endpoint-security coverage and whose backup status nobody could confirm.** See [inventory](../technology/inventory.md). If that machine's drive fails, the organization loses its participant history. If it's stolen or compromised, the organization has disclosed the criminal records of people who trusted it with them — a population for whom that disclosure does specific, lasting harm.

So this project is proposed in two phases, and **Phase 0 should happen whether or not the rest is ever funded**:

**Phase 0 — stop the bleeding (days, not weeks).** Establish whether a backup exists. If it doesn't, create one: encrypted, off that machine, tested by actually restoring it. Bring the machine inside endpoint coverage or take it off the network. Document who has access. **Nothing about consolidation, nothing rearranged, nothing improved** — just make it so the worst outcome stops being available. A competent volunteer can do this in under a week, and it is worth more than the rest of the project combined.

**Phase 1 — consolidation.** Everything below.

## Confirm first (dependencies)

1. **Is the Salesforce org recoverable, or should it be started over?** Ten donated seats, an implementation abandoned in 2023, some 2022–23 enrollments inside. Unanswerable from outside and it determines the whole shape of the project. Note that the website's live **Web-to-Lead form still posts into it** — real inquiries from real people are landing in a queue nobody watches. That's a same-day fix regardless of what happens next.
2. **What the state portal and the three funders literally require**, in writing, with their definitions of enrolled / completed / placed. The organization holds these as staff knowledge. Getting them written down is half the value of this project and can begin before any technical work.
3. **What is actually in the legacy database** — schema, record counts, which fields are populated, which are abandoned. Expect surprises; seventeen years of a system nobody retired means dead fields, workaround fields, and at least one field being used for something other than its name.
4. **Whether the three-year follow-up spreadsheet can be reconstructed** or only carried forward. The organization's signature claim depends on it, and if its history can't be validated, the honest move is to say so and start measuring properly from now.
5. **Reporting calendar.** Per [constraints](constraints.md), cutover happens between reporting periods. Establish the windows before planning anything.

## What a volunteer would do (Phase 1, roughly 10–16 weeks)

1. **Define the participant record** — one agreed set of fields, with the funders' competing definitions mapped onto it explicitly rather than resolved away. Three definitions of "placed" is a fact about the funding environment, not a data-quality problem to be cleaned up.
2. **Choose the destination.** Either revive Salesforce NPSP or move to something the organization can maintain. Per [constraints](constraints.md), the deciding criterion is **who inherits it** — a second system only one person understands is a worse outcome than the current mess.
3. **Migrate from the legacy database**, working from a copy. Per [constraints](constraints.md): **conviction-history fields are pseudonymized or masked in the working environment**, and the reason is written down. If the migration can be done without a volunteer ever seeing a real conviction record, do it that way.
4. **Fold the spreadsheets in** — outcomes, retention follow-up, wraparound disbursements. Keep the originals untouched as the reference copy until the new system has produced a full reporting cycle correctly.
5. **Build the state-portal export** so hand-keying stops, or is at least reduced to review-and-submit.
6. **Build the follow-up workflow** so three-year retention becomes a scheduled task with a record, instead of one person's diligence.
7. **Run parallel for one full reporting cycle.** Both systems live, outputs compared, discrepancies explained before anything is retired. Then cut over, between periods.
8. Leave a **runbook**: add a cohort, run each funder report, submit to the state, onboard a staff member, and restore from backup.

**Definition of done:** one participant record, three funder reports generated from it without hand-reconciliation, the state export working, conviction histories in a backed-up access-controlled system, the legacy machine retired, and the retention question answerable from a query.

## What the volunteer should bring

- Real **data-migration** experience, especially the unglamorous part: profiling a legacy schema, reconciling records that don't match, deciding what to do with the ones that never will.
- **Nonprofit CRM** familiarity — Salesforce NPSP specifically would help, including honest judgment about when reviving an abandoned org is more expensive than starting over.
- **Sensitive-data handling** instincts. Masking, least privilege, encrypted backups, and the discipline not to look at things because they're there.
- Patience for **funder-definition archaeology**, which is most of the first month.
- Willingness to write **documentation a non-specialist can follow** — per [constraints](constraints.md), a deliverable.

Per [constraints](constraints.md), and worth restating because it is unusual: this organization **does not require a blanket background check**, deliberately and for reasons it has thought through — it would be incoherent for an organization that spends its week arguing against exactly that screen. What it requires instead is a **signed confidentiality agreement**, **task-scoped least-privilege access**, and **masked conviction-history fields**. Also firm: **no risk scores, no flags, no predictive models on participant data**, and no AI applied to it. A volunteer who wants to add a completion-likelihood score will be turned down.

## Capacity gained

The organization can answer its own central question. Funder reporting stops being a reconciliation exercise. The state portal stops being one person's undocumented skill. And the records of several thousand people who trusted this organization with their criminal history stop sitting on one machine in a back office.

## Data sensitivity

**The highest in this collection.** Conviction histories, income verification, benefits status, employer-required drug screens, and in some cases immigration documentation — for a population where disclosure causes specific, durable harm.

Every control in [constraints](constraints.md) applies, and the strongest one is a scoping decision rather than a permission setting: **design the work so a volunteer never needs to see a real conviction record.** Masked fields in the working environment, real data moved by a script whose output the volunteer verifies structurally rather than by reading. That is achievable for most of this project, and where it isn't, the organization wants the exception written down.

Phase 0 exists because the current arrangement fails this standard already, before any volunteer touches it.
