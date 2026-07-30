---
type: volunteer-constraints
title: "synthetic-Sierra Foothills Community Health — Volunteer constraints & preferences"
description: "The org's rules for technology volunteers — mostly HIPAA obligations rather than preferences. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic", "hipaa"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & preferences

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**. Note what makes this one different from the collection's other constraints files: most of what follows is **not a preference**. It is regulatory obligation, and we cannot waive it for a volunteer we like.

## The threshold — no BAA, no project

A volunteer whose work brings them into contact with **protected health information** is a **business associate** under HIPAA. That requires a **signed Business Associate Agreement** before any access, and it makes the volunteer subject to the same obligations we carry, including breach-notification duties.

This is not paperwork we can skip for a short engagement or a trusted friend of the organization. **The exposure is ours**, the penalties are real, and there is no version of this where we proceed on good faith and sort out the agreement later. If a volunteer or their employer cannot sign one, the project does not happen in a form that touches PHI — and we will try to find a form that doesn't.

**Corollary that matters practically:** we would rather scope a project so that 80% of it happens on de-identified or synthetic data, with a small supervised slice touching real records, than have a volunteer inside our PHI for three months. Design that way from the start.

## What PHI means here, specifically

Wider than people expect. It is not just diagnoses. **A patient's name alongside the fact that they are our patient is PHI.** An appointment time is PHI. A list of patient identifiers with no clinical content attached is PHI. The fact that someone visited our behavioral health service is among the most sensitive things we hold.

Practical consequences for a volunteer:

- **No screenshots.** Not for documentation, not for a bug report, not "with the names blurred."
- **No data leaves our environment.** No copying a table to a laptop to work on at home, no test file in personal cloud storage, no pasting a record into a chat or a search box or a model.
- **De-identification is a technical standard, not an intention.** Removing the name column does not de-identify a record. If the project needs realistic data, ask us for a synthetic set — we can produce one, and it is a better answer than a redaction someone did their best on.
- **No PHI into any AI tool**, of any kind, at any point, regardless of the vendor's assurances, unless it is covered by an executed BAA that our compliance officer has reviewed. This has come up and the answer has been no.

## Clinical safety outranks everything

**A record-matching error can hurt someone.** Merging two patients who are different people puts one person's allergies and medications in another person's chart. Failing to merge two records for the same person leaves a clinician with half a history. The second is our current state and it is bad; the first is worse.

So:

- **No automated merge without clinical review.** A matching algorithm may *propose*; a licensed clinical staff member decides, patient by patient, for every merge. There is no confidence threshold high enough to skip this, and a volunteer who proposes an auto-merge above 0.98 similarity has not understood the failure mode.
- **Every merge is reversible and logged.** If we cannot unwind a merge, we do not perform it.
- **Nothing goes into a production clinical system by a volunteer's hand.** Volunteers build, test, and hand over; our staff and our EHR vendor execute against production.
- **Do not touch the medication, allergy, or problem list logic.** Ever. Those are the fields where an error becomes an injury, and they are the vendor's and our clinicians' territory.

## Reporting must not break

Our federal reporting is mandatory, annual, in a defined format, and audited. A migration that changes how patients are counted mid-year creates a reporting problem that takes a year to explain. **Cutover between reporting periods, with our compliance staff in the room for the planning, or not at all.**

## Working with us

- **Confidentiality agreement and BAA signed, background check completed, HIPAA training done** — the same onboarding a new employee gets. Expect two to three weeks before you can start.
- **Least-privilege, time-boxed access**, reviewed by our compliance officer, revoked on completion.
- **Clinical staff time is the scarcest resource here.** Six physicians, eleven mid-levels, and a full schedule. You will get the medical director in scheduled thirty-minute increments and you should come to those with specific questions.
- **Remote is fine for most of the build.** Anything touching production, or the older system's server, is on-site and escorted.
- **Spanish helps** for anything patient-facing, though this project is back-office.
- **Handover:** we have contracted IT support and an EHR vendor, which is more than most organizations in this collection — but no internal developer. Anything requiring custom code maintenance has to be something our vendor or our IT contractor will own, and that has to be arranged before it is built, not after.

## What we would say no to

- An automated patient-matching system that merges without review.
- Any proposal involving putting patient data through a general-purpose AI service.
- A "quick look at the data to scope it" before the BAA is signed. This is the most common request and the answer is always no.
- Anything that touches the mobile unit's clinical workflow without a clinician co-designing it. We know the paper-notes problem is real; we are not fixing it with something a clinician hasn't signed off on.
