---
type: offer
title: Broken Offer (validator self-test fixture)
description: An intentionally non-conforming record. scripts/validate.py --self-test asserts that this FAILS.
tags: [fixture, do-not-publish]
timestamp: 2026-06-20T00:00:00Z
x-civic:
  profile: civic/0.1
  status: ACTIVE
  category: Operations
  capability: project-management
  relations:
    - target: nonexistent-partner.md
      type: complements
      note: "this edge has no matching prose link and no real target"
---

# Broken Offer

This fixture deliberately violates the profile, in several ways at once:

- `x-civic.profile` is `civic/0.1`, not `civic/0.5`.
- As an `offer` it is missing the required `offer` block and `provenance.vendor_url`.
- It declares an `x-civic.relations` edge that has no matching prose link title (and points at a file that does not exist).

`scripts/validate.py --self-test` loads this file and confirms the validator rejects it. If this record ever *passes*, the validator has regressed.
