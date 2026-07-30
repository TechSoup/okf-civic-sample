---
type: technology-inventory
title: "synthetic-Valle Verde Food Network — Technology inventory"
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
| **Microsoft 365 Business Premium** | Productivity / identity | 2018 | Donated; ~22 seats. Office staff use it fully; **route staff barely touch it** |
| **QuickBooks Online Plus** | Accounting | 2016 | Renewed annually |
| **Zoom** | Meetings | 2020 | Discounted; funder and coalition calls |
| **Canva for Nonprofits** | Design | 2021 | Route flyers, though see the note on written materials below |
| **Bitdefender** | Endpoint security | 2019 | Office machines |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Microsoft Surface tablets (4) | Hardware | 2021 | Refurbished hardware program — **acquired for route data capture, now in a drawer.** See below |
| Mailchimp | Email marketing | 2019 | Superseded by Constant Contact per the website fingerprint; one of them is dormant |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

### The four tablets in a drawer

In 2021 the organization acquired four refurbished tablets specifically so route coordinators could capture household counts digitally instead of on paper. They were used for about six weeks.

They failed for a reason nobody checked first: **the software they were meant to run required a connection to save.** On a route with no signal, a coordinator would enter twenty households, hit a dead zone, and lose the entry. After the second time that happened, the coordinators went back to paper, and they were right to. The tablets are in a drawer in the warehouse office.

This is the most instructive line in the bundle. The hardware was appropriate, free, and useless, because the assumption underneath the software was wrong. **Any project proposing to digitize route capture has to answer this failure first** — see the [volunteer project](../technical-volunteers/index.md), which does.

## Sourced directly — the systems that actually run the operation

None of this came through TechSoup and none of it is visible to a website scan.

| Technology | Category | Detail |
|---|---|---|
| **Paper route sheets** | Route data capture | The real system. Clipboard per route, tallied at the warehouse, keyed in up to two weeks later |
| **WhatsApp** | Coordination — **load-bearing** | See below. The organization's actual nervous system |
| Food-bank client management platform | Inventory / distribution reporting | Used for warehouse inventory and state reporting; **not** used on routes |
| Google Sheets | Route scheduling, volunteer rosters, water-distribution logs | Several, owned by different staff |
| Four vehicles with no telematics | Logistics | Route timing is estimated, not measured |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm the client-management platform's name and plan, and whether the state reporting export actually works or is re-keyed.*

### WhatsApp is infrastructure here, and nobody chose it

The eleven promotoras, the four route coordinators, and most of the volunteer base coordinate on **WhatsApp**. Route changes, vehicle breakdowns, a community reporting that the water delivery didn't arrive, a family that needs a box held back — all of it moves through WhatsApp groups. It works because it is on everyone's phone already, it survives bad connectivity better than nearly anything else, and it handles voice messages, which matters enormously given the [language and literacy picture](../population.md).

It is also, by any ordinary standard, an unmanaged system holding operational information on personal devices with no retention policy, no organizational account, no export, and no continuity plan if the person who administers a group leaves. Both of those paragraphs are true.

**The honest position for anyone advising this organization: do not try to replace it.** Every alternative is worse on the dimensions that made WhatsApp win — voice, reach, resilience, and being already installed. The useful work is at the edges: making sure the groups have more than one admin, that critical decisions don't only exist in a chat thread, and that the organization has thought about what's in there. A volunteer project that proposes migrating this to a "proper" tool has misread the situation.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Constant Contact | Email marketing | derived |
| Google Analytics | Analytics | derived |
| Google Translate widget | Accessibility | derived — **and worth a look** |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "low-moderate").*

The **Google Translate widget** deserves a note. It's a common, well-intentioned addition, and for this organization's population it does close to nothing: it translates to Spanish adequately, does not handle **Mixtec or Triqui** meaningfully, and is text-to-text, which misses the literacy issue entirely. Not harmful. Just a solution shaped for a different problem than this organization has.

## Known unknowns

- **Whether the client-management platform's state export works.** If it doesn't, someone is re-keying, and nobody documented that.
- **What is in the WhatsApp groups.** Almost certainly some household-specific information shared in the course of coordinating a hold-back or a delivery. The organization's no-identifiers policy is real for its records; whether it holds in a chat thread is unexamined.
- **Route timing.** No telematics, so the two-week cycle is planned from experience rather than measured. The organization suspects two routes are badly balanced and cannot demonstrate it.
- **Whether the four tablets still charge.** Five years in a drawer.
- **Backup of the Google Sheets** that hold water-distribution logs — the closest thing the organization has to a compliance record for the water program.

## A derived signal worth acting on

The site is functional and unremarkable, which for this organization is the right outcome — its audience is funders and packing-house partners, not the communities it serves. The communities are reached by promotoras and WhatsApp. A recommendation to "improve the website to better reach beneficiaries" would be advice for a different organization, and it's the kind of thing an automated assessment produces when it doesn't know who the website is for.

[^order-history]: Product order history (simulated)
[^org-staff]: Organization staff, directly (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
