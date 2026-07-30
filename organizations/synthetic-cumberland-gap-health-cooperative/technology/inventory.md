---
type: technology-inventory
title: "synthetic-Cumberland Gap Health Cooperative — Technology inventory"
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

## The fax pile

The finding first.

**Most clinical information arrives at this organization as a fax.** Specialist consultation notes, lab results from the reference laboratory, hospital discharge summaries from the facility ninety minutes away, imaging reports, prior-authorization responses, pharmacy queries, benefits correspondence for black lung claims. Between **60 and 120 pages a day**, as unstructured PDFs in a fax server's inbox.

One person — the practice manager, with help when she's out — opens each document, works out what it is and which patient it belongs to, renames it, and files it into the EHR. It takes **most of a working morning, every day**. When she is on leave, the queue reaches several hundred documents and things get missed. A discharge summary sitting unread for four days is a clinical problem, not a filing problem.

The organization would love this to be otherwise, and it is not within its power: **it does not control how the hospital, the lab, or the specialists send things.** Interoperability is a thing that happens to a fourteen-person clinic, not something it negotiates. This is the subject of the [volunteer project](../technical-volunteers/index.md), and the project deliberately does not attempt to fix the sending side.

## The telehealth attempt, and why it failed

Stood up in 2020 with grant funding. Video visit platform, tablets for the exam rooms, staff training, the whole package. Competently done.

It is used today by a small number of patients. **For roughly 40% of the patient population it does not work at all**, because the connection where they live will not carry a video call — no wired service available, or satellite that a call defeats, or a metered mobile connection that twenty minutes would exhaust.

**Nothing was done wrong.** The organization got connected, bought the right equipment, trained its staff, and the intervention still failed, because the constraint was never on its side of the wire. The grant reported a successful implementation. The patients who most needed to avoid a winding drive still make it.

Two things worth extracting:

**A capability flag can be true and misleading.** "Has telehealth: yes" is accurate here and conveys almost the opposite of the situation. Anything reading capability flags across a corpus will overestimate this organization's remote-care reach.

**The digital-divide framing is usually pointed the wrong way for rural health.** The standard recommendation set — improve the organization's connectivity, adopt cloud tools, offer virtual services — assumes the organization is the bottleneck. Here it is the patients, and the organization's response has been the correct one: **more home visits**, which is expensive, unreimbursed, and works.

## Sourced directly — the practice systems

| Technology | Category | Detail |
|---|---|---|
| **Small-practice EHR** | Clinical | Cloud-hosted, appropriate to its size, works. Integrated scheduling and billing |
| **Fax server** | Inbound clinical documents | The organization's actual front door. See above |
| **Fixed wireless internet** at the clinic | Infrastructure | Adequate. A backup mobile hotspot for outages, which are not rare |
| **Telehealth platform** | Clinical | Real, retained, used by few. See above |
| **Paper** | Board minutes, home-visit notes, consent forms | Home-visit clinical notes are often taken on paper and entered later |
| Practice-management billing clearinghouse | Revenue cycle | External, vendor-provided |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm the EHR vendor and whether its API or document-import interface is usable, since the volunteer project depends on it.*

**Home-visit notes are on paper**, for the same reason the [Sierra Foothills mobile unit](../../synthetic-sierra-foothills-community-health/technology/inventory.md) charts on paper and [Valle Verde's](../../synthetic-valle-verde-food-network/technology/inventory.md) route sheets are on clipboards. Three organizations in this collection, three service areas with no signal, three paper workarounds. The pattern is worth noticing: **paper is what competent organizations use when the network isn't there**, and reading it as backwardness gets the diagnosis wrong every time.

## Acquired through TechSoup

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Basic** | Productivity / email | 2019 | Donated; ~16 seats. Email and documents; not the clinical stack |
| **Zoom** | Meetings | 2020 | Discounted. Administrative and continuing-education use; clinical telehealth is a separate platform |
| **Bitdefender** | Endpoint security | 2020 | All office machines |
| **Canva for Nonprofits** | Design | 2023 | Patient education handouts, community notices |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Refurbished desktop computers (6) | Hardware | 2018 | Refurbished hardware programme. Ageing; two have been retired |
| QuickBooks Online | Accounting | 2017 | Believed active; the bookkeeper is a contractor and may run it on her own subscription — **unconfirmed, and worth confirming** |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

**The QuickBooks ambiguity is a real pattern**, not an oversight in this bundle. A small organization using a contract bookkeeper often cannot say whose subscription the books live on, which matters if the relationship ends. Order history says the organization acquired it; reality may be that the contractor's own licence is doing the work. Neither the TechSoup lane nor a website scan can tell the difference.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| Wix | Website / CMS | derived |
| Google Analytics | Analytics | derived |
| Telehealth platform link (external) | Clinical | derived |
| No patient portal detected | — | derived |
| No online scheduling | — | derived |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "low").*

A **"low" tier that is roughly fair**, unlike [the Law Center's](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md). This organization's public web presence genuinely is minimal, and that is a reasonable allocation of a $1.1M budget when the patient population is older, less online, and reached by phone and by truck. The recommendation "add online scheduling" is not harmful here, just close to pointless — the patients who cannot use a video visit are not booking appointments in a browser either.

## Known unknowns

- **Whether the EHR can accept documents programmatically** — an API, a watched folder, a structured import. The volunteer project's feasibility rests entirely on this and nobody has asked the vendor.
- **Whose QuickBooks subscription the books are on.** See above.
- **What happens to home-visit paper notes** between the visit and the EHR entry — where they are, in whose bag, for how long. PHI in a truck, undocumented.
- **Backup and recovery for the fax server**, which holds documents that have not yet been filed anywhere else. A failure there loses clinical information that exists in no other place the organization controls.
- **HIPAA risk assessment.** Required, and no evidence of a current one. Unlike [Sierra Foothills](../../synthetic-sierra-foothills-community-health/README.md), this organization has no compliance officer — the same obligations, a seventh of the budget, and nobody whose job it is.
- **Retention schedule**, particularly for records that function as evidence in black lung benefits claims and have obligations ordinary clinical retention doesn't cover.

## A derived signal worth acting on

The site runs **Google Analytics**, which for a clinic serving substance-use recovery patients deserves a second look — not the site's traffic data as such, but whether any page path or query string could indicate that a specific visitor was looking at the recovery programme. Almost certainly benign as configured. Worth ten minutes of somebody's attention, in a county small enough that a parking lot is a disclosure.

[^org-staff]: Organization staff, directly (simulated)
[^order-history]: Product order history (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
