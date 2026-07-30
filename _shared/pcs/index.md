# PCS classification hubs — the required layer

**⚠ Part of a synthetic collection. Every organization listed in these hubs is fabricated** — see the [collection README](../../README.md). **The codes themselves are real.**

Candid's **Philanthropy Classification System** is the controlled vocabulary that `civic/0.6` requires. Three of its five facets carry the profile's three required classification keys:

| Facet | `x-civic` key | Answers | Nodes here |
|---|---|---|---|
| Subject | `subject` | what an organization does | 19 |
| Population | `population` | who it serves | 17 |
| OrgType | `org_type` | what kind of organization it is | 3 |

PCS also has **Strategy** and **Transaction** facets, which this collection does not yet use; they are the natural vocabulary for describing how support and money flow between organizations.

## This folder used to be empty, and the reason it no longer is

Earlier versions of this collection shipped `_shared/pcs/` deliberately empty, because assigning codes from memory would have put invented identifiers into a real vocabulary's namespace. That reasoning was right and it has been satisfied rather than abandoned: every code below was read out of Candid's published 2024 taxonomy, and the US organizations' codes were **crosswalked mechanically** through the taxonomy's own former-NTEE column rather than guessed. Titles and scope notes are Candid's, unmodified. The subset in use is vendored as [`pcs-codes.json`](pcs-codes.json) so nothing here needs the network.

**Nothing was fabricated to fill this folder.** Where a code genuinely did not fit — the Colombian *corporación* and the Kenyan trust have no PCS OrgType level-2 equivalent — the level-1 parent is used deliberately and the record says so, which is still better than forcing a closer-looking child.

## PCS reaches all fifteen; NTEE reaches twelve

This is the finding that made PCS the required layer. NTEE is maintained by the US IRS and cannot apply to the Polish, Colombian, or Kenyan organizations — an NTEE rollup silently covers 80% of this collection, with no error and no null. PCS Subject and Population classify *activity and people* rather than tax status, so they apply everywhere.

One honest caveat: **PCS is not uniformly jurisdiction-neutral.** Candid's own scope note for `EA040000` (Public charities) describes US 501(c) organizations specifically. The generic parents are neutral, which is why the two non-US organizations without a matching form sit at `EA000000`.

## Subject — `subject`

* [SB040000 — Vocational education](SB040000.md) - 1 member(s) *(← NTEE B30)*
* [SC030000 — Natural resources](SC030000.md) - 1 member(s) *(← NTEE C30)*
* [SC030100 — Air quality](SC030100.md) - 2 member(s) *(← NTEE C21)*
* [SC030400 — Water resources](SC030400.md) - 1 member(s) *(← NTEE C32)*
* [SC030407 — Water pollution](SC030407.md) - 1 member(s) *(← NTEE C22)*
* [SE040200 — Community health care](SE040200.md) - 2 member(s) *(← NTEE E21)*
* [SE050000 — Out-patient medical care](SE050000.md) - 1 member(s) *(← NTEE E30)*
* [SE050100 — Health care clinics](SE050100.md) - 2 member(s) *(← NTEE E32)*
* [SE130200 — Environmental health](SE130200.md) - 1 member(s) *(← NTEE E78)*
* [SE130700 — Water access, sanitation and hygiene](SE130700.md) - 1 member(s)
* [SJ040000 — Legal services](SJ040000.md) - 3 member(s) *(← NTEE I80)*
* [SJ040700 — Public interest law](SJ040700.md) - 2 member(s) *(← NTEE I83)*
* [SM010000 — Agriculture](SM010000.md) - 1 member(s) *(← NTEE K20)*
* [SN020300 — Employment](SN020300.md) - 2 member(s)
* [SN020302 — Job training](SN020302.md) - 3 member(s) *(← NTEE J22)*
* [SR040100 — Immigrant and refugee rights](SR040100.md) - 1 member(s) *(← NTEE R21)*
* [SS030600 — Food aid](SS030600.md) - 3 member(s) *(← NTEE K30)*
* [SS030601 — Food banks](SS030601.md) - 2 member(s) *(← NTEE K31)*
* [SS090300 — Immigrant and refugee services](SS090300.md) - 4 member(s)

## Population — `population`

* [PA010000 — Children and youth](PA010000.md) - 2 member(s) *(← NTEE A2)*
* [PA020000 — Adults](PA020000.md) - 1 member(s) *(← NTEE A5)*
* [PA020300 — Older adults](PA020300.md) - 1 member(s) *(← NTEE A6)*
* [PE030000 — Black/African people](PE030000.md) - 1 member(s) *(← NTEE E2)*
* [PG010000 — Immigrants and migrants](PG010000.md) - 4 member(s)
* [PG010200 — Migrant workers](PG010200.md) - 2 member(s) *(← NTEE P2)*
* [PG010400 — Refugees and displaced people](PG010400.md) - 2 member(s) *(← NTEE O2)*
* [PG010700 — Undocumented immigrants](PG010700.md) - 1 member(s)
* [PG030000 — Economically disadvantaged people](PG030000.md) - 9 member(s) *(← NTEE P0)*
* [PG040000 — Justice-involved people](PG040000.md) - 1 member(s)
* [PG040300 — Detainees](PG040300.md) - 1 member(s)
* [PG090000 — People living in rural areas](PG090000.md) - 6 member(s)
* [PG100000 — People living in urban areas](PG100000.md) - 4 member(s)
* [PH040000 — Pregnant people](PH040000.md) - 1 member(s)
* [PJ020000 — Unemployed people](PJ020000.md) - 3 member(s)
* [PJ080000 — Farmers](PJ080000.md) - 1 member(s)
* [PJ130000 — Farm workers](PJ130000.md) - 3 member(s)

## OrgType — `org_type`

* [EA000000 — Non-governmental organizations](EA000000.md) - 2 member(s) *(← NTEE N)*
* [EA030000 — Foundations](EA030000.md) - 1 member(s)
* [EA040000 — Public charities](EA040000.md) - 12 member(s) *(← NTEE PC)*

*Every Members list in this folder is generated by `scripts/build_hubs.py` from the organizations' required frontmatter. Do not edit them by hand.*
