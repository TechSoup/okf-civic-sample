---
type: technology-inventory
title: "synthetic-Corporación Río Vivo — Technology inventory"
description: "What the organization runs, each item tagged with how we know it — in a context where a location dataset is a safety question. Fabricated."
tags: ["technology", "inventory", "synthetic", "colombia", "security"]
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
- **acquired-via-TechSoup-network** — obtained through the TechSoup Global Network partner serving Colombia.
- **sourced-directly** — the org told us.

## What is deliberately not written down

**This section comes first because it is the most important part of the inventory, and because an inventory that only lists what exists would misrepresent this organization entirely.**

Things Río Vivo deliberately does **not** keep in any shared or digital system:

| Not recorded | Why |
|---|---|
| **Community monitor names alongside monitoring points** | Together they identify who will be where. Held compartmentalized — the accompaniment staff know their own communities' monitors and no central list exists |
| **Sampling schedules in advance** | A schedule is a location and a time for a named person. Communicated verbally or over Signal, close to the date, not stored |
| **Full-precision coordinates in circulating documents** | Reduced precision in anything that leaves the organization or moves between systems |
| **Community meeting attendance lists** | Who attended and who spoke. Notes record decisions, not attributions |
| **Anything about security incidents in cloud systems** | Threats received, protective measures, travel plans. Paper and in-person only |

**Every one of those absences would be scored as a data-management deficiency by a standard assessment.** All five are deliberate protective decisions made by an organization whose partners are in genuine physical danger.

This is the fourth bundle in this collection where absence is sophistication rather than immaturity — after [the California Law Center](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md), [North Star](../../synthetic-north-star-immigrant-defense/technology/inventory.md), and [Valle Verde](../../synthetic-valle-verde-food-network/technology/inventory.md) — and it is the one where getting it wrong has the worst consequences.

## Acquired through the TechSoup network (Colombia)

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2019 | Donated; ~19 seats. Used for administration; **not** for anything sensitive |
| **Bitdefender GravityZone** | Endpoint security | 2020 | All devices, full-disk encryption enforced. Genuinely load-bearing here |
| **Zoom** | Meetings | 2021 | Discounted; funder and coalition calls |
| **Canva for Nonprofits** | Design | 2022 | Community education materials in Spanish |
| **QGIS-adjacent mapping tooling / geospatial** | Geospatial | 2021 | Nonprofit programme. Used with deliberate precision limits |

**Previously acquired:**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Refurbished laptops (8) | Hardware | 2020, 2023 | Field and office use |

*Provenance: **acquired-via-TechSoup-network**[^order-history] (simulated).*

**No QuickBooks — it is a US-only product.** As in [the Polish bundle](../../synthetic-fundacja-prawo-i-schronienie/technology/inventory.md), the organization bought accounting software commercially, because Colombian accounting has requirements a US product does not meet: **DIAN electronic invoicing**, *retención en la fuente*, and the annual reporting that RTE status requires.

**Three countries, the same finding.** Productivity, security, and design software travels internationally through the donation catalogues. **Accounting, payroll, and compliance software does not**, because it is jurisdiction-specific — and that is precisely the category a small NGO most needs help with. Any analysis comparing TechSoup order histories across countries should expect the international organizations to look thinner, and should not read that as lower capacity.

## Sourced directly

| Technology | Category | Detail |
|---|---|---|
| **Signal** | All sensitive communication | The organization's actual nervous system. Disappearing messages by default. **Not a preference — a protective measure** |
| **Commercial Colombian accounting software** | Finance | DIAN electronic invoicing, retención, RTE reporting. No donated option |
| **Community monitoring records** | Field data | **Owned by the eleven community organizations.** Held under agreements. See [README](../../../README.md) |
| **Field instruments** | Monitoring | Portable water-quality meters, community-operated |
| **Accredited laboratory** | Verification | Contracted, periodic. The budget constraint on how much verified data exists |
| **Paper** | Security matters, sensitive meeting records | Deliberate. See above |
| Case and action tracking | Legal | A modest system for administrative and legal actions |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm the connectivity situation on the tributaries and whether the geospatial tooling's precision limits are documented practice or one staff member's habit.*

### Connectivity

Field areas on both tributaries have **poor and intermittent mobile coverage.** Community monitors record readings on paper and report by phone or Signal when they reach signal, sometimes a day or more later.

The same constraint appears in [Fresno County](../../synthetic-valle-verde-food-network/technology/inventory.md), [Letcher County](../../synthetic-cumberland-gap-health-cooperative/technology/inventory.md), and [the Sierra Foothills mobile unit](../../synthetic-sierra-foothills-community-health/technology/inventory.md) — four organizations on three continents, four paper workarounds, and in each case paper is the competent response to an absent network rather than evidence of backwardness.

**Here it has an additional advantage nobody planned:** paper does not synchronize, so a monitor's readings are not automatically creating a timestamped location record in a cloud system.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Cloudflare | CDN / DDoS protection | derived — **the site is attacked** |
| No analytics | — | derived — deliberate |
| No monitoring-point map published | — | derived — **deliberate, and the important one** |
| Aggregated findings only | Content | derived |
| Spanish only | Content | derived — appropriate; the audience is Colombian |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "low-moderate" — and, as elsewhere, misleading).*

### The map that is not there

The two coalition partners both publish maps. [Riverbend Air](../../synthetic-riverbend-air-alliance/technology/inventory.md) publishes sensor locations on a public map. [Gulf Corridor](../../synthetic-gulf-corridor-justice-project/technology/inventory.md) publishes facility and sampling locations. Both are good practice: transparency, verifiability, community access.

**Río Vivo does not, and must not.** A map of monitoring points in contested rural territory, in this country, is a map of where defenders work.

An automated assessment sees a missing feature that both peer organizations have. A benchmarking exercise across the coalition would flag this organization as lagging its partners. **The correct reading is that it is the one making the right decision for its context**, and no signal available from outside distinguishes those two readings.

## Known unknowns

- **Whether the geospatial precision limits are documented** or are one staff member's practice. If practice, they leave when she does. **Most tractable and most valuable unknown in the bundle.**
- **What is in the Microsoft 365 tenancy that shouldn't be.** The organization's policy is that sensitive material stays out. Nobody has audited whether it holds.
- **Whether community agreements are written**, for all eleven, and whether they say the same things. The data-sovereignty arrangement is the organization's most important governance structure and may be partly informal.
- **Ley 1581 obligations** — whether database registration and authorization requirements have been addressed.
- **What happens to community data if the organization closes.** No documented succession, and eleven communities' records are involved.
- **Whether any funder has ever received underlying data**, and under what authorization.

## A derived signal worth acting on

**Cloudflare is present and doing real work** — the site is attacked, and availability matters because aggregated findings are how communities and journalists see the evidence.

The action is not on the website. It is documenting the protective practices — precision limits, compartmentalization, what stays off digital systems — so they survive staff turnover. **Right now this organization's most important security control is a set of habits held by a handful of people.** That is the [volunteer project](../technical-volunteers/index.md)'s real substance, underneath the dashboard the organization asked for.

[^order-history]: Product order history (simulated)
[^org-staff]: Organization staff, directly (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
