---
type: volunteer-request
title: "Three funder reports from one participant record, and a second person who can run them"
description: "Replace per-cohort spreadsheets with one consistent participant record that produces all three funders' reports — carrying their conflicting definitions rather than resolving them."
tags: ["technical-volunteers", "request", "draft", "synthetic", "reporting"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: reporting-dashboard
---

# Volunteer project — Cohort outcome reporting

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

Every cohort gets its own spreadsheet, and every spreadsheet is a little different from the last one because whoever set it up copied whichever version they had.

Four times a year our program director spends about four days assembling three reports from those spreadsheets, because our federal subaward, our state allocation, and our transition grant each define a placement differently, and then she keys the results into the state portal by hand.

She is also the only person who can do any of this. If she took a month off we could not report, and that is a bigger risk to this organization than any of the technology on our list.

## What this project is not

**It is not a database project, and it is not a CRM project.** Per [constraints](constraints.md), and worth stating up front because the instinct is strong:

Spreadsheets are not the problem. A twelve-person organization tracking 190 participants a year in spreadsheets is being sensible. The problems are that the spreadsheets are **inconsistent between cohorts**, that three funder definitions are **reconciled in one person's head**, and that the reporting knowledge **exists in one person**.

None of those requires a platform. Two of them are solved by a consistent structure and a written definition layer, and the third is solved by documentation and a second trained person. A CRM would solve none of them and add an administration burden this organization has correctly refused. See what happened at [Motor City Trades](../../synthetic-motor-city-trades-institute/technology/inventory.md), which is three and a half times the size and got halfway through exactly that implementation.

## Confirm first (dependencies)

1. **Does the state workforce portal have an export or an import?** Nobody has asked. If it accepts a structured upload, hand-keying largely disappears and the project's value roughly doubles. If it's one-way and manual, the project still works and produces the report for a human to key.
2. **The three funder definitions, in writing, from the source documents.** Not from memory. This is the single most valuable artefact this project can produce and it can begin on day one with no technology at all. Expect to find that at least one definition is ambiguous and that the organization has been making a defensible interpretation nobody has recorded.
3. **What a monitoring visit asks.** Per [constraints](constraints.md), whatever gets built has to be explainable by a staff member to an auditor. Find out what that conversation actually looks like before choosing an approach.
4. **The reporting calendar**, so cutover happens between quarters.
5. **Which fields are actually used** across the last eight cohort spreadsheets, and which are vestigial. Expect a third of the columns to be dead.

## What a volunteer would do (roughly 5–8 weeks, in a between-cohort window)

1. **Write the definition layer first.** One document: every field, what it means, which funder wants it, and how each funder defines placement, completion, and credential attainment. **Per [constraints](constraints.md), carry all three definitions — do not resolve them into one.** This document is the deliverable that matters most and it is prose, not code.
2. **Design one cohort template** that serves all three funders, with the conflicting definitions as separate derived columns rather than as a single "placed" flag. Boring, explicit, and legible to an auditor.
3. **Consolidate the historical cohorts** into that structure, and **document what couldn't be mapped** rather than quietly dropping it. Some old cohorts will be missing fields that later became required; a known gap is reportable, an invisible one is a finding at a monitoring visit.
4. **Build the three reports as saved, repeatable outputs** — each producing exactly what one funder asks for, traceable back to the definition document. Spreadsheet-native or a light managed tool, per [constraints](constraints.md): configuration over code.
5. **If the portal accepts an upload**, build it. If not, produce the report in the exact order and format the portal's screens ask for, which turns hand-keying from interpretation into transcription.
6. **Train a second person.** Explicitly in scope, and arguably the point of the whole project. The program director should not be the only person who can produce a federal report, and a runbook nobody has walked through is not a solution.
7. Leave a **runbook** the second person has actually used to produce one real report end to end, plus the definition document, plus a short note on what to do when a funder changes a definition — which they will.

**Definition of done:** a new cohort starts in the standard template; each of the three funder reports is produced from it without hand-reconciliation; the definition document explains every number in all three; **and somebody other than the program director has produced a real quarterly report start to finish.**

## What the volunteer should bring

- **Patience for definition archaeology.** Most of the first two weeks is reading grant agreements and asking "but what do they mean by placed." If that sounds tedious rather than interesting, this is the wrong project.
- **Spreadsheet and light data-tooling craft** — real skill in the boring direction. Well-structured sheets, validated inputs, derived columns, repeatable outputs. No platform needed.
- **Documentation writing for a non-technical reader**, including one who is an auditor.
- **The discipline not to build the bigger thing.** Per [constraints](constraints.md) this is the crux, and a volunteer who spends week three proposing a proper database has stopped listening.
- Comfort **training a staff member**, patiently, as a deliverable rather than an afterthought.

Per [constraints](constraints.md): signed confidentiality agreement, least-privilege access, **work from the synthetic cohort the organization provides**, and three hard nos — **conviction history must never become a filter, flag, or sort order**; **no scoring, ranking, or predicting participants**; and **do not resolve the three funder definitions into one number**.

## Capacity gained

Four days a quarter of the program director's time, which in a twelve-person organization is real. More importantly: **the organization stops having a single point of failure on a mandatory federal report.** And a monitoring visit gets a document instead of an explanation.

Second-order, if the portal turns out to accept an upload: a further day or two a quarter, and one fewer place for a transcription error to enter a compliance report.

What it does not do: tell the organization whether its graduates are still employed at twelve months. It genuinely does not track that, says so, and this project does not change it — that would need follow-up staffing, not a report. See [eligibility](../verification.md) for why the organization's honesty about that costs it something.

## Data sensitivity

**Moderate, with two sharp edges.**

Most of the data is ordinary program information — enrollment, attendance, credentials, placement. Not harmless, but not high-stakes, and workable from a synthetic cohort for nearly all of the build.

The two edges, both flagged in [constraints](constraints.md) and both worth restating: **conviction history**, which exists in these records because the organization has to counsel people honestly about which licensed tracks are closed to them, and which must never become a filter or a sort order; and **recovery status and treatment schedules**, present because the organization coordinates training around appointments. In a county of 21,000, either one leaking is not an abstract privacy harm — it is something a participant's neighbour finds out.

A volunteer should design so that both categories are **visible to the people who need them for counselling and invisible to the reporting layer entirely.** No funder asks for them. There is no reason for them to appear in any output this project produces.
