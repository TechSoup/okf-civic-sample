---
type: doc
title: What the graph makes answerable
description: Worked use cases against the synthetic collection, with the queries written out — and what each one needs beyond the four required fields.
tags: [okf, civic-profile, use-cases, sample-data]
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# What the graph makes answerable

> **⚠ Every organization in these examples is fabricated.** Every number below is made up. The point is the *shape* of the question and what it costs to answer.

The profile requires four fields. This document is the argument for why you would ever add a fifth.

Each use case below says what it needs, and the queries are real — they run against this repo. Nothing here needs a database, a server, or an index. It is a directory of markdown files and about fifteen lines of Python.

## Setup

Every example uses this much:

```python
import glob, os, re, yaml

def orgs():
    for p in sorted(glob.glob('organizations/synthetic-*/README.md')):
        fm = re.match(r'^---\n(.*?)\n---', open(p).read(), re.S).group(1)
        d = yaml.safe_load(fm)
        d['_slug'] = os.path.dirname(p)
        yield d
```

---

## 1. "Who else does what we do?" — four required fields, nothing more

The narrowest useful question, and it needs **only the required layer**.

```python
target = 'SS030600'   # PCS Subject: Food aid
for o in orgs():
    if target in o['x-civic']['subject']:
        print(o['title'])
```

Returns Frogtown Community Table, Eastside Harvest Collective, and Valle Verde Food Network — in three states, doing recognizably different work.

**And that is the limit worth seeing.** One runs mobile pantry routes to unincorporated communities with no grocery store, one farms vacant urban land, one stocks a shop-style shelf for five immigrant communities' cooking. Their procurement, storage, staffing, language requirements, and definitions of success have almost nothing in common. `SS030600` is true of all three and tells you very little about any of them.

**A classification code is a filter, not a similarity measure.** Hold that whenever a code is used as a proxy for "these are alike."

---

## 2. "Who else works here?" — needs the optional place layer

This is the question that pays for a shared place node, and it cannot be answered from the four required fields.

```python
by_place = {}
for o in orgs():
    s = o['x-civic'].get('situation')
    if s: by_place.setdefault(s, []).append(o['title'])
```

Detroit returns a food-security organization, an air-quality project, and a trades institute. **Three program areas, one city, sharing almost nothing except an address** — which is exactly why the answer is useful. A referral, a joint funding approach, and a shared-services conversation all start here.

**What it costs:** one optional field (`situation`) and one shared node per place.

### The strongest case in the collection

[Letcher County, Kentucky](../_shared/situations/US-KY-letcher.md) hosts two organizations in unrelated sectors — a rural clinic and a workforce training organization. **The same community fact defeated a program at each of them:** the county's broadband availability killed the clinic's telehealth and undermines the workforce organization's remote-work track.

One cause. Two sectors. Two organizations. One address.

Store connectivity as an *organizational* attribute and you record two independent technology weaknesses and never see that there is a single problem belonging to the county. That is what a situation node is for, and no amount of per-organization data substitutes.

---

## 3. "Find complementary services for the same person" — needs `provides` + place + population

The referral question. Two organizations in one place with **different** `provides` and **overlapping** `population` are a stack a single person can walk.

```python
from itertools import combinations
for a, b in combinations(list(orgs()), 2):
    xa, xb = a['x-civic'], b['x-civic']
    if xa.get('situation') != xb.get('situation'): continue
    if xa.get('provides') == xb.get('provides'): continue
    shared = set(xa['population']) & set(xb['population'])
    if shared:
        print(f"{a['title']} + {b['title']}  shared population: {sorted(shared)}")
```

The pairs this surfaces are the useful kind. In Saint Paul, a **food shelf** and an **immigration legal defense practice** share `PG010000` (immigrants and migrants). An immigration question surfaces at a food shelf long before it reaches a law office — which is why one of them holds monthly clinic hours in the other's back room.

**Note what the query did not need:** nobody wrote down "these two complement each other." It is computed from `provides` + `situation` + `population`. That is the argument for keeping the required set small — **most of the useful graph is derivable, so it should not be a field.**

Flip the two conditions — same `provides`, same place — and you get substitutes instead: the organizations a person could be referred to *instead*.

---

## 4. "Where could funding flow?" — needs `provides`, and PCS Strategy would help

A funder's version of the same query. What a funder provides and what an organization needs are the same axis read from two ends.

```python
need = 'workforce-training'
for o in orgs():
    if o['x-civic'].get('provides') == need:
        print(o['title'], o['x-civic']['registration_country'], o['x-civic'].get('budget_currency'))
```

Three organizations, at $3.2M, $1.7M, and $920K, in Detroit, New Orleans, and rural Kentucky. Same function, three wildly different operating contexts — and one of them ([Crescent City](../organizations/synthetic-crescent-city-career-lab/verification.md)) has a determination that has expired, which a funder needs to know before wiring anything.

