---
type: volunteer-request
title: "Finish the clinical migration that stopped in 2023"
description: "Consolidate two electronic health records so no clinician is looking at half a patient's history — starting by establishing how many patients actually exist twice."
tags: ["technical-volunteers", "request", "draft", "synthetic", "data-migration", "hipaa"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: data-migration-crm-consolidation
---

# Volunteer project — EHR consolidation

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

We absorbed a clinic in 2023 and never finished bringing its records over. The money ran out, the person running the project left, and the site kept seeing patients on Monday because that's what you do.

Three years later there are about 2,600 people in the old system, and somewhere between 300 and 600 of them are also in ours — we don't know the number, which tells you something. Most are agricultural worker families whose names are spelled three ways across five years of episodic visits.

Our medical director has a standing instruction: if a patient is from that town, check the other system before you prescribe. That instruction works because our clinicians are careful. It is not a system, it is a habit, and habits fail on a Friday afternoon with a full waiting room.

## Before anything else: the BAA

**This project cannot begin without a signed Business Associate Agreement.** Not a formality to sort out in week two — the threshold condition. See [constraints](constraints.md). Plan on two to three weeks of onboarding: BAA, confidentiality agreement, background check, HIPAA training. A volunteer who cannot get a BAA signed, personally or through their employer, cannot do the PHI-touching parts of this work.

**The scope below is deliberately arranged so that most of it doesn't need PHI.** That is not squeamishness, it's good design under this constraint: the smaller and more supervised the PHI-touching slice, the more likely this project happens at all.

## Confirm first (dependencies)

1. **Does the older EHR vendor still support full structured export** — medications, allergies, problem lists, immunizations as data, not as a PDF bundle? This single answer determines whether the project is difficult or close to impossible. Ask before anything else. See [inventory](../technology/inventory.md).
2. **What the EHR vendor and IT contractor will own afterwards.** Per [constraints](constraints.md), anything needing ongoing maintenance must have an owner arranged *before* it is built. This organization has contracted support, which is an advantage over most of the collection — use it.
3. **The reporting calendar**, with compliance staff. Cutover happens between federal reporting periods or not at all.
4. **Whether the dental system is in scope.** Recommendation: no. It is a third island, lower stakes, and including it will sink the timeline. Say so early rather than letting it drift in.
5. **What the medical director requires for merge review** — the format, the fields shown, the sign-off record. This shapes the whole tool and needs clinical input on day one, not at the end.

## What a volunteer would do

### Phase 1 — count the duplicates (no PHI access needed, and it's the most valuable deliverable)

The organization does not know its own duplicate count. Establishing it is the foundation of everything and can be done **without the volunteer seeing patient data at all**:

- Specify the matching logic — name variants, date-of-birth transpositions, address history, phone reuse across a household — and note that this population's naming patterns include Spanish compound surnames recorded inconsistently, which most off-the-shelf matching handles badly.
- **The organization's staff run it** against real data and report back counts and a sample of match categories. The volunteer tunes the logic from aggregate results.
- Deliver a number with confidence bands, and a breakdown: certain matches, probable, ambiguous, and the ones a human will have to look at individually.

By itself this changes the conversation — from "300 to 600, we think" to a defensible figure the organization can put in a funding request to finish the job.

### Phase 2 — the merge review tool (limited, supervised PHI access)

- Build the interface where a **clinical staff member reviews each proposed match** and decides. Two records side by side, the fields that matter for safety surfaced first — medications, allergies, problem list — with differences highlighted.
- **Merge is never automatic.** Per [constraints](constraints.md), no confidence threshold is high enough. The algorithm proposes, a licensed person decides, patient by patient.
- **Every decision is logged and reversible.** If a merge can't be unwound, it doesn't happen.
- Handle the ambiguous cases as first-class, not as an error state. Some pairs will be genuinely undecidable from the record and will need a phone call to the patient. The tool should make that a normal outcome with a place to record it.

### Phase 3 — migration and cutover (executed by staff and vendor, not the volunteer)

- Map the older system's structured data to the primary system's schema, field by field, with the vendor.
- **Do not touch medication, allergy, or problem-list transformation logic** — per [constraints](constraints.md), vendor and clinician territory, and the place where an error becomes an injury.
- Run in parallel: the older system stays readable, nothing is decommissioned until a full reporting cycle has been produced correctly from the consolidated data.
- Cut over between reporting periods, with compliance in the room.
- **The volunteer builds and hands over. Staff and vendor execute against production.**

### Throughout

- Write the **reporting reconciliation story**: how patient counts change on consolidation, why, and how the organization explains it to an auditor. Merging duplicates *reduces* the reported patient count, which looks like shrinkage in a federal report and is actually accuracy. Nobody wants to discover that during an audit.
- Leave a **runbook**: run the matcher, review a proposed match, reverse a merge, produce the reconciled report.

**Definition of done:** the duplicate count is known rather than estimated; every identified duplicate has been reviewed by a clinician and either merged or explicitly left separate with a reason; the standing check-the-other-system instruction is retired because there is no other system; and a federal reporting cycle has been produced from the consolidated record with the count change documented.

## What the volunteer should bring

- **Record linkage / entity resolution** experience, specifically the unglamorous kind — probabilistic matching, name-variant handling, and the judgment to know when to stop and hand a case to a human. Familiarity with non-Anglo naming conventions is a genuine advantage here.
- **Healthcare data** experience: HL7 or FHIR literacy, an understanding of what a problem list is and why it is not a free-text field, and the instinct to leave clinical logic to clinicians.
- **HIPAA fluency** — enough to know what PHI is before someone tells you, and enough to be the person in the room who says "we can't screenshot that."
- The discipline to build a **review tool rather than an automation**. This is the crux. A capable engineer's instinct is to raise the threshold and merge the easy 90%. Per [constraints](constraints.md), that instinct is wrong here and a volunteer who argues with it will not be a good fit.
- Willingness to write documentation an IT contractor and a compliance officer will both read.

Per [constraints](constraints.md): **BAA before access**, no screenshots, no data leaving the environment, no PHI into any AI tool, **no automated merge**, nothing into production by a volunteer's hand, and cutover only between reporting periods.

## Capacity gained

No clinician is looking at half a patient's history. The medical director's standing instruction — careful, human, and fragile — becomes unnecessary. Quarterly federal reporting stops being a hand-merge of two exports, which removes both a few days of staff time and a category of audit risk. And roughly 2,600 patients in one foothill town become patients of this organization in the data as well as in fact, including getting access to the patient portal they currently can't use.

The organization also gets something it can act on: a real duplicate number, in a funding request, to finish a job that stopped for want of money three years ago.

## Data sensitivity

**Protected health information, which is a legal category rather than a description.** Names, dates of birth, addresses, medications, allergies, diagnoses, appointment history — and the fact of being a patient here at all, which for behavioral health and prenatal services is among the most sensitive information the organization holds.

The whole scope is arranged around minimizing exposure: **Phase 1 needs no PHI access at all** and delivers the most valuable single output; Phase 2 needs supervised, time-boxed, least-privilege access; Phase 3 is executed by staff and vendor. A volunteer might complete this project having seen real patient records only inside a review tool they built, under a BAA, for the duration of a review period.

That is the shape to aim for, and it is worth noting as a general pattern: **when the data is this sensitive, the design question is not "how do we protect the volunteer's access" but "how much of this can be done without it."** Rather a lot, as it turns out.
