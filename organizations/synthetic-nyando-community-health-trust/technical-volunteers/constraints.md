---
type: volunteer-constraints
title: "synthetic-Nyando Community Health Trust — Volunteer constraints & preferences"
description: "The org's own rules for technology volunteers. Org-owned and editable. Fabricated."
tags: ["technical-volunteers", "constraints", "org-owned", "synthetic", "kenya"]
synthetic: true
status: stable
generated: { by: human:org-staff, at: 2026-07-29T00:00:00Z }
x-civic:
  profile: civic/0.6
---

# Volunteer constraints & preferences

> **⚠ Synthetic.** In a real bundle **this file is the organization's to edit**, and it starts from sensible defaults and diverges as the org fills it in. An agent scoping a project must treat these as non-negotiable.

## Start by understanding what we already have

We say this first because of what usually happens.

Our website is a page somebody built because a donor asked for one. We know it scores badly. What we actually run is **142 community health promoters capturing structured household data on phones, offline, feeding the national health information system every month for twelve years.** 9,600 registered households. Monthly supervision that catches a misread indicator in week three.

**If your proposal begins by offering us a data system, you have read our website and not our work.** We have been offered a CRM four times.

We are genuinely glad of technical help. We need it in specific places, and those places are not where an outside assessment points.

## The promoter cost test

**Every proposal is judged on one question before any other: does this increase or decrease what a promoter spends?**

Our promoters are community members on stipends, not salaried staff. Most of them are women. **They pay for mobile data and airtime out of those stipends** in order to submit the reporting we require of them, and about thirty use their own handsets.

That is money moving from the poorest people in this operation to our donor deliverables, and we are not proud of it.

So:

- **Anything that increases sync volume, app size, update frequency, or required connectivity is presumptively rejected.** If your design needs more data, it needs to come with the data.
- **Anything that reduces what promoters spend is welcome even if it is unglamorous.** Smaller payloads. Fewer syncs. Compression. Working over SMS where a form is overkill.
- **Do not build anything that assumes a promoter has a smartphone.** About thirty do not have one we provided.
- **Do not build anything requiring a promoter to be online at a particular moment.**

## Supervision is the thing that works — do not add to it

Our data is good because 23 staff sit with promoters monthly and review records. **The software makes offline capture possible; supervision makes the data true.**

An intervention that improves the tooling while adding to the supervision burden will make our data worse. If your project creates new things for supervisors to check, chase, or explain, say so plainly and let us weigh it.

## Household data

- **Signed confidentiality agreement** before any access, and a conversation with our programme manager.
- **Household health data is sensitive.** Names, locations, pregnancies, illnesses, child immunization status, in a community where everyone knows everyone.
- **We are subject to Kenya's Data Protection Act (2019)** and we have not fully assessed our obligations under it. If you know this area, telling us honestly where we stand would be a real contribution — and it is a different, smaller ask than the project below.
- **Develop against synthetic data.** We can construct a realistic fake catchment.
- **No household data into any AI service.**
- **No screenshots, nothing on personal devices, nothing in personal cloud storage.**
- **No individual promoter performance scoring.** We supervise promoters through relationships, monthly, in person. A dashboard ranking 142 women by indicator completion would be used to discipline the ones with the hardest catchments — the flooded ones, the far ones — and it would destroy the trust the whole model runs on. This is a firm no.

## Language

- **Promoters work in Dholuo. Reporting is in English. Training is mixed.** Several promoters have limited written English and are already recording into English-labelled forms, which is a real source of error.
- **If you can reduce the amount of English a promoter must read, that is a data-quality improvement**, not a nicety. Icons, Dholuo labels, voice.
- **We write any community-facing text**, not you.
- **English is fine for working with our office staff.**

## Practical

- **Our programme manager is your contact.** She is also our best data person and she is in the field a great deal. Expect scheduling to be slow and asynchronous.
- **Remote is fine and is what we expect.** If you want to visit, we will host you, and we will be honest that hosting a visitor costs us staff time.
- **Our bandwidth is limited too.** Long video calls are expensive for us. Prefer written, or short calls.
- **Handover:** 23 staff, no developer, and no prospect of one. **Open source and self-hostable where we can be, managed and cheap where we cannot.** Anything requiring ongoing developer attention will fail, and we will be worse off.
- **Do not assume our platform choices were uninformed.** They were made by people who had to make them work in this county. Ask why before proposing a change.

## What we would say no to

- A CRM.
- Anything that increases promoter data costs.
- Individual promoter performance rankings.
- Household data in an AI service.
- A rebuild of our field data platform.
- A proposal premised on our being at an early stage of digital adoption.
