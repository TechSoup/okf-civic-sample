---
type: volunteer-constraints
title: "synthetic-Black Mountain Workforce Partnership — Volunteer constraints & preferences"
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

*Pre-seeded with defaults for a small workforce organization carrying federal subaward obligations, then revised where the defaults didn't fit a twelve-person shop in a county of 21,000.*

## Build smaller than you want to

This is the constraint we most need volunteers to accept, and the one they most often argue with.

We have twelve staff, no IT person, no developer, and no realistic prospect of either. **Anything that needs code maintained will decay, and then we will be worse off than we are now** — we will have lost the spreadsheet workflow we understood and gained a system nobody can fix.

We know what happened to organizations our size that accepted a donated enterprise CRM and got halfway through an implementation. We are not doing that. If your proposal involves a platform whose administration is a job, the answer is no, however good the platform is.

**Configuration over code. Managed services over anything we host. Boring over clever.** If the choice is between an elegant solution one person understands and a plain one four of us can maintain, we want the plain one.

## Our reporting cannot break

Two-thirds of our money is public, across three funders, and **a missed or wrong report has financial consequences we cannot absorb.**

- **The state portal is the system of record and we do not control it.** Whatever you build feeds it; it does not become the authority.
- **Do not resolve our funders' conflicting definitions.** Three funders define a placement three different ways. That is a fact about our funding environment, not a data-quality problem, and a system that picks one and reports it everywhere will produce a wrong number for two funders. Carry all three.
- **Change nothing mid-reporting-period.** Cut over between quarters, with our program director in the planning.
- **Assume we will be monitored.** A site visit asks how a number was produced. If the answer requires understanding a script, that is a problem. Anything you build must be explainable by a staff member to an auditor.

## Participant data

- **Signed confidentiality agreement** before any access.
- **Least-privilege, task-scoped** — same as we'd give a new employee.
- **Work from de-identified or synthetic data.** We can produce a realistic fake cohort. Ask.
- **Conviction history is the tightest tier.** Some of our participants have records, and some of our healthcare tracks have licensing screens they cannot pass. Those fields exist because we have to counsel people honestly about which tracks are open to them. **They must never become a filter, a flag, or a sort order in anything you build.**
- **No scoring, ranking, or predicting participants.** Not completion likelihood, not employability, not risk. Our participants have been sorted by algorithms before and it did not go well for them. If a funder asks us for this, we will have that argument with the funder.
- **Recovery status and treatment schedules** are in some of our records because we coordinate around appointments. Radioactive. Leave them where they are.

## Working with our people

- **The program director is the project's main contact and the bottleneck.** She is the only person who can produce our federal report, which is exactly the problem this project should fix, and she has maybe four hours a week. Come prepared.
- **Instructors are teaching.** The workable windows are the two-to-three-week gaps between cohorts. Ask us when those are before proposing a schedule.
- **Remote is fine for most of it.** Note that our building has a genuinely good connection and much of our county does not — do not design assuming our participants have what we have.
- **Please talk to a participant or two** before you build the thing they will be recorded in, if they are willing. It changes what you think matters.

## About the laptops and the workstations

If you are looking for something useful beyond the project we asked for: our **lending library has no asset tracking worth the name and no wipe policy between borrowers**, and job applications contain a great deal about a person. We know. A volunteer who sorted that out in a week would be doing us a real favour, and it is a different, smaller ask than the reporting project.

We would also rather you did not write anything down that draws a bright line around graduates keeping a laptop after they finish. It is not in any grant agreement and it is one of the most useful things we do.

## What we would say no to

- An enterprise CRM implementation. See above.
- Any model that scores or ranks participants.
- A system that resolves our three funder definitions into one number.
- Anything that would make our federal report harder to explain to a monitor than it is now.
