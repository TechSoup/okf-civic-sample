---
type: classification
title: "SDG 8 — Decent work and economic growth"
description: "UN Sustainable Development Goal 8 — promote sustained, inclusive economic growth, full and productive employment, and decent work for all."
resource: https://sdgs.un.org/goals
aliases: ["SDG-08", "sdg:8", "SDG 8", "Decent work and economic growth"]
tags: ["cskg", "hub", "sdg", "classification", "employment"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "sdg:8"
scheme: "SDG"
scheme_authority: "United Nations"
scheme_uri: "https://sdgs.un.org/goals"
x-civic:
  profile: civic/0.6
---

# SDG 8 — Decent work and economic growth

**A shared classification node.** Organizations carry this goal number in optional `x-civic.sdg`; the Members list below is generated from that key by `scripts/build_hubs.py`.

**Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all.**

## Four members, and the fourth one is why this hub is interesting

Three are the workforce organizations — training people for jobs. The fourth is a **legal-aid practice**, and it belongs here for a reason the other three do not:

[The Farmworker Law Center](../../organizations/synthetic-central-valley-farmworker-law-center/README.md) does not create employment. It litigates **wage theft, unlawful piece-rate deductions, missed breaks, and unsafe conditions** — the *decent* half of "decent work," which is the half a training programme cannot deliver.

**The goal contains two different theories of change and this hub holds both:**

| Approach | Members | Mechanism |
|---|---|---|
| **Get people better jobs** | The three workforce organizations | Train, credential, place |
| **Make existing jobs lawful** | The Farmworker Law Center | Enforce the rules on the employer |

Neither substitutes for the other. A farmworker who wins a wage claim still has the same job; a trained welder still works wherever the labour market allows. **A query grouping these four as "employment organizations" would find them similar and they are doing near-opposite work.**

Worth knowing if you are building anything that clusters by shared goal. Goal-sharing is a weak similarity signal, and this hub is the demonstration.

## A note on what nobody in this hub tracks

**None of the four organizations can tell you whether the work its participants got was decent, or lasted.**

- [Motor City Trades](../../organizations/synthetic-motor-city-trades-institute/README.md) publishes a three-year retention figure resting on one spreadsheet maintained by one person.
- [Black Mountain](../../organizations/synthetic-black-mountain-workforce-partnership/README.md) states plainly that it does not track long-term retention.
- [Crescent City Career Lab](../../organizations/synthetic-crescent-city-career-lab/README.md) gets wage-gain data for about half its placements.
- The Law Center's case outcomes are **privileged and were not examined**.

So the goal is about durable, decent employment, and the collection's four members hold, between them, almost no evidence about durability or decency. That is not a fault in the sample data — it is what workforce outcome measurement generally looks like, and [J22](../ntee/J22.md) sets out how differently the three trainers handle it.

## Members
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Black Mountain Workforce Partnership](../../organizations/synthetic-black-mountain-workforce-partnership/README.md) — post-coal workforce training organization in Letcher County, Kentucky, training people for remote work in a co
- [synthetic-Central Valley Farmworker Law Center](../../organizations/synthetic-central-valley-farmworker-law-center/README.md) — Central Valley legal-aid organization representing farmworkers in wage, housing, and immigration matters
- [synthetic-Crescent City Career Lab](../../organizations/synthetic-crescent-city-career-lab/README.md) — New Orleans workforce organization whose verification determination has expired — an organization in good stan
- [synthetic-Motor City Trades Institute](../../organizations/synthetic-motor-city-trades-institute/README.md) — Detroit pre-apprenticeship and trades-training organization, mid-sized, with real technical debt
<!-- /GENERATED -->

## Related

- [J22](../ntee/J22.md) / [J20](../ntee/J20.md) — the three trainers, and the outcome-reporting comparison
- [SDG-04](SDG-04.md) — quality education. The three trainers
- [SDG-16](SDG-16.md) — peace, justice, strong institutions. Where the Law Center's other half sits
- [SDG-01](SDG-01.md) — no poverty. One member
