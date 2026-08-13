---
type: doc
title: The Civic Profile (x-civic)
description: A proposed OKF extension profile for civil-society organizations. Four required fields on top of core OKF.
tags: [okf, civic-profile, proposal]
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# The Civic Profile (`x-civic`) — a proposed OKF extension for civil society

**Status:** draft proposal, v0.6 · **Namespace:** `x-civic` · **Builds on:** [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

> **v0.6 is a re-scoping, not an increment.** Earlier versions of this profile described *resource catalogs* — meal sites, discount offers — and grew to about a dozen fields including a federation model and an audience-resolution registry. v0.6 describes **organizations**, requires **four fields**, and deletes almost everything else.
>
> Two things drove that. First, core OKF moved from v0.1 to **v0.2**, which made provenance, trust, lifecycle, and attestation first-class in core — absorbing four things this profile had been carrying. Second, we concluded that a profile requiring a lot is a profile nobody adopts. The OKF spec requires exactly one field. A domain profile should be embarrassed to require many more.
>
> **Breaking changes from v0.5:** `eligibility.eligible_audiences` and the audience registry are gone; `capability` is renamed `provides`; `serves` is renamed `population` and becomes a code list; `x-civic.status` is deleted in favour of core `status`; the federation model (`namespace`, `base_uri`, CURIE targets, `registry/peers.json`) is withdrawn pending a real use for it; `pcs_subject` becomes `subject`; the `offer` and `meal-site` record types are no longer part of the profile.

## What this profile requires

Four fields, plus the profile declaration, on the one record describing the organization:

```yaml
type: org                                # core OKF — the only field core requires
x-civic:
  profile: civic/0.6
  subject: [SS030601, SS030600]           # Candid PCS Subject facet
  population: [PG010000, PG030000]        # Candid PCS Population facet
  org_type: EA040000                      # Candid PCS OrgType facet
  registration_country: US                # ISO 3166-1 alpha-2
```

That is the entire normative content of the profile. Everything else in this document is either an explanation of why, or an **optional** convention.

### Why these four

They are the questions you cannot answer *about* an organization without asking the organization, and which every consumer needs before it can do anything else:

| Field | Question | Vocabulary |
|---|---|---|
| `subject` | What does it do? | PCS **Subject** — 867 codes, 18 top-level branches |
| `population` | Who does it serve? | PCS **Population** — 802 codes, 11 categories |
| `org_type` | What kind of organization is it? | PCS **OrgType** — 93 codes |
| `registration_country` | Under whose law does it exist? | ISO 3166-1 alpha-2 |

Mission area, demographics served, organizational form, and jurisdiction. Nothing else is required because nothing else is *always* knowable — and a required field that cannot always be filled in is a field that gets faked.

### Two conformance levels, and this one cannot break the other

This distinction matters more than any field in the profile.

**Core OKF v0.2 conformance** (§11) requires three things: parseable frontmatter on every non-reserved `.md`, a non-empty `type` in each, and `index.md`/`log.md` following §8/§9 when present. §11 also says a consumer **MUST NOT** reject a bundle for unknown additional frontmatter keys, unknown `type` values, missing optional fields, or broken cross-links.

**So nothing under `x-civic` can make a bundle non-conformant with OKF.** A generic OKF reader ignores the whole namespace. That is what "namespaced and additive" buys, and it is why the profile is safe to propose.

**civic/0.6 conformance** is therefore a **promise a record opts into** by declaring `x-civic.profile`. If you declare it and omit `population`, your declaration is false — but your bundle is still perfectly good OKF. `scripts/validate.py` reports the two levels separately for exactly this reason.

## What is NOT required, and why that is the design

Every bundle in this collection carries far more than four fields. All of it is optional, and it is what makes a bundle worth reading:

| Optional | What it adds |
|---|---|
| `provides` | The specific function the organization offers, as a substitution/matching axis |
| `registration.{scheme,id,tax_status,legal_form}` | How to look the organization up, where a registry exists |
| `budget_currency`, budget figures | Size, in a stated currency |
| `operating_locations`, `situation` | Where it works, as distinct from where it is registered |
| `ntee`, `sdg` | Additional classification layers |
| `relations` | Asserted organization-to-organization edges (`partners_with`, `coalition_with`, `learn_with`) |
| `verifiable_by` | Who could answer "how do I know this?" |
| `org_type_note`, `classification_note` | Why a code was chosen, or deliberately not assigned |
| Whole documents | `population.md`, `programs.md`, `impact.md`, `what_i_need_funding_for.md`, `technology/`, `technical-volunteers/`, `verification.md` |

**The rule: a required field must be answerable by every organization in the world. Anything else is an enrichment.** The three international bundles in this collection exist to test that rule, and one of them — [Nyando](../organizations/synthetic-nyando-community-health-trust/README.md), which has no usable registry record — is the reason `registration.id` is not required.

## Classification: why Candid PCS

The profile binds three of its four required fields to Candid's [Philanthropy Classification System](https://taxonomy.candid.org). Three reasons.

**1. It has the facets we need, already separated.** Subject answers *what*, Population answers *who*, OrgType answers *what kind*. Most sector vocabularies conflate at least two of those.

**2. It is not jurisdictional.** This is the finding that decided it. **NTEE is maintained by the US IRS and classifies US tax-exempt entities**, so it cannot apply to a Polish *fundacja*, a Colombian *corporación*, or a Kenyan trust. An NTEE-based rollup over this collection silently returns twelve of fifteen — no error, no null, the three international organizations simply are not in the result set. PCS Subject and Population classify *activity and people*, which every organization has regardless of tax status.

**3. It ships its own NTEE crosswalk.** 555 of 867 Subject codes carry a former NTEE/GCS code. The twelve US organizations in this collection were crosswalked **mechanically** through that column rather than assigned by hand. That is the difference between a code you can defend and a code you remembered.

**One honest caveat.** PCS is not *uniformly* jurisdiction-neutral. Candid's own scope note for `EA040000` (Public charities) describes US 501(c) organizations specifically. The generic parents are neutral, which is why the two organizations whose legal form has no PCS equivalent — the Colombian *corporación* and the Kenyan trust — sit at the level-1 `EA000000` (Non-governmental organizations) and say so in `org_type_note`. **Using a parent code deliberately is better than forcing a closer-looking child**, and better still than inventing one.

### Don't fabricate codes

Earlier versions of this collection shipped an empty `_shared/pcs/` folder with a document explaining that assigning codes from memory would put invented identifiers into a real vocabulary's namespace. That reasoning was right. It has now been **satisfied rather than abandoned**: every code was read out of Candid's published 2024 taxonomy, and the subset in use is vendored as [`_shared/pcs/pcs-codes.json`](../_shared/pcs/pcs-codes.json) with attribution, so tooling runs offline.

The rule stands for anyone extending this: **an empty slot documented as empty is a better artifact than a folder of plausible-looking codes somebody made up.**

> **Attribution.** The Philanthropy Classification System is © Candid, available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: <https://taxonomy.candid.org>. A producer using PCS codes must credit Candid and indicate modifications, and must not charge users a premium for the ability to use PCS. This profile *recommends* PCS; a bundle MAY use another vocabulary, but interoperating tools will expect PCS.

## Geography

`registration_country` is required, as ISO 3166-1 alpha-2. Sub-national placement is optional (`operating_locations`, and a `situation` node edge).

**Registration country and operating geography are different facts** and the profile keeps them apart. An INGO registered in the United States and working in Kenya has `registration_country: US`; a query for "organizations working in Kenya" finds it only through the optional operating layer. That is a deliberate trade: making the operating layer required would fail organizations that cannot enumerate where they work.

PCS has no geography facet, which is why this one field is not PCS-bound.

## Two layers of link, and the one this profile actually cares about

Core OKF §6.1 says links are **untyped**: "the specific kind is conveyed by the surrounding prose, not by the link itself." This profile does not fight that. It adds one distinction on top.

**Controlled edges live in frontmatter.** The required PCS codes and country are frontmatter values, not prose links. They generate the hub nodes in [`_shared/`](../_shared/index.md), and the hub membership lists are **derived** from them by `scripts/build_hubs.py` — never hand-maintained. Frontmatter is authoritative; the hub is a projection.

**Emergent terms live in prose, as wikilinks that resolve to nothing.**

```markdown
The five largest communities are [[Hmong]], [[Karen]], [[Somali]], [[Oromo]], and [[Latino]].
```

There is no `Hmong.md`. There does not need to be one. §6.1 requires a consumer to tolerate a link whose target does not exist because "it may simply represent not-yet-written knowledge" — so an unresolved wikilink is not a broken link, it is a **proto-hub**.

This is the profile's central claim about how a civic vocabulary should grow. PCS Population has exactly one code for LGBTQIA+ people (`PC010000`), one for immigrants and migrants (`PG010000`), one for farm workers (`PJ130000`). Those codes are correct, queryable, and comparable across producers. They are also the least interesting true thing about who any real organization serves. An organization that writes `[[Mixteco]]`, `[[Triqui]]`, `[[consejos comunitarios]]`, or `[[returning citizens]]` is making a distinction that matters to its work and that no committee ratified.

**The controlled vocabulary makes bundles comparable. The emergent one makes them true.** When enough producers reach for the same term independently, that shape becomes visible, and *then* someone writes the page and it becomes a real node. Vocabulary grows from below instead of being issued from above.

Practically: **a wikilink that resolves to a file is a mistake** — use a markdown link, so a plain OKF consumer sees the edge. `scripts/validate.py` enforces that, and reports unresolved terms as information rather than error. `--terms` lists them.

### Asserted vs computed edges

Optional `x-civic.relations` records organization-to-organization edges that **cannot be computed**: `partners_with`, `coalition_with`, `learn_with`. A referral agreement between a food shelf and an immigration practice is a fact about the world.

What is *not* stored, because it is derivable: "these two organizations are substitutes" (same `provides`, same place), "these two complement each other" (different `provides`, same place, same `population`). Deriving those is a query, not a field. **That is most of the argument for why the required set stays small** — much of the useful graph is computed from four fields plus a place.

## What core OKF v0.2 now handles, so this profile does not

This section is mostly a list of things deleted from v0.5. Anyone who read the earlier profile should read it.

| Need | v0.5 carried | v0.2 core does it with |
|---|---|---|
| Where did this claim come from? | a custom `provenance` block | **`sources`** with `id`, plus markdown footnotes keyed to `sources[].id` (§5.1) |
| Per-source trustworthiness | — | `author`, `usage_count`, `last_modified` credibility signals (§5.1) |
| Who confirmed it? | a determination log | **`verified: [{by, at}]`** + the actor convention `human:`/`process:` (§5.2, §7) |
| How much should I trust it? | confidence scores | **trust tiers** derived from `verified` — unverified / machine-confirmed / human-reviewed (§5.3) |
| Is it still true? | `last_audited` | **`stale_after`**, an absolute date (§5.5) |
| Record lifecycle | `x-civic.status`, a 5-state enum | **`status: draft \| stable \| deprecated`** (§5.4) |
| Last content change | `timestamp` | **`generated: {by, at}`** (§5.2, §13.1) |

Two consequences worth stating plainly.

**"Nobody has verified this" is a first-class state and always was.** A record with no `verified` key is *unverified* under §5.3, and §11 forbids a consumer from rejecting it. [Nyando](../organizations/synthetic-nyando-community-health-trust/verification.md) — the organization a verification process could not establish either way — needs no special field. It just has no `verified` key. The profile does not need to invent a way to say *I don't know*.

**A lapsed determination is a date comparison.** [Crescent City Career Lab](../organizations/synthetic-crescent-city-career-lab/verification.md) was approved and its determination expired; its `stale_after` is in the past. No lifecycle machinery required.

## Verification is a path, not a passport

A bundle does not carry a credential. It carries the facts an eligibility decision keys off — `org_type` and `registration_country`, both required — and, optionally, a pointer to who could adjudicate.

```yaml
x-civic:
  verifiable_by: [techsoup]     # optional: who can answer "how do I know?"
```

The distinction: `sources` says *where this came from*; `verifiable_by` says *who you can ask*. A determination is a moment in time and belongs outside the bundle — obtained at query time from TechSoup, GlobalGiving, Charity Navigator, or whoever the consumer trusts. The optional `verification.md` document in each bundle records that somebody looked, when, and what they could not establish, on core `verified` + `stale_after`.

**This is why confidence scores are not a profile field.** Frogtown Table would score 0.88 and Motor City Trades 0.96, at 7.5× the budget with three participant systems that disagree. Both numbers would be correct. **Verification confidence measures how much of an organization exists in retrievable form** — which tracks size, regulatory burden, and proximity to institutions that generate paperwork, and does not track competence. Standardizing a field for it would invite exactly the ranking it cannot support.

## Money

Optional, and if present: **an amount carries its currency** (`budget_currency`, ISO 4217) and **is not converted**. A figure converted to USD is an exchange rate on an unstated date pretending to be a fact about an organization. If a view needs one currency, it converts at read time with a rate it can cite.

Where two figures disagree — [Eastside Harvest](../organizations/synthetic-eastside-harvest-collective/README.md) has a self-reported budget and a filed return 47% apart — **the bundle carries both and refuses to pick.** A single-valued field forces a choice and launders one number into a fact. (OKF §10's Attested Computation is the eventual right home for "was this number produced the way we said"; out of scope here.)

## Document conventions

Not required, but this is what the bundles do and it is worth copying.

- **`README.md` is the canonical record** and carries the frontmatter. Consumers should find the organization by `type: org`, not by filename — the filename is a convention for humans.
- **`index.md` is a listing** and carries no frontmatter except `okf_version` on a bundle root (§8, §12).
- **`log.md` records changes to the bundle**, in §9's date-grouped form. It is *not* where determinations go; that separation is deliberate.
- **`generated.by` records who owns a document.** A bundle's `technical-volunteers/constraints.md` carries `human:org-staff` because the organization authored it and it is binding on anything scoping work from the bundle. A tool reading a bundle can tell from the actor which documents are not its to rewrite. This replaces the per-record `authority` field an earlier draft proposed — the actor convention already does the job.
- **Mark synthetic data at the record level.** `synthetic: true` on every fabricated record, not only on the collection README, because files get separated from their context. Note this is a *producer* key at the top level, not under `x-civic` — "is this real" is not civic-specific, and we think it belongs in core OKF. That is a proposal for upstream, not a profile field.

## Relationship to Open Referral / HSDS

For human-services data, the sector's established standard is **[Open Referral / HSDS](https://docs.openreferral.org/)** v3.0.1 — UUID-keyed objects (`Organization`, `Service`, `Location`, `Eligibility`) in JSON Schema, serialized as datapackages, with an API.

**This profile aligns to HSDS rather than competing with it.** HSDS is the structured *data-exchange* layer; OKF + `x-civic` is the human- and AI-readable *knowledge* layer beside it. For overlapping fields they round-trip:

| This profile | HSDS 3.0.1 |
| :--- | :--- |
| an org bundle (`type: org`) | `Organization` |
| `title` | `organization.name` |
| `x-civic.registration.id` | `organization.tax_id` / external identifier |
| `x-civic.operating_locations` | `Location` |
| `x-civic.population` | `Eligibility` (partially) |
| `programs.md` | `Service` (one per program, when broken out) |
| `x-civic.subject` | `taxonomy_term` |
| `x-civic.provides` (substitution axis) | *no direct HSDS object* |
| document bodies — gotchas, constraints, context | *no HSDS equivalent* |

What OKF adds: **verbose, agent-ready context** (the prose a model needs to actually advise someone), human editability in Git, and an emergent vocabulary layer. What HSDS does better: strict validation, relational integrity, a mature exchange ecosystem.

## Alignment with the OKF spec discussion

- **Untyped links** — §6.1. The profile adds typed edges only in frontmatter and does not overload link syntax. It no longer implements the link-title token convention proposed in issue [#101](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/101); a reader MAY accept those tokens, but this profile authors edges in frontmatter.
- **Lifecycle and provenance** — issue [#120](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/120) proposed `status`, a relationship index, and a rationale trail as core conventions. v0.2 delivered most of it, and this profile now uses core `status` rather than its own enum.
- **Freshness** — issues [#94](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/94) and [#97](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/97); handled by `stale_after` and `sources[].last_modified` in v0.2.

## Open questions for the community

1. **Should `synthetic` be core?** "Is this record about a real thing" is not civic-specific, and a marker no consumer is required to check is a marker that fails. We would rather propose it upstream than keep it as a producer key.
2. **Is four the right number?** We think a domain profile should require almost nothing. Is `org_type` pulling its weight, given that `registration_country` plus `subject` already narrows a lot?
3. **A shared vocabulary for `provides`.** The substitution/matching axis is where the sector would get the most from convergence, and it is the one field here with no controlled vocabulary behind it. PCS **Strategy** (`UD000000` capacity-building, `UF000000` capital and infrastructure, `UB000000` regranting) may be the right binding for the funding side of it.
4. **Emergent-term promotion.** When does an unresolved term become a real node, who writes it, and how is ambiguity handled? `[[Karen]]` is a people of Myanmar and also a common given name. A shared namespace with no disambiguation eventually collides, and we do not have an answer.
5. **Should a profile version pin an OKF version?** `civic/0.6` assumes v0.2 semantics throughout. Nothing currently expresses that dependency.
