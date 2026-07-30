---
type: volunteer-constraints
title: "synthetic-Riverbend Air Alliance — Volunteer constraints & preferences"
description: "The org's own rules for technology volunteers. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & preferences

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**, and it starts from sensible defaults and diverges as the org fills it in. An agent scoping a project must treat these as non-negotiable.

*Stub — pre-seeded with defaults appropriate to an organization whose data is used as evidence in regulatory proceedings, and which holds residential addresses for its sensor hosts.*

- **Never break the record (highest priority).** The sensor time series is **evidence used in permit proceedings**. A gap introduced by a volunteer's migration is not a bug, it is a hole in the organization's case that cannot be backfilled. Any work touching the data path must be **additive and reversible**: read from the existing pipeline, don't cut over until the new path has run in parallel long enough to trust, and never be the only copy.
- **Chain of custody matters more than elegance.** If the organization cannot explain in a hearing how a number got from a sensor to a slide, the number is worth less. A volunteer must document the path, and should prefer a boring traceable design over a clever one.
- **Sensor-host addresses are confidential and not negotiable.** 31 households volunteered a porch on the understanding that their address stays private. Host records require a signed confidentiality agreement and least-privilege access. **Nothing a volunteer builds may increase the spatial precision of what's published**, and any new visualization must be checked for whether it narrows a sensor to a household.
- **Do not overstate the data.** The network is uncalibrated, and the organization is deliberately careful in how it describes its own readings. A volunteer must not build interfaces that present these numbers with more confidence than they carry — no unqualified comparisons to regulatory thresholds, no removing the uncertainty language because a chart looks cleaner without it.
- **Youth corps involvement is welcome but supervised.** Members are 14–18. Volunteers working alongside them require a **background check**. The organization would rather a project include the youth corps than not, so scope with that in mind, but the safeguarding requirement is firm.
- **Remote is fine for pipeline work; site visits need a host's permission.** Sensors are on private property. A volunteer does not go to a host's home without the organization arranging it.
- **Handover:** the organization has real technical literacy but no dedicated IT staff and no developer. A solution requiring ongoing code maintenance will decay. Prefer managed services and documented configuration over something bespoke.
- **Eligibility limits:** *(none beyond the above — the org adds any here, with the reason, so it travels with the request.)*
