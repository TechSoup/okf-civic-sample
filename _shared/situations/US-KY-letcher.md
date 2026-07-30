---
type: situation
title: "Letcher County, Kentucky"
description: "Situation node for Letcher County, Kentucky — the collection's clearest demonstration of why community conditions belong to the place."
aliases: ["US-KY-letcher", "Letcher County", "Whitesburg, KY"]
tags: ["cskg", "hub", "situation", "united-states", "rural", "appalachia"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "situation/US-KY-Letcher"
country: "US"
subdivision: "US-KY"
locality: "Letcher County, Kentucky"
x-civic:
  profile: civic/0.6
---

# Letcher County, Kentucky

**A shared situation node.** Organizations carry this place key in optional `x-civic.situation`; the Members list below is generated from that key by `scripts/build_hubs.py`.

A *situation* describes a **place, not an organization.** This node is the collection's strongest argument for that design, and the argument is below.

## One community-level fact defeated a program at each of two organizations

**This is the demonstration.** Two organizations link here. They are in unrelated sectors — a rural clinic and a workforce training organization. Each built a program that the county's **broadband and mobile availability** defeated:

| Organization | Program | What happened |
|---|---|---|
| [Cumberland Gap Health](../../organizations/synthetic-cumberland-gap-health-cooperative/README.md) | **Telehealth**, stood up 2020 with grant funding | Roughly **40% of patients cannot use a video visit** — no wired service available, satellite that a call defeats, or a metered connection twenty minutes would exhaust. The clinic did everything right; the constraint was never on its side of the wire |
| [Black Mountain Workforce](../../organizations/synthetic-black-mountain-workforce-partnership/README.md) | **Remote-work readiness track** | Graduates trained for remote jobs **cannot reliably work from home.** The organization built workstations in its own building so they can do remote work from a room in Whitesburg — quietly turning a training programme into a co-working facility |

**One cause. Two sectors. Two organizations. One address.**

Store connectivity as an *organizational* attribute and a corpus records **two independent technology weaknesses** — a clinic with a struggling telehealth programme, a workforce organization with a weak track — and misses that there is a single infrastructure problem with a location. Any intervention aimed at either organization's technology would fail, because neither organization's technology is the problem.

**That is what situation nodes are for.** Nothing else in this collection makes the case as plainly, which is why these two bundles are paired here.

A second-order effect worth noting: both organizations' **capability assessments** flag them down for things caused by this county fact, and neither assessment has any way to say so. See [the clinic's](../../organizations/synthetic-cumberland-gap-health-cooperative/technology/capability.md) and [the workforce organization's](../../organizations/synthetic-black-mountain-workforce-partnership/technology/capability.md).

## Community indicators
<!-- STUB — the statistical layer attaches here. Deliberately not populated. -->

**Stub, and deliberately empty** — see [index](index.md). Letcher County is a real place with real numbers, and fabricating them would be worse than fabricating a nonprofit.

What would populate it:

- **Population and decline** — US Census Bureau, ACS. Sustained out-migration is central to both members' operating reality
- **Broadband and mobile availability** — FCC, and **state and local measurement, because FCC maps have historically overstated rural availability.** For this node the difference between claimed and actual coverage is the whole point
- **Post-coal employment** — Bureau of Labor Statistics; state workforce agency; mine employment records
- **Occupational lung disease prevalence** — federal black lung programme data; NIOSH. Shapes the clinic's caseload and its benefits-advocacy work
- **Distance to hospital and specialist care** — the county has no hospital of its own
- **Transit** — effectively none
- **Substance use and treatment capacity** — the clinic runs recovery support because nobody else in the county does

## The most reciprocal partnership in the collection

The two organizations here run a **health-careers pathway together**: Black Mountain trains people for medical assistant, phlebotomy, and CNA roles; Cumberland Gap Health provides clinical placements and hires some of the graduates.

**Each is the other's supplier and customer.** Most `partners_with` edges in this collection are referral pathways running one direction; this one is a mutual dependency, and a query treating all partnership edges as equivalent will flatten a real difference. It also means the pathway **appears in both bundles' programme lists** and will be double-counted by any aggregation that does not know the two entries are one programme.

## Organizations here
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Black Mountain Workforce Partnership](../../organizations/synthetic-black-mountain-workforce-partnership/README.md) — post-coal workforce training organization in Letcher County, Kentucky, training people for remote work in a co
- [synthetic-Cumberland Gap Health Cooperative](../../organizations/synthetic-cumberland-gap-health-cooperative/README.md) — small rural clinic in Letcher County, Kentucky, where the broadband problem belongs to the patients as much as
<!-- /GENERATED -->

## Related

- [E32](../ntee/E32.md) — community clinics. The clinic member, alongside a peer with 7× the budget and identical HIPAA obligations
- [J22](../ntee/J22.md) — job training. The workforce member, alongside the outcome-reporting comparison
- [US-CA-fresno](US-CA-fresno.md) — where the same connectivity problem defeats two more organizations
