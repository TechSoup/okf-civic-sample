---
type: technology-inventory
title: "synthetic-Sierra Foothills Community Health — Technology inventory"
description: "What the organization runs, each item tagged with how we know it. Fabricated."
tags: ["technology", "inventory", "synthetic"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-staff
    resource: "simulated conversation with organization staff"
    title: "Organization staff, directly (simulated)"
    author: human:org-staff
    last_modified: 2026-03-02
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

## The two-EHR problem

The finding first, because it is the reason this bundle exists in the collection.

In **2023 Sierra Foothills absorbed a small independent clinic** in a foothill town — took on its patients, its site, and two of its staff. The clinical migration was scoped, started, and **never finished**. Funding for the integration ran out, the person leading it left, and the site kept running on its existing system because patients needed to be seen on Monday.

Three years later:

| | Main system | Absorbed site's system |
|---|---|---|
| Patients | ~11,400 | ~2,600 |
| Vintage | Current, supported, integrated with practice management | Older, supported but on an end-of-life track |
| Reporting | Feeds federal and payer reporting directly | **Exported and merged by hand, quarterly** |
| Record matching | — | **Manual, by name and date of birth** |

**An estimated 300–600 people exist in both systems** — the estimate is that loose, which is itself the problem. Most are agricultural worker households whose care is episodic and whose names are recorded inconsistently across years and systems.

The consequence is clinical, not administrative. **A clinician at one site can be looking at half a patient's history** — half the medication list, half the allergy record, half the prenatal history — without any indication that a second record exists. The organization knows this, has a manual check-before-you-prescribe practice for patients from that town, and describes it as the thing that keeps the medical director up at night.

Quarterly federal reporting is produced by hand-merging two exports, which means the organization's audited patient counts rest on a spreadsheet reconciliation.

## Clinical and practice systems — sourced-directly

Procured commercially, contracted, regulated. **Not in the TechSoup lane and never will be.**

| System | Category | Detail |
|---|---|---|
| Electronic health record (primary) | Clinical | Current, supported, integrated with practice management and billing |
| Electronic health record (absorbed site) | Clinical | Older, end-of-life track, ~2,600 patients. The migration that stopped |
| Practice management / billing | Revenue cycle | Integrated with the primary EHR only |
| Dental practice system | Clinical | Separate again — a third clinical data island, smaller and lower-stakes |
| Patient portal | Patient access | Tied to the primary EHR. Absorbed-site patients have no portal |
| Mobile unit connectivity | Infrastructure | Cellular, unreliable on the rotation. Charting is often done back at base from paper notes |
| Interpretation line | Language access | Contracted; for languages not staffed bilingually |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm vendor names, contract terms, and — critically — **whether the older system's vendor still supports export**, since the migration's feasibility depends on it.*

### The mobile unit charts on paper

Worth pulling out: the mobile unit's connectivity is unreliable enough that clinicians frequently take **paper notes in the field and chart back at base**. Same roads, same dead zones as [Valle Verde's](../../synthetic-valle-verde-food-network/technology/inventory.md) pantry routes.

That is a clinical documentation delay, with the associated risks — a note written six hours later is a worse note — and it is the specific problem where the organization's peer at [Nyando](../../synthetic-nyando-community-health-trust/README.md) is genuinely further along, having built an offline-first field workflow out of necessity years ago. The `learn_with` edge is not ceremonial.

## Acquired through TechSoup

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2015 | Donated then, later partially converted to paid as seat count grew past the donation cap. ~95 seats |
| **Zoom** | Meetings / telehealth-adjacent | 2020 | Discounted. **Administrative use only** — clinical telehealth runs through the EHR's own module |
| **Bitdefender GravityZone** | Endpoint security | 2018 | Renewed; covers administrative endpoints. Clinical devices are managed under a separate arrangement |
| **Adobe Acrobat Pro** | Documents | 2019 | Several seats; a clinic runs on forms |
| **Canva for Nonprofits** | Design | 2022 | Patient-facing materials, community outreach |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| QuickBooks Online | Accounting | 2014 | **Outgrown and replaced** with a fund-accounting platform around 2021 — a normal graduation, not a failure |
| Asana | Project management | 2019 | Discounted; usage unclear |
| Tableau | Data visualization | 2022 | Nonprofit program; used by one analyst for board reporting. Actually adopted, unlike elsewhere in this collection |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

### What the TechSoup lane gets wrong about this organization

At $7.9M with 88 staff, this organization spends **far more on technology it bought commercially than on anything it received**. The donated and discounted lane covers productivity, security, and design — real value, and completely peripheral to what the organization's technology actually is.

Two implications worth noting:

**The TechSoup signal is most informative for small organizations and least informative for large ones.** For [Frogtown Table](../../synthetic-frogtown-community-table/technology/inventory.md) at $430K, the order history is close to a complete inventory. Here it describes maybe 15% of the picture and none of the important part. Any corpus-level analysis weighting this lane equally across organizations will systematically misdescribe the large ones.

**The QuickBooks line is a graduation, not a lapse.** An organization that acquired an accounting tool and later replaced it with something bigger did the right thing. A lapse-detection heuristic reading "acquired 2014, no longer active" as attrition would score this as a loss. It's growth.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Patient portal login (subdomain, EHR-vendor hosted) | Patient access | derived |
| Google Analytics | Analytics | derived |
| Constant Contact | Email marketing | derived |
| Online appointment request form | Intake | derived |
| Accessibility overlay widget | Accessibility | derived — **and of doubtful value** |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "moderate-high").*

The **accessibility overlay** deserves the same treatment as the translate widget on [Valle Verde's](../../synthetic-valle-verde-food-network/technology/inventory.md) site: a purchased widget that produces a compliance-shaped artifact and does considerably less for actual users than fixing the underlying markup would. Common, well-intentioned, and worth flagging rather than counting as an accessibility measure.

## Known unknowns

- **The true duplicate-patient count.** "300–600" is the organization's own estimate. Establishing the real number is the first task of the migration and may be the single most valuable deliverable.
- **Whether the older EHR vendor still supports full export**, including structured medication and allergy data rather than a document dump. Determines whether the migration is difficult or nearly impossible.
- **What the mobile unit's paper notes contain and how long they persist** before being charted and destroyed. PHI on paper in a vehicle, with no documented handling.
- **Whether the dental system will ever be integrated.** Currently a third island. Lower stakes, no plan.
- **The Microsoft 365 configuration** as it relates to PHI — whether administrative mail ever contains patient information, and whether the tenancy is configured on the assumption that it does. Nobody has audited this. The same unexamined-tenancy problem as [the Law Center's](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md), with HIPAA attached.

## A derived signal worth acting on

The **online appointment request form** posts into a queue monitored during business hours. Reasonable. Worth confirming it is not collecting anything that constitutes PHI over an unexamined path, and that its confirmation email does not disclose the existence of an appointment to whoever else reads that inbox — an ordinary oversight with real consequences for a patient whose reason for visiting is behavioral health or prenatal care.

[^org-staff]: Organization staff, directly (simulated)
[^order-history]: Product order history (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
