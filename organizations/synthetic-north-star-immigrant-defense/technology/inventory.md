---
type: technology-inventory
title: "synthetic-North Star Immigrant Defense — Technology inventory"
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

## The disconnection, not a contradiction

The finding first. Unlike [Motor City Trades](../../synthetic-motor-city-trades-institute/technology/inventory.md), this organization does not have systems that disagree. It has systems that **don't talk**, and one seam matters far more than the others.

| System | Holds | Connected to |
|---|---|---|
| **Immigration case management platform** | Matters, deadlines, filings, conflicts, client records | Nothing else |
| **Pro bono network spreadsheets** | ~90 attorneys: trained when, available, capacity, cases taken | Nothing. Maintained by two staff |
| **Rapid-response log** | Calls received, disposition, who was on shift | Nothing. A shared document |
| **Court calendar tracking** | Hearing dates, some of which are not in the case platform | Partially, by hand |

**The seam that costs the most: cases and pro bono attorneys are in different worlds.** Ninety outside attorneys carry a large share of the organization's 1,300 matters, and no system knows which attorney has which case. A supervising attorney cannot see everything one network member is carrying. Nobody can produce a reliable list of who is active this quarter. A pro bono client sometimes calls the main line and reaches someone who cannot find their matter.

None of this is a data-quality problem in the usual sense. Each system is accurate. **The organization grew fourfold in four years and added a system each time it needed one**, which is what fast-growing organizations do, and the integration work never had a moment when it was anyone's priority.

## Sourced directly — including what is deliberately absent

| Technology | Category | Detail |
|---|---|---|
| **Immigration case management platform** | Practice | Sector product, appropriate, licensed commercially. Works |
| **Signal** | Client and staff communication | Widely used, deliberately. Disappearing messages on by default for internal discussion |
| **Encrypted device policy** | Endpoint | Full-disk encryption enforced; specific protocol for travel — see below |
| **Rapid-response forwarding arrangement** | Operations | A phone tree and a shared log. Fragile by choice — see [programs](../programs.md) |
| Court e-filing portals | Filing | External, per-jurisdiction credentials |
| **Short retention schedules** | Records | Documented and enforced. Deliberately shorter than the sector norm |
| **Minimal logging** | Records | Deliberate. See below |
| **No client-facing portal** | — | Deliberate. A login is a record of who is a client |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm the case platform's vendor arrangement, and whether the travel protocol is written down or is staff practice.*

### The absences are the sophisticated part, and they invert normal advice

Four things this organization does **less** of than good practice would normally recommend, each for a stated reason:

**Short retention.** Most organizations are advised to retain more, for continuity and for reporting. This one retains the minimum its professional obligations require, because **data it no longer holds cannot be compelled, breached, or seized.** Records that must be kept are kept; nothing else lingers.

**Minimal logging.** Comprehensive audit logging is nearly always recommended, and it is genuinely valuable for detecting misuse. Here it also creates **a detailed record of which staff member accessed which client's file when** — a document with obvious value to a hostile party and no defensive value proportionate to that risk. The organization logs what it must and no more.

**No client-facing portal.** Convenient for clients, and normally a good idea. But **a portal account is a durable, structured record that a specific person is this organization's client**, sitting on infrastructure the organization does not fully control. It has decided the convenience is not worth the artefact.

**No web analytics.** Same reasoning as [the Law Center's](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md) — a visitor log for a removal-defense website is a hazard to the people in it.

**Every one of these scans as immaturity** to an automated assessment, and would generate a recommendation to fix it. All four are considered decisions with reasoning the organization can articulate. This is the second bundle in the collection to make that point and it makes it harder: at the Law Center the absences were mostly about privacy, here at least two of them are about **resisting compulsion**, which is a threat model most nonprofit technology advice does not have a category for.

### The travel protocol

Staff who cross a border carry **clean devices** — no client data, no case platform access, credentials removed and restored afterwards. This exists because device searches at ports of entry operate under weaker protections than searches elsewhere, and an attorney's laptop full of client files is a specific hazard.

Worth noting as an example of a control that is **entirely invisible to every provenance lane**. It doesn't appear in order history, it doesn't appear in a website scan, and it is arguably the most sophisticated single thing in this inventory.

## Acquired through TechSoup

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2016 | Donated then, largely converted to paid as the organization grew past the cap. ~30 seats. Conditional access and device policy configured — **reviewed, unlike most tenancies in this collection** |
| **Zoom** | Meetings / remote hearings | 2020 | Discounted; heavily used for detained client calls and remote hearings |
| **Bitdefender GravityZone** | Endpoint security | 2018 | All devices, with full-disk encryption enforced |
| **Adobe Acrobat Pro** | Documents | 2017 | Many seats. Immigration practice is a PDF practice at volume |
| **DocuSign** | E-signature | 2021 | Retainers and authorizations |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Canva for Nonprofits | Design | 2021 | Know-your-rights materials in eight languages |
| Asana | Project management | 2019 | Discounted; used by the policy team only |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

**Note the Microsoft 365 line against [the Law Center's](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md) and [Sierra Foothills'](../../synthetic-sierra-foothills-community-health/technology/inventory.md).** All three hold confidential material in a donated tenancy. Two have never reviewed the configuration. This one has — conditional access, device policy, retention deliberately set. Same product, same donation lane, radically different risk position, and **nothing in the order history distinguishes them.** If you are inferring capability from acquisition, these three bundles are the counter-example.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Cloudflare | CDN / DDoS protection | derived — **and it is doing real work here** |
| No analytics | — | derived — deliberate |
| No trackers or pixels | — | derived — deliberate |
| No client portal | — | derived — deliberate |
| Know-your-rights materials in 8 languages | Content | derived |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "low-moderate" — and, as with the Law Center, that tier is misleading).*

**Cloudflare is not decorative here.** An organization doing this work can expect its site to be attacked, and its public materials are how people find out what to do in the hours after a detention. Site availability is a program function.

## Known unknowns

- **Whether the travel protocol is written down** or lives as staff practice. If it's practice, it leaves with the staff who practice it.
- **Whether the pro bono attorneys' own devices and systems** meet any standard. Ninety outside attorneys handling North Star client files on their own firm infrastructure, with no visibility for the organization. **Arguably the largest exposure in this bundle**, and it sits outside the organization's control entirely.
- **What is in the rapid-response log** and how long it stays there. It is a shared document containing the names of people who have just been detained.
- **Whether the retention schedule is actually enforced** or merely documented. Different things.
- **Continuity for the rapid-response line** if the forwarding arrangement fails at 2 a.m.
- **What the case platform vendor would do** with a records demand, and whether the organization has asked.

## A derived signal worth acting on

Nothing on the public site needs fixing, which is unusual in this collection. The site is minimal, protected, multilingual, and deliberately uninstrumented, and that is the right shape.

The thing worth acting on is not visible from outside: **the ninety pro bono attorneys.** They are the organization's capacity and its widest exposure, they are tracked in a spreadsheet, and nobody can say what security practices they follow with client files. That is the subject of the [volunteer project](../technical-volunteers/index.md), and the security half of it may matter more than the tracking half.

[^org-staff]: Organization staff, directly (simulated)
[^order-history]: Product order history (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
