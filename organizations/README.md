---
type: bundle-collection
title: Organization bundles
description: Fifteen synthetic nonprofit organization bundles — enough shape to build against and enough content to experiment with.
tags: [okf, civic-profile, org-bundle, synthetic, sample-data]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-30T00:00:00Z }
x-civic:
  profile: civic/0.6
  maintainer: TechSoup
---

# Organization bundles

> Fifteen synthetic nonprofit organizations, one folder each. They exist to show the **shape** of an organization bundle, and to carry enough real content that you can actually build something against them.

> ## ⚠ EVERY ORGANIZATION IN THIS FOLDER IS FABRICATED
>
> All fifteen are **invented**. The names, registration numbers, addresses, websites, budget figures, staff counts, programs, technology inventories, verification determinations, and volunteer projects are made up. Nothing here describes a real nonprofit.
>
> Every folder name and title carries a `synthetic-` prefix, and every record carries `synthetic: true` in its frontmatter — at the **record** level, because files get separated from their README.
>
> **Do not** load these into a production graph, count them in any total, cite a figure from them, or let a script that writes to real systems read them without a `synthetic: true` filter.
>
> The classification codes and places these bundles link out to in [`../_shared/`](../_shared/index.md) are **real**, and marked `synthetic: false`. Only the organizations are invented.

## What these are for

Two things at once, and the second is the reason there is so much prose in them.

**They show the shape.** Each folder is a complete organization bundle in the Open Knowledge Format — plain markdown with YAML frontmatter, no database and no platform — conforming to the proposed `x-civic` civic profile. If you want to know what a bundle *is*, read one.

**They are big enough to experiment on.** A schema example would be twenty lines. These are not that. Each bundle carries programs, a population description, a technology inventory, a capability assessment, volunteer constraints and a scoped project request, a budget, classification codes, place and peer edges, and a dated verification determination. That is enough for a graph query to return something interesting, an eligibility rule to have edge cases, or a model to be asked a real question and have the material to answer it.

Because they are synthetic you can paste any of it into a prompt, a log, a bug report, or a demo without exposing anyone's data.

## Start here

**[`synthetic-frogtown-community-table/`](synthetic-frogtown-community-table/README.md)** is the worked reference — the smallest organization in the set, the tidiest, and the one carrying the fullest explanation of why the frontmatter looks the way it does. Read it before the others.

## Seeing the graph — open the repository root, not this folder

**Open the repository root as the Obsidian vault.** Not this folder, and not a single bundle.

Obsidian's graph is scoped to the vault. It indexes every markdown file underneath the vault root at any depth, so opening the root gets you every bundle *and* the classification and place nodes in [`../_shared/`](../_shared/index.md) that the bundles link to. Folders do not partition the graph, so there is nothing to gain by opening a subfolder.

Open *this* folder as the vault and `_shared/` falls outside it. Seventy-four nodes — the PCS, NTEE, SDG, and situation hubs — never appear, and the 110 links reaching for them cannot resolve. You keep the fifteen org clusters and the asserted peer edges between them, and you lose the classification clustering and the place nodes, which is most of what makes the graph worth looking at.

## The fifteen

Three organizations in each of five program areas, scattered across geography on purpose so the program areas do not collapse into isolated islands. Sizes span roughly $430K to $7.9M and the equivalent in local currency abroad.

| Organization | Program area | Place | Rough size | State |
|---|---|---|---|---|
| [Frogtown Community Table](synthetic-frogtown-community-table/README.md) | Food security | Saint Paul, MN | $430K | **worked reference** |
| [Eastside Harvest Collective](synthetic-eastside-harvest-collective/README.md) | Food security | Detroit, MI | $1.4M | ⚠ budget unreconciled |
| [Valle Verde Food Network](synthetic-valle-verde-food-network/README.md) | Food security | Fresno County, CA | $2.1M | clean |
| [Riverbend Air Alliance](synthetic-riverbend-air-alliance/README.md) | Environmental justice | Detroit, MI | $680K | clean |
| [Gulf Corridor Justice Project](synthetic-gulf-corridor-justice-project/README.md) | Environmental justice | New Orleans, LA | $1.5M | clean |
| [Corporación Río Vivo](synthetic-corporacion-rio-vivo/README.md) | Environmental justice | Cali, **Colombia** | COP 1,900M | clean |
| [Motor City Trades Institute](synthetic-motor-city-trades-institute/README.md) | Workforce training | Detroit, MI | $3.2M | clean |
| [Black Mountain Workforce Partnership](synthetic-black-mountain-workforce-partnership/README.md) | Workforce training | Letcher County, KY | $920K | clean |
| [Crescent City Career Lab](synthetic-crescent-city-career-lab/README.md) | Workforce training | New Orleans, LA | $1.7M | ⚠ determination lapsed |
| [Central Valley Farmworker Law Center](synthetic-central-valley-farmworker-law-center/README.md) | Legal aid & immigration | Fresno County, CA | $1.8M | clean |
| [North Star Immigrant Defense](synthetic-north-star-immigrant-defense/README.md) | Legal aid & immigration | Saint Paul, MN | $2.6M | clean |
| [Fundacja Prawo i Schronienie](synthetic-fundacja-prawo-i-schronienie/README.md) | Legal aid & immigration | Warsaw, **Poland** | PLN 4.8M | clean |
| [Sierra Foothills Community Health](synthetic-sierra-foothills-community-health/README.md) | Rural health | Fresno County, CA | $7.9M | clean |
| [Cumberland Gap Health Cooperative](synthetic-cumberland-gap-health-cooperative/README.md) | Rural health | Letcher County, KY | $1.1M | clean |
| [Nyando Community Health Trust](synthetic-nyando-community-health-trust/README.md) | Rural health | Kisumu County, **Kenya** | KES 62M | ⚠ evidence insufficient |

