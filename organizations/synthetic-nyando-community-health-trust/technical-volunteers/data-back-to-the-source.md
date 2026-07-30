---
type: volunteer-request
title: "Our data goes up every month and never comes back"
description: "Get the organization's own submitted health data back into a form supervisors and promoters can use locally — without adding a shilling to what promoters spend on mobile data."
tags: ["technical-volunteers", "request", "draft", "synthetic", "offline-first", "infrastructure"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: hardware-network-infrastructure
---

# Volunteer project — Getting our own data back

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

Every month, 142 promoters submit household data and we aggregate it and send it up. Twelve years of this.

When our programme manager wants to know whether antenatal follow-up in one catchment has slipped, she cannot easily find out. When a promoter asks how her households compare to last year — a reasonable question from someone who collected the data — we do not have an answer for her. The numbers went somewhere and we are not the ones who can query them.

We are not complaining about the national system. We are required to report and we believe in reporting. But **the data flows up and nothing flows back**, and the people who collected it are the last to see it.

## What this project is not

**Not a new data system, and not a rebuild of our field platform.** Per [constraints](constraints.md), and worth restating because it is the thing that keeps getting offered.

Our offline capture works. 9,600 registered households, twelve years of continuous monthly submission, monthly supervision that catches errors early. See [inventory](../technology/inventory.md). **We are asking for a return path, not a replacement.**

If you have read an automated assessment of us — which scores us the lowest of the fifteen organizations in this collection — please read [capability](../technology/capability.md) before scoping anything.

## The hard test, before the scope

**Per [constraints](constraints.md): does this increase or decrease what a promoter spends on mobile data?**

Our promoters buy the data bundles that submit our reporting, out of stipends. Roughly thirty use their own handsets. **A project that gives them a nice dashboard they pay to load has made things worse**, and we would rather have nothing.

So the target is explicit: **the return path must cost a promoter nothing, or less than now.** That is a design constraint on the same level as correctness.

## Confirm first (dependencies)

1. **Can we query our own submitted data at all?** Read access, an API, a scheduled export, anything. **The entire project depends on this and nobody has established it.** It is a conversation with the county health records office, and it may need to happen before a volunteer is even useful.
2. **If not, can we reconstruct from our own side?** Our mobile platform holds what the promoters captured before aggregation. If the national system is one-way, the return path is built from our own data rather than from theirs — different project, still valuable, and arguably better since it is unambiguously ours.
3. **What our supervisors actually want to see** at a monthly meeting. Ask three of them. Expect the answer to be small and specific — this catchment, these three indicators, this year against last.
4. **What promoters want to know about their own households**, asked directly through our programme manager. We suspect it differs from what supervisors want.
5. **Measure what promoters currently spend on data and airtime.** Per [the folder note](index.md), this is a week of work needing no technology and it may be the most valuable thing produced here. Do it early regardless of the rest.
6. **Kenya's Data Protection Act obligations** as they bear on household data moving into any new view. We have not assessed this. Flag rather than assume.

## What a volunteer would do (roughly 6–10 weeks, mostly asynchronous)

1. **Establish the return path** — dependency 1 or 2. Whichever it is, document it so the next person does not have to rediscover it.
2. **Build the supervisor view first**, because it is where the leverage is. Per [constraints](constraints.md), supervision is what makes our data true, and a supervisor walking into a monthly meeting already knowing which catchments moved is a better meeting. Small, printable, and usable on an office machine or a phone at a link facility.
3. **Build the promoter view to be free at the point of use.** This is the design problem. Options worth exploring, cheapest first:
   - **Printed sheets** handed out at the monthly supervision meeting. Costs a promoter nothing, works on no battery, and is the answer we would probably choose ourselves.
   - **SMS summaries** — a few lines a month, works on any handset including the thirty that are not ours.
   - **Data bundled into an existing sync** so no additional connection is needed.
   - **A local view on the phone**, populated during a sync that was happening anyway.
   
   Note that the lowest-technology option is a serious candidate and may win. Per [constraints](constraints.md), unglamorous is fine.
4. **Do not create new supervision work.** If the views need chasing, correcting, or explaining, that lands on 23 staff who are already stretched. Say so if your design does that.
5. **No individual promoter rankings.** Per [constraints](constraints.md) this is a firm no — a leaderboard across 142 women would punish whoever has the flooded catchment and the long walks, and it would break the trust the model runs on. Catchment-level trends for the promoter's own use, not comparison.
6. **Reduce the English where you can.** Per [constraints](constraints.md), several promoters are recording into English-labelled forms with limited written English, and that is a live source of error. Dholuo labels and icons in anything promoter-facing are a data-quality improvement. We write the text.
7. Leave a **runbook** our programme manager can follow, and confirm who maintains anything ongoing — per [constraints](constraints.md), if it needs a developer it will fail.

**Definition of done:** a supervisor arrives at a monthly meeting knowing which catchments moved; a promoter can see how her own households are doing without spending anything to find out; promoter data costs are measured and written down; and no new work has been added to supervision.

## What the volunteer should bring

- **Low-bandwidth and zero-bandwidth thinking.** The best answer here might be paper. A volunteer who cannot take that seriously is the wrong fit.
- **Health information systems familiarity** — ideally the national-reporting-system family and the open-source mobile health data tooling around it. Knowing how these systems are typically configured saves weeks.
- **Integration patience.** Getting read access to your own data out of a government system is a bureaucratic problem more than a technical one, and progress will be slow and non-linear.
- **Respect for what exists.** Per [constraints](constraints.md), our platform choices were made by people who had to make them work in this county. Ask why before proposing a change.
- **Comfort working asynchronously across time zones**, with a contact who is often in the field, and with our limited bandwidth for long calls.
- Willingness to write documentation for non-developers.

Per [constraints](constraints.md): confidentiality agreement first, **develop against synthetic data**, no household data into any AI service, no screenshots, nothing on personal devices, **no individual promoter performance scoring**, no increase in promoter data costs, and no new burden on supervision.

## Capacity gained

Supervision gets sharper, which is the highest-leverage improvement available in this organization — it is already the mechanism that makes the data good, and giving supervisors the prior month's trends before the meeting rather than after makes it better at no additional cost.

And the promoters who collect the data get to see it. That sounds soft and it is not: **142 people are producing information about their own neighbours' health and cannot currently learn anything from it.** Closing that loop is a matter of respect, and — from what our supervisors report anecdotally — it is also likely to improve data quality, because a person who can see their own numbers cares more about whether they are right.

What this does not do: change the stipend model, resolve who should pay community health workers, or fix that promoters subsidize our reporting. It can, however, **produce the number** that makes that argument to a funder, and that is worth asking for even though we did not put it at the top.

## Data sensitivity

**Household health data in a community where everyone knows everyone.** Names, locations, pregnancies, illnesses, child immunization status. The disclosure risk is not abstract — it is a neighbour learning something about a neighbour.

Two specifics for this project:

**Aggregation is not automatically safe at this scale.** A promoter's catchment is 65–70 households. An indicator reported at catchment level with a small numerator can identify a specific household — the same small-cell problem [the Louisiana bundle](../../synthetic-gulf-corridor-justice-project/population.md) describes. Any view needs suppression built in, not left to the person reading it.

**A promoter should see her own catchment and not her neighbour's.** That is both a privacy boundary and, per [constraints](constraints.md), the reason no cross-promoter comparison exists.

Most of the build can happen on the synthetic catchment the organization provides. **The printed-sheet option, if it wins, involves no new digital storage of household data at all** — which is worth noting, because the cheapest option here is also the one with the smallest data-protection surface. That is not a coincidence and it is worth looking for more often.
