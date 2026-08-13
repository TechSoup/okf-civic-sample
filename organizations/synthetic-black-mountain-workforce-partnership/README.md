---
type: org
title: "synthetic-Black Mountain Workforce Partnership"
description: "A fabricated post-coal workforce training organization in Letcher County, Kentucky, training people for remote work in a county without broadband."
resource: https://synthetic-black-mountain-workforce.example.org
aliases: ["synthetic-Black Mountain Workforce", "Black Mountain Workforce Partnership"]
tags: ["org-bundle", "nonprofit", "synthetic", "workforce-training", "appalachia", "post-coal", "cskg"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: org-site
    resource: "https://synthetic-black-mountain-workforce.example.org"
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
  subject: ["SN020302", "SB040000"]                 # PCS Subject facet
  population: ["PG090000", "PJ020000", "PG030000"]  # PCS Population facet
  org_type: EA040000                                # PCS OrgType facet
  registration_country: US                          # ISO 3166-1 alpha-2
  # ---- OPTIONAL below. None of it affects conformance. ----
  provides: workforce-training
  registration:
    scheme: "IRS-EIN"
    id: "00-1000008"
    tax_status: "501(c)(3)"
  budget_currency: USD
  ntee: ["J22"]      # optional US-only layer; reaches 12 of 15
  sdg: ["1", "4", "8"]        # optional global layer; reaches 15 of 15
  situation: US-KY-letcher
  relations:
    - { target: synthetic-cumberland-gap-health-cooperative, type: partners_with }
  verifiable_by: [techsoup]
---

# synthetic-Black Mountain Workforce Partnership

> **⚠ SYNTHETIC.** This organization does not exist. Its name, EIN, address, website, budget figures, programs, technology, and eligibility determination are all invented. The EIN uses the prefix `00-`, which the IRS never assigns. Provenance labels below are simulated. See the [collection README](../../README.md).

synthetic-Black Mountain Workforce Partnership ("Black Mountain") trains adults in Letcher County, Kentucky, for the jobs that exist rather than the ones that used to. In the organization's own words:

> Everybody who comes through our door has already been told to learn to code. We are not going to say it again. We are going to ask what work is actually available within an hour's drive, or over a wire that actually reaches your house, and start from there.

*Mission: **org-sourced**[^org-site] (simulated).*

Beyond that statement the picture is **derived** and would need confirmation: it enrolls about **190 adults a year** across several short-cycle tracks, most of them under sixteen weeks, and it places graduates into healthcare support roles, commercial driving, electrical and solar installation, and — with real difficulty, discussed below — remote administrative work. It was founded in **2013**, in the years when the county's mining employment fell steeply, and received IRS exemption the same year.

It is a **small** nonprofit — annual revenue around **$920,000**, assets around **$310,000**, and about **12 staff**. Roughly two-thirds of revenue is public: a federal workforce subaward passed through a regional board, a state allocation, and an economic-transition grant. The rest is foundation money. Its address is **44 Black Mountain Road, Whitesburg, KY 41858**. *(mechanical[^registry], simulated.)*

- **What it does →** classified as [J22](../../_shared/ntee/J22.md) (job training and employment).
- **Who it serves →** [population](population.md) — working-age adults in Letcher County; see also [SDG-08](../../_shared/sdg/SDG-08.md) (decent work), [SDG-04](../../_shared/sdg/SDG-04.md) (quality education), and [SDG-01](../../_shared/sdg/SDG-01.md) (no poverty).
- **Where →** [US-KY-letcher](../../_shared/situations/US-KY-letcher.md) (Letcher County, Kentucky).
- **Programs →** [programs](programs.md).
- **What it accomplished →** [impact](impact.md).
- **What it needs funding for →** [funding priorities](what_i_need_funding_for.md).
- **Is it eligible? →** [eligibility](verification.md) — yes, validated at 92% confidence.
- **What it runs →** [technology](technology/index.md). Including a laptop lending library that is doing more than anyone planned.
- **Technology volunteers →** [technical-volunteers](technical-volunteers/index.md).
- **Who it works with →** [synthetic-Cumberland Gap Health Cooperative](../synthetic-cumberland-gap-health-cooperative/README.md), also in Letcher County. Black Mountain trains people for medical assistant, phlebotomy, and CNA roles; the clinic provides the clinical placements and hires some of the graduates. **This is the most reciprocal partnership in the collection** — each organization is simultaneously the other's supplier and customer, and neither could run its part alone.

## The contradiction the organization lives inside

Black Mountain runs a **remote-work readiness track**, because remote work is the honest answer to "what jobs pay a living wage within reach of Letcher County." It is also the track that fails most often, for a reason that has nothing to do with the training:

**A substantial share of graduates cannot reliably work from home, because the connection where they live will not carry a workday.** Video calls drop. Uploads fail. A metered connection makes an eight-hour VPN session expensive. Some have no wired option at any price.

The organization's response has been to build **workstations at its own building** with a decent connection, so graduates can do remote work from a room in Whitesburg. That works, and it is a strange thing to have to do, and it quietly converts a remote-work program into a co-working program with a training front end.

This is the same broadband constraint that killed telehealth at [its partner clinic](../synthetic-cumberland-gap-health-cooperative/technology/inventory.md) — **one infrastructure gap, defeating two unrelated organizations' programs, in two different sectors.** The pair of bundles is in this collection partly so that connection is visible. A corpus that stored connectivity as an *organizational* attribute would record two independent technology weaknesses and miss that there is one problem, it belongs to the county, and it lives in [the situation node](../../_shared/situations/US-KY-letcher.md).

## One thing verification could not establish

**Whether placements last.** The organization reports placement at completion, because that is what its funders require and what it can actually observe. It does not know how many graduates are still in the job at twelve months, and it does not claim to.

That is more honest than [Motor City Trades](../synthetic-motor-city-trades-institute/README.md), which does claim a three-year figure on considerably thinner evidence — and it is worth noting that the honesty **costs Black Mountain something**, because a competitive application from an organization reporting "we don't track that" reads worse than one reporting a number nobody checks.

A collection like this can make that visible. Two workforce organizations, one reporting an unverifiable long-term figure and one declining to, and the reporting environment rewards the first. *(mechanical: the simulated determination labels retention data "Not collected — organization states so explicitly.")*

---
*Fabricated bundle. See [log](log.md) for its history and the [collection README](../../README.md) for what the whole set is for.*

[^org-site]: The organization's own website and published materials

[^registry]: Registry record (simulated)
