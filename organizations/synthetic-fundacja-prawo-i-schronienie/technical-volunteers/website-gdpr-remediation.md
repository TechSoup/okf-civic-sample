---
type: volunteer-request
title: "Stop sending asylum applicants' accounts to a US processor"
description: "Remove unlawful third-country transfers from the website, then build the records of processing and lawful-basis documentation that should have existed since 2019."
tags: ["technical-volunteers", "request", "draft", "synthetic", "gdpr", "security", "website"]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  project_shape: website-security-remediation
---

# Volunteer project — Website GDPR remediation

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. In a real bundle: **draft, the organization owns this**, scoped against its own bundle, edited and blessed before posting.

## The need, in the org's words

Our website has a contact form. A person in the asylum procedure fills it in with their name, their nationality, and a free-text description of their situation — which means, in practice, an account of why they fear returning home. Health, religion, ethnicity, sometimes sexual orientation. Special category data, every time.

That form posts to a **form-handling service in the United States.** Our analytics are American too, and our cookie banner does not actually stop the script from loading.

Our contractor built the site in 2021 using the tools everyone uses. Nobody made a decision here. We only understood it properly when our DPO — one of our lawyers, holding the role alongside her caseload — read the audit trail this spring.

We have been transferring special category data about applicants for international protection to a third country, without a transfer mechanism, for about five years.

## Why this is urgent rather than important

Most projects in a collection like this improve something. **This one stops something.**

Every day the site is up in its current state, more special category data goes to a US processor. That is a continuing breach, the data subjects are people for whom exposure carries real consequences, and the volume grows while anyone deliberates.

**Sequence matters more than completeness here.** A volunteer who begins with the records of processing — the tidier, more satisfying work — will produce good documentation while the transfer continues. Stop the flow first, even crudely.

## Confirm first — but do not let this delay Phase 0

1. **Which services the site actually calls**, in full. Analytics, form handler, fonts, embedded media, error reporting, anything. Per [constraints](constraints.md), the ones nobody thinks of are the ones that got the organization here. Expect the list to be longer than the fingerprint in [inventory](../technology/inventory.md) suggests.
2. **What the form processor has stored since 2021**, whether it can be exported, and whether it can be deleted. There may be five years of asylum accounts sitting in a US account nobody has opened.
3. **Whether any transfer mechanism was ever put in place.** Almost certainly not. Establish it rather than assume it.
4. **What the DPO needs the documentation to look like.** She is the one who would answer to a supervisory authority. Her requirements are the specification, and per [constraints](constraints.md) she has limited time — book it early.
5. **The case management vendor's DPA and its sub-processors**, and where they are. Outside the immediate fix, in scope for the documentation.

## What a volunteer would do

### Phase 0 — stop the transfer (days, and it does not wait for the rest)

- **Remove the US analytics.** Replace with an EEA-hosted or self-hosted alternative, or nothing at all. The organization's traffic data is not worth a continuing breach, and [one organization in this collection](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md) runs no analytics at all deliberately.
- **Move the forms off the US processor** to an EEA-hosted handler, or — simpler and immediately available — **replace the form with a mail address and a phone number until a compliant handler is in place.** Losing a convenient form for three weeks is a smaller harm than continuing.
- **Fix the cookie banner** so it actually gates non-essential scripts rather than announcing them.
- **Remove any US-hosted fonts, embeds, and error reporting**, which are transfers too.

Per [constraints](constraints.md), introduce nothing new that is US-hosted, including a script or a font.

### Phase 1 — deal with what has accumulated

- **Retrieve and assess the historical form submissions.** Five years, containing special category data.
- **Decide with the DPO what must be kept**, on what basis, and delete the rest. Per [constraints](constraints.md), data minimization is a legal requirement — data held without a basis should not be held.
- **Document the breach assessment.** Whether this requires notification is the DPO's call and a lawyer's judgement, not a volunteer's, but the volunteer's technical account of what was transferred and for how long is what that judgement rests on. **Write it carefully.**

### Phase 2 — the documentation that should have existed

- **Records of processing activities.** Every category of personal data, its purpose, its lawful basis, who it is shared with, where it goes, how long it is kept. Tedious, required, and mostly interviews rather than technology.
- **Lawful basis per category**, explicitly, including the higher-bar condition relied on for special category data.
- **A data protection impact assessment** for the high-risk processing this organization plainly does.
- **Retention schedule per category**, reconciled with the professional-secrecy obligations that already govern case files.
- **Data-subject request procedure** — how the organization would actually answer an access or erasure request, tested once rather than assumed. Per [constraints](constraints.md), build for extraction and deletion.

### Throughout

- **Do not touch the multilingual content.** Per [constraints](constraints.md), the Polish, Ukrainian, and Russian text is canonical and the volunteer is not the person who writes it. It is also the site's genuine strength.
- Leave a **runbook** the operations manager can follow: adding a service and checking where it is hosted, responding to a data-subject request, and reviewing the records of processing annually.

**Definition of done:** no personal data leaves the EEA without a documented mechanism; historical submissions are assessed and either lawfully retained or deleted; a record of processing activities exists and the DPO signs it off; a data-subject access request has been answered end-to-end as a test; and the site works, in four languages, as it did.

## What the volunteer should bring

- **Real GDPR fluency** — not privacy sympathies. Records of processing, lawful basis, special category conditions, transfer mechanisms, DPIAs, and data-subject rights as concrete artefacts. **A volunteer who knows US privacy practice and assumes GDPR is a stricter version of it will do this wrong**, because it is a different structure.
- **Practical web work**: identifying every third-party call a page makes, and replacing US-hosted dependencies with EEA-hosted or local ones.
- **The judgement to sequence correctly** — stop the flow before documenting it. This is the single most important quality for this project.
- **Comfort writing for a lawyer**, since the DPO signs off and a supervisory authority may read it.
- Willingness to do a lot of **unglamorous interviewing** in Phase 2. Most of a record of processing comes from asking staff what they actually do.

Per [constraints](constraints.md): **written processor agreement before access**, no new US-hosted dependencies of any kind, **no personal data into any AI service**, nothing on personal devices, no reading of case files, no extra fields, and **immediate notification of any incident** — the organization has 72 hours and it starts when you tell them.

## Capacity gained

The organization stops breaking the law. More concretely: **people in the asylum procedure stop having their accounts of persecution copied to a third-country processor** because a web contractor used a normal tool in 2021.

Beyond that, the Phase 2 documentation is the thing the organization needs and cannot get from a technologist alone or a lawyer alone. A record of processing is a technical inventory with legal structure, and it makes every subsequent decision — a new tool, a funder's data request, a subject access request — answerable instead of alarming.

What this does not fix: the DPO is still a lawyer with a caseload holding a compliance function. That is a staffing question, and it is worth the volunteer saying so.

## Data sensitivity

**Special category data about applicants for international protection.** In terms of consequence for the data subject, this is at the top of the range anywhere in this collection.

The project has an uncomfortable property worth naming: **the historical form submissions have to be looked at in order to be dealt with.** Someone must determine what is in five years of accumulated submissions before deciding what to delete. Per [constraints](constraints.md) a volunteer does not read case files — and these are not case files, they are pre-intake enquiries sitting in a third-party service, which is precisely why they are a problem.

The right handling is for the volunteer to build the **extraction and assessment tooling** and for the organization's own staff, under the DPO's direction, to make the content determinations. A volunteer should be able to complete this project having seen the *structure* of those submissions and not their contents. Where that is impossible, the exception should be written down and time-boxed, per the organization's own instinct in [constraints](constraints.md).

Everything in Phase 0 and most of Phase 2 requires no access to personal data at all.
