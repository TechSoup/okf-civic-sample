---
type: doc
title: The Civic Profile (x-civic)
description: A proposed OKF extension profile for civil-society knowledge.
tags: [okf, civic-profile, proposal]
timestamp: 2026-06-20T00:00:00Z
---

# The Civic Profile (`x-civic`) — a proposed OKF extension for civil society

**Status:** draft proposal, v0.1 · **Namespace:** `x-civic` · **Builds on:** OKF v0.1

Core [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) is deliberately minimal — the only required field is `type`, and producers may add any keys. That minimalism is a feature. But the nonprofit/civil-society sector consistently needs a handful of the *same* things that core OKF leaves open. This profile gathers them into one namespaced, additive convention so different producers can interoperate.

It is offered as a **starting point for discussion** with the OKF community — exactly the kind of domain profile a lightweight governance process could ratify (core stays tiny; communities steward profiles).

## Why a profile (not core changes)

- Keeps core OKF small and vendor-neutral.
- Lets the civic sector converge without waiting on the base spec.
- Compatible by construction: everything lives under `x-civic:`, so any OKF consumer can ignore it safely.

## Proposed fields (all under `x-civic:`)

| Field | Purpose |
|---|---|
| `status` | Lifecycle: `PROPOSED` · `INITIALIZED` · `ACTIVE` · `ARCHIVED` · `REJECTED`. Only `INITIALIZED`/`ACTIVE` are "live"; `ARCHIVED`/`REJECTED` retain the record (and a reason) so mistakes aren't repeated. |
| `category` | Human-facing grouping (e.g. Basic Needs, Legal, Digital Inclusion). |
| `capability` | The *function* a resource provides (e.g. `digital-skills-training`). Two resources sharing a capability are **alternatives/substitutes** — the civic analog of "you only need one of these." |
| `eligibility` | Who qualifies: `org_types`, `regions`, mission/NTEE codes, income notes, etc. |
| `operational_status` | Real-world state of the service (e.g. `operational`, `comingSoon`) — **distinct from `status`**. `status` describes the *knowledge record*; `operational_status` describes the *thing the record is about*. A site can be a valid `ACTIVE` record while `comingSoon` in reality. |
| `provenance` | `last_audited` (date) and `source` on every record, plus a type-specific identifier — `range_id` for directory records, `vendor_url` for offers. Trust depends on freshness and traceability. |
| `reason` | Required when `status` is `ARCHIVED` or `REJECTED` — the "looks like a discount/offer but isn't" record. |

## Relationships as graph edges

Use normal markdown links in the body for referral partners, parent programs, and alternatives. To make the *type* of each edge machine-readable — not just legible to a human reading the prose — this profile adopts the link-title convention proposed in OKF issue [#101](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/101): a leading token before a colon in the link title names the edge.

```
[Martin Luther King Jr. Center](martin-luther-king-jr-center.md "alternative: same free-summer-meals capability, nearby")
```

Two civic edge types are used in this bundle, both grounded in `capability`:

- **`alternative`** — the targets share a `capability`; you need only one (substitutes). Used among the meal sites.
- **`complements`** — the targets provide *distinct* capabilities that work together as a stack. Used among the offers.

Existing OKF consumers that ignore link titles still see valid links; tools that read them get typed edges. Shared `capability` values let a tool reason about substitution even where no explicit edge is written.

## Relationship to Open Referral / HSDS

For human-services directory data (e.g. 211), the sector's established standard is **[Open Referral / HSDS](https://docs.openreferral.org/)** — the Human Services Data Specification (currently **v3.0.1**): a non-hierarchical set of UUID-keyed objects (`Organization`, `Service`, `Location`, `Schedule`, `Eligibility`) defined in JSON Schema, serialized as CSV/JSON datapackages, with an API (HSDA).

**This profile does not compete with HSDS — it aligns to it.** HSDS is the structured *data-exchange* layer; OKF + `x-civic` is the human- and AI-readable *knowledge* layer beside it. For the overlapping fields they round-trip cleanly:

| This bundle (OKF + `x-civic`) | HSDS 3.0.1 |
| :--- | :--- |
| a meal-site / resource document | `Service` (+ `Service_at_Location`) |
| `title` | `service.name` |
| `x-civic.location` (address, lat/long) | `Location` |
| `x-civic.hours`, `x-civic.season` | `Schedule` (RFC 5545 RRULE) |
| `x-civic.serves`, `x-civic.eligibility` | `Eligibility` |
| the org operating a site | `Organization` |
| `provenance.range_id` | external identifier |
| `x-civic.capability` (substitution / alternatives) | *no direct HSDS object — OKF adds this* |
| document body (gotchas, guidance, context) | *no HSDS equivalent — OKF's value-add* |

What OKF adds on top of HSDS: **verbose, agent-ready context** (the prose a model needs to actually advise someone), **cross-domain generality** (the same format carries offers and skills too, not just directories), **human editability** (markdown in Git, not a normalized database), and **federation** over Git. What HSDS does better: strict validation, relational integrity, and a mature exchange ecosystem. A clean division of labor — and a documented OKF↔HSDS crosswalk like this one is exactly the kind of "human-services profile" worth proposing to both communities.

## Alignment with the OKF spec discussion

This profile was revised to track active proposals in the OKF issue tracker rather than invent parallel conventions:

- **Typed link edges** follow [#101](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/101) (link-title relationship tokens) — see "Relationships as graph edges" above.
- **Lifecycle `status` and `provenance`** overlap [#120](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/120), which proposes `status`, `aliases`, a relationship index, and a rationale trail as *core* conventions. We arrived at the same needs independently, from the civic domain. If core OKF adopts a `status` vocabulary, we will map our five-state enum (`PROPOSED`…`REJECTED`) onto it; #120's current draft proposes a simpler `active`/`deprecated`.
- **`provenance` / freshness** relates to [#94](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/94) (inline citation) and [#97](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/97) (recommending `timestamp` for staleness detection).

## Open questions for the community

- Should `status` and `provenance` be promoted toward core OKF (as [#120](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/120) proposes), or stay profile-level?
- A shared controlled vocabulary for `capability` and `category` — and should `alternative` / `complements` be registered as edge types alongside #101's starter vocabulary?
- How to express eligibility precisely without reinventing HSDS?
