---
type: volunteer-constraints
title: "synthetic-North Star Immigrant Defense — Volunteer constraints & threat model"
description: "The org's rules for technology volunteers, written as a threat model. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic", "threat-model"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & threat model

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**. It is written as a threat model rather than a preference list, because the difference matters: several things a competent volunteer would consider obviously good practice are wrong here, and we would rather explain why than keep saying no.

## Our threat model

Most organizations protect data because disclosure would be embarrassing or harmful. Ours is different in a specific way: **there are parties who actively want what we hold.**

What we plan for:

**Lawful process.** Subpoenas, records demands, and requests whose validity we have to assess rather than assume. Some we must comply with. Some we must resist, and resisting requires that our counsel be involved before anyone hands anything over. **A volunteer who receives any request for our data refers it to us immediately and responds to nothing.**

**Device seizure — including at borders.** Searches at ports of entry operate under weaker protections than searches elsewhere. Our staff cross borders with clean devices. This is why.

**Targeted harassment.** Of our staff and of our clients. It has happened to organizations doing this work. It shapes what we publish, what we store, and what we put a name on.

**The client list itself.** A list of our clients is a list of people in removal proceedings, with addresses, in one place. It is the most dangerous thing we hold and its value to a hostile party is obvious. Every design decision starts here.

## What follows — and why our "gaps" are decisions

Please read this section before recommending anything. We have been offered each of the following as an improvement.

**We retain the minimum our professional obligations require.** Not more. Data we do not hold cannot be compelled, breached, or seized. Do not propose longer retention "for continuity" or a data warehouse "for analysis." If your project creates a new store of client information, it needs a deletion schedule before it has a first record.

**We log the minimum we must.** Comprehensive audit logging is good advice almost everywhere. Here it produces a detailed record of which staff member opened which client's file when — a document with obvious value to someone hostile and limited defensive value against our actual threats. Do not add logging without asking us what it is for.

**We do not have a client portal and we do not want one.** A portal account is a durable, structured record that a specific person is our client, sitting on infrastructure we do not fully control. The convenience is real. The artefact is worse.

**We have no web analytics.** A visitor log for a removal-defense website is a hazard to the people in it. This is not an oversight.

**We are cautious about cloud services, selectively.** Not reflexively — our email and documents are in a mainstream cloud tenancy and we have configured it deliberately. But every new service is a new party who may be compelled, may be breached, and may change its terms. The question we ask is not "is this vendor reputable" but **"what happens when someone serves them instead of us."**

**A note on how this reads.** We know this whole section scans as low digital maturity. We have seen the assessment. We would rather score badly and be right.

## On AI

- **No client information into any general-purpose AI service.** Not for drafting, not for summarizing, not for translation, not "just to test." Our concern is not only training data — it is that we would be adding a party who can be compelled and about whose retention we know less than we know about our own.
- **Locally-run is a different conversation** and one we are open to having.
- **No predicting, scoring, or ranking clients or cases.** We ration representation because we have to, and those decisions are made by attorneys who can be asked to justify them. A model would become the decision, and it would learn from data reflecting who has historically been able to make a tidy account of their own persecution.
- **No machine translation as a record.** Same as any legal-services setting: a machine rendering of a client's account is not what the client said, and a mistranslated fact becomes a false statement in a filing.

## Privilege and professional obligations

- **Client communications and work product are privileged.** A volunteer does not read case files. Not a trust question — we do not have authority to grant that access.
- **Conflicts screening runs before anything creates a matter.** No automation may acknowledge, contact, or record an inquiry in a way that could conflict us out of representing someone.
- **Deadlines are the malpractice risk.** In immigration practice a missed filing date can be irreversible for a person. Anything touching deadlines fails loudly, and treats uncertainty as failure.

## Working with us

- **Signed confidentiality agreement, background check, and a conversation with our operations director about the threat model** before access. The third one is not a formality; if it goes badly for either side, we stop there.
- **Least-privilege, time-boxed, revoked on completion.** Reviewed by a person, not a process.
- **Develop against synthetic data.** We will produce a realistic fake caseload. Ask for it. Do not develop against real matters, and do not "just look at the real data to understand the shape."
- **No screenshots.** Not for documentation, not for a ticket, not redacted.
- **Nothing on a personal device**, and nothing in personal cloud storage, ever.
- **Attorney time is very scarce** — fourteen attorneys, 1,300 matters. Our operations director is your main contact. Attorney input comes in scheduled short increments.
- **Do not name us in a portfolio, a case study, a blog post, or a conference talk** without asking. This is unusual and we mean it. Publicity about our systems is information about our systems.
- **Handover:** we have no internal developer. Configuration over code, and anything requiring maintenance needs an owner agreed in advance.

## What we would say no to

- More logging, longer retention, a client portal, or analytics.
- Any new third-party service holding client data without a hard look at what happens when it is served.
- Any AI touching client information without a local deployment we control.
- Case or client scoring, of any kind, for any purpose.
- A volunteer who wants to write about the work publicly.
