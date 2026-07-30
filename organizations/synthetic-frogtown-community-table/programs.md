---
type: programs
title: synthetic-Frogtown Community Table — Programs & services
description: What the organization runs, and the one room doing more than the program list admits.
tags: [programs, services, synthetic]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: https://synthetic-frogtown-table.example.org
    title: The organization's own website and published materials
    author: human:org-staff
    last_modified: 2026-03-02
x-civic:
  profile: civic/0.6
  subject: [SS030601, SS030600, SS090300]
  provides: food-shelf
---

# Programs & services

**⚠ Synthetic — fabricated data.** The list below is derived from published materials;[^org-site] a real organization would confirm and replace it with its own description.

Four and a half staff, one building, sixty volunteers.

- **The food shelf** — open four days a week, shop-style rather than pre-boxed, organized so it can be navigated by someone who reads no English. Stocked for what the surrounding households actually cook: bulk rice, fresh herbs and greens, halal meat, whole fish, dried beans in the right varieties. This is the organization.
- **Community kitchen** — the shelf's back room, used for cooking sessions, shared preparation of bulk purchases, and increasingly as neutral community meeting space that has nothing to do with food.
- **Garden plots** — a small number of raised beds on an adjacent lot, allocated to households, growing crops the shelf cannot source reliably.
- **Elder delivery** — a volunteer route to homebound elders, weekly, which is also the organization's main way of knowing how those households are doing.
- **Immigration clinic hours** — a partner legal practice holds monthly clinic hours in the back room. Frogtown Table provides the room and the trust; the partner provides the lawyers.

The shelf operation is what the required `subject` codes describe: `SS030601` (Food banks), `SS030600` (Food aid), and `SS090300` (Immigrant and refugee services).

## The back room is doing more than the program list admits

Look at what happens in one room: cooking sessions, bulk preparation, community meetings, and a monthly legal clinic. **The organization has accidentally built the neighbourhood's most trusted meeting space**, and its program list describes it as a kitchen.

That matters because trust is the asset here. The reason an immigration legal clinic works in this back room and would not work in an office downtown is that people already come to this building for something else.

## Which of these should become its own file first

**The back room, as a thing in itself** — call it community space. It is currently invisible, folded into "community kitchen," and it is hosting a partner organization's legal practice. It has its own scheduling, its own trust requirements, and its own confidentiality considerations on clinic days that a kitchen does not have.

**Elder delivery** is second. It is one line, and it is a weekly welfare check on the organization's most isolated households, performed by volunteers with no training in what to do if something is wrong. That is a program with a risk profile, described as a delivery route.

This is what growth looks like in an OKF bundle: a bullet becomes a file, the file gets its own frontmatter and its own `subject` codes, and the directory gains an `index.md`. Nothing needs restructuring to allow it.

## A note on how small this is

Everything above is run by **4.5 FTE**. When a program officer asks this organization to add outcome measurement, or a funder asks for a new report, the marginal hour comes out of the shelf being open. Worth holding while reading the [volunteer project](technical-volunteers/index.md), which was deliberately scoped small for exactly this reason.

[^org-site]: The organization's own website and published materials
