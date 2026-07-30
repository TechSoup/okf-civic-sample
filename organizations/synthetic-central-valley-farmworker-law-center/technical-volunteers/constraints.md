---
type: volunteer-constraints
title: "synthetic-Central Valley Farmworker Law Center — Volunteer constraints & preferences"
description: "The org's own rules for technology volunteers, grounded in professional-responsibility obligations. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & preferences

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**. An agent scoping a project must treat these as non-negotiable — and here, more than in the collection's other bundles, that is literal: several of these are professional-responsibility obligations that the organization cannot waive even if it wanted to.

## Things that are not ours to negotiate

**Privilege is absolute.** Client communications and work product are privileged. A volunteer does not read case files. If a project cannot be done without access to privileged material, the project does not happen in that form — we will find another form or not do it. This is not a matter of trust in any individual; we do not have the authority to grant the access.

**No unauthorized practice of law.** Nothing built for us may give legal advice, assess the merits of a matter, tell a person what their rights are in their situation, or produce anything a person could reasonably mistake for advice from this office. That includes a chatbot, a triage form that says "you may have a claim," and an email autoresponder that says anything substantive. The line is not "is it accurate" — it is "does it constitute advice," and a correct answer given by a machine is still a problem.

**Conflicts screening happens before anything else.** Our case-management system does conflicts checking for a reason. No intake pathway may create a matter, contact a person about a matter, or generate a record that looks like a matter, before a conflicts check has run. A well-meaning automation that acknowledges an inquiry can conflict us out of representing someone.

**Deadlines are malpractice risk.** A missed statute of limitations is not a data-quality issue, it is harm to a client and exposure for the organization. Anything touching deadline tracking must fail loudly and never silently. If a system is uncertain whether a deadline was captured, it must behave as though it wasn't.

## On AI specifically

We are not opposed to it and we are not naive about it. The rules:

- **A model may draft; only a person decides.** Anything a model produces is a draft for a human to review, correct, and take responsibility for. No model output enters the case system, reaches a client, or informs a representation decision without a named person having approved it.
- **No merit assessment, no case scoring, no prioritization model.** We are oversubscribed and we ration, and those decisions are made by people who can be asked to justify them. A score would become the decision within a month, it would encode whatever is in its training data about which claims look real, and the people it would quietly deprioritize are the ones whose accounts are least tidy — which correlates with exactly the vulnerabilities that make someone need us most. Not built here.
- **No client-facing conversational anything.** See unauthorized practice above. Also: our clients' first contact with us is a decision they've weighed carefully, and a bot is a bad answer to it.
- **Client information does not go to a general-purpose model.** Any AI processing of client-derived content requires an arrangement with no training on inputs, no retention beyond processing, documented data handling, and a signed agreement. If that isn't available, we do it without AI.
- **Interpretation is a professional skill, not a translation task.** A machine rendering of a client's account into English is not a record of what they said and must never be treated as one. A mistranslated fact becomes a false statement in a filing, and the person who pays for it is the client.

## Working with us

- **Confidentiality agreement, signed, before anything.** Firm, no exceptions, and it is the control we actually rely on.
- **Least-privilege access, task-scoped.** Same standard we apply to new staff.
- **Background check** required for any role with access to client-adjacent systems, and for anyone present at intake.
- **Work from synthetic or pseudonymized data.** We can produce realistic non-client test data. Ask for it; do not develop against real matters.
- **Attorney availability is genuinely scarce.** Seven attorneys, 900 matters. Expect to work primarily with our operations staff and get attorney time in short, scheduled increments. A project needing sustained attorney attention needs to justify it.
- **Spanish is required** for anything involving contact with clients or presence at intake. For backend work it isn't, but you will understand the problem worse without it.
- **Handover:** no IT staff. Configuration over code, managed services over self-hosted, and documentation in plain language. Anything requiring a developer to maintain will decay and we will be worse off than before.

## What we would say no to, plainly

A volunteer who wants to build us a case-prediction model, an intake chatbot, or a "smart" prioritization queue. We have been offered all three. The answer is no, and the reason is in the AI section above, and we would rather say it here than in a meeting after someone has spent a month on it.
