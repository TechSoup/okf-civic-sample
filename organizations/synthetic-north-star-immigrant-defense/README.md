---
type: org
title: "synthetic-North Star Immigrant Defense"
description: "A fabricated Saint Paul immigration legal-defense organization whose client data is a target, not merely confidential."
resource: https://synthetic-north-star-defense.example.org
aliases: ["synthetic-North Star Defense", "North Star Immigrant Defense"]
tags: ["org-bundle", "nonprofit", "synthetic", "legal-aid", "immigration", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-north-star-defense.example.org"
    title: "The organization's own website and published materials"
    author: human:org-staff
    last_modified: 2026-03-02
  - id: registry
    resource: "simulated registry extract"
    title: "Registry record (simulated)"
    author: process:registry-import
    last_modified: 2026-01-15
x-civic:
  # ---- REQUIRED by civic/0.6. These five keys are the whole profile. ----
  profile: civic/0.6
  subject: ["SJ040000", "SJ040700", "SS090300"]     # PCS Subject facet
  population: ["PG010000", "PG010700", "PG040300"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: immigration-legal-defense
  registration:
    scheme: "IRS-EIN"
    id: "00-1000010"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["I80", "I83", "P84"]      # optional US-only layer; reaches 12 of 15
  sdg: ["10", "16"]        # optional global layer; reaches 15 of 15
  situation: US-MN-saint-paul
  relations:
    - { target: synthetic-frogtown-community-table, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-North Star Immigrant Defense

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-North Star Immigrant Defense ("North Star") represents people facing removal from the United States, in Minnesota's immigration courts and in detention. In the organization's own words:

> There is no public defender in immigration court. A person with a lawyer wins at several times the rate of a person without one, and whether you get a lawyer is mostly a question of whether somebody like us had capacity the week you were detained.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it employs **fourteen attorneys**, **nine accredited representatives and paralegals**, and support staff; it carries roughly **1,300 active matters**; it runs a **24-hour rapid-response line**; and it coordinates a **pro bono network of about 90 private-practice attorneys** who take cases under supervision. It was founded in **2003**, and roughly quadrupled in size between 2017 and 2021.

It is a **mid-large** nonprofit for legal aid — annual revenue around **$2,600,000**, assets around **$740,000**. Funding is foundations, a state allocation, a county contract for detained representation, individual donors, and court-awarded fees. Its office is at **1120 University Bend, Saint Paul, MN 55104**. *(mechanical, simulated.)*

- **What it does →** classified as [I80](../../_shared/ntee/I80.md) (legal services); also [I83](../../_shared/ntee/I83.md) (public interest law) and [P84](../../_shared/ntee/P84.md) (ethnic and immigrant services).
- **Who it serves →** [population](population.md) — people in removal proceedings and their families; see also [SDG-16](../../_shared/sdg/SDG-16.md) (peace, justice, strong institutions) and [SDG-10](../../_shared/sdg/SDG-10.md) (reduced inequalities).
- **Where →** [US-MN-saint-paul](../../_shared/situations/US-MN-saint-paul.md) (Saint Paul, Ramsey County, Minnesota).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, validated at 93% confidence.
- **What it runs →** [technology](technology/index.md). Grew fourfold in four years and the systems show it.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md). **Its constraints file is a threat model rather than a privacy policy** — the sharpest security posture in this collection, and for concrete reasons.
- **Who it works with →** [synthetic-Frogtown Community Table](../synthetic-frogtown-community-table/README.md), also in Saint Paul. North Star holds monthly clinic hours in the food shelf's back room. The shelf provides the room and, more importantly, the trust; North Star provides the lawyers. It reaches people who would not come to a law office.

## Why this organization's security posture is different in kind

Every organization in this collection holds sensitive information. This one holds information that **somebody actively wants**, and that changes the whole shape of the problem.

The organization's working threat model — written out in [constraints](technical-volunteers/constraints.md) — includes:

- **Lawful process it must sometimes resist and sometimes comply with**: subpoenas, records requests, and demands whose validity has to be assessed rather than assumed.
- **Device seizure**, including staff devices at ports of entry, where the ordinary protections are weakest.
- **Targeted harassment of staff and of clients**, which has happened to organizations doing this work and shapes decisions about what is published and what is stored.
- **The specific hazard of a client list.** A list of this organization's clients is a list of people in removal proceedings, with addresses. It is the single most dangerous artefact the organization holds, and its value to a hostile party is obvious.

The practical consequence is that **ordinary good practice is not sufficient here, and some ordinary good practice is actively wrong.** Cloud convenience, comprehensive logging, long retention, and detailed analytics are all things a well-run organization normally wants more of. This organization wants less of several of them, deliberately, and can explain why for each.

Compare [synthetic-Central Valley Farmworker Law Center](../synthetic-central-valley-farmworker-law-center/README.md), the collection's other legal-aid bundle. That organization's constraints are about **privilege and the unauthorized practice of law** — professional-responsibility boundaries. This one's are about **adversarial risk**. Both are legal aid; the failure modes barely overlap. Reading the two constraints files against each other is the most instructive pairing in the collection for anyone designing systems for legal services.

## One thing verification could not establish

**Case outcomes were not examined, because they are privileged** — the same boundary as at the Law Center, and the same reasoning: the information cannot lawfully be provided and a verification process has no business asking.

There is a second limitation here that is specific to this organization, though. **Its most meaningful capacity number is one it will not publish**: how many people called the rapid-response line and were turned away because there was nobody free. The organization tracks it internally. It does not report it, because a published figure showing that most callers get no lawyer would discourage the calls, and a call that doesn't happen is a person who definitely gets no lawyer.

That is a defensible judgement and it means **the single most important thing about this organization's effectiveness is deliberately absent from every public record.** Worth noting for anyone building capacity or need models from published nonprofit data: the numbers that would matter most are often the ones an organization has a good reason not to publish.

*(mechanical[^registry]: the simulated determination labels case-level data "Not examined — privileged"; capacity-turnaway figures "Organization-held, not published.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials
[^registry]: Registry record (simulated)
