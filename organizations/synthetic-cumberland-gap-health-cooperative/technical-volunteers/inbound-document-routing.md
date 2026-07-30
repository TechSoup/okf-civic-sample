---
type: volunteer-request
title: "Stop sorting the fax pile by hand every morning"
description: "Classify and route 60–120 inbound clinical faxes a day into the EHR, with a person confirming every patient match and no clinical inference anywhere."
tags: ["technical-volunteers", "request", "draft", "synthetic", "ai-assisted", "documents"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: ai-assisted-intake-triage
---

# Volunteer project — Inbound clinical document routing

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

Between sixty and a hundred and twenty pages arrive in the fax inbox every day. Consult notes, lab results, discharge summaries from the hospital ninety minutes away, imaging reports, prior authorizations, pharmacy questions, benefits correspondence.

Our practice manager opens each one, works out what it is and whose it is, renames it, and files it in the chart. It takes most of every morning. When she took two weeks off in March we came back to four hundred documents and a discharge summary from day three that nobody had read.

We cannot change how the hospital sends things. This is what interoperability looks like from a fourteen-person clinic.

## Two smaller things first

The organization asked for the fax project. Scoping against this bundle turns up two things that may matter more, and it is more useful to name them than to bury them:

**The fax server's backup status is unverified.** Until a document is filed, the fax server is the only place it exists that the organization controls. A drive failure would lose clinical information outright. **Establishing whether a backup exists, and creating a tested one if it doesn't, is a few days of work and should happen regardless of whether the rest of this project ever starts.** See [inventory](../technology/inventory.md).

**There is no current HIPAA risk assessment and no compliance officer.** That is a regulatory exposure, and the honest advice may be that this needs a paid consultant rather than a volunteer. Worth saying plainly — a volunteer offering to do the fax project could reasonably point out that the organization's bigger problem is one they should spend money on.

## What it would do

Read each inbound fax, work out **what kind of document it is** and **which patient it belongs to**, propose a filing destination, and let a person confirm — turning most of a morning into a review queue that takes twenty minutes.

## Confirm first (dependencies)

1. **Can the EHR accept documents programmatically?** An API, a watched folder, a structured import — anything. **The whole project depends on this and nobody has asked the vendor.** Do this before writing a line of code; if the answer is no, the project becomes a much smaller one about naming and pre-sorting files for a human to import.
2. **What the fax server can do** — where documents land, in what format, whether it can be read from, whether it does OCR already.
3. **Whether an acceptable AI arrangement exists.** Per [constraints](constraints.md), PHI needs a BAA the organization's clearinghouse lawyer will look at, and a locally-run model is easier for them to approve than a cloud service. Establish this early; it may steer the whole technical approach toward something running on the organization's own hardware.
4. **The document taxonomy, from the practice manager.** She already has one in her head — the categories she sorts into. Write it down. This is an hour's conversation and it is the specification.
5. **What the black lung benefits documents require.** Per [constraints](constraints.md), those are legal evidence and must not be altered, compressed, or re-rendered. Identify them and route them untouched.

## What a volunteer would do (roughly 6–10 weeks)

1. **Sit with the practice manager for one morning's sort.** Everything about the real taxonomy, the ambiguous cases, and why patient matching is hard is visible in two hours and guessable in none.
2. **Build classification** into her categories: consult note, lab result, discharge summary, imaging report, prior authorization, pharmacy, benefits correspondence, other. **Category and patient identity only** — per [constraints](constraints.md), no summarizing, no diagnosis extraction, no urgency flag, no clinical inference of any kind.
3. **Build patient matching** against the EHR's patient list, and expect it to be harder than it looks: faxes carry names inconsistently, dates of birth are sometimes absent, and in this county a name match is genuinely ambiguous because patients are related to each other. **Design for the ambiguous case as normal**, not as an error.
4. **Build the review queue.** Document preview, proposed category, proposed patient, and a confirm action. Per [constraints](constraints.md) a person confirms **every** patient match before filing — no confidence threshold skips this. Tune for the practice manager to move fast through the obvious ones, not for automation.
5. **Bias hard toward the human queue.** Per [constraints](constraints.md) the organization would rather 30% go to a person than 2% file wrongly. Build and tune with that preference explicit, and report the two rates separately so the trade is visible rather than buried in an accuracy number.
6. **Route black lung documents untouched**, flagged as such, no transformation.
7. **File into the EHR** via whatever the vendor supports — with the organization's staff executing against production, per [constraints](constraints.md).
8. **Handle the leave case**, which is the one that produced the March incident: if the queue exceeds a threshold, somebody other than the practice manager gets told.
9. Leave a **runbook**: add a category, correct a misfiling, retrain or adjust matching, recover from a fax-server outage — and per [constraints](constraints.md), **confirm before building that the EHR vendor or the local IT contractor will own whatever needs maintaining.**

**Definition of done:** a morning's faxes are reviewed and filed in twenty minutes instead of three hours; no document is filed to a patient without a person confirming; the ambiguous ones are visibly queued rather than silently guessed; and a two-week absence produces a queue somebody else knows about.

## What the volunteer should bring

- **Document classification and OCR** experience with genuinely bad inputs — faxes are skewed, low-contrast, sometimes upside down, sometimes stapled crooked and scanned as one page.
- **Entity matching** judgment, and specifically the humility to route to a human. The skill being asked for is calibration, not accuracy.
- **Healthcare document literacy** — enough to recognize the document types without needing clinical judgment, and enough discipline to stop there.
- If a local model is the route: **the ability to run something small on modest hardware** and hand it over in a state a local IT contractor can maintain.
- **HIPAA fluency**, and enough contract sense to be useful about the BAA — per [constraints](constraints.md) the organization has openly said its paperwork is thin here and help would be welcome.
- Willingness to write documentation for a practice manager and a local contractor, not for a developer.

Per [constraints](constraints.md): **BAA before access**, build against synthetic documents the organization provides, no screenshots, nothing on a personal laptop, **no clinical inference**, **no urgency triage**, **a person confirms every patient match**, and nothing enters the EHR by the volunteer's hand.

## Capacity gained

The practice manager gets most of a working morning back, every day — in a fourteen-person organization that is a meaningful fraction of total administrative capacity. A discharge summary is read the day it arrives rather than the day someone reaches it. And a two-week absence stops being a clinical risk.

What it does not do: fix interoperability. The hospital still faxes. This project makes the fax pile tractable rather than making it go away, and a proposal claiming otherwise would be overselling.

## Data sensitivity

**Protected health information throughout, and the county makes it sharper.** Every document is PHI. The patient list used for matching is PHI. In a county of 21,000 where patients are related to each other, a document filed to the wrong chart is both a clinical error and a disclosure to a family member — see [constraints](constraints.md), which is blunt about this.

The scope is arranged so a volunteer can do most of the work on **synthetic documents the organization constructs**, verifying behaviour structurally rather than by reading clinical content. That is the pattern this collection keeps arriving at for sensitive data: not "how do we protect the volunteer's access" but "how much of this can be done without it." Here, most of it.

The **substance-use recovery** documents are the most sensitive category and deserve explicit handling in the design — arguably they should route to a restricted queue that fewer people see, which is a conversation for the practice manager and the nurse practitioners rather than a decision for a volunteer to make.
