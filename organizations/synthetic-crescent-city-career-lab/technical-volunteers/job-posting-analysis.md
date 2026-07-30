---
type: volunteer-request
title: "What are regional employers actually asking for?"
description: "Gather and analyze regional job postings so curriculum decisions rest on evidence instead of anecdote — with the postings themselves always traceable behind any finding."
tags: ["technical-volunteers", "request", "draft", "synthetic", "ai-assisted", "labor-market"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: ai-assisted-intake-triage
---

# Volunteer project — Regional job posting analysis

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

We teach a fourteen-week IT support course. The question we cannot answer well is whether it still matches what employers around here are hiring for.

What we have instead: an instructor who reads job postings when he has time, three employer partners who tell us what they think, and a certification body's curriculum that updates on its own schedule for its own reasons. All useful. None of it is a picture of the regional market.

Last year we found out from a graduate — not from any of our sources — that two large local employers had started asking for something we do not teach. He learned it himself and got the job. We were glad and we should not have needed him to tell us.

## What makes this project unusual in a good way

**It touches no personal data.** It analyzes public job postings, which are employers' own marketing material. No participant information, no client records, no PHI, nothing privileged.

That is worth stating because it is genuinely rare among AI proposals in a nonprofit context, and it means this project can start quickly, be developed openly, and be worked on by a volunteer without an extended onboarding. Contrast [the Law Center's](../../synthetic-central-valley-farmworker-law-center/technical-volunteers/intake-triage-assist.md) intake project or [the clinic's](../../synthetic-sierra-foothills-community-health/technical-volunteers/ehr-consolidation.md) record consolidation, where most of the design effort goes into keeping a volunteer away from the data.

**The risk here is different, not absent.** Per [constraints](constraints.md): the danger is that a model's reading of the labor market starts deciding what people are trained for. Postings are noisy and aspirational, job descriptions get copied from the last one, and a training programme that chases a keyword produces graduates nobody wanted. The design has to keep a human judgement in the middle, deliberately.

## Confirm first (dependencies)

1. **Which sources are appropriate and permitted.** Some job boards offer APIs; some prohibit collection in their terms. Per [constraints](constraints.md), gather only in ways the organization would be comfortable explaining — honour robots directives, respect terms, throttle, prefer an API. **Establish this before writing a collector**, not after.
2. **What geography and which roles.** "Regional" needs a definition — the metro, the parish, a commuting radius? And which job titles map to which of the organization's three tracks. This is a conversation with the director of programs and it bounds everything.
3. **What the instructors would actually use.** Ask the three of them what question they would want answered before a curriculum review. If the answer is "which tools appear most often in postings for the jobs our graduates get," the project is narrow and achievable. If it is broader, narrow it.
4. **Whether the certification body's curriculum can be compared against systematically**, or whether that comparison stays a human reading.
5. **Who will run this after you leave.** Per [constraints](constraints.md), an owner agreed in advance, and not "an instructor could probably figure it out." If the honest answer is nobody, build something that produces a report quarterly with no maintenance rather than a live system.

## What a volunteer would do (roughly 6–10 weeks)

1. **Define the question narrowly** with the director of programs and the instructors, per dependency 3. A tightly-scoped question answered well beats a labor-market dashboard nobody trusts.
2. **Build collection** from permitted sources, politely, with the source and date recorded for every posting. **Provenance matters here for the same reason it matters in [Gulf Corridor's](../../synthetic-gulf-corridor-justice-project/technical-volunteers/archive-integrity.md) archive**: a finding is only usable if someone can go back and read what it came from.
3. **Extract structured attributes** — role, tools and technologies named, certifications requested, years of experience, wage if stated, whether the posting is remote. This is where a model earns its place: postings are free text and the variation is enormous. **Extraction only. No judgement, no ranking of importance, no inference about the market.**
4. **Keep every posting behind every number.** Per [constraints](constraints.md), any finding links back to the actual postings so an instructor can read them and judge. This is a hard requirement and it shapes the data model — store the postings, not just the aggregates.
5. **Report frequencies honestly.** Counts, date ranges, and the number of postings behind each figure. Per [constraints](constraints.md): **do not make a weak signal look strong.** If a tool appears in nine postings out of four hundred, the chart must say nine, and it should be hard to read that as a trend.
6. **Flag the noise explicitly.** Duplicate postings across boards, staffing-agency listings that aren't real openings, postings that have been up for eight months, and descriptions copied verbatim between employers. **Quantify how much of the corpus is noise** — it is likely a lot, and an analysis that hides it is worse than no analysis.
7. **Produce a quarterly report** rather than a live dashboard, unless dependency 5 turns up a real owner. A report that arrives four times a year and gets read beats a dashboard that goes stale in month three.
8. Leave a **runbook and a method note** — what was collected, from where, with what limitations, and how to run it again.

**Definition of done:** the instructors have, in front of them, what regional employers asked for in postings over a defined period, with counts, with the noise quantified, and with every figure traceable to postings they can read. A curriculum review happens using it. **The organization decides what to teach; the report does not.**

## What the volunteer should bring

- **Web data collection done responsibly** — APIs where available, terms and robots honoured, polite throttling. Per [constraints](constraints.md), the ethics here are part of the specification.
- **Practical NLP or LLM-based extraction** from messy free text, and the discipline to stop at extraction.
- **Statistical honesty.** The single most important quality for this project. The ability to say "this is nine postings and it means very little" when a chart would look better otherwise.
- **Data-quality instincts** for a genuinely dirty corpus: duplicates, ghost postings, agency reposts, copy-paste descriptions.
- Willingness to write a **method note** an instructor can read and a **plain-language limitations section** — which for this project is not a disclaimer, it is a deliverable.

Per [constraints](constraints.md): **nothing that asks more of participants**, **no scoring or predicting individuals**, **no curriculum recommendation the organization is expected to act on directly**, and **no collection the organization would not want to explain**.

## Capacity gained

Curriculum decisions get an evidence base. The organization stops finding out about a market shift from a graduate who noticed it himself.

Second-order and possibly more valuable: **the same data tells the organization something about its employer relationships.** If a large local employer is hiring constantly and has never taken a graduate, that is a business-development finding. And it may sharpen the reported "~30 employer partners" figure that currently mixes a standing pipeline with a one-off placement — see [programs](../programs.md).

What it does not do: fix completion rates. Per [population](../population.md), people leave in weeks four to seven because of money and childcare, and no amount of curriculum alignment touches that.

## Data sensitivity

**Effectively none, which is the point of including this project in the collection.**

Job postings are public marketing material. There is no participant data, no client data, no health information, nothing privileged, and no meaningful confidentiality obligation. A volunteer can develop in the open, publish their method, and talk about the work.

Two small qualifications. **Source terms are an obligation even without a privacy dimension** — per [constraints](constraints.md), collect only in ways the organization would be comfortable explaining. And **the output has a different kind of consequence**: a finding that changes a curriculum changes what people spend fourteen weeks of their evenings learning, which is real even though no data was sensitive. The care in this project belongs in the analysis rather than in the access controls.

If your framework for reviewing AI proposals would put this project through the same process as [an EHR consolidation](../../synthetic-sierra-foothills-community-health/technical-volunteers/ehr-consolidation.md), that is worth noticing.
