---
type: org
title: Fixture — invented codes and a bad country
description: Every controlled value here is wrong in a different way.
synthetic: true
status: published
timestamp: '2026-07-29T00:00:00Z'
generated: { by: nobody }
x-civic:
  profile: civic/0.5
  subject: [SS999999]
  population: [PG010000]
  org_type: PA010000
  registration_country: USA
sources:
  - title: A source with no resource
---

# Fixture: invalid vocabulary

Deliberately wrong, one error per line:

- `timestamp` was superseded by `generated.at` in OKF v0.2 (§13.1).
- `status: published` is not in the v0.2 vocabulary (§5.4).
- `generated.by: nobody` does not follow the actor convention (§7).
- a `sources` entry has no `resource`, which §5.1 requires.
- `x-civic.profile` is a stale version.
- `SS999999` looks like a PCS Subject code and does not exist. **This is the failure the profile cares most about** — a fabricated code in a real vocabulary's namespace is worse than an empty field, because it breaks any downstream crosswalk that trusts it.
- `PA010000` is a real code, but it is a Population code used as `org_type`.
- `USA` is ISO 3166-1 alpha-3; the profile requires alpha-2.
