---
type: technology-inventory
title: "synthetic-Riverbend Air Alliance — Technology inventory"
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
| **Microsoft 365 Business Basic** | Productivity / email | 2019 | Donated; ~9 seats. The whole staff is here — no second suite in this org |
| **Zoom** | Meetings | 2020 | Discounted; used for hearings, coalition calls, and youth corps sessions |
| **Canva for Nonprofits** | Design | 2022 | Advisory graphics and hearing handouts |
| **Adobe Creative Cloud** | Design / mapping graphics | 2021 | Discounted; used for the printed corridor maps |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Malwarebytes | Endpoint security | 2021 | Discounted; renewal status unclear |
| Tableau | Data visualization | 2023 | Nonprofit program; **acquired, then never adopted** — see below |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

### The Tableau line is the interesting one

An organization acquired a serious data-visualization tool in 2023 and **never used it**. Its public map runs on something else entirely, and its board reporting is done in spreadsheets. Nobody did anything wrong; a capable tool arrived, the person who wanted it left or got busy, and there was no one to carry it.

This is a pattern worth being able to see across a corpus: **acquisition is not adoption**, and order history alone will confidently tell you an organization has a capability it does not have. Anything reading `acquired-via-TechSoup` as evidence of a working capability will get this one wrong. It's here so you can test that.

## The sensor network — sourced-directly, and the actual core

This is the organization's program infrastructure. None of it came through TechSoup and none of it is visible to a website scan, so it is **sourced-directly** and effectively invisible to both of the other provenance lanes.

| Component | Count | Detail |
|---|---|---|
| Low-cost particulate sensors (PM2.5/PM10, commodity type) | 31 | Host-sited on residents' homes; wifi-connected, mains-powered |
| Single-board-computer gateways | 4 | Aggregate readings where host wifi is unreliable |
| Reference co-location site | 0 | **None.** No calibration against a regulatory-grade monitor — see [README](../../../README.md) |
| Public map / dashboard | 1 | Third-party hosted service tied to the sensor vendor's platform |
| Historical data archive | partial | Roughly 2019 onward, with gaps; storage arrangement undocumented |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm counts, vendor platform, and — most importantly — **where the historical data actually lives and who can retrieve it**.*

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| Squarespace | Website / CMS | derived |
| Mailchimp | Email marketing | derived |
| Embedded third-party map widget | Data display | derived |
| Google Analytics | Analytics | derived |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "moderate").*

## What the three lanes together reveal

Each lane alone gives a wrong impression, and the disagreement is the finding:

- **Order history alone** says: a reasonably equipped small nonprofit with Microsoft 365, Adobe, and a data-visualization platform. Sounds capable.
- **Website fingerprint alone** says: a Squarespace site with an embedded map widget. Sounds like a communications shop.
- **Sourced-directly** says: 31 field sensors, four gateways, no calibration, an undocumented data archive, and a program that lives or dies on a vendor platform nobody has a contract note for.

Only the third lane describes what this organization actually is, and it is the only lane that requires someone to *ask*. Worth remembering when weighing how much of a corpus can be built from signals that arrive automatically.

## Known unknowns

- **Where the historical data lives.** Roughly seven years of readings, described as archived, with no documented storage location, owner, or export path. If the vendor platform changed terms tomorrow, it is not clear the organization could retrieve its own evidence. This is the most serious unknown in the bundle.
- **No alerting on sensor failure.** Dead sensors appear to be discovered by someone noticing a flat line on the map, which means the gap in the record is already permanent by the time anyone knows. Directly the subject of the [volunteer project](../technical-volunteers/index.md).
- **No CRM.** Donors, sensor hosts, youth corps families, and hearing attendees appear to be tracked in separate spreadsheets. Sensor-host records include home addresses, which makes the spreadsheet question a data-protection question.
- **No data-retention or host-privacy policy** is evidenced, despite the organization holding 31 residential addresses tied to environmental readings.

## A derived signal worth acting on

The site fingerprint flagged **no privacy policy** on a site that publishes a map derived from data collected at private residences. The addresses themselves are not published, but the map's spatial resolution is fine enough that a determined reader could narrow a sensor to a block. *Derived* — confirm first — but it is a live question for an organization whose hosts volunteered a porch, not a public record.

[^order-history]: Product order history (simulated)
[^org-staff]: Organization staff, directly (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
