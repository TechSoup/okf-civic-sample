---
type: doc
title: The Civic Profile (x-civic)
description: A proposed OKF extension profile for civil-society knowledge.
tags: [okf, civic-profile, proposal]
timestamp: 2026-06-20T00:00:00Z
---

# The Civic Profile (`x-civic`) — a proposed OKF extension for civil society

**Status:** draft proposal, v0.4 · **Namespace:** `x-civic` · **Builds on:** OKF v0.1

> **v0.4 changes.** One change from v0.3, in eligibility: the flat `eligibility.org_types` field is replaced by **`eligibility.eligible_audiences`** — an OR-list of *audience* keys, each resolving (via a producer-local audience registry shipped with the bundle) to an `(org_type AND subject)` PCS clause. A record is eligible to a user matching **any** audience, so one record can serve several distinct audiences at once (e.g. nonprofits **or** public libraries) — which a single flat `(org_types AND pcs_subject)` pair could not express. `eligibility.pcs_subject` remains as an optional, independent mission restriction. The interoperable contract is the *resolved clauses*, so a conformant bundle publishes its audience registry. This is the one breaking change in 0.4.
>
> **v0.3 changes.** Two changes from v0.2: (1) the typed-edge vocabulary expands from `complements`/`alternative` to also include `conflicts`, `requires`, `related`, and `learn-with` (see "Relationships as graph edges"); `requires` is **directional** (one-way), the rest are symmetric/reciprocal. (2) Subject and organization-type eligibility now use **Candid's Philanthropy Classification System (PCS)** as the recommended controlled vocabulary — the `eligibility.ntee_codes` key is renamed to `eligibility.pcs_subject`, and `eligibility.org_types` values are PCS OrgType codes. The vocabulary change is the one breaking change in 0.3; everything else remains additive and namespaced under `x-civic`.
>
> **v0.2 (prior).** Introduced `x-civic.profile` on every record carrying an `x-civic` block, and a generated `x-civic.relations` list mirroring the prose link-title edges. Both live under `x-civic`, so a v0.1 (or any plain OKF) consumer ignores them and still reads valid records.

Core [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) is deliberately minimal — the only required field is `type`, and producers may add any keys. That minimalism is a feature. But the nonprofit/civil-society sector consistently needs a handful of the *same* things that core OKF leaves open. This profile gathers them into one namespaced, additive convention so different producers can interoperate.

It is offered as a **starting point for discussion** with the OKF community — exactly the kind of domain profile a lightweight governance process could ratify (core stays tiny; communities steward profiles).

## Why a profile (not core changes)

- Keeps core OKF small and vendor-neutral.
- Lets the civic sector converge without waiting on the base spec.
- Compatible by construction: everything lives under `x-civic:`, so any OKF consumer can ignore it safely.

## Proposed fields (all under `x-civic:`)

| Field | Purpose |
|---|---|
| `profile` | The profile version this record conforms to (`civic/0.4`). **Required on every record that uses an `x-civic` block** — it qualifies the namespace so a consumer knows which conventions apply. |
| `status` | Lifecycle: `PROPOSED` · `INITIALIZED` · `ACTIVE` · `ARCHIVED` · `REJECTED`. Only `INITIALIZED`/`ACTIVE` are "live"; `ARCHIVED`/`REJECTED` retain the record (and a reason) so mistakes aren't repeated. |
| `category` | Human-facing grouping (e.g. Basic Needs, Legal, Digital Inclusion). |
| `capability` | The *function* a resource provides (e.g. `digital-skills-training`). Two resources sharing a capability are **alternatives/substitutes** — the civic analog of "you only need one of these." |
| `eligibility` | Who qualifies: `eligible_audiences` (an OR-list of producer-local *audience* keys, each resolving to an *(org_type AND subject)* Candid PCS clause — see "Eligibility vocabularies" below), `regions`, optional `pcs_subject` (independent mission restriction), `rules`. The sentinel `ALL` means "no restriction on a facet." |
| `operational_status` | Real-world state of the service (e.g. `operational`, `comingSoon`) — **distinct from `status`**. `status` describes the *knowledge record*; `operational_status` describes the *thing the record is about*. A site can be a valid `ACTIVE` record while `comingSoon` in reality. |
| `provenance` | `last_audited` (date) and `source` on every record, plus a type-specific identifier — `range_id` for directory records, `vendor_url` for offers. Trust depends on freshness and traceability. |
| `reason` | Required when `status` is `ARCHIVED` or `REJECTED` — the "looks like a discount/offer but isn't" record. |
| `relations` | A machine-readable list of this record's typed edges, each `{target, type, note}`. **Generated from the prose link titles, not hand-maintained** (see below) — a YAML-parseable projection for consumers that don't parse markdown link titles. |

## Relationships as graph edges

