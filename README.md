---
type: bundle-collection
title: Civic Knowledge Sample
description: Fifteen synthetic nonprofit organization bundles in the Open Knowledge Format, plus the x-civic civic profile they conform to.
resource: https://github.com/TechSoup/okf-civic-sample
tags: [okf, civic-profile, org-bundle, synthetic, sample-data]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  maintainer: TechSoup
---

# Civic Knowledge Sample — civil-society knowledge as Open Knowledge Format bundles

> Fifteen synthetic nonprofit organization bundles, a graph you can query, and a five-field profile extension for the civic sector.

![license: CC BY-SA 4.0](https://img.shields.io/badge/license-CC_BY--SA_4.0-blue)
![format: OKF v0.2](https://img.shields.io/badge/format-OKF_v0.2-success)
![civic profile: v0.6](https://img.shields.io/badge/civic_profile-v0.6-orange)
![maintained by TechSoup Global Network](https://img.shields.io/badge/maintained_by-TechSoup_Global_Network-7B2FBE)

**[Learn more about TechSoup](https://about.techsoup.org/) · [Support TechSoup](https://www.every.org/techsoup)**

> ## ⚠ EVERY ORGANIZATION IN THIS COLLECTION IS FABRICATED
>
> All fifteen organizations are **invented**. The names, registration numbers, addresses, websites, budget figures, staff, programs, technology inventories, verification determinations, and volunteer projects are made up. Nothing here describes a real nonprofit.
>
> Every folder name and title carries a `synthetic-` prefix. Every record carries `synthetic: true` in its frontmatter — at the **record** level, not just here, because files get separated from their README.
>
> **Do not** load this collection into a production graph, count these organizations in any total, cite a figure from them, or let a script that writes to real systems read them without a `synthetic: true` filter.
>
> Two things here are **not** fabricated, and are marked `synthetic: false`: the **Candid PCS classification codes** and the **places**. Those are real. The reasoning is in [`_shared/`](_shared/index.md).

## What this is

A reference implementation showing how a nonprofit organization can be described in Google's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) — plain markdown with YAML frontmatter, no database, no platform, no lock-in — plus a proposed **civic profile** (`x-civic`) for the handful of things the sector needs that core OKF deliberately leaves open.

It is also a working **Obsidian vault**. Clone it, open the folder in [Obsidian](https://obsidian.md), and open graph view. The clusters, the cross-border coalition edges, and the unresolved emergent terms are all visible immediately.

**Start with [`organizations/synthetic-frogtown-community-table/`](organizations/synthetic-frogtown-community-table/README.md).** It is the worked reference: the smallest organization in the set, the tidiest, and the one carrying the fullest explanation of why the frontmatter looks the way it does.

## Layout

```
organizations/     the fifteen org bundles, one folder each — see its own README
_shared/           classification and place nodes the bundles link to
docs/              the civic profile, worked use cases, and the field-level data dictionary
schemas/           JSON Schema for the profile, plus fixtures that must fail
scripts/           validator, hub generator, PCS extractor, per-org JSON export, and schema-mapping (e.g. PDC)
```

Everything that describes an organization is under [`organizations/`](organizations/README.md), which carries its own README covering what the bundles are for, what is in one, and which three are deliberately broken.

## The profile is five fields

`civic/0.6` requires this much, on the one record with `type: org`:

```yaml
x-civic:
  profile: civic/0.6
  subject: [SS030601, SS030600]          # Candid PCS Subject — what it does
  population: [PG010000, PG030000]       # Candid PCS Population — who it serves
  org_type: EA040000                     # Candid PCS OrgType — what kind of organization
  registration_country: US               # ISO 3166-1 alpha-2
```

That is the whole thing. Core OKF requires only `type`; the profile adds four bindings to controlled vocabularies and stops.

Everything else the bundles carry — programs, populations in prose, impact narratives, funding priorities in the organization's own voice, technology inventories, capability assessments, volunteer constraints and requests, partnership and coalition edges, budgets, SDG and NTEE codes, place nodes, third-party determinations — is **optional enrichment**. It makes a bundle far more useful and **none of it affects conformance**. See [`docs/civic-profile.md`](docs/civic-profile.md) for the reasoning, [`docs/use-cases.md`](docs/use-cases.md) for what the optional layers buy you, and [`docs/data-dictionary.md`](docs/data-dictionary.md) for the field-by-field reference.

## The idea worth stealing: two layers of link

**Required frontmatter edges are controlled.** PCS Subject, PCS Population, OrgType, ISO country. They generate the hub pages in [`_shared/`](_shared/index.md), and they are what make a bundle comparable to any other producer's bundle anywhere.

**Prose wikilinks are emergent.** An organization writing `[[Karen]]`, `[[Mixteco]]`, `[[consejos comunitarios]]`, or `[[Dholuo]]` about the people it serves is authoring a term nobody pre-approved. OKF v0.2 §6.1 requires a consumer to tolerate a link whose target does not exist — "it may simply represent not-yet-written knowledge" — so an unresolved wikilink is not an error, it is a **proto-hub**. When enough bundles reach for the same term, the shape becomes visible in the graph and somebody can write the page.

This matters because PCS Population has exactly one code for LGBTQIA+ people, one for immigrants and migrants, one for farm workers. Those codes are correct, and they are the least interesting true thing about who any of these organizations serves.

**The controlled vocabulary makes bundles comparable. The emergent one makes them true.** A bundle needs both layers, and only one of them is required.

Run `python3 scripts/validate.py --terms` to see every emergent term in the collection and how many records reach for it.

## The fifteen

All under [`organizations/`](organizations/README.md). Three organizations in each of five program areas, scattered across geography on purpose so the program areas do not collapse into isolated islands. Sizes span roughly $430K to $7.9M and the equivalent in local currency abroad.

| Organization | Program area | Place | Rough size | State |
|---|---|---|---|---|
| [Frogtown Community Table](organizations/synthetic-frogtown-community-table/README.md) | Food security | Saint Paul, MN | $430K | **worked reference** |
| [Eastside Harvest Collective](organizations/synthetic-eastside-harvest-collective/README.md) | Food security | Detroit, MI | $1.4M | ⚠ budget unreconciled |
| [Valle Verde Food Network](organizations/synthetic-valle-verde-food-network/README.md) | Food security | Fresno County, CA | $2.1M | clean |
| [Riverbend Air Alliance](organizations/synthetic-riverbend-air-alliance/README.md) | Environmental justice | Detroit, MI | $680K | clean |
| [Gulf Corridor Justice Project](organizations/synthetic-gulf-corridor-justice-project/README.md) | Environmental justice | New Orleans, LA | $1.5M | clean |
| [Corporación Río Vivo](organizations/synthetic-corporacion-rio-vivo/README.md) | Environmental justice | Cali, **Colombia** | COP 1,900M | clean |
| [Motor City Trades Institute](organizations/synthetic-motor-city-trades-institute/README.md) | Workforce training | Detroit, MI | $3.2M | clean |
| [Black Mountain Workforce Partnership](organizations/synthetic-black-mountain-workforce-partnership/README.md) | Workforce training | Letcher County, KY | $920K | clean |
| [Crescent City Career Lab](organizations/synthetic-crescent-city-career-lab/README.md) | Workforce training | New Orleans, LA | $1.7M | ⚠ determination lapsed |
| [Central Valley Farmworker Law Center](organizations/synthetic-central-valley-farmworker-law-center/README.md) | Legal aid & immigration | Fresno County, CA | $1.8M | clean |
| [North Star Immigrant Defense](organizations/synthetic-north-star-immigrant-defense/README.md) | Legal aid & immigration | Saint Paul, MN | $2.6M | clean |
| [Fundacja Prawo i Schronienie](organizations/synthetic-fundacja-prawo-i-schronienie/README.md) | Legal aid & immigration | Warsaw, **Poland** | PLN 4.8M | clean |
| [Sierra Foothills Community Health](organizations/synthetic-sierra-foothills-community-health/README.md) | Rural health | Fresno County, CA | $7.9M | clean |
| [Cumberland Gap Health Cooperative](organizations/synthetic-cumberland-gap-health-cooperative/README.md) | Rural health | Letcher County, KY | $1.1M | clean |
| [Nyando Community Health Trust](organizations/synthetic-nyando-community-health-trust/README.md) | Rural health | Kisumu County, **Kenya** | KES 62M | ⚠ evidence insufficient |

## What is deliberately broken

Three of the fifteen carry an unresolved problem, in three program areas, three countries, three *different* failure modes. If your tooling only ever sees the twelve clean ones, it is not tested.

1. **[Eastside Harvest Collective](organizations/synthetic-eastside-harvest-collective/README.md)** — eligible, but its self-reported budget and its filed return disagree by 47% and nobody reconciled them. The bundle refuses to pick a number. *Tests: does your code pick one, or notice there are two?*
2. **[Crescent City Career Lab](organizations/synthetic-crescent-city-career-lab/README.md)** — was approved, then the determination **expired**. Its `stale_after` is in the past. *Tests: does your code check freshness, or assume a determination on file means yes?*
3. **[Nyando Community Health Trust](organizations/synthetic-nyando-community-health-trust/README.md)** — organization-shaped but thinly sourced: no usable registry record, almost no web presence, and **no `verified` key at all**, which under OKF §5.3 is the *unverified* tier. *Tests: can your logic say "I don't know" instead of "no"?*

The third one is the important one. Core OKF makes "nobody has confirmed this" a first-class, non-rejectable state — §11 requires a consumer to accept it. That is not something this profile had to invent.

## The graph — what to explore

**1. Required classification → PCS hub.** Every organization links to [`_shared/pcs/`](_shared/pcs/index.md) nodes through its required frontmatter. This is the edge a rollup walks, and the only layer that reaches all fifteen.

**2. Place → situation node.** Eight [situation nodes](_shared/situations/index.md) hold community context, most hosting organizations from *different* program areas. Detroit has food security, environmental justice, and workforce training pointing at one place node. That is what makes "who else works here" answerable.

Read [Letcher County](_shared/situations/US-KY-letcher.md) for the strongest argument in the collection: two organizations in unrelated sectors, and **the same community fact — broadband — defeated a program at each.** One cause, two sectors, one address. Store connectivity as an organizational attribute and you record two independent weaknesses and miss that there is a single problem belonging to the county.

**3. Organization → organization.** Five same-place partnerships, drawn across program areas because that is how referral actually works — a food line is a legal-intake doorway, a farm crew is a trades pipeline.

**4. Edges that ignore geography.** A three-organization environmental-justice coalition spanning Detroit, New Orleans, and Cali; and a cross-border rural-health peer-learning pair, California and Kenya. Two clinics, wildly different stacks, same problem. **The organization with the closest peers is the one whose peers are farthest away** — see [Detroit](_shared/situations/US-MI-detroit.md).

## What building fifteen instead of one surfaced

**1. `ein` and `501(c)(3)` do not generalize.** Neither exists in Poland, Colombia, or Kenya. The required identity field is `registration_country`; the scheme and identifier are **optional**, because Nyando has no usable registry record and requiring an ID would make "insufficient evidence" unrepresentable.

**2. PCS reaches everywhere; NTEE cannot.** NTEE is an IRS vocabulary, so an NTEE rollup silently covers 80% of this collection — no error, no null, the three international organizations simply are not in the result set. PCS classifies *activity and people* rather than tax status. That is why PCS is the required layer and NTEE is optional. One honest caveat: PCS is not *uniformly* neutral — Candid's own scope note for `EA040000` (Public charities) describes US 501(c) organizations, which is why the two non-US organizations without a matching legal form sit at the generic `EA000000` and say so in `org_type_note`.

**3. Money needs a currency, and conversion is somebody else's job.** Every budget figure carries `budget_currency`. The international bundles state PLN, COP, and KES and **do not** convert, because a converted number is an exchange rate on an unstated date pretending to be a fact about an organization.

**4. Verification confidence measures legibility, not competence.** Frogtown Table scores 0.88 and runs the tidiest technology in the collection. Motor City Trades scores 0.96 at 7.5× the budget, with three participant systems that disagree and a CRM abandoned mid-implementation. Both numbers are correct and the ordering is the point. If you are building anything that ranks organizations on a confidence figure, that pair is your test case.

## Conformance

Two independent levels, and the second cannot affect the first:

- **Core OKF v0.2: conformant.** Every non-reserved `.md` has parseable frontmatter and a non-empty `type`; `index.md` is a listing carrying at most `okf_version`; `log.md` uses the §9 date-grouped shape. Provenance rides on `sources` with footnote attribution, trust on `generated`/`verified`, lifecycle on `status`/`stale_after`.
- **civic/0.6: conformant.** Every record declaring `x-civic.profile` satisfies the profile, and every `type: org` record carries the five required keys with codes that resolve against the vendored PCS subset.

Nothing under `x-civic` can make a bundle non-conformant with core OKF — §11 requires consumers to tolerate unknown keys. That is the whole reason the extension is namespaced.

```sh
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python scripts/validate.py           # both levels, plus hub freshness
./venv/bin/python scripts/validate.py --terms   # the emergent vocabulary
./venv/bin/python scripts/build_hubs.py         # regenerate every membership list
```

For per-organization JSON export and mapping a bundle's frontmatter onto another schema (a worked example targets [Philanthropy Data Commons](https://philanthropydatacommons.org/base-fields-list/)), see [`scripts/README.md`](scripts/README.md).

## The membership lists are generated

Every `<!-- GENERATED -->` block in [`_shared/`](_shared/index.md) is rebuilt from the organizations' own frontmatter by `scripts/build_hubs.py`, and `validate.py` fails if one is stale. Earlier versions of this collection maintained those lists by hand and documented the drift as a known problem; it is now a tool instead of a caveat.

## How to use it

**As sample data.** Build, test, break, and demo against it — a crosswalk script, a graph query, an eligibility rule, an agent that reads a bundle and drafts a volunteer request — without exposing a real organization's data to a prototype. Because it is synthetic you can paste it into any prompt, log, or transcript.

**As agent input.** Point a model at one bundle and ask what an organization would ask: *scope a volunteer project*, *summarize what we run*, *tell me what's missing*. Each bundle has enough structure to answer and enough gaps to be interesting. Note that a bundle's `technical-volunteers/constraints.md` is **org-authored and binding** — it carries `generated.by: human:org-staff`, and a tool that scopes work from a bundle must honor it.

**As a fixture.** Fifteen bundles, forty-odd shared nodes, three deliberate defects, stable file paths, a validator. Good enough to assert against.

**As an Obsidian vault.** Open the repo root as the vault so links resolve across bundle boundaries.

See [`docs/use-cases.md`](docs/use-cases.md) for worked examples with the queries written out.

## Extending it

Add a sixteenth by copying a bundle folder inside [`organizations/`](organizations/README.md), renaming it `synthetic-<something>`, rewriting the contents, and assigning PCS codes. Then run `scripts/build_hubs.py` — the hub membership lists, the situation rosters, and the `_shared/` indexes all rebuild themselves. If you use a PCS code the collection has not used before, run `scripts/extract_pcs.py` against Candid's published taxonomy first so its title and scope note get vendored.

**If you add a real organization to this collection, you have broken the one guarantee it makes. Don't.**

## Relationship to Open Referral / HSDS

For human-services data the sector's established standard is **[Open Referral / HSDS](https://docs.openreferral.org/)** (v3.0.1). This does not compete with it: HSDS is the structured *data-exchange* layer — normalized UUID-keyed objects, JSON Schema, an API — and OKF plus `x-civic` is the human- and AI-readable *knowledge* layer beside it. An organization bundle maps onto HSDS `Organization`; see the crosswalk in [`docs/civic-profile.md`](docs/civic-profile.md). What OKF adds is the verbose context a model needs to actually advise someone, human editability in Git, and the prose that has no HSDS equivalent. What HSDS does better is strict validation, relational integrity, and a mature exchange ecosystem.

## Licensing and attribution

Content licensed under [CC BY-SA 4.0](LICENSE) — deliberately viral, so derivatives stay open and credit the source.

The **Philanthropy Classification System** is © Candid, used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), unmodified. Source: <https://taxonomy.candid.org>. See [NOTICE](NOTICE).

## Contributing

This is a reference implementation and an open invitation — adopt the pattern, or argue with the profile. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgments

Developed with AI assistance: drafted and structured in collaboration with Anthropic's **Claude**, using **Claude Code**. The direction, data choices, profile design, and review were human (TechSoup). We name it in the spirit of showing the work.
