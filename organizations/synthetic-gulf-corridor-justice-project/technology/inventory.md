---
type: technology-inventory
title: "synthetic-Gulf Corridor Justice Project — Technology inventory"
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

## The archive has no integrity story

The finding first, because it is the one that matters.

The organization publishes about **14,000 documents** — permits, agency monitoring reports, correspondence obtained through records requests, and its own sampling results. They are cited in proceedings, quoted by journalists, and used by academic researchers. This archive is **the community's evidence base** for twenty years of a permitting record.

There is **no integrity mechanism of any kind**:

- No cryptographic hash recorded when a document is added.
- No record of **where each document came from** — which agency, which records request, which date, which custodian. Provenance exists in the memory of two staff members and, patchily, in the file naming.
- No **audit trail** of changes: if a document were replaced with an altered version, nothing would reveal it.
- No **immutable copy** anywhere. The archive is files on a server plus a backup that is a copy of the same files.
- No **chain of custody** for the organization's own sampling results — the laboratory reports are in the archive; the record of how a sample got from a bottle to that report is not.

Now put that beside the adversary described in [README](../../../README.md). An opposing expert does not have to disprove a monitoring report. They have to raise a reasonable question about whether the copy in this archive is the document the agency issued. **The organization cannot currently answer that question with anything better than "we put it there and we didn't change it."**

The site has also been **defaced once** — briefly, in 2024, with the archive untouched as far as anyone can tell, and "as far as anyone can tell" is precisely the problem. After a defacement with no integrity records, the organization could not demonstrate that nothing else was modified. It assumes nothing was.

This is the [volunteer project](../technical-volunteers/index.md), and it is the clearest case in this collection of a security problem that is not about keeping secrets.

## Sourced directly

| Technology | Category | Detail |
|---|---|---|
| **Document archive** | The evidence base | ~14,000 documents. Self-hosted, searchable, no integrity mechanism. See above |
| **Sampling programme records** | Field data | Sample logs on paper and in spreadsheets; laboratory reports as PDFs in the archive. Chain of custody undocumented |
| **Health survey data** | Respondent-level health information | Spreadsheets and paper forms. **No HIPAA coverage, no privilege, discoverable.** See [population](../population.md) |
| **Public map** | Data display | Facility locations, sampling points, permit status. Built on a hosted mapping service |
| **Accredited laboratory** | Analysis | External vendor. The expensive constraint on how many samples exist |
| Records-request tracking | Operations | A spreadsheet. Requests, responses, appeals, deadlines |

*Provenance: **sourced-directly**[^org-staff] (simulated). Confirm where the archive is actually hosted and who administers it — this determines what is possible in the volunteer project.*

### The health survey data is the confidentiality exception

Everything else in this inventory is meant to be public. This is not.

Respondent-level health information — symptoms, household cancer history, pregnancy outcomes — tied to addresses, in spreadsheets, held by an advocacy organization with **no HIPAA obligation and no privilege**. It is therefore **discoverable**, and the organization's revised consent language tells respondents so.

Two practical consequences a volunteer must understand:

**It must be separated from everything else.** The organization's instinct is to keep all its data together; for this category that instinct is wrong. It should live apart, with tighter access, and it must never end up in the public archive by an accident of file organization.

**Aggregation is not anonymization here.** "Three households on this block reported a childhood cancer" identifies people in a community this size. The organization suppresses small cells and has declined to publish findings it could not report safely. Any tooling built over this data has to carry that suppression, not leave it to whoever runs the query.

## Acquired through TechSoup

*Product names and acquisition years only. **No order numbers, invoice IDs, or transaction identifiers.***

**Currently active:**

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Premium** | Productivity / identity | 2017 | Donated; ~18 seats |
| **Zoom** | Meetings / hearings | 2020 | Discounted; remote hearing participation, coalition calls |
| **Adobe Acrobat Pro** | Documents | 2018 | Heavy — this organization processes agency PDFs at volume |
| **Bitdefender GravityZone** | Endpoint security | 2019 | Staff machines |
| **Canva for Nonprofits** | Design | 2021 | Hearing handouts, community notices |
| **ArcGIS / mapping (nonprofit programme)** | Geospatial | 2022 | **Genuinely adopted and central** — the public map runs on it |

**Previously acquired (confirm current use):**

| Technology | Category | Acquired | How |
|---|---|---|---|
| Tableau | Data visualization | 2023 | Nonprofit programme; used for two board presentations |
| Asana | Project management | 2019 | Discounted; organizing team uses a whiteboard instead |

*Provenance: **acquired-via-TechSoup**[^order-history] (simulated).*

**The mapping line is worth noting as the collection's counter-example on adoption.** Three other bundles here show a data or visualization tool acquired and never used — [Riverbend Air](../../synthetic-riverbend-air-alliance/technology/inventory.md), [Motor City Trades](../../synthetic-motor-city-trades-institute/technology/inventory.md), and Tableau in the row above. This organization's geospatial platform is **fully adopted and load-bearing**, because it maps directly onto a program need someone was already doing badly by hand.

The pattern across the four: **acquisition converts to adoption when it replaces work somebody is already doing, and doesn't when it offers a capability nobody was missing.** Order history cannot see the difference.

## Detected on their website

| Technology | Category | How we know |
|---|---|---|
| WordPress | Website / CMS | derived |
| Cloudflare | CDN / DDoS protection | derived — **added after the 2024 defacement** |
| Document archive (search-indexed) | Content | derived |
| Embedded map | Data display | derived |
| Matomo (self-hosted analytics) | Analytics | derived — **an interesting choice** |
| No third-party trackers | — | derived |

*Provenance: **derived**[^web-fingerprint] (simulated web/DNS fingerprint; digital-maturity tier "moderate").*

**Self-hosted analytics rather than a third-party service** is a deliberate middle path worth flagging. [The Law Center](../../synthetic-central-valley-farmworker-law-center/technology/inventory.md) runs no analytics at all, because a visitor log is a hazard to its clients. This organization *wants* to know who reads its archive — journalist traffic and hearing-driven spikes are useful signals — but does not want a third party holding the log, partly because that third party could be served. So it runs its own.

Three organizations in this collection, three different analytics postures, all considered: none, self-hosted, and ordinary third-party. **The same fingerprint field with three different meanings.**

## Known unknowns

- **Whether the 2024 defacement touched anything besides the front page.** Unanswerable, because there were no integrity records. This is the most consequential unknown in the bundle.
- **Where each archive document came from.** Provenance lives in two people's memories.
- **Whether the backup is a real backup** or a synchronized copy that would propagate a corruption.
- **Who administers the archive server**, and whether anyone besides one staff member can.
- **Chain of custody for sampling** — whether a sample's path from bottle to laboratory report could be documented if challenged.
- **Where the health survey data actually is**, in full, including old paper forms. If any of it has ever been stored in a location that also holds public archive material, that is a live problem.
- **What the organization would do if served for its survey data.** It knows it is discoverable. It has not decided what it would do.

## A derived signal worth acting on

**Cloudflare was added after the defacement**, which means the organization responds to incidents and learns. Good sign. The gap is that it addressed **availability** and not **integrity** — the site is now harder to knock over and no easier to verify. That is the natural response, because availability failures are visible and integrity failures are not, and it is exactly the asymmetry the [volunteer project](../technical-volunteers/index.md) exists to correct.

[^org-staff]: Organization staff, directly (simulated)
[^order-history]: Product order history (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
