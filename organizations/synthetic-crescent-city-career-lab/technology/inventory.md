---
type: technology-inventory
title: "synthetic-Crescent City Career Lab — Technology inventory"
description: "What the organization runs, each item tagged with how we know it. Fabricated."
tags: ["technology", "inventory", "synthetic"]
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

**⚠ Synthetic — fabricated data. No transaction, order, or scan behind any line below. And note that this bundle's [determination has expired](../verification.md).**

Each item carries its **provenance** — *how we know they have it*:

- **derived** — fingerprinted from their website/DNS. A guess, not confirmation.
- **acquired-via-TechSoup** — they got it through us. In a real bundle this is the one signal no one else has.
- **sourced-directly** — the org told us.

## Acquired through TechSoup

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2016 | Donated; ~24 staff seats plus a participant tier — see below |
| **Zoom** | Meetings / instruction | 2020 | Discounted; heavily used, because a working participant sometimes attends from a break room |
| **QuickBooks Online Plus** | Accounting | 2015 | Renewed continuously |
| **Bitdefender GravityZone** | Endpoint security | 2019 | Staff machines and the training lab |
| **Adobe Creative Cloud** | Design | 2019 | Two seats, comms |
| **Canva for Nonprofits** | Design | 2021 | Recruitment, employer materials |
| **Refurbished laptops (48 cumulative)** | Hardware | 2019, 2022, 2025 | Training lab plus a loan pool. Genuinely central to instruction |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Asana | Project management | 2019 | Discounted; superseded by Microsoft Planner |
| Tableau | Data visualization | 2022 | Nonprofit programme; **used in instruction**, which is unusual — see below |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

### An organization that teaches technology uses its own differently

Two things in this inventory are program infrastructure rather than overhead, and it changes how they should be read:

**The laptops are the classroom.** Forty-eight over three batches, in a training lab plus a loan pool for participants who need a machine at home to practise on. For most organizations in this collection, hardware supports the work. Here it *is* the work, and a laptop that fails is a seat that goes empty.

**Tableau is in the curriculum.** The data track teaches it. This is the only bundle in the collection where an acquired analytics tool is genuinely used — and it is used to *teach*, not to analyze the organization's own data. Compare the acquired-and-never-adopted Tableau lines at [Riverbend Air](../../synthetic-riverbend-air-alliance/technology/inventory.md) and [Motor City Trades](../../synthetic-motor-city-trades-institute/technology/inventory.md), and the fully-adopted mapping platform at [Gulf Corridor](../../synthetic-gulf-corridor-justice-project/technology/inventory.md).

**Four bundles, one product, four different fates**, and the order history records the same thing in each case. A corpus analysis inferring capability from acquisition would credit all four organizations with data-visualization capability. One teaches it, one uses a different tool for real work, and two have never opened it.

## Sourced directly

| Technology | Category | Detail |
|---|---|---|
| **Learning management system** | Instruction | Licensed commercially. Genuinely used — cohort content, assignments, participant progress |
| **Training lab** | Instruction | ~20 stations, refreshed in batches |
| **State workforce reporting portal** | Reporting — mandated | External, hand-keyed |
| **Participant tracking** | Records | In the LMS for progress; in spreadsheets for placement and wage data |
| **Employer contact records** | Development | A spreadsheet. See the caution in [programs](../programs.md) about what "employer partner" means |
| Microsoft 365 participant accounts | Identity | Participants get a working email address and cloud storage for the duration. Small thing, real effect |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm the LMS vendor and whether its progress data can feed the placement spreadsheets, which would remove a manual step.*

## The departed-staff problem, showing up twice

The development director who left in November 2025 is the reason [the verification determination lapsed](../verification.md) — the renewal notice went to her deactivated address and nobody else knew it was due.

**The same gap exists in the technology and nobody has audited it.** She was the administrator or the named account holder for an unknown number of things: the donor platform, at least two funder portals, the organization's registrations with two job boards, and probably some subscriptions on a card. Her Microsoft account was deactivated correctly. **External accounts registered to her work address were not, because nobody had a list.**

Worth flagging as a pattern rather than an incident. **An organization's account inventory is usually only discovered when someone leaves**, and the discovery is partial and reactive. The lapsed determination is one visible consequence of that; there are probably others nobody has found yet.

## Known unknowns

- **What external accounts were registered to the departed director's address.** Nobody has a list. This is the most tractable and most useful unknown in the bundle.
- **Whether the LMS can export progress data** into the placement tracking, or whether someone re-keys it.
- **Whether wage-gain data can be improved.** The organization gets it for about half of placements and would like more; whether that is a collection problem or an employer-cooperation problem is unknown.
- **Loan-pool laptop accountability** — 48 acquired, current disposition not tracked closely. The same gap as at [Black Mountain](../../synthetic-black-mountain-workforce-partnership/technology/inventory.md).
- **What is on returned laptops.** Participants practise on them, log into things, and hand them back. No documented wipe procedure.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Google Analytics | Analytics | derived |
| Mailchimp | Email marketing | derived |
| Online application form | Intake | derived |
| Calendly | Scheduling | derived |
| Cloudflare | CDN | derived |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "moderate").*

Unremarkable and appropriate. The site is a real intake channel for this organization — unlike [Valle Verde](../../synthetic-valle-verde-food-network/technology/inventory.md) or [Black Mountain](../../synthetic-black-mountain-workforce-partnership/technology/inventory.md), whose participants arrive by other routes. Career Lab's population is working adults with smartphones who search for training, so a functioning web application form is doing real work here.

## A derived signal worth acting on

The **online application form** collects date of birth and the last four digits of a Social Security number, apparently because the state reporting portal requires identifiers. That data is arriving by email into a shared inbox.

**Worth an hour of somebody's attention.** It is exactly the kind of thing that happens when a compliance requirement meets a website form and nobody thinks about the path in between — and it is a more concrete exposure than anything else in this inventory.

[^order-history]: Product order history (simulated)
[^org-staff]: Organization staff, directly (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
