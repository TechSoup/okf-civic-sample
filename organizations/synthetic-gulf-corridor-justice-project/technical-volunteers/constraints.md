---
type: volunteer-constraints
title: "synthetic-Gulf Corridor Justice Project — Volunteer constraints & preferences"
description: "The org's own rules for technology volunteers, shaped by a lawful, well-funded adversary. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & preferences

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**. Ours is shaped less by privacy than by the fact that everything we publish will be attacked by people who are competent, funded, patient, and acting entirely within the law.

## Assume an expert will try to discredit it

Whatever you build, assume a paid expert will examine it in a proceeding and look for a way to make it unreliable. That is not paranoia; it is the last four permit hearings.

Practical consequences:

- **Boring and traceable beats clever.** If we cannot explain in a hearing how a number or a document got where it is, in plain language, it is worth less to us. A sophisticated pipeline nobody can narrate is a liability.
- **Document your own work as evidence.** The method note you write is part of the deliverable, not overhead. Someone may read it aloud in a proceeding.
- **Never overstate our data.** Our sampling is limited by laboratory cost, and our health survey is community-administered and self-reported. We describe both carefully and we are sometimes quoted less carefully. **Do not build interfaces that present our numbers with more confidence than they carry** — no unqualified comparisons to regulatory thresholds, no removing an uncertainty note because a chart reads better without it. Our carefulness is an asset and stripping it costs us more than a tidier visual gains.
- **Reversible and additive.** Nothing that mutates the archive in place. Nothing that becomes the only copy.

## The archive is evidence, not a website

Our document archive is cited in proceedings. Treat it as a records system:

- **Never alter a document.** Not to compress it, not to re-render it, not to fix an orientation, not to OCR it in place. If a derived version is useful, it is a **new file alongside the original**, clearly labelled, and the original is untouched forever.
- **Provenance is part of the record.** Where a document came from — which agency, which request, which date — matters as much as its contents. If you touch the archive, capture provenance; do not let it stay in two people's memories.
- **Additions are appends.** We do not delete from the archive, and anything that could delete from the archive needs to not be able to.

## The health survey is the one thing that must not be public

Everything else we hold is meant to be seen. Our survey data is not.

- **Respondent-level health information at known addresses.** Symptoms, household cancer history, pregnancy outcomes.
- **No HIPAA coverage and no privilege**, which means it is **discoverable in litigation.** Our consent form says so since 2023. Response rates fell and we kept the language.
- **Keep it physically and logically separate from the public archive.** Our instinct is to keep our data together; for this category that instinct is wrong. It must not be possible for a survey file to end up in the public archive through a mistake in file organization.
- **Aggregation is not anonymization.** "Three households on this block" identifies people here. Any query interface must carry small-cell suppression itself; we will not rely on whoever runs the query remembering.
- **Signed confidentiality agreement** for any access, and we would strongly prefer you not need any.

## Availability matters on specific days

Our site goes down or gets very busy around hearing dates. Sometimes that is legitimate interest, sometimes it isn't. We added a protection layer after we were defaced in 2024.

- **Know our calendar.** Do not schedule a deployment, migration, or maintenance window near a hearing or comment deadline. Ask us for the dates.
- **The site being up is a program function**, not a convenience. People come to it to find out what to do about a permit with thirty days left on it.

## On AI

- **Public documents, fine, with care.** Classification, extraction, and search over agency documents is a reasonable use and would help us. But **anything an extraction produces is a lead, not a fact** — if a model tells us a permit contains a number, a person verifies it against the document before it goes anywhere near a filing.
- **No survey data into any AI service.** Same reasoning as any other disclosure risk, plus discoverability.
- **No model-generated analysis presented as ours.** We will not put our name on a conclusion we cannot reconstruct and defend line by line.

## Working with us

- **Confidentiality agreement** for anything touching survey data; not needed for archive or public-facing work.
- **Our scientific staff are the scarce resource** — two people, and they are usually writing comments against a deadline. Our operations lead is your main contact.
- **Remote is fine.** A visit to the corridor is welcome and will change what you think this work is.
- **Handover:** sixteen staff, no developer. Configuration over code, managed over self-hosted where the archive's integrity requirements allow it, and documentation an operations lead can follow. One person currently administers our archive server and that is already too few.
- **Attribution:** you may say you worked with us. Please check before publishing anything specific about how our systems are arranged.

## What we would say no to

- Anything that modifies documents in the archive.
- A rebuild of our public map. It works and it is central; leave it alone.
- Survey data in the cloud, in an AI service, or anywhere near the public archive.
- A visualization that drops our uncertainty language.
- Deployment in a hearing week.
