---
type: technology-inventory
title: "synthetic-Fundacja Prawo i Schronienie — Technology inventory"
description: "What the organization runs, each item tagged with how we know it — including what the donated catalogue does not reach. Fabricated."
tags: ["technology", "inventory", "synthetic", "poland", "gdpr"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: order-history
    resource: "simulated donated-and-discounted product order history"
    title: "Product order history (simulated)"
    author: process:order-history
    last_modified: 2026-06-30
  - id: org-staff
    resource: "simulated conversation with organization staff"
    title: "Organization staff, directly (simulated)"
    author: human:org-staff
    last_modified: 2026-03-02
  - id: web-fingerprint
    resource: "simulated website and DNS fingerprint"
    title: "Website/DNS fingerprint (simulated)"
    author: process:web-fingerprint
    last_modified: 2026-07-01
x-civic:
  profile: civic/0.6
---

# Technology inventory

**⚠ Synthetic — fabricated data. No transaction, order, or scan behind any line below.**

Each item carries its **provenance** — *how we know they have it*:

- **derived** — fingerprinted from their website/DNS. A guess, not confirmation.
- **acquired-via-TechSoup-network** — obtained through the TechSoup Global Network partner serving Poland. Note the lane name differs from the US bundles, deliberately.
- **sourced-directly** — the org told us.

## The catalogue is different, and the clearest example is accounting

**QuickBooks does not appear in this inventory and cannot.** It is a US-only product. Neither can several other things that show up routinely in the twelve US bundles here.

What this organization does instead: **it bought Polish accounting software commercially, at full price.** The software has to handle Polish accounting standards, Polish VAT, ZUS social-insurance contributions, and the specific reporting that OPP status imposes — none of which a US product does. There was never a donated option, so there was never a decision to make.

The general point is worth stating plainly because it is easy to miss from a US vantage:

**Donated-software availability is not global, and it is least global exactly where local requirements are strongest.** Productivity, security, and design tools travel well — they do the same thing everywhere. **Accounting, payroll, HR, and compliance software is jurisdiction-specific**, so it is both the category a small NGO most needs help with and the category the donation catalogue is least able to serve. A Polish NGO gets a donated office suite and pays commercial rates for the thing that has to know about ZUS.

Anyone comparing "technology acquired through TechSoup" across countries should expect the international organizations to show **thinner and differently-shaped** order histories, and should not read that as lower engagement or lower capacity.

## Acquired through the TechSoup network (Poland)

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2019 | Donated; ~24 seats. **Configured for EU data residency** — see the GDPR section |
| **Bitdefender GravityZone** | Endpoint security | 2020 | All devices, full-disk encryption enforced |
| **Zoom** | Meetings / remote hearings | 2021 | Discounted |
| **Canva for Nonprofits** | Design | 2022 | Information materials in Polish, Ukrainian, and Russian |
| **Adobe Acrobat Pro** | Documents | 2021 | Legal practice; heavy use |

**Previously acquired:**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Refurbished laptops (12) | Hardware | 2022 | During the 2022 surge, when the organization tripled its staff in months |

*Provenance: **acquired-via-TechSoup-network**[^order-history] (simulated).*

## Bought commercially — and this is the larger half

| Technology | Category | Detail |
|---|---|---|
| **Polish accounting and payroll software** | Finance | Commercial. Handles Polish standards, VAT, ZUS, and OPP reporting. **No donated option exists** |
| **Legal case management** | Practice | Commercial, EU-hosted. Matters, deadlines, conflicts |
| **Sworn/specialist interpretation services** | Language access | Contracted, per-hearing. A real budget line and a bottleneck |
| **Signal** | Sensitive communication | Deliberate, for client contact where it is appropriate |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm the case management vendor's hosting location and its data-processing agreement — material to the volunteer project.*

## Where GDPR changes the answers

**This section has no equivalent in the twelve US bundles**, and it contains this organization's most significant exposure.

### What is in decent shape

- **Microsoft 365 is configured for EU data residency**, which someone thought about deliberately. Better than the unreviewed tenancies at [the California Law Center](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md) and [Sierra Foothills](../../synthetic-sierra-foothills-community-health/technology/inventory.md).
- **Case management is EU-hosted** with a data-processing agreement on file.
- **Endpoint encryption** is enforced.
- **A data protection officer is designated** — a staff lawyer holding it alongside a caseload, which is common and not ideal.

### What is not

- **No records of processing.** GDPR requires a record of processing activities, and the organization does not have a current one. This is a documented obligation, unmet.
- **Lawful basis is not documented per category.** The organization has reasonable practices and has not written down which basis covers what — a distinction that matters when a regulator or a data subject asks.
- **Special category data is handled without a specific assessment.** Asylum matters routinely involve health data, religious belief, ethnic origin, and sexual orientation, all of which carry a higher bar. The organization holds them appropriately in practice, without the assessment the higher bar implies.
- **The website transfers personal data outside the EEA.** See below. **This is the concrete problem.**
- **No data protection impact assessment** for the high-risk processing this organization plainly does.
- **Retention is not defined per data category** — only broadly, by professional obligation.

### The website is the sharp edge

The public site — see the fingerprint table below — runs **US-based analytics** and posts its **contact and advice-request forms through a US-based form processor**. The forms are how a person in the asylum procedure first contacts the organization, and they collect name, contact details, nationality, and a free-text description of the person's situation.

So: **personal data, including special category data, about applicants for international protection, is being transferred to a US processor**, apparently without a transfer mechanism anybody has assessed, and with a cookie banner that does not actually gate the analytics script.

Three reasons this is worse than the equivalent finding in a US bundle:

**It is unlawful, not merely unwise.** Transfers outside the EEA require a valid mechanism and an assessment. Absent those, this is a compliance breach with a supervisory authority that can act on it.

**The data subjects are exactly the people for whom exposure is most consequential.** An asylum applicant's account of persecution, sitting in a third-country processor's logs.

**Nobody chose it.** The site was built in 2021 by a contractor who used ordinary tools. The analytics and the form processor are the defaults of the web industry, and the defaults of the web industry are American.

That last point generalizes past this bundle: **an EU nonprofit that builds a website the normal way ends up non-compliant by default**, because the normal way means US-hosted services. It takes deliberate work not to.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| US-based analytics platform | Analytics | derived — **transfer problem** |
| US-based form processor | Intake forms | derived — **transfer problem, and it carries special category data** |
| Cookie consent banner | Consent | derived — **present but does not gate the analytics script** |
| Cloudflare | CDN | derived |
| Content in Polish, Ukrainian, Russian, English | Content | derived — genuinely multilingual, well done |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "moderate").*