Use normal markdown links in the body for referral partners, parent programs, and alternatives. To make the *type* of each edge machine-readable — not just legible to a human reading the prose — this profile adopts the link-title convention proposed in OKF issue [#101](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/101): a leading token before a colon in the link title names the edge.

```
[Martin Luther King Jr. Center](martin-luther-king-jr-center.md "alternative: same free-summer-meals capability, nearby")
```

The civic edge vocabulary (unchanged since v0.3):

| Token | Meaning | Direction |
|---|---|---|
| `complements` | Targets provide *distinct* capabilities that work together as a stack. | symmetric |
| `alternative` | Targets share a `capability`; you need only one (substitutes). | symmetric |
| `conflicts` | Targets should **not** be deployed together — incompatible, mutually exclusive, or interfering. The inverse of `complements`. | symmetric |
| `requires` | The source depends on the target; the target must be in place first (prerequisite). | **directional** |
| `related` | A general "see also" with no stronger claim. | symmetric |
| `learn-with` | Links an offer to a `course`/training (or vice versa) that helps adopt it. | symmetric |

**Symmetric vs directional.** Symmetric edges must be **reciprocal** — if A links to B, B links back to A with the same token (the validator enforces this). `requires` is **directional** by nature (A requires B does not imply B requires A), so reciprocity is not expected; the validator only checks that the target exists.

`complements`, `alternative`, and `conflicts` reason over `capability` (shared capability → substitutes; distinct capabilities → complements; interfering capabilities → conflicts). Existing OKF consumers that ignore link titles still see valid links; tools that read them get typed edges.

### The prose links are the source of truth; `relations` is generated

The link-title tokens in the document body are the **single, human-edited source of truth** for edges — this keeps the profile aligned with #101 rather than forking a parallel convention. For consumers that parse YAML but not markdown link titles, the same edges are mirrored into a structured `x-civic.relations` list:

```yaml
x-civic:
  relations:
    - target: martin-luther-king-jr-center.md   # the link's href
      type: alternative                          # the link-title token
      note: same free-summer-meals capability, nearby
```

`relations` is **derived, never hand-maintained**: `scripts/validate.py --write` regenerates it from the prose links, and a plain `scripts/validate.py` run fails if the two ever diverge. Edges are also expected to be **reciprocal** — if A links to B as an `alternative`/`complements`, B links back the same way — which the validator enforces.

## Eligibility vocabularies (audiences over PCS)

As of v0.4, eligibility is expressed as **audiences**. A record's `eligibility.eligible_audiences` is an **OR-list of audience keys**; a user qualifies if they match **any** one. Each audience resolves to an **(org_type AND subject)** predicate over two Candid PCS facets:

- **org_type** — PCS **OrgType** facet codes (e.g. `EB000000` = *Governments and agencies*).
- **subject** — PCS **Subject** facet codes (e.g. `SH020400` = *Public libraries*).

So the audience `public_library` = *(OrgType: government) AND (Subject: public libraries)*, and an offer open to `[nonprofit, public_library]` is eligible to a nonprofit of any mission **OR** a public library. This OR-of-(AND) shape is the v0.4 change: it expresses an offer open to more than one distinct audience, which the flat `org_types` + `pcs_subject` of v0.3 could not.

**Audience keys are producer-local; the resolved clauses are the interoperable contract.** Two producers may use different keys for the same `(org_type, subject)` clause, so tools must not interoperate on key strings. A conformant bundle therefore **ships its audience registry** — see [`registry/audiences.json`](../registry/audiences.json) in this sample — mapping each key to its clause, so any consumer can resolve `eligible_audiences` without external knowledge.

- **`eligibility.pcs_subject`** (optional) — an independent, offer-level **mission restriction** from the PCS **Subject** facet (e.g. `SA000000` = *Arts and culture*), ANDed on top of audience eligibility and distinct from an audience's own subject. Replaces the NTEE-specific `ntee_codes` of v0.2 (PCS ships an NTEE→PCS crosswalk).
- The sentinel **`ALL`** on either facet means "no restriction on that facet." Other axes (`regions`, free-text `rules`) are **not** PCS — geography in particular has no PCS facet.

> **Attribution.** The Philanthropy Classification System is © Candid, made available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: <https://taxonomy.candid.org>. A producer using PCS codes must credit Candid and indicate any modifications; it must not charge users a premium for the ability to use PCS. This profile recommends — but does not mandate — PCS; a bundle MAY use another subject/org-type vocabulary, but interoperating tools expect PCS.

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
- A shared controlled vocabulary for `capability` and `category` — and should the civic edge vocabulary (`complements`, `alternative`, `conflicts`, `requires`, `related`, `learn-with`) be registered alongside #101's starter set, including the symmetric-vs-directional distinction?
- Is recommending Candid PCS for `pcs_subject` / `org_types` the right call for a *general* civic profile, or should the profile stay vocabulary-neutral and leave PCS to a regional sub-profile?
- How to express eligibility precisely without reinventing HSDS?
