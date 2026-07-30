---
type: org
title: Fixture — an org record missing a required profile field
description: Declares civic/0.6 but omits `population`. Core OKF still passes; the profile claim is false.
synthetic: true
status: stable
generated: { by: process:fixture, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  subject: [SS030600]
  org_type: EA040000
  registration_country: US
---

# Fixture: missing a required field

This record is **valid core OKF v0.2** — it has parseable frontmatter and a non-empty `type`, which is all §11 requires. It is **not** valid `civic/0.6`, because it declares the profile and then omits `population`.

The validator must report those two facts separately. A consumer that rejected this document outright would be violating §11.
