---
type: verification
title: "synthetic-Fundacja Prawo i Schronienie — Eligibility & verification"
description: "The organization's simulated verification determination, kept as a log. Approved — via a registry more machine-readable than the American one."
tags: ["eligibility", "verification", "determination", "synthetic", "poland"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
verified: { by: process:airt-simulated, at: 2026-05-28T00:00:00Z }
stale_after: 2027-05-28
sources:
  - id: determination
    resource: "simulated validation determination, workspace SYNTH-WORKSPACE-0013"
    title: "Validation determination (simulated)"
    author: process:airt-simulated
    last_modified: 2026-05-28
  - id: registry
    resource: "simulated registry extract"
    title: "Registry record (simulated)"
    author: process:registry-import
    last_modified: 2026-01-15
x-civic:
  profile: civic/0.6
---

# Eligibility & verification

**⚠ Synthetic — this determination was never made. It is fabricated to give the record a realistic shape.**

A **log**, written by the validation system. Each re-validation appends a new entry; nothing is overwritten. Everyone else reads this file; only the validation system writes it. Edit history for the *bundle* is separate — see [log](log.md).

## Current status: **ELIGIBLE**

## Determination v1 — 2026-05-28

**APPROVE**, 92% confidence (HIGH).

**What was checked, and note that none of it is an IRS record:**

- **KRS registration confirmed** — entity existence, legal form (*fundacja*), registered address, statutory purpose, and **named board and supervisory-board members**, all from the public National Court Register.
- **NIP and REGON confirmed** against the respective registers.
- **OPP status confirmed** on the current public list of public benefit organizations, including the reporting obligations that status carries.
- **Filed annual financial statements reviewed** — publicly available through the KRS repository.
- **Compliance screening** (OFAC, PEP, debarment, adverse media, FATF, sanctions) cleared with no matches. **EU sanctions lists checked in addition**, which the US bundles do not require.

## The finding worth recording: this was easier than the American cases

**It would be reasonable to expect a non-US organization to be harder to verify. For Poland it is easier.**

The KRS is a **public court register** with an online search interface, structured entity records, and filed financial statements in a repository. Board members are named as a matter of registration rather than as a matter of the organization's own disclosure. OPP status is a current public list. Almost everything a verification process wants exists in a retrievable, structured, authoritative form.

Set against the US bundles in this collection:

| Organization | Governance evidence | Financial evidence | Confidence |
|---|---|---|---|
| **This one** (Poland) | Named in the public court register | Filed statements in a public repository | **0.92** |
| [Frogtown Table](../synthetic-frogtown-community-table/verification.md) (US) | Minutes in a folder in an office | Bookkeeper, board review, no audit | 0.88 |
| [Cumberland Gap Health](../synthetic-cumberland-gap-health-cooperative/verification.md) (US) | Minutes on paper | Financial review, no audit | 0.90 |

**The mechanism is the registry, not the country.** Poland requires foundations to file more, publicly, in a structured form, than US law requires of a small 501(c)(3). That is a fact about administrative regimes.

This matters because the collection's third international bundle, [Nyando in Kenya](../synthetic-nyando-community-health-trust/verification.md), is **genuinely difficult to verify** and receives a determination of insufficient evidence. Read together, the two international bundles say something more useful than either alone: **verifiability tracks the information environment an organization sits in, and that varies enormously between countries in both directions.** A collection with one international example would have taught a simpler and wronger lesson.

## Scope limitations

**Case-level information: not examined — professional secrecy.** Polish obligations binding *radcowie prawni* and *adwokaci*. Functionally the same limit as the attorney-client privilege boundary at [the California Law Center](../synthetic-central-valley-farmworker-law-center/verification.md), arriving through different legal architecture.

Worth stating for schema purposes: **"privileged" is a US term of art and does not port.** The protection exists in most jurisdictions under different names with different scope. A boolean field asserting `privileged: true` is embedding an American framework, and a bundle format meant to be international needs a more neutral way to say "this cannot be examined, for reasons of legal professional obligation."

**GDPR compliance: not assessed.** The organization's data-protection posture was not evaluated, and this is a real gap rather than a boundary — see [inventory](technology/inventory.md), where the volunteer project exists because there are genuine questions about records of processing and cross-border transfers. A verification process shaped around US organizations has no step for it, and for an EU organization it is a compliance question with regulatory consequences.

**Noted:** part of the organization's individual support arrives through the **1% tax designation** mechanism, for which there is no donor record. Not an eligibility question; relevant to anyone modelling its finances.

- **Next re-validation due:** 2027-05-28.

*Provenance: **mechanical**[^registry] (simulated), distilled from a fabricated determination. In a real bundle the full screening battery would live in the workspace record — here that pointer is the invented id `SYNTH-WORKSPACE-0013`.*

<!-- Next re-validation (due 2027-05-28) appends here as "## Determination v2 — …". -->

[^determination]: Validation determination (simulated)
[^registry]: Registry record (simulated)
