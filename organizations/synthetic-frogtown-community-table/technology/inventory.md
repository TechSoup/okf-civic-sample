---
type: technology-inventory
title: synthetic-Frogtown Community Table — Technology inventory
description: What the organization runs, each item attributed to how we know it. One serious problem in an otherwise tidy stack.
tags: [technology, inventory, synthetic]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: order-history
    resource: "simulated donated-and-discounted product order history"
    title: Product order history (simulated)
    author: process:order-history
    last_modified: 2026-06-30
  - id: web-fingerprint
    resource: "simulated website and DNS fingerprint"
    title: Website/DNS fingerprint (simulated)
    author: process:web-fingerprint
    last_modified: 2026-07-01
  - id: org-staff
    resource: "simulated conversation with organization staff"
    title: Organization staff, directly (simulated)
    author: human:org-staff
    last_modified: 2026-03-02
x-civic:
  profile: civic/0.6
---

# Technology inventory

**⚠ Synthetic — fabricated data. No transaction, order, or scan behind any line below.**

Every claim on this page is attributed to one of three sources, declared in the frontmatter and cited inline. **The attribution is the useful part** — three sources that see different things, and where they disagree is where the findings are.

- `order-history`[^order-history] — the organization acquired it through a donation or discount programme. In a real bundle this is the signal nobody else has.
- `web-fingerprint`[^web-fingerprint] — inferred from the website or DNS. A guess, not a confirmation.
- `org-staff`[^org-staff] — the organization said so. Unverified, and often the only way to learn about something neither of the other two can see.

## Acquired through a donation or discount programme

*Product names and acquisition years only. No order numbers, invoice IDs, or transaction identifiers — there is no real transaction behind these, and a fabricated order number invites someone to go looking for it.*

**Currently active — and this is nearly the whole inventory:**[^order-history]

| Technology | Category | Acquired | Detail |
|---|---|---|---|
| **Microsoft 365 Business Basic** | Productivity / identity / email | 2016 | Donated; 6 seats. The only suite. Everyone is in it |
| **QuickBooks Online Simple Start** | Accounting | 2015 | Renewed continuously. Right size for the organization, not oversized |
| **Bitdefender** | Endpoint security | 2019 | Every machine. Five of five |
| **Canva for Nonprofits** | Design | 2021 | Shelf signage in five languages, volunteer recruitment, donor appeals |

**Previously acquired:**[^order-history]

| Technology | Category | Acquired | How |
|---|---|---|---|
| Refurbished desktops (3) | Hardware | 2019 | Refurbished hardware programme; still in service |
| Zoom | Meetings | 2020 | Discounted; allowed to lapse in 2023 when the board went back to meeting in person |

### The lapsed Zoom line is a decision, not attrition

Small, and worth flagging for anyone building lapse-detection heuristics. The organization had Zoom, stopped needing it, and let it go.

That reads in an order history as **attrition** — an organization losing a capability, possibly a sign of decline. It is the opposite: an organization that noticed it was no longer using something and stopped carrying it.

There are at least four stories with an identical signal shape — *a product in the order history that is no longer active*: a deliberate decision, a never-adopted purchase, a graduation to something larger, and a genuine lapse. Distinguishing them requires asking. Any corpus analysis treating "acquired, now inactive" as one category is collapsing four different things into one number.

## Told to us directly

| Technology | Category | Detail |
|---|---|---|
| **Donor database** (small-nonprofit product) | Fundraising | Used properly: gifts recorded, acknowledgements sent, reports reconciled against the accounting system monthly |
| **Google Sheets** (two) | Shelf counts, volunteer schedule | Two sheets, consistent structure, one owner each. Not a sprawl |
| **Self-hosted WordPress site** | Website + the only donation channel | See below. The problem |
| Paper sign-in at the shelf | Household counts | Tallied weekly. No names — see [population.md](../population.md) |

*Confirm the donor database product and plan, and who administers the website. The answer to the second one is the crux.*[^org-staff]

### Donors are named; shoppers are counted

A clean data-practice distinction, worth noting because few organizations draw it this sharply. The **donor database holds full records** — names, addresses, giving history, reconciled monthly against the books. The **shelf holds counts** — households, household size, neighbourhood, no names, no immigration status.

Two data regimes in one 4.5-FTE organization, with different rules, applied consistently. See [population.md](../population.md) for why the second one is firm.

## The one serious problem

**The website is a self-hosted WordPress installation, several major versions behind, running an old donation plugin, and it is the organization's only online giving channel.**

Specifics, all inferred from the fingerprint and all needing confirmation:[^web-fingerprint]

- WordPress core is **well behind current** — enough that publicly-documented vulnerabilities apply.
- The **donation plugin has not had a release in over three years** and appears to be unmaintained upstream.
- **No web application firewall**, no managed-host protection layer.
- **The theme is a commercial theme whose licence has lapsed**, so it is not receiving updates either.
- **Nobody administers it.** Built in 2018 by a volunteer who has since moved away. Nobody at the organization has logged into the admin panel in over a year, and it is not certain anyone has working credentials.[^org-staff]
- It processes roughly **$70,000 a year** in individual gifts — a sixth of the organization's revenue.[^org-staff]

An unmaintained donation form is not merely a website problem. It is a **payment-adjacent system nobody owns**, taking money from donors who trust this organization, on software with known holes. If it were compromised, the organization would learn about it from its donors.

Everything else in this inventory is in good order. This one thing is genuinely bad, and it is bad in the specific way small organizations end up exposed: a volunteer built something helpful, left, and the thing kept running.

## Detected on the website

| Technology | Category |
|---|---|
| WordPress (outdated core) | Website / CMS |
| Donation plugin (unmaintained) | Payments |
| Commercial theme (lapsed licence) | Presentation |
| No CDN or WAF | — |
| No analytics | — |
| Facebook page link | Social |

*Digital-maturity tier from the fingerprint: "low."*[^web-fingerprint]

The absent analytics is worth a sentence, because absence is ambiguous. At some organizations no analytics is a deliberate protective decision that scans as immaturity. Here it is just an absence — nobody chose it, and nothing much turns on it. **Same missing signal, different meaning, and a fingerprint cannot tell the two apart.** Only asking does.

## Known unknowns

- **Whether anyone has working admin credentials for the website.** The single most important unknown in this bundle. If the answer is no, the volunteer project starts differently.
- **Where the donation plugin's transaction records live**, and whether the organization could reconstruct a year of online giving if the site were lost.
- **Whether the site has already been compromised.** Nobody has looked. An unmaintained WordPress with an old plugin is a common target, and the usual outcome is not defacement but something quiet.
- **Who owns the domain registration**, and whether the renewal is on a card belonging to someone who no longer works there. This kills small organizations' websites more often than hacking does.
- **Whether the donor database and the website's donation records agree.** The monthly reconciliation is against the accounting system; the website may be a third number.

An empty slot documented as empty is the intended state for all five of these. None of them should be filled in with a guess to make the record look finished.

[^order-history]: Product order history (simulated)
[^web-fingerprint]: Website/DNS fingerprint (simulated)
[^org-staff]: Organization staff, directly (simulated)