**What is missing and would be worth adding:** PCS has a **Strategy** facet — `UD000000` capacity-building and technical assistance, `UF000000` capital and infrastructure, `UB000000` regranting, `UJ000000` network-building — and a **Transaction** facet for grant types. This collection does not use either yet. They are the natural vocabulary for describing how support moves between organizations, and they already exist, so nobody has to invent one. See the open questions in [the profile](civic-profile.md).

---

## 5. "Which of these can I trust today?" — needs nothing from the profile at all

This is entirely core OKF v0.2, and it is worth demonstrating precisely because the profile contributes nothing.

```python
from datetime import date
for p in sorted(glob.glob('organizations/synthetic-*/verification.md')):
    d = yaml.safe_load(re.match(r'^---\n(.*?)\n---', open(p).read(), re.S).group(1))
    v = d.get('verified')
    tier = 'unverified' if not v else (
        'human-reviewed' if str(v.get('by','')).startswith('human:') else 'machine-confirmed')
    stale = d.get('stale_after') and d['stale_after'] < date.today()
    print(f"{p.split('/')[0]:52} {tier:17} {'STALE' if stale else 'current'}")
```

Three distinct outcomes across the fifteen, and all three are ordinary spec behaviour:

| Organization | Trust tier | Freshness | Why it matters |
|---|---|---|---|
| Most of the fifteen | machine-confirmed | current | `verified.by` is a `process:` actor (§5.3) |
| [Crescent City Career Lab](../organizations/synthetic-crescent-city-career-lab/verification.md) | machine-confirmed | **STALE** | approved, then `stale_after` passed |
| [Nyando Community Health Trust](../organizations/synthetic-nyando-community-health-trust/verification.md) | **unverified** | — | **no `verified` key at all** |

**The Nyando case is the one to test against.** No `verified` key means *unverified* under §5.3, and §11 forbids a consumer from rejecting the record for it. So "nobody could establish this either way" is representable with **no field, no enum, and no special case** — the absence carries the meaning.

An eligibility system that maps *unverified* to *ineligible* has made a decision the data did not support. That distinction is the whole reason this bundle exists.

---

## 6. "Rank these organizations" — the query you should not ship

Included because it is the most likely thing someone builds, and this collection was arranged to break it.

Verification confidence is not a profile field, deliberately. If you reconstruct one from the prose in the `verification.md` files, you get:

| Organization | Budget | Confidence | Technology reality |
|---|---|---|---|
| [Frogtown Community Table](../organizations/synthetic-frogtown-community-table/verification.md) | $430K | **0.88** | One suite, one donor database used properly, endpoints covered, no shadow systems. **Tidiest in the collection** |
| [Motor City Trades Institute](../organizations/synthetic-motor-city-trades-institute/verification.md) | $3.2M | **0.96** | Three participant systems that disagree, a CRM abandoned mid-implementation, a web form posting into an unwatched queue |

**Both determinations are correct.** Motor City Trades genuinely is more verifiable — it has an audit, government contracts, published minutes, and a regulator asking questions. Frogtown genuinely is less verifiable: at $430K no audit is compelled, its board minutes are in a folder, and its strongest evidence is seventeen years of continuous operation that no registry records.

And the better-run organization scores eight points lower.

**Verification confidence measures legibility — how much of an organization exists in retrievable form.** That correlates with size, regulatory burden, and how many institutions generate paperwork about you. It does not correlate with competence, and here it runs opposite to it.

A ranking built on it will systematically prefer large, heavily-audited, institutionally-adjacent organizations over small competent ones, **while consuming entirely accurate data.** Test against this pair before shipping anything that sorts.

---

## 7. "What vocabulary are organizations reaching for that we don't have?" — the emergent layer

The one query that has no equivalent in a conventional schema.

```python
terms = {}
for p in glob.glob('organizations/synthetic-*/**/*.md', recursive=True):
    body = open(p).read()
    for t in re.findall(r'\[\[([^\]|]+)\]\]', body):
        if not os.path.exists(os.path.join(os.path.dirname(p), t + '.md')):
            terms.setdefault(t.strip(), set()).add(p.split('/')[1])
for t, where in sorted(terms.items(), key=lambda kv: -len(kv[1])):
    print(f'{len(where)} bundle(s)  [[{t}]]')
```

Or just `python3 scripts/validate.py --terms`. Today it returns ten terms across five bundles:

`[[Karen]]` · `[[Oromo]]` · `[[Hmong]]` · `[[Somali]]` · `[[Latino]]` · `[[Triqui]]` · `[[Ukrainian]]` · `[[Dholuo]]` · `[[campesino]]` · `[[consejos comunitarios]]`

**None of these is a PCS code and none of them needed to be.** Look at what the controlled layer says about the same organizations: `PG010000` (Immigrants and migrants), `PG010400` (Refugees and displaced people), `PE030000` (Black/African people). Correct, comparable, and it flattens five distinct communities — with different languages, different foods, different literacy profiles, and in two cases a long history of being mistaken for each other — into one bucket.

