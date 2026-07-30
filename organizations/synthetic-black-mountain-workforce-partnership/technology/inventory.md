---
type: technology-inventory
title: "synthetic-Black Mountain Workforce Partnership — Technology inventory"
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

**⚠ Synthetic — fabricated data. No transaction, order, or scan behind any line below.**

Each item carries its **provenance** — *how we know they have it*:

- **derived** — fingerprinted from their website/DNS. A guess, not confirmation.
- **acquired-via-TechSoup** — they got it through us. In a real bundle this is the one signal no one else has.
- **sourced-directly** — the org told us.

## Acquired through TechSoup

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2017 | Donated; ~14 staff seats. Also used to give participants a working email address, which matters more than it sounds |
| **Zoom** | Meetings / instruction | 2020 | Discounted; employer interviews, remote instruction, regional board meetings |
| **Bitdefender** | Endpoint security | 2019 | Staff machines and — importantly — the lending laptops |
| **Canva for Nonprofits** | Design | 2021 | Recruitment materials, employer one-pagers |
| **Refurbished laptops (34 cumulative)** | Hardware | 2018, 2021, 2024 | Three batches through the refurbished hardware programme. **The lending library.** See below |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| QuickBooks Online | Accounting | 2015 | Believed active; the organization uses a part-time bookkeeper |
| Asana | Project management | 2020 | Discounted; not evidently in use |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

### The lending library is doing four jobs and was designed for one

Thirty-four refurbished laptops over three batches, acquired so participants could complete coursework. About **22 are still in service**. What they are actually used for:

1. **Coursework** — the original purpose, still real.
2. **Job search and applications** — for participants with no home computer, which is a large share.
3. **Remote work, after graduation** — some graduates keep a laptop informally because they need one for the job they just got, and nobody has been willing to ask for it back. There is no policy covering this.
4. **Household use** — a laptop in a house with school-age children gets used for homework. Also not covered by any policy, and also not something the organization is inclined to police.

**Uses 3 and 4 are not in any grant agreement**, and they are arguably the highest-value things the hardware does. The organization is aware and has quietly decided not to look too hard.

Worth pulling out because it complicates a clean idea: the **acquired-via-TechSoup** lane is the strongest provenance signal available, and here it records *the acquisition accurately and the use not at all*. Order history says "34 laptops for participant coursework." Reality is a small circulating public computing resource in a county that lacks one. No provenance lane sees that. Somebody had to ask, and then be told candidly.

There are real risks in it: no asset tracking beyond a spreadsheet, no clear ownership boundary, PII on machines that leave, and no policy if one is lost or sold. The organization would rather have those risks than have the laptops sitting in a cupboard, which is a defensible position and one nobody has written down.

## Sourced directly — including the part that is infrastructure

| Technology | Category | Detail |
|---|---|---|
| **Graduate workstations (6)** | Public infrastructure | Desks and machines on the organization's good connection, so graduates can do remote jobs. See [README](../../../README.md) |
| **Business-grade internet** at the building | Infrastructure | Genuinely good — the reason the workstations work, and unusual for the county |
| **State workforce reporting portal** | Reporting — mandated | External, keyed by hand, the system of record for enrollment and placement |
| **Google Sheets** (many) | Everything else | Cohort tracking, employer contacts, wraparound disbursements, laptop inventory, retention attempts |
| Learning management — none | Instruction | Instruction is in person or over Zoom; no LMS |
| Participant records — see below | Records | There is no participant database. This is the project |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm whether the state portal offers any export, or whether reporting is a one-way hand-keying exercise.*

### There is no participant database

The organization's participant records are **spreadsheets**, one per cohort, structured slightly differently each time because whoever set up the cohort made their own copy of the last one.

Twelve staff, 190 enrollments a year, three funders with three definitions of a placement, and a state portal that must be keyed by hand. The **program director produces every report personally**, from spreadsheets, by hand, and it takes her about four days a quarter. She is also the person who would have to be replaced if she left, and nobody else can produce the federal report.

Compare [Motor City Trades](../../synthetic-motor-city-trades-institute/technology/inventory.md): three systems, none authoritative, and an abandoned Salesforce implementation. Same underlying problem — **the reporting environment demands more data structure than either organization has capacity to maintain** — arrived at from opposite directions. One accumulated systems it couldn't finish; the other never started and stayed in spreadsheets. Neither is doing it wrong given what they have.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Google Analytics | Analytics | derived |
| Mailchimp | Email marketing | derived |
| Online interest form | Intake | derived |
| Facebook page embed | Social | derived — **and it's the real front door** |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "low-moderate").*

The **Facebook embed** matters more than the website. In this county Facebook is where community information actually circulates, and the organization's page — not its site — is how most participants first hear about a cohort. A recommendation to invest in the website over the page would be pointed at the wrong channel, the same way a recommendation to improve [Valle Verde's](../../synthetic-valle-verde-food-network/technology/inventory.md) website misreads who that website is for.

## Known unknowns

- **Whether the state portal has an export.** Determines whether the volunteer project can close the loop or only feed the hand-keying. Nobody has asked.
- **Who owns the 12 laptops that aren't accounted for** out of 34. Some retired, some with graduates, some unknown. No asset system.
- **What PII is on the lending laptops** and whether anything is wiped between borrowers. Job applications contain a great deal about a person.
- **Whether the workstation facility is allowable** under the grants that pay for it. The organization believes so. Nobody has confirmed in writing, and it is the kind of thing a monitoring visit asks about.
- **What happens if the program director leaves.** Not a technology question, and it is the largest operational risk in this bundle.
- **Whether QuickBooks is on the organization's subscription or the bookkeeper's** — the same ambiguity as at [the partner clinic](../../synthetic-cumberland-gap-health-cooperative/technology/inventory.md), and a common pattern for small organizations with contract finance help.

## A derived signal worth acting on

The website's **interest form** posts to a shared inbox. For an organization whose real intake channel is Facebook and word of mouth, that is fine and low-stakes. What's worth ten minutes: confirming the form doesn't ask for a Social Security number or a conviction history, which intake forms sometimes do because somebody copied a template — and which would put sensitive data into an ordinary mailbox.

[^order-history]: Product order history (simulated)
[^org-staff]: Organization staff, directly (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
