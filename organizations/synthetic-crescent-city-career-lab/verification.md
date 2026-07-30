---
type: verification
title: "synthetic-Crescent City Career Lab — Eligibility & verification"
description: "The organization's simulated verification determination — EXPIRED. Approved in 2024, never re-validated."
tags: ["eligibility", "verification", "determination", "synthetic", "lapsed"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2024-02-14T00:00:00Z }
stale_after: 2026-02-14
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0012"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2024-02-14
x-civic:
  profile: civic/0.6
---

# Eligibility & verification

**⚠ Synthetic — this determination was never made. It is fabricated to give the record a realistic shape.**

A **log**, written by the validation system. Each re-validation appends a new entry; nothing is overwritten. Everyone else reads this file; only the validation system writes it. Edit history for the *bundle* is separate — see [log](log.md).

## Current status: **PENDING RE-VALIDATION — the determination on file has expired**

> **Read this before using the determination below.** It says **APPROVE, 94% confidence**. It was issued **2024-02-14** with a **two-year term**. It **expired 2026-02-14** and has not been renewed. At the time this bundle was created it was **165 days out of date**.
>
> **The correct reading is "unverified," not "approved" and not "rejected."** The organization shows no sign of any problem. Nobody has checked for five and a half months.

## Determination v1 — 2024-02-14 — ⚠ EXPIRED 2026-02-14

**APPROVE**, 94% confidence (HIGH). The registration ID matched the simulated registry exactly, 501(c)(3) status was active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches. Governance was documented — a thirteen-member board including four employer representatives and two graduate seats.

**Debarment screening was materially significant** — the organization holds a state workforce allocation and city economic-development funds.

**Out of scope:** employer-partnership depth was not assessed. See [README](README.md) — the reported figure of ~30 employer partners mixes standing pipelines with one-off placements.

**Term:** two years. **Re-validation due 2026-02-14.**

## How the lapse happened

This is the useful part of this bundle, and it is deliberately unremarkable.

The organization's development director held the relationship and had completed the original validation. She left in **November 2025**. Her email account was deactivated in December, per the organization's normal offboarding.

The re-validation notice was sent in **January 2026** to her address. It bounced into a queue nobody monitors. A reminder went to the same address in February. Nobody at Career Lab knew a re-validation was due, because the person who knew had left and it was not written down anywhere else. Nobody outside noticed, because an expiry is not an event — **it is the absence of an event**, and absences do not generate alerts unless something is built to notice them.

The organization is, as far as anyone can tell, exactly as eligible as it was in 2024. **The record is simply out of date, and no part of the system was arranged to say so out loud.**

Three things about this failure mode are worth extracting:

**It is the most common one.** Fraud is rare. Organizations losing standing is uncommon. **Records quietly going stale is routine**, and it is the case least likely to be handled well because nothing about it looks like a problem.

**Nothing else in the bundle changed.** Programs, technology, partnership, population — all current, all fine. A reader skimming this bundle for signs of trouble would find none. The only field that changed did so by the calendar advancing.

**The determination is worse than useless if read carelessly**, because it is emphatic. It says APPROVE at high confidence, and a system that surfaces the determination without its term will show a strong positive signal that is no longer true.

## What this bundle tests

- **Does your code compare `stale_after` to today**, or does it infer approval from a determination being present? The frontmatter here carries `verified.at: 2024-02-14` and `stale_after: 2026-02-14` — a date in the past. Nothing in the record says the word "expired"; the expiry is something you have to compute. A system reading only the APPROVE text will get it wrong.
- **Does an expiry surface where a human sees it?** In this bundle it is in frontmatter, in a banner on [README](README.md), in the bundle [index](index.md), and here. In a real corpus it is often one date field nobody renders.
- **Can your model represent three states?** Eligible, not eligible, and **not currently known**. A boolean cannot, and collapsing the third into either of the first two is wrong in opposite ways: treated as approved, an unchecked organization passes; treated as rejected, a good organization is penalized for an administrative gap that is arguably the verifying party's fault.
- **Does status propagate along edges?** [Gulf Corridor](../synthetic-gulf-corridor-justice-project/verification.md) holds a current determination and a `partners_with` edge to this bundle. It should be unaffected. Confirm that in your traversal.
- **Does anything compute staleness?** `stale_after` is in the frontmatter, and `scripts/validate.py` reports this record as past its term — but as *information*, not an error. Nothing here refuses to serve the bundle or downgrades it. That is the realistic part: computing the expiry is easy, and deciding what to do about it is the actual question.

## What should happen next

A re-validation should be requested, sent to an **organizational address rather than an individual's**, and the term should be tracked by whoever holds the record rather than depending on the organization remembering. The offboarding lesson — that a departing staff member's address was a single point of failure for an external compliance relationship — belongs in the organization's own practice.

<!-- Determination v2 appends here when re-validation occurs. Status returns to ELIGIBLE only at that point. -->

[^determination]: Validation determination (simulated)
