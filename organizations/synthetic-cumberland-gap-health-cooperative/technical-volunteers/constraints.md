---
type: volunteer-constraints
title: "synthetic-Cumberland Gap Health Cooperative — Volunteer constraints & preferences"
description: "The org's rules for technology volunteers — HIPAA obligations met with fourteen staff and no compliance officer. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic", "hipaa"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & preferences

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**. Like [the larger clinic in this collection](../../synthetic-sierra-foothills-community-health/technical-volunteers/constraints.md), much of what follows is regulatory obligation rather than preference. Unlike that clinic, we have fourteen staff and nobody whose job is compliance, so we are stricter about scope and slower to say yes.

## The threshold — BAA, and we will need help with it

A volunteer whose work touches **protected health information** is a **business associate** under HIPAA and needs a signed **Business Associate Agreement** before any access. Same rule as everywhere.

Here is our honest position: **we do not have a lawyer on call and we do not have a compliance officer.** Our BAA template is one our billing clearinghouse gave us years ago. If you are a volunteer who knows this territory, the most useful hour you could give us might be spent on that document rather than on the project — and we would rather you told us that than worked around it.

We are not going to skip it. We are telling you it is a real friction and that we know our paperwork is thinner than it should be.

## Design so you don't need our data

We would much rather scope a project where a volunteer **never touches a live record**. Not because we distrust anyone, but because our capacity to supervise access is genuinely limited — the practice manager who would be watching over your shoulder is the same person whose workload the project is meant to reduce.

So:

- **Ask us for synthetic documents.** We can construct realistic fake faxes. Build against those.
- **Structural verification, not reading.** Verify that a document was classified and routed correctly by checking the classification and the destination, not by reading the clinical content.
- **No screenshots, ever**, including "with the name covered." No data on a personal laptop. Nothing pasted into a search box, a chat, or an AI tool.
- **De-identification is a standard, not an effort.** If you need real-shaped data, ask; do not redact something yourself and consider it handled.

## On AI, for this project specifically

We are open to it — this is a document-sorting problem and that is a reasonable place for a model. The limits:

- **Classification and routing only. No clinical inference of any kind.** The model may say "this looks like a discharge summary for a patient whose name appears to be X." It may not summarize the document, extract a diagnosis, flag anything as urgent, or tell a clinician what it thinks. A clinician reads clinical content. Always.
- **A person confirms every match before it files.** Especially patient identity. A discharge summary filed to the wrong patient's chart is a serious clinical error, and in a county this size, a specific and potentially devastating privacy breach — our patients are related to each other.
- **Uncertain goes to a human queue, and we would rather it be over-cautious.** A model that routes 70% confidently and hands 30% to a person is a success. One that routes 95% and gets 2% wrong is a disaster we would rather not have bought.
- **PHI does not go to a general-purpose AI service** without a BAA our billing clearinghouse's lawyer has looked at. If a vendor won't sign one, we do this differently or not at all. Locally-run is easier for us to say yes to.
- **No urgency triage.** We know it is tempting — flag the discharge summary that needs attention today. That is a clinical judgment with real consequences if it is wrong in either direction, and it is not going to a model.

## Clinical and privacy specifics for this county

- **Being seen here is disclosure.** The county has 21,000 people and everyone is somebody's cousin. Anything that makes a patient's reason for visiting more visible — an appointment reminder naming a programme, a document title on a shared screen, a printout on a desk — causes real harm. Our substance-use recovery patients are the acute case and the rule applies to everyone.
- **Records that support black lung benefits claims are legal evidence.** They have retention and integrity obligations beyond ordinary clinical records. Do not build anything that alters, compresses, or re-renders those documents.
- **Nothing goes into the EHR by a volunteer's hand.** You build and hand over; our staff and our vendor execute.

## Working with us

- **BAA, confidentiality agreement, background check, HIPAA training** before access. Realistically two to three weeks, and we are slow because there is no one whose job this is.
- **Our practice manager is the project's main contact and also the bottleneck.** She is the person doing the fax sorting, she knows more about this problem than anyone, and she has about three hours a week to give you. Come to meetings prepared.
- **Clinical staff time is nearly unavailable.** Two nurse practitioners and a physician at 0.4 FTE, with a full schedule. Assume you get fifteen minutes when you truly need it.
- **Remote is fine.** Our internet is adequate for calls. Note that yours may be better than the county's — do not design assuming our patients' bandwidth.
- **Handover:** no IT staff, no developer, and no realistic prospect of either. Our EHR vendor and a local contractor are what we have. **If something needs code maintained, it must be something one of them will own, agreed before you build it.** We have been left with an orphaned system before and it cost us more than the problem it solved.
- **Eligibility limits:** as above. We will not waive the BAA. We will tell you honestly if we think a consultant is a better fit than a volunteer for a given piece of work.