Watch `[[Karen]]` in particular: it appears in **four records across two bundles**, authored independently. That is a term with cross-producer weight and nobody approved it. At some point it earns a page, and the moment it gets one, every one of those wikilinks becomes a resolved edge and the graph gains a node — with no migration, no schema change, and no coordination.

**That is what the emergent layer is for.** The controlled vocabulary makes bundles comparable; the emergent one makes them true.

Two honest problems, both open:
- **Ambiguity.** `[[Karen]]` is a people of Myanmar and also a common given name. A flat namespace with no disambiguation eventually collides.
- **Promotion.** Nothing decides when a term becomes a node, or who writes it.

---

## 8. Point an agent at a bundle

The least code of all, and the reason the prose matters as much as the frontmatter.

> *Read `organizations/synthetic-frogtown-community-table/` and scope a technology volunteer project. Honor `technical-volunteers/constraints.md`.*

A capable model gets this right, and the interesting part is what stops it going wrong. [`constraints.md`](../organizations/synthetic-frogtown-community-table/technical-volunteers/constraints.md) is **org-authored** — it carries `generated.by: human:org-staff` — and it says, in the organization's own words: *do not redesign our website, we have been offered that twice, our problem is that the donation form is running unmaintained software and we are not sure anyone has the admin password.*

An agent that reads the technology inventory and stops there proposes a redesign. An agent that reads the constraints proposes a locksmith.

Three constraints in that file that no schema field would have captured:
- March through November the farm staff at a *different* bundle are outdoors and unreachable in daylight, so project work is winter work.
- Do not build anything that starts identifying people in a food line, however useful the data would be — that is a program commitment, not a data gap.
- Every project must leave documentation a non-technical staff member can follow; a solution only one person understands is worse than the notebook.

**This is the case for verbose knowledge.** A normalized record would carry the technology inventory and lose all three.

---

## 9. "What does the organization say for itself?" — the org-voice layer, deliberately outside the profile

Every bundle also carries `impact.md` and `what_i_need_funding_for.md`. Both say so in their own frontmatter: *"Not part of the published civic/0.6 profile."* Nothing under `x-civic` requires them, resolves them against a vocabulary, or reads them for conformance.

```python
import glob, re, yaml

def doc(path):
    body = open(path).read()
    fm = re.match(r'^---\n(.*?)\n---', body, re.S).group(1)
    return yaml.safe_load(fm), body.split('---', 2)[2].strip()

for p in sorted(glob.glob('organizations/synthetic-*/what_i_need_funding_for.md')):
    meta, prose = doc(p)
    print(meta['title'])
```

They exist for a narrower reason than every other optional layer in this collection: not to be queried, but to be **read** — by a person deciding what to fund, or by an agent drafting a grant narrative or a volunteer scope. `impact.md` is the organization's own account of what happened; `what_i_need_funding_for.md` is its own account of what it needs next, in its own words, not backed into a funder's category. Frogtown Table's is explicit about it: *"flexible support that doesn't require us to build out grant-specific reporting infrastructure matters more to us than a larger, narrower award would."* No `provides` code or budget figure says that.

**What it costs:** nothing to conformance — these are two more optional `type` values core OKF already tolerates (§11). **What it buys:** exactly the kind of verbose, agent-ready prose [use case 8](#8-point-an-agent-at-a-bundle) argues for, this time pointed at a funder's question instead of a volunteer's.

---

## What each use case cost

| Use case | Needs beyond the four required fields |
|---|---|
| 1. Who else does what we do | **nothing** |
| 2. Who else works here | `situation` + a shared place node |
| 3. Complementary services | `provides` + `situation` |
| 4. Where funding could flow | `provides`; PCS Strategy would improve it |
| 5. What can I trust today | **nothing from the profile** — core `verified` / `stale_after` |
| 6. Ranking | don't |
| 7. Emergent vocabulary | prose wikilinks; no schema at all |
| 8. Agent scoping a project | the document bodies, and an org-authored constraints file |
| 9. What the org says for itself | `impact.md` / `what_i_need_funding_for.md`; outside the profile entirely |

**Four fields make a bundle findable. The optional layers make it useful. The prose makes it actionable.** That is the argument for a small required core, and it is why `civic/0.6` stops where it does.

## Try breaking it

- Write a rollup on `ntee` and notice it silently returns twelve of fifteen — no error, no null.
- Read Eastside Harvest's budget and see whether your code picks a number or notices there are two.
- Feed Nyando to an eligibility rule and see whether it says *no* or *I don't know*.
- Add a sixteenth organization, then run `scripts/build_hubs.py` and watch every membership list, place roster, and index rebuild itself.
- Delete a `subject` code and run `scripts/validate.py` — core OKF still passes, `civic/0.6` fails. That separation is the point.