Twelve are clean. Three carry a deliberate defect, described below.

## What is in a bundle

Every folder has the same fourteen files, so anything you write against one works against all fifteen.

| File | What it holds |
|---|---|
| `README.md` | The canonical organization record. Carries the required `x-civic` frontmatter and the prose describing the organization |
| `index.md` | A plain listing of the folder — the progressive-disclosure entry point. No frontmatter but `okf_version` |
| `log.md` | Edit history for the bundle, date-grouped. Reserved, carries no frontmatter |
| `population.md` | Who the organization serves, in prose. Where the emergent vocabulary lives |
| `programs.md` | What it runs |
| `impact.md` | Outcomes and results, in the organization's own voice. Optional enrichment, not part of the published profile |
| `what_i_need_funding_for.md` | Funding priorities, in the organization's own voice. Optional enrichment, not part of the published profile |
| `verification.md` | A dated third-party determination about the organization — or, in one case, the absence of one |
| `technology/inventory.md` | What software it actually runs |
| `technology/capability.md` | An assessment of what it can do with that software |
| `technology/index.md` | Listing |
| `technical-volunteers/constraints.md` | **Org-authored and binding.** Carries `generated.by: human:org-staff` — a tool scoping work from a bundle must honor it |
| `technical-volunteers/<project>.md` | One scoped volunteer project request, named for the project |
| `technical-volunteers/index.md` | Listing |

## What is deliberately broken

Three of the fifteen carry an unresolved problem, in three program areas, three countries, three *different* failure modes. If your tooling only ever sees the twelve clean ones, it is not tested.

1. **[Eastside Harvest Collective](synthetic-eastside-harvest-collective/README.md)** — eligible, but its self-reported budget and its filed return disagree by 47% and nobody reconciled them. The bundle refuses to pick a number. *Tests: does your code pick one, or notice there are two?*
2. **[Crescent City Career Lab](synthetic-crescent-city-career-lab/README.md)** — was approved, then the determination **expired**. Its `stale_after` is a date in the past, and nothing in the record says the word "expired" — you get there by comparing that date to today. *Tests: does your code check freshness, or assume a determination on file means yes?*
3. **[Nyando Community Health Trust](synthetic-nyando-community-health-trust/README.md)** — organization-shaped but thinly sourced: no usable registry record, almost no web presence, and **no `verified` key at all**, which under OKF §5.3 is the *unverified* tier. *Tests: can your logic say "I don't know" instead of "no"?*

The third one is the important one. Core OKF makes "nobody has confirmed this" a first-class, non-rejectable state — §11 requires a consumer to accept it.

## How these connect to each other

The bundles are not isolated. Two kinds of edge run between and out of them, and they behave differently on purpose.

**Derived edges** come from required and optional frontmatter — `subject`, `population`, `org_type`, `ntee`, `sdg`, `situation`. They generate the membership lists in [`../_shared/`](../_shared/index.md) automatically, so a query for "food-security organizations" or "who else works in Detroit" resolves without anyone maintaining a list.

**Asserted edges** live in `x-civic.relations` and cannot be computed from anything: `partners_with`, `coalition_with`, `learn_with`. Nothing in the required frontmatter would ever pair a $7.9M California clinic network with a Kenyan community health trust, which is exactly why that edge had to be written down by a person.

## Adding a sixteenth

Copy a bundle folder, rename it `synthetic-<something>`, rewrite the contents, and assign PCS codes. Then run `../scripts/build_hubs.py` — the hub membership lists, the situation rosters, and the `_shared/` indexes all rebuild themselves from your frontmatter. If you use a PCS code the collection has not used before, run `../scripts/extract_pcs.py` against Candid's published taxonomy first so its title and scope note get vendored.

Validate with `../scripts/validate.py`, which checks core OKF v0.2 and civic/0.6 and fails if a generated list has gone stale.

**If you add a real organization to this folder, you have broken the one guarantee it makes. Don't.**

## More

- [Collection README](../README.md) — what the whole repository is, and the reasoning behind the profile
- [`docs/civic-profile.md`](../docs/civic-profile.md) — the `x-civic` profile, v0.6. Five required fields
- [`docs/use-cases.md`](../docs/use-cases.md) — worked examples with the queries written out
- [`docs/data-dictionary.md`](../docs/data-dictionary.md) — lookup tables for every file and frontmatter field in a bundle
- [`_shared/`](../_shared/index.md) — the classification and place nodes these bundles link to
