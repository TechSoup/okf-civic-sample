---
type: technology-inventory
title: "synthetic-Central Valley Farmworker Law Center — Technology inventory"
description: "What the organization runs, each item tagged with how we know it — including what it deliberately doesn't run. Fabricated."
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
| **Microsoft 365 Business Premium** | Productivity / identity | 2016 | Donated; ~19 seats. Also the organization's largest unexamined risk — see below |
| **Zoom** | Meetings | 2020 | Discounted; remote hearings, client calls, interpreter three-ways |
| **QuickBooks Online Plus** | Accounting | 2015 | Renewed annually; court-awarded fee accounting is handled here |
| **DocuSign** | E-signature | 2021 | Retainer agreements and authorizations |
| **Adobe Acrobat Pro** | Documents | 2019 | Heavy use — legal practice is a PDF practice |
| **Bitdefender GravityZone** | Endpoint security | 2018 | All machines, including laptops that leave the office |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Canva for Nonprofits | Design | 2022 | Know-your-rights materials |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

### The Microsoft 365 question nobody has asked

The organization's email, files, and calendars — including privileged client communications and work product — live in a donated Microsoft 365 tenancy that was set up in 2016 by a volunteer and has not been reviewed since.

Nobody has established: what the **retention and deletion policy** is, whether **e-discovery and audit logging** are configured in a way consistent with privilege obligations, whether **conditional access** is enforced on laptops that travel to labor camps and courthouses, or what would happen to privileged material if a device were lost.

None of that is a criticism of the donation. It's what happens when a capable enterprise platform is configured once by a volunteer for a nineteen-person legal-aid office with no IT staff. **It is arguably a more serious exposure than anything in the volunteer project this bundle carries**, and it is here because a bundle should surface the risk even when the organization has scoped its ask elsewhere.

## Sourced directly — the practice systems

| Technology | Category | Detail |
|---|---|---|
| **Legal-aid case management platform** | Matters, deadlines, conflicts, reporting | The system of record for the practice. Sector-standard product, licensed directly, not via TechSoup |
| **Paid telephone interpretation line** | Language access | For Mixtec, Triqui, and other languages the organization cannot staff. A real budget line |
| **Signal** | Sensitive communication | Used with some clients and for internal discussion of sensitive matters. A considered choice, not a drift |
| **Paper and voice-recorded intake** | Field intake | The tailgate and know-your-rights channel. Advocate's handwritten notes or a recorded voice memo, keyed into the case system days later — the subject of the volunteer project |
| Court e-filing portals (several) | Filing | External; state and federal, each with its own credentials |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm the case-management platform's plan and whether its deadline-tracking module is actually configured, or whether deadlines are tracked in a calendar alongside it.*

## Detected on their website — and what wasn't

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Cloudflare | CDN / DDoS protection | derived |
| **No analytics platform** | — | derived — **deliberate** |
| **No third-party trackers, pixels, or ad tags** | — | derived — **deliberate** |
| **No embedded chat widget** | — | derived — **deliberate** |
| **No social-media embeds** | — | derived — **deliberate** |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier reported as **"low"** — see immediately below, because that tier is wrong).*

### The fingerprint scored this organization "low" for doing the right thing

An automated assessment sees a WordPress site with no analytics, no tag manager, no pixels, no chat, and no social embeds, and concludes: unsophisticated, under-resourced, not measuring anything. Low digital maturity.

What is actually going on: **this organization decided not to keep a log of who visits an immigration legal-aid website.**

Analytics would mean a third party holding a record of IP addresses and page paths for people researching removal defense. A chat widget would mean a vendor holding transcripts of first contact from someone deciding whether it is safe to ask for help. A Facebook pixel would mean informing a social platform which of its users read the page about what to do if immigration agents come to your workplace.

The organization thought about each of these and declined. It cannot tell you its site's bounce rate. That is the trade it chose, and it is the correct trade for its population.

**This is the single most important test case in the collection for anything that scores organizations automatically.** Every signal a fingerprint can see points to immaturity. The reality is a more considered privacy posture than most well-resourced organizations manage. There is no way to tell the difference from the outside — you have to ask, and the answer lives in the `sourced-directly` lane or nowhere.

If your assessment pipeline produces a "low digital maturity" score for this bundle and recommends installing analytics, it is working exactly as designed and giving advice that would harm people.

## Known unknowns

- **The Microsoft 365 configuration**, in full — retention, audit, conditional access, device policy. See above. The organization's largest unexamined exposure.
- **Whether case-management deadline tracking is configured** or whether deadlines live in a parallel calendar. Material to the volunteer project, since a statute-of-limitations miss is the failure mode that matters most.
- **What is on the laptops** that travel to labor camps and courthouses, and what happens if one is lost or seized.
- **Whether the voice-recorded intakes are retained**, where, and for how long. They are informal by nature and may contain privileged content in an uncontrolled location — a staff member's phone.
- **Retention schedule for closed matters.** None evidenced. Legal-aid case files have professional retention obligations that a general-purpose policy won't satisfy.

## A derived signal worth acting on

**Cloudflare is present and correctly configured**, which combined with the deliberate absence of trackers suggests someone at some point thought carefully about this site. Worth finding out who, and whether they're still available — an organization with a good decision in its history and nobody who remembers making it is one staff change away from someone helpfully adding Google Analytics.

[^order-history]: Product order history (simulated)
[^org-staff]: Organization staff, directly (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
