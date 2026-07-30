---
type: situation
title: "New Orleans, Louisiana"
description: "Situation node for New Orleans and the adjacent river parishes. The place two organizations in this collection operate in — not the organizations."
aliases: ["US-LA-orleans", "New Orleans", "Orleans Parish"]
tags: ["cskg", "hub", "situation", "united-states", "urban", "coastal"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "situation/US-LA-Orleans"
country: "US"
subdivision: "US-LA"
locality: "New Orleans, Orleans Parish, Louisiana"
x-civic:
  profile: civic/0.6
---

# New Orleans, Louisiana (Orleans Parish and adjacent river parishes)

**A shared situation node.** Organizations carry this place key in optional `x-civic.situation`; the Members list below is generated from that key by `scripts/build_hubs.py`.

A *situation* describes a **place, not an organization.**

## Community indicators
<!-- STUB — the statistical layer attaches here. Deliberately not populated. -->

**Stub, and deliberately empty** — see [index](index.md).

What would populate it, for the organizations linking here:

- **Population, income, and poverty** by neighbourhood and parish — US Census Bureau, ACS
- **Industrial permitting and emissions** along the river corridor — EPA and state environmental agency records. Central to one member's entire operation
- **Health outcomes** — state and parish surveillance, including the cancer and respiratory data that a household health survey exists to supplement
- **Storm exposure and displacement history** — FEMA; state records. Recurring rather than exceptional, and it disrupts both members
- **Coastal land loss** — USGS; state coastal authority
- **Labour market composition**, particularly the tourism weighting that makes household income seasonal and storm-vulnerable
- **Coastal and remediation infrastructure investment** — the pipeline both members' shared green-jobs work depends on

## The storm is a community condition, and it lands on both members

Worth being explicit, because it is the second-clearest instance in this collection of a place fact producing effects in two unrelated bundles — after [Letcher County's broadband](US-KY-letcher.md).

- [Crescent City Career Lab](../../organizations/synthetic-crescent-city-career-lab/README.md) loses weeks from late-summer cohorts and maintains a re-entry pathway for participants who **disappear mid-cohort because a storm ended a home.** Its bundle lists storm-season contingency as a programme, because in this city it is one.
- [Gulf Corridor](../../organizations/synthetic-gulf-corridor-justice-project/README.md) operates in communities where storm exposure compounds industrial exposure, and where displacement makes a longitudinal health survey harder to sustain.

Neither organization's completion rates or data continuity can be read without it, and **it belongs to the coast rather than to either organization.**

## Two organizations, one principle

The members here run a **green-jobs pathway** together, and the principle both state is the same: **people who live with the pollution should get the jobs cleaning it up.** Gulf Corridor knows which remediation and coastal work is genuinely coming and which employers are credible; Career Lab trains and places.

## And this node holds the collection's verified-meets-unverified pair

**Gulf Corridor's determination is current (APPROVE, 0.91). Career Lab's expired in February 2026 and was never renewed** — its `stale_after: 2026-02-14` is in the past.

They are connected by a `partners_with` edge, which makes this the place to test something specific: **status must not propagate along partnership edges.** Gulf Corridor's eligibility is unaffected by its partner's lapse, and its [eligibility file](../../organizations/synthetic-gulf-corridor-justice-project/verification.md) records the pairing explicitly so anything traversing the graph encounters it.

The lapse itself is mundane and that is why it is here: a development director left, the renewal notice went to her deactivated address, and nobody knew. **An expiry is the absence of an event, and absences do not raise alarms unless something is built to notice them.**

## Organizations here
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Crescent City Career Lab](../../organizations/synthetic-crescent-city-career-lab/README.md) — New Orleans workforce organization whose verification determination has expired — an organization in good stan
- [synthetic-Gulf Corridor Justice Project](../../organizations/synthetic-gulf-corridor-justice-project/README.md) — Louisiana environmental-justice organization whose public evidence archive is contested by a well-resourced ad
<!-- /GENERATED -->

## Edges that leave

Gulf Corridor holds `coalition_with` links to [Detroit](US-MI-detroit.md) and [Cali, Colombia](CO-VAC-cali.md) — fenceline-monitoring peers sharing methodology and no geography. See [C20](../ntee/C20.md) for why the same method requires incompatible practices in the three places.

## Related

- [C20](../ntee/C20.md) / [C30](../ntee/C30.md) — the environmental member
- [J22](../ntee/J22.md) / [J20](../ntee/J20.md) — the workforce member
- [SDG-13](../sdg/SDG-13.md) — climate action. The coalition triangle
- [SDG-16](../sdg/SDG-16.md) — peace, justice, strong institutions. The environmental member
