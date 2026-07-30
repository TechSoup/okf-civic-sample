---
type: volunteer-constraints
title: "synthetic-Fundacja Prawo i Schronienie — Volunteer constraints & preferences"
description: "The org's rules for technology volunteers, substantially set by GDPR and Polish professional obligations. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic", "poland", "gdpr"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & preferences

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**. Note how much of it is law rather than preference — and law that a volunteer from outside the EU may not expect.

## A volunteer here has a legal status

This surprises people, so we say it first. Under **GDPR**, if you handle personal data on our behalf you are not simply helping — you are acting as a **processor** or under our authority as controller. That means:

- **A written agreement is required** before you touch personal data, setting out what you may process, for what purpose, for how long, and what happens at the end. Not a courtesy document. A legal instrument, and we are the ones a supervisory authority would come to.
- **You cannot decide to do something else with the data.** A processor acting outside the controller's instructions becomes a controller in their own right, with their own liability.
- **You must tell us immediately about any incident**, and we have **72 hours** to notify the supervisory authority. There is no version of "let me look into it over the weekend first."
- **Sub-processing needs our authorization.** If your approach involves a third-party service touching our data, that service is a sub-processor and we have to agree to it in advance and know where it is.

If that sounds heavier than volunteering elsewhere, it is, and it is not ours to soften.

## Where data may go

- **Prefer the EEA. Assume anything else is a legal question.** Transfers outside the EEA need a valid mechanism and a documented assessment. We are already in trouble on exactly this point — see [inventory](../technology/inventory.md) — and we are not adding to it.
- **Do not introduce a US-hosted service** without asking. This includes the ones you would not think of as services: an analytics script, a font CDN, a form handler, an error-reporting tool, a chat widget. **The defaults of the web industry are American and that is how we got into this.**
- **No personal data into any AI service.** Not for translation, not for drafting, not for testing. Beyond the transfer problem, we could not tell a data subject what happened to their data, which we are obliged to be able to do.
- **Nothing on personal devices or in personal cloud storage.**

## Data subjects have rights, and your design has to allow for them

This is the part most likely to be unfamiliar. The people in our records can **require** things of us:

- **Access** — we must be able to tell a person everything we hold about them. If you build something that stores personal data in a way we cannot search and extract, you have made us unable to comply.
- **Erasure and rectification** — we must be able to correct or delete. **A system that cannot delete is not acceptable here**, which is a meaningfully different requirement from the append-only archives some organizations want.
- **Portability** — in some cases, provide the data in a usable form.

So: **build for extraction and deletion from the start.** Retrofitting a data-subject-access capability onto a system that was not designed for it is expensive and we cannot afford it twice.

## Special category data

Our asylum work routinely involves **health data, religious belief, ethnic origin, political opinion, and sexual orientation** — because that is what a persecution claim is made of. Under GDPR these are **special categories** with a higher bar for processing.

Practically: assume any free-text field in which a client describes their situation contains special category data, and treat it accordingly. **This includes the free-text box on our website contact form**, which is the specific thing we need help with.

## Professional secrecy

Our lawyers are bound by Polish professional-secrecy obligations. **A volunteer does not read case files.** Not a matter of trust — we lack the authority to permit it, in the same way [the American organizations in this collection](../../synthetic-central-valley-farmworker-law-center/technical-volunteers/constraints.md) describe under a different legal doctrine.

## Data minimization is a rule, not a virtue

Under GDPR we may only collect what we need for a stated purpose. So:

- **Do not add fields because they might be useful.** That is not permitted, not merely untidy.
- **Do not build analytics into an intake process** to see how people use it, without asking. It may need its own basis.
- **If your design collects less, that is a compliance improvement**, not a reduction in functionality.

## Working with us

- **Written processor agreement, confidentiality undertaking, and a conversation with our DPO** before access. Our DPO is one of our lawyers holding it alongside a caseload, so book time.
- **Our operations manager is your main contact.** Lawyers are in procedure.
- **English is fine** for working with us. Note that **our public materials are canonical in Polish, Ukrainian, and Russian** — if your work touches user-facing text, you are not the person who writes it.
- **Remote is fine.**
- **Handover:** twenty staff, no developer. Configuration over code, EEA-hosted managed services over anything we run, and documentation our operations manager can follow — in English is acceptable, and Polish is better.

## What we would say no to

- Any new US-hosted dependency, including a script or a font.
- Personal data in an AI service.
- A system we cannot delete from or extract from.
- Extra fields "for later."
- A volunteer who wants to start before the paperwork. We know it is slow. It is not optional.
