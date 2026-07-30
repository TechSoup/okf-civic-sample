---
type: technology-inventory
title: "synthetic-Nyando Community Health Trust — Technology inventory"
description: "What the organization runs, each item tagged with how we know it — the collection's best field data operation. Fabricated."
tags: ["technology", "inventory", "synthetic", "kenya", "offline-first"]
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
- **acquired-via-TechSoup-network** — obtained through the TechSoup Global Network partner serving Kenya.
- **sourced-directly** — the org told us.

## The field data operation

The best in this collection, and almost none of it visible to any provenance lane except asking.

| Component | Detail |
|---|---|
| **Mobile data collection platform** | Open-source, offline-first, purpose-built for community health work. Forms mirror the national indicator set. Promoters capture household visits with **no connectivity required at the point of capture** |
| **Devices** | ~110 basic Android smartphones organization-provided; the remainder of the 142 promoters use their own. **Two tiers, unequal, and the organization knows it** |
| **Sync** | Opportunistic. When a promoter reaches coverage — at a link facility, a market, a road — pending records upload |
| **Solar charging** | At the four link facilities and in some promoter households. Mains power is unreliable; a dead phone is a lost week |
| **National health information system** | Aggregated monthly submission in the required format. **Externally held, twelve years continuous** |
| **Supervision workflow** | Monthly meetings at link facilities where records are reviewed. **This, not the software, is why the data is good** |
| **Mobile money** | Promoter stipends disbursed by mobile money. Efficient, traceable, and near-universal here |
| **SMS** | Reminders and alerts to promoters, and some household messaging. Works on any handset |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm the platform version and hosting, and whether the organization has any query access to its own submitted data — the volunteer project depends on the answer.*

### Supervision is the technology

Worth pulling out because it is the finding most likely to be misread.

An outside observer credits the mobile platform for this organization's data quality. **The organization credits monthly supervision meetings** — 23 paid staff sitting with promoters at four link facilities, reviewing records, catching a misunderstood indicator definition in week three rather than in a quarterly report.

The software makes offline capture possible. **The supervision makes the data true.** Any intervention that improves the tooling while adding to the supervision burden would make the data worse, and that is exactly the kind of trade an enthusiastic technology project makes without noticing.

### What the promoters pay

**Mobile data and airtime for the reporting the organization requires come substantially out of promoter stipends.** Sync consumes data. Coordination consumes airtime. Roughly a fifth of promoters use their own handsets.

So the people at the bottom of this operation are **subsidizing the organization's donor deliverables**, in small amounts, continuously, out of a stipend that is already contested nationally as inadequate. See [population](../population.md).

The organization states this plainly and says it would fix it first with unrestricted money. It is recorded here because **a technology inventory that lists an impressive offline workflow without noting who pays for the sync is describing the achievement and hiding the cost.** Any project touching this system should be measured partly on whether it increases or decreases what promoters spend.

## Acquired through the TechSoup network (Kenya)

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Basic** | Productivity / email | 2020 | Donated; ~20 seats. Office staff only — the field operation does not touch it |
| **Bitdefender** | Endpoint security | 2021 | Office machines |
| **Canva for Nonprofits** | Design | 2023 | Training materials, community posters in Dholuo and Kiswahili |
| **Zoom** | Meetings | 2021 | Donor calls, and the twice-yearly exchange with the California partner |

*Provenance: **acquired-via-TechSoup-network**[^order-history] (simulated).*

**Note how little of this organization's real technology came through the donation catalogue.** The mobile platform is open source. The devices were bought with programme funds. The national reporting system is government. Mobile money is commercial infrastructure everyone uses. Solar was a grant line.

**No QuickBooks — US-only.** As in [Poland](../../synthetic-fundacja-prawo-i-schronienie/technology/inventory.md) and [Colombia](../../synthetic-corporacion-rio-vivo/technology/inventory.md), accounting is a commercial local product, because Kenyan requirements — including KRA electronic tax invoicing and the reporting its exemption status requires — need software that knows about them.

**Three international bundles, the same pattern, stated once more because it is the most transferable finding in the set:** productivity, security, and design tools travel through the donation catalogues. **Accounting, payroll, and compliance software does not, because it is jurisdiction-specific** — and that is precisely the category a small organization most needs help with. An analysis comparing TechSoup order histories across countries will see thinner international records and should not read that as lower capacity. Here it would be badly wrong: this is the most technically capable field operation in the collection and its order history is four lines.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| Basic hosted site builder | Website | derived |
| No analytics | — | derived — probably never added rather than chosen |
| Facebook page link | Social | derived — the real channel |
| Content in English | Content | derived |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier **"very low"** — and this is the collection's most badly wrong automated tier).*

### A "very low" digital maturity tier for the best field data operation in the collection

An automated assessment sees a minimal site-builder page, no analytics, no CRM, no anything, and returns **very low digital maturity.** It is the lowest tier assigned to any of the fifteen bundles.

The organization runs 142 offline-first mobile data collectors feeding a national health information system with twelve years of continuous monthly submissions.

**Every signal available to a web-based assessment is absent, and every capability that matters is present.** The two facts are unrelated, because this organization's technology faces its promoters and the county health system, not the internet. Its website exists because a donor asked.

This is the strongest case in the collection for the same point [the California Law Center](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md) and others make more mildly: **web-observable signal is a proxy for how much an organization talks to the internet**, and treating it as a proxy for technical capability will systematically misrank organizations whose work is offline, rural, or non-Anglophone. The bias is not noise. It has a direction.

## Known unknowns

- **Whether the organization can query its own submitted data** in the national system, or only submit to it. **The volunteer project depends entirely on this** and nobody has established it.
- **Total promoter out-of-pocket cost** for data and airtime. Nobody has measured it. Measuring it is cheap and would be the strongest possible input to a funding conversation.
- **What happens on the ~30 promoter-owned handsets** — what else is on them, what happens when one is sold or shared, whether household data persists.
- **Data Protection Act 2019 obligations** — Kenya has a data protection framework with a Data Commissioner, and whether the organization's household data practices meet its requirements has not been assessed.
- **Hosting and continuity of the mobile platform** — where the server is, who administers it, what a failure would cost.
- **Whether household registers survive a promoter leaving.** Twelve years in, turnover has happened, and the answer is not documented.

## A derived signal worth acting on

Nothing on the website. It is irrelevant to this organization's function and improving it would help nobody.

The action is **measuring what the promoters spend.** It is a week of work, it requires no technology, and it converts a known injustice into a number that can go in a budget request. **A volunteer who did only that would have done more good here than one who rebuilt the website.**

[^org-staff]: Organization staff, directly (simulated)
[^order-history]: Product order history (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
