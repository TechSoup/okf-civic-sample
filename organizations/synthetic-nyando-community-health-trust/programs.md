---
type: programs
title: "synthetic-Nyando Community Health Trust — Programs & services"
description: "What the organization runs. Fabricated."
tags: ["programs", "services", "synthetic", "kenya"]
synthetic: true
status: stable
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
  subject: ["SE040200", "SE130700"]
---

# Programs & services

**⚠ Synthetic — fabricated data. And note that this bundle's [verification returned insufficient evidence](verification.md).**

*The list below is **derived** (simulated) from public materials; a real organization would confirm and replace it with its own description.*

- **Community health promoter network** — 142 promoters attached to four link health facilities, each covering 65–70 households on a visit schedule. This is the organization; everything else is delivered through it.
- **Maternal and newborn health** — antenatal visit follow-up, birth planning, facility-delivery encouragement, postnatal visits. The largest share of promoter activity and the indicators the national system most closely tracks.
- **Child health** — immunization follow-up, growth monitoring, and integrated management of common childhood illness at household level within the promoters' scope of practice.
- **Malaria** — net distribution and follow-up, fever referral, and seasonal intensification around the rains.
- **Household water treatment and safe storage** — health work that becomes flood-response work for part of every year.
- **Referral and accompaniment to facilities** — the promoter's most consequential act: recognizing that a household member needs a facility and getting them there. Referral completion is tracked.
- **Promoter training and supervision** — cohort training, monthly supervision meetings at the link facilities, and refresher rounds. Substantial, continuous, and the reason the data is as good as it is.
- **Reporting into the national health information system** — monthly, in the required format. Not overhead; a statutory and program obligation that structures the whole operation.

*(Community health promotion is the activity. No NTEE code — see the classification note in [README](README.md).)*

## Program boundaries are set by national policy, not by the organization

Worth stating because it inverts the assumption in most of this collection.

For the US bundles, an organization's program list is largely its own description of what it does. Here it substantially is not: **the community health strategy, the promoter scope of practice, the indicator set, the reporting format, and the link-facility structure are national policy.** The organization implements within a defined framework and its programme list looks the way it does because the framework does.

Two consequences for anyone modelling this:

**Programme structure is comparable across Kenyan community health organizations** in a way that US nonprofit programme lists are not comparable to each other. Two organizations implementing the same national strategy will report the same indicators the same way. That is a considerable advantage for any corpus analysis — and it exists in exactly the bundle whose institutional documentation is least retrievable.

**A "programme" here is not a thing the organization invented and could change.** Anything that treats programme definitions as organizational self-description, and therefore as revisable or as a signal of strategy, is misreading this bundle.

## Which of these should become its own file first

**Promoter training and supervision.** It is one bullet, it is where most of the organization's 23 paid staff spend their time, and it is the mechanism that makes everything else work — the data quality this bundle is notable for is a product of monthly supervision, not of the mobile forms. Describing it after the health services understates it.

**Household water treatment** is the second candidate, because it is two programmes wearing one label: routine health promotion for most of the year, and flood response for part of it, with different funders, different urgency, and different partners.

## What the `learn_with` edge actually exchanges

The [Sierra Foothills](../synthetic-sierra-foothills-community-health/programs.md) edge is not ceremonial. What moves across it:

**From Nyando to California:** how to run a structured field workflow where connectivity fails — offline capture, sync discipline, supervision that catches data errors before they compound, and the practice of a defined household catchment per worker. Sierra Foothills' mobile unit currently charts on paper because it has none of this.

**From California to Nyando:** clinical integration with a facility EHR, behavioural health integration, and the specific experience of an organization that has to survive a payer environment.

**Neither direction is charity.** And the organization with the smaller budget is the one exporting the more transferable practice, which is worth noticing given how rarely a corpus is arranged so that could be visible.
