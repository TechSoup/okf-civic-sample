---
type: technology-inventory
title: "synthetic-Motor City Trades Institute — Technology inventory"
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
- **acquired-via-TechSoup** — they got it through us. In a real bundle this is the one signal no one else has.
- **sourced-directly** — the org told us.

## The three systems problem

Before the tables, the finding, because the tables don't make it obvious on their own.

**Three systems hold pieces of the same participant's record, and none of them is authoritative:**

| System | Holds | Who uses it | Status |
|---|---|---|---|
| **Legacy participant database** (desktop, single-machine, ~2009) | Intake, attendance, completion, conviction-history fields | Program staff, 2 people who know it | Running. Nobody wants to touch it |
| **Salesforce** (Nonprofit Success Pack) | Partial contact records, some 2022–2023 enrollments, employer relationships | Development staff, partially | **Implementation abandoned mid-project, 2023** |
| **Spreadsheets** (shared drive, several) | Placement outcomes, three-year retention follow-up, wraparound disbursements | One staff member each | The de-facto authority for anything about outcomes |

Plus a **fourth, external**: the state workforce reporting portal, which the organization must key data into by hand and which is the only place a genuinely reconciled version of enrollment exists — held by someone else.

So the organization's most important claim — *is this graduate still in the trade three years later* — lives in a spreadsheet on a shared drive, maintained by one person, reconstructed partly from phone calls and social media. And its most sensitive data — conviction histories — lives in a seventeen-year-old desktop database on a single machine.

That is the whole picture. Everything below is detail.

## Acquired through TechSoup

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2017 | Donated; ~40 seats. Genuinely the organization's identity backbone |
| **QuickBooks Online Advanced** | Accounting | 2014 (Desktop), migrated 2021 | Renewed continuously; a real audit runs off it |
| **Zoom** | Meetings | 2020 | Discounted; employer interviews and remote bridge sessions |
| **DocuSign** | E-signature | 2021 | Enrollment paperwork, employer agreements. Heavy use |
| **Bitdefender GravityZone** | Endpoint security | 2019 | Renewed; covers office machines, **not** the legacy database machine |
| **Adobe Creative Cloud** | Design | 2018 | Single seat, comms staff |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Salesforce (Nonprofit Success Pack) | CRM | 2022 | Donated 10 seats — **implementation abandoned**, see above |
| Asana | Project management | 2019 | Discounted; superseded by Microsoft Planner, likely dormant |
| Tableau | Data visualization | 2023 | Nonprofit program; used once for a board presentation |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated). Note how much this lane gets right and how much it misses: it correctly shows a well-equipped organization, and it would let you conclude the organization has a working CRM. It does not.*

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Constant Contact | Email marketing | derived |
| Salesforce Web-to-Lead form | CRM intake | derived — **and this is the trap** |
| Calendly | Scheduling | derived |
| Google Analytics | Analytics | derived |
| Google Tag Manager | Tag management | derived |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "moderate-high").*

### The fingerprint's most confident wrong answer

The website carries a live **Salesforce Web-to-Lead form**. A fingerprint sees that and concludes, reasonably, that this organization runs Salesforce as its CRM. Order history agrees — ten donated seats, 2022.

Both signals point the same direction, they corroborate each other, and **they are both wrong**. The implementation stopped in 2023. The form still posts into an org nobody works in; inquiries submitted through the website land in a queue that is checked, when it is checked, by someone going in specifically to look. Program staff work in the legacy database. Outcomes live in spreadsheets.

This is the most useful test case in the bundle. Two independent provenance lanes agreeing is normally the strongest signal available, and here it produces a confident, corroborated, false conclusion. **Only sourced-directly catches it** — someone had to ask. If you are weighting provenance lanes, this is the case that argues against treating agreement as truth.

## Known unknowns

- **Whether the legacy database is backed up.** It runs on one machine. It contains conviction histories for thousands of people. Bitdefender coverage explicitly does not extend to it. Nobody could say whether a backup exists or when it was last tested. **This is the most serious risk in any bundle in this collection.**
- **Who has access to the conviction-history fields.** No access-control documentation. In a single-machine desktop database, "access control" plausibly means who knows the password.
- **What the state portal expects, in writing.** Reporting definitions are held as staff knowledge. When the person who does the keying is out, the reporting stops.
- **Whether the Salesforce org can be recovered or should be started over.** Material to the volunteer project and unanswerable from outside.
- **Retention policy for participant records.** None evidenced. An organization holding conviction histories with no retention schedule is keeping them forever by default.

## A derived signal worth acting on

The WordPress installation is current and reasonably maintained — unusually, this organization's public-facing technology is in better shape than its internal systems. The site's live **Salesforce form is the exception**: it is collecting real inquiries from real people into a system nobody monitors. That is a small fix with an immediate benefit, and it is the kind of thing that goes unnoticed for years precisely because the form works.

[^order-history]: Product order history (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
