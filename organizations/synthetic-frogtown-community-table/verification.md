---
type: verification
title: synthetic-Frogtown Community Table — Verification
description: A simulated third-party determination about this organization. Entirely optional, and a snapshot rather than a passport.
tags: [verification, determination, synthetic]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-04-17T00:00:00Z }
stale_after: 2027-04-17
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0009"
    title: Validation determination (simulated)
    author: process:airt-simulated
    last_modified: 2026-04-17
---

# Verification

**⚠ Synthetic — this determination was never made.** It is fabricated to give the record a realistic shape.

## This file is optional, and that is the point

Nothing in `civic/0.6` requires a determination. The two facts a consumer needs in order to reason about eligibility — `org_type` and `registration_country` — are required frontmatter on [README.md](README.md), and they are facts about the organization rather than a verdict about it.

**A bundle carries a path toward validation, not a passport.** This document records that somebody looked, when, and what they could not establish. It goes stale, which is why it declares `stale_after: 2027-04-17`. A consumer that needs a current answer should re-ask, and `x-civic.verifiable_by` on the org record names who can be asked.

Note the trust mechanics, which are core OKF v0.2 rather than anything this profile invented:

- `verified: { by: process:airt-simulated, at: … }` makes this record **machine-confirmed** under §5.3 — a non-`human:` actor confirmed it.
- [README.md](README.md) carries **no** `verified` key at all, which makes it **unverified**. That is the correct tier for fabricated content, and §11 requires a consumer to accept it anyway rather than reject the bundle.
- `stale_after` is an absolute date, so "is this still good?" is a date comparison and not a judgement call.

## Determination — 2026-04-17

**APPROVE**, 88% confidence (MODERATE).[^determination] The registration ID matched the simulated registry exactly, exempt status is active, and all compliance screening (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches.

Nothing was wrong. Read the next section before drawing any conclusion from the number.

## Why 88%, and what it does not mean

The score is low because **there is very little of this organization written down in places an outsider can retrieve**:

- **No independent audit.** At $430K the organization is well below any threshold that would compel one. It has a bookkeeper and an annual board review. Entirely appropriate, and it produces no external document.
- **Board governance is documented thinly.** A seven-member board exists, meets, and keeps minutes. Two members are congregational representatives, three are from the communities the shelf serves. The minutes are in a folder.
- **Almost no independent web presence.** A small site, a Facebook page, two directory listings. Nothing to cross-reference.
- **No press coverage, no grant databases, no third-party evaluation.**
- **Its strongest evidence is unusable.** Seventeen years of continuous operation, four congregations that have funded it the whole time, and an executive director whom a large share of the neighbourhood knows by name. All real. None of it a retrievable record.

## Confidence measures legibility, not competence

This organization has one productivity suite, one donor database used properly, one accounting system, endpoint protection on every machine, and no shadow systems — see [technology/inventory.md](technology/inventory.md). Its data practice is careful and its books reconcile monthly.

An organization several times its size with three participant systems that disagree, an abandoned CRM, and an unwatched web form would score **higher**, because it has an audit, government contracts, published minutes, and a regulator asking questions.

Both numbers would be correct, and the ordering is the point. **Verification confidence measures how much of an organization has been written down somewhere an outsider can retrieve.** That tracks size, regulatory burden, and proximity to institutions that generate paperwork. It does not track competence, and here it runs opposite to it.

If you are building anything that ranks, scores, or filters organizations on a confidence figure, this is the failure mode to test for. A system that prefers the higher-scoring organization on the grounds that it is better run has drawn exactly the wrong conclusion from accurate data.

**Noted, not flagged:** the organization has no deputy for its executive director. Not an eligibility question — see [README.md](README.md).

- **Next re-validation due:** 2027-04-17, which is what `stale_after` records.

[^determination]: Validation determination (simulated)
