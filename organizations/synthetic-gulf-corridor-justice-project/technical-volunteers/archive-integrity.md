---
type: volunteer-request
title: "Make 14,000 documents provable"
description: "Add integrity, provenance, and chain-of-custody records to a public evidence archive cited in legal proceedings, so its authenticity cannot be questioned in a hearing."
tags: ["technical-volunteers", "request", "draft", "synthetic", "security", "integrity"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: website-security-remediation
---

# Volunteer project — Archive integrity & provenance

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

We publish about fourteen thousand documents. Permits, agency monitoring reports, correspondence we got through records requests, our own laboratory results. Lawyers cite them. Journalists quote them. Researchers use them.

In 2024 somebody defaced our front page. We restored it in a few hours and as far as we can tell nothing else was touched.

**"As far as we can tell" is the problem.** We have no hashes, no change log, no immutable copy. If somebody had quietly replaced a monitoring report with an altered version, we would not know, and we could not prove they hadn't.

We have been waiting for the hearing where opposing counsel asks how we know a document in our archive is the document the agency issued. We do not have a good answer. We would like one before we need it.

## Why this is the right project, not the obvious one

The obvious project after a defacement is website hardening, and the organization already did that — a protection layer went in after the incident. **Availability got attention because availability failures are visible.**

Integrity failures are invisible. Nothing is broken, nothing is down, nobody has complained, and the question only arrives in a proceeding at the worst possible moment. This project addresses the part that got no attention because it never announced itself.

## Confirm first (dependencies)

1. **Where the archive actually lives and who administers it.** One staff member currently, which is already too few. Everything below depends on the answer.
2. **Whether the backup is a real backup or a synchronized copy.** If it syncs, a corruption propagates and the organization has one copy wearing two hats. Per [constraints](constraints.md), nothing may become the only copy — check whether that is already violated.
3. **How much provenance can be reconstructed.** For each document: which agency, which records request, what date, from whom. Some is in file naming, some is in two people's memories, some is gone. Establish the honest scope early — **a partial provenance record that is explicit about its gaps is far more defensible than a complete-looking one that quietly guesses.**
4. **What form of proof would actually satisfy a proceeding.** Worth asking a lawyer the organization works with, because the answer shapes the design: a published hash manifest, a timestamping service, a notarized deposit, or simply a rigorous internal log may each be sufficient or insufficient depending on jurisdiction and challenge. Do not over-engineer past what would be persuasive.
5. **The hearing calendar.** Per [constraints](constraints.md), no deployment or migration near a hearing or comment deadline.

## What a volunteer would do (roughly 6–10 weeks)

1. **Hash everything, now.** Before anything else, before any tidying: compute and record a cryptographic hash for all 14,000 documents as they currently stand. This establishes a baseline from today even though it cannot reach backwards. It is a day's work and it is the single highest-value hour in the project.
2. **Publish the manifest** so the hashes are externally attested rather than only asserted — a public record, ideally timestamped by something outside the organization's control. The goal is that "we didn't change it" becomes checkable by anyone rather than a claim.
3. **Build ingest with integrity built in.** Every new document, from the moment it arrives: hash recorded, provenance captured (source, request, date, custodian), append-only, no path that can alter or delete an existing file. Per [constraints](constraints.md) — **and design it so deletion is not possible rather than merely not permitted.**
4. **Reconstruct provenance as far as it honestly goes**, and mark the rest **explicitly unknown**. Per the dependency above: do not infer. A document labelled "provenance not recorded" is usable; one labelled with a guess is a liability the first time the guess is wrong.
5. **Create a genuinely separate immutable copy** — write-once storage, or a separate custodian, or both. Not a sync. Per [constraints](constraints.md), additive and never the only copy.
6. **Document chain of custody for the sampling programme.** Currently the laboratory reports are in the archive and the record of how a sample got from a bottle to that report is not. Build a simple log — who took it, when, where, how it was stored and transported, which laboratory. **This is unglamorous and it is what makes a sampling result survive challenge.**
7. **Never modify a document.** Per [constraints](constraints.md), if OCR or a derived version is useful, it is a **new file alongside the untouched original**, clearly labelled.
8. **Write the method note** — plain language, how a document gets from an agency to the archive and how anyone can verify it. Per [constraints](constraints.md) this is a deliverable, and it exists to be read aloud in a proceeding.
9. **Check the survey data is nowhere near any of this.** Per [constraints](constraints.md), respondent-level health data must be physically and logically separate from the public archive, and a file-organization mistake must not be able to put it there. Verify the current state; report what you find to the operations lead rather than fixing it silently.
10. Leave a **runbook**: add a document, verify a document, respond to a challenge about authenticity, and restore from the immutable copy.

**Definition of done:** every document in the archive has a recorded hash and an externally attested manifest; new documents cannot enter without provenance; provenance gaps are labelled rather than guessed; an immutable copy exists that is not a sync; sampling chain of custody is logged; and the organization has a one-page method note that answers "how do you know this is the document the agency issued."

## What the volunteer should bring

- **Digital preservation or records-management** thinking. This is closer to archival practice than to web security, and someone with library or archives experience may be a better fit than a security engineer.
- **Practical cryptography** — hashing, manifests, timestamping — with the judgement to keep it simple enough to explain in a hearing. Per [constraints](constraints.md), boring and traceable beats clever.
- **Append-only system design**, and the discipline to make destructive operations impossible rather than discouraged.
- **The restraint not to improve the documents.** The instinct to OCR, straighten, and compress is strong and it is prohibited here.
- Willingness to write **plain-language documentation** that will be read by lawyers and possibly by an opposing expert.

Per [constraints](constraints.md): **never alter a document**, additive and reversible only, **no survey data anywhere near this work**, no deployment in a hearing week, and do not touch the public map.

## Capacity gained

The organization gets an answer to the question it has been waiting for. More broadly: **an archive that is provable is worth more than an archive that is merely accurate**, because its value in a proceeding no longer depends on the organization's credibility being unchallenged.

Second-order, and arguably as valuable: the provenance work forces down into records what currently lives in two people's memories. That is a continuity problem this bundle has in several places, and this project fixes it for the most important asset.

What it does not do: make the organization's sampling more extensive or its survey more rigorous. Those are laboratory-cost and methodology questions. This project makes what exists defensible; it does not make it stronger.

## Data sensitivity

**Almost all of this work is on data intended to be public**, which makes it an unusually good project for a volunteer with no prior relationship to the organization. There is nothing to leak in 14,000 published agency documents.

Two exceptions:

**The health survey data**, which must stay entirely out of scope. Per [constraints](constraints.md) it is respondent-level health information at known addresses, without HIPAA coverage or privilege, and therefore discoverable. The volunteer's only involvement should be **checking that it is not accidentally adjacent to the public archive** and reporting what they find.

**The archive's own security arrangements.** Once integrity mechanisms exist, how they work becomes information an adversary would find useful — not the hashes, which should be public, but the operational details of the append-only path and the immutable copy. Per [constraints](constraints.md), check before publishing specifics about how the organization's systems are arranged. This is the one place where a project about making things provable also creates something worth keeping quiet.
