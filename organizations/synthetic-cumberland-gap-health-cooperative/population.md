---
type: population
title: "synthetic-Cumberland Gap Health Cooperative — Who it serves"
description: "The Letcher County patients the organization serves. Fabricated."
tags: ["population", "beneficiaries", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-cumberland-gap-health.example.org"
    title: "The organization's own website and published materials"
    author: human:org-staff
    last_modified: 2026-03-02
x-civic:
  profile: civic/0.6
  population: ["PG090000", "PG030000", "PA020300"]
---

# Who Cumberland Gap Health serves

**⚠ Synthetic — fabricated data.**

Cumberland Gap Health serves **Letcher County residents** — about **3,100 distinct patients** a year, which is a large share of a county of roughly 21,000 people. Patients skew **older than the county** and considerably older than any other population in this collection: median patient age in the mid-fifties, with a substantial cohort over seventy. Payer mix is heavily public — Medicare, Medicaid, and black lung benefits — with a meaningful uninsured share. *(**derived**, simulated, from the practice management system; not externally audited, unlike [Sierra Foothills'](../synthetic-sierra-foothills-community-health/population.md) federally-reported counts.)*

## Two access barriers, and one of them is not the organization's

**Transport.** Roughly 40% of patients cannot get to the clinic on their own. The county has effectively no public transit, distances are short in miles and long in minutes, and a number of patients are on winding roads that a sedan does badly in winter. This is why the organization does home visits — not as an enhancement, as the only way to see those people.

**Broadband — and this is the one that matters for anything technological.** Roughly the same share of patients **cannot use a video visit**, because the connection where they live will not carry one. Some have no wired service available at any price. Some have satellite service that a video call defeats. Some have a phone with a data cap that a twenty-minute consultation would eat.

Note the direction of the problem. **The clinic's own connectivity is mediocre but workable. Its patients' connectivity is the binding constraint**, and the organization cannot fix it, buy around it, or train its way out of it. See [inventory](technology/inventory.md) for what happened when it tried.

## Sub-populations that shape the practice

**Former miners with occupational lung disease** — a distinctive and consequential group. Their care involves pulmonary management, and their financial lives involve federal black lung benefits, which means the organization does **benefits documentation and advocacy** as a routine part of clinical work. Medical records here are also legal evidence in a benefits claim, which changes how they must be kept.

**Older patients with multiple chronic conditions** — the core caseload. Diabetes, hypertension, COPD, often together, often with medication regimes that a limited income makes difficult to sustain.

**Patients in substance-use recovery** — a program the organization runs because nobody else in the county does. The most sensitive information it holds, in a county small enough that being seen in the parking lot is a disclosure. That fact has real design consequences: anything the organization builds that makes a patient's reason for visiting more visible, including a well-meant appointment reminder that names the program, causes harm.

**Working-age adults in training** — a small but growing group, referred through the health-careers pathway with [Black Mountain Workforce Partnership](../synthetic-black-mountain-workforce-partnership/README.md). Notable because they are the organization's future staff as well as its patients.

*Provenance: **derived**[^org-site] (simulated) throughout, from the practice management system. The organization should confirm the counts; nothing here is externally audited.*

Community context for Letcher County — population decline, the post-coal economy, broadband availability, distance to the nearest hospital, occupational disease prevalence — belongs to the place, not here: see [US-KY-letcher](../../_shared/situations/US-KY-letcher.md). This file says *who*; the situation node says *the conditions around them*. Two organizations in this collection share that node, and they are each other's most important partner.

[^org-site]: The organization's own website and published materials
