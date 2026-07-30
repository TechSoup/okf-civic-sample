---
type: classification
title: "SDG 16 — Peace, justice and strong institutions"
description: "UN Sustainable Development Goal 16 — promote peaceful and inclusive societies, provide access to justice for all, and build effective, accountable institutions."
resource: https://sdgs.un.org/goals
aliases: ["SDG-16", "sdg:16", "SDG 16", "Peace, justice and strong institutions"]
tags: ["cskg", "hub", "sdg", "classification", "justice"]
synthetic: false
status: stable
generated: { by: process:build-hubs, at: 2026-07-29T00:00:00Z }
id: "sdg:16"
scheme: "SDG"
scheme_authority: "United Nations"
scheme_uri: "https://sdgs.un.org/goals"
x-civic:
  profile: civic/0.6
---

# SDG 16 — Peace, justice and strong institutions

**A shared classification node.** Organizations carry this goal number in optional `x-civic.sdg`; the Members list below is generated from that key by `scripts/build_hubs.py`.

**Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels.**

## Five members, three countries, and the hub that reaches every legal-aid organization here

**This is the hub [I80](../ntee/I80.md) should have been.** All three legal-aid practices in this collection are here, including the Polish foundation that no NTEE code can reach — plus two environmental organizations whose work runs through regulatory and legal process.

Access to justice is the through-line, and it takes four distinct forms:

| Organization | The justice mechanism |
|---|---|
| [Farmworker Law Center](../../organizations/synthetic-central-valley-farmworker-law-center/README.md) | Wage, housing, and safety claims for people whose employer is often also their landlord |
| [North Star Defense](../../organizations/synthetic-north-star-immigrant-defense/README.md) | Representation in a court system with no public defender |
| [Prawo i Schronienie](../../organizations/synthetic-fundacja-prawo-i-schronienie/README.md) | Asylum procedure, temporary protection, and migrant employment rights |
| [Gulf Corridor](../../organizations/synthetic-gulf-corridor-justice-project/README.md) | Making a permitting proceeding answerable to the people it affects |
| [Río Vivo](../../organizations/synthetic-corporacion-rio-vivo/README.md) | *Acciones populares*, *tutelas*, and *consulta previa* support for collective territories |

## Four legal systems, and "privileged" does not port

The three legal-aid organizations all operate under an obligation of confidentiality toward their clients, and **the obligation has a different name and a different shape in each jurisdiction**:

- **US** — attorney-client privilege, a term of art with specific doctrine.
- **Poland** — professional secrecy binding *radcowie prawni* and *adwokaci*.
- **Colombia** — its own professional-secrecy framework (and the Colombian organization is not a law firm; it works with counsel).

**A schema field reading `privileged: true` is quietly asserting an American legal framework.** Three of the five bundles here would need a more neutral way to say "this cannot be examined, for reasons of legal professional obligation" — a point [the Polish bundle](../../organizations/synthetic-fundacja-prawo-i-schronienie/verification.md) raises explicitly.

## And four different reasons a determination could not see inside

If you read the five eligibility files together you get the collection's full taxonomy of unexaminable:

1. **Privileged / professionally secret** — the three legal practices. A legal boundary; a system that penalizes it is badly designed.
2. **Not owned by the organization** — [Río Vivo](../../organizations/synthetic-corporacion-rio-vivo/verification.md)'s monitoring data belongs to eleven community organizations. Verification had no standing to ask.
3. **Deliberately unpublished** — [North Star](../../organizations/synthetic-north-star-immigrant-defense/verification.md) tracks how many rapid-response callers get no lawyer and withholds it, so a published figure does not deter calls.
4. **Out of scope** — [Gulf Corridor](../../organizations/synthetic-gulf-corridor-justice-project/verification.md)'s health survey methodology, which eligibility verification is the wrong instrument to assess.

**Four absences, four meanings, and none of them distinguishable from the shape of the data.** Only a statement carries the difference. These five bundles are the test set for whether your completeness metric can tell them apart.

## The adverse-media warning lives here too

Two members — [Gulf Corridor](../../organizations/synthetic-gulf-corridor-justice-project/verification.md) and [Río Vivo](../../organizations/synthetic-corporacion-rio-vivo/verification.md) — return heavy adverse-media results, because being publicly attacked is what happens to effective advocacy organizations. In the Colombian case, **stigmatizing defenders is a documented tactic that has preceded violence**, and an automated screen that lowers confidence on adverse-media volume would convert that campaign into a compliance finding.

That is the most consequential note in this collection about automated verification, and it is in [Río Vivo's eligibility file](../../organizations/synthetic-corporacion-rio-vivo/verification.md).

## Members
<!-- GENERATED from the organizations' x-civic frontmatter — do not edit by hand; run scripts/build_hubs.py -->
- [synthetic-Central Valley Farmworker Law Center](../../organizations/synthetic-central-valley-farmworker-law-center/README.md) — Central Valley legal-aid organization representing farmworkers in wage, housing, and immigration matters
- [synthetic-Corporación Río Vivo](../../organizations/synthetic-corporacion-rio-vivo/README.md) — Colombian watershed-defense organization where digital security is physical security, and where the communitie
- [synthetic-Fundacja Prawo i Schronienie](../../organizations/synthetic-fundacja-prawo-i-schronienie/README.md) — Warsaw foundation providing legal aid to refugees and migrants — the collection's GDPR bundle, and the one wit
- [synthetic-Gulf Corridor Justice Project](../../organizations/synthetic-gulf-corridor-justice-project/README.md) — Louisiana environmental-justice organization whose public evidence archive is contested by a well-resourced ad
- [synthetic-North Star Immigrant Defense](../../organizations/synthetic-north-star-immigrant-defense/README.md) — Saint Paul immigration legal-defense organization whose client data is a target, not merely confidential
<!-- /GENERATED -->

## Related

- [I80](../ntee/I80.md) — legal services. Two of the three legal-aid organizations
- [SDG-10](SDG-10.md) — reduced inequalities. Three members overlap
- [SDG-13](SDG-13.md) — climate action. Two members overlap
- [SDG-08](SDG-08.md) — decent work. One member overlaps
- [SDG-06](SDG-06.md) — clean water. One member overlaps
