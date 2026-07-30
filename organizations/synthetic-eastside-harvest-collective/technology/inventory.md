---
type: technology-inventory
title: "synthetic-Eastside Harvest Collective — Technology inventory"
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

## Acquired through TechSoup

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers** — there is no transaction behind these, and a fabricated order number invites someone to go looking for it.*

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2022 | Donated; ~12 seats |
| **QuickBooks Online** | Accounting | 2019 | Renewed annually since |
| **Canva for Nonprofits** | Design | 2023 | Used heavily for distribution-day signage and social |
| **Zoom** | Meetings | 2021 | Discounted; board and funder calls |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Bitdefender | Endpoint security | 2022 | Discounted; unclear whether renewed |
| Asana | Project management | 2020 | Discounted; the team appears to have drifted to a shared spreadsheet |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated). In a real bundle these would be transactions rather than inferences, and high confidence. Currency of the "previously acquired" items is not tracked in this record.*

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Google Workspace (Gmail) | Email | derived |
| Mailchimp | Email marketing | derived |
| Square | Payments (market sales) | derived |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "low-moderate").*

## The contradiction the fingerprint exposes

Look at the two tables together. The TechSoup history says **Microsoft 365 Business Premium**, donated, twelve seats. The website fingerprint says **Google Workspace (Gmail)** for mail.

Both are probably true. That means the organization has **two productivity suites and two identity systems**, is very likely paying attention to only one of them, and has staff accounts, files, and calendars split across both. Nobody chose this — it's what happens when an organization gets a donated suite while its email is already somewhere else and there is no IT person to finish the move.

This is the single most useful thing in this bundle, and it's only visible because two provenance lanes disagree. A website scan alone would have missed the Microsoft tenancy entirely. Order history alone would have missed that mail never moved. It is the basis of the [volunteer project](../technical-volunteers/index.md).

## Known unknowns

- **No CRM or donor database** is evidenced anywhere — not in the TechSoup history, not in the fingerprint. For a $1.4M-to-$2M organization with individual donors, that is either a spreadsheet doing a CRM's job or a system nobody has told us about. Confirm before assuming either.
- **Program data lives in Airtable**, according to the org's own materials, but Airtable does not appear in the TechSoup history and would not show up in a website scan — so it is **sourced-directly** and unverified. The volunteer project depends on it, so step zero is confirming it.
- **No harvest-weight tracking system** is evidenced. Pounds grown and pounds distributed appear to be recorded on paper at the sites and typed up later, which is the reporting problem the volunteer project exists to solve.

## A derived signal worth acting on

The site fingerprint flagged **an out-of-date WordPress installation** with at least two plugins well behind current, and **no MFA enforced** on the Google Workspace domain. Both are *derived* — confirm first — but a lapsed WordPress with a payment-adjacent audience is a concrete basis for a future volunteer request, separate from the one already scoped.

[^order-history]: Product order history (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