**Note what a US-shaped assessment would say about this site**: WordPress, analytics present, forms working, CDN configured, multilingual content, cookie banner in place. That reads as a competently-built site — arguably better than several US bundles here. **The assessment has no reason to flag anything, and the site is the organization's largest compliance exposure.** A maturity rubric built in one jurisdiction cannot see a legal problem that only exists in another.

## Known unknowns

- **Whether any transfer mechanism exists** for the analytics and form processor. Probably not, and it needs establishing rather than assuming.
- **What is in the form processor's stored submissions**, going back to 2021, and whether it can be exported and deleted.
- **Whether the case management vendor's DPA covers sub-processors** and where they are.
- **How the DPO role is actually resourced.** A staff lawyer with a caseload holding a compliance function is a title more than a capacity.
- **Retention in practice** versus retention as professional obligation.
- **What happened during the 2022 surge.** The organization tripled staff in months under emergency pressure. Nobody has audited what data practices were adopted then and never revisited — and that is the period covering the largest client group in the bundle.

## A derived signal worth acting on

**The multilingual content is genuinely good** — Polish, Ukrainian, Russian, and English, maintained rather than machine-translated once. That is unusual and it is the site's real strength.

The action is everything in the GDPR section, and the order matters: **stop the ongoing transfer first**, then document, then assess. A volunteer who begins with the records of processing will produce useful paperwork while special category data continues to flow to a US processor every day.

[^order-history]: Product order history (simulated)
[^org-staff]: Organization staff, directly (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
