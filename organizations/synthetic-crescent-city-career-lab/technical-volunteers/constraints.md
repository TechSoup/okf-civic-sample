---
type: volunteer-constraints
title: "synthetic-Crescent City Career Lab — Volunteer constraints & preferences"
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

## Our participants are working two jobs

This is the fact everything else follows from. Most people in our cohorts are employed while they train, on schedules they do not control, and they are training in the evenings and on weekends. See [population](../population.md).

- **Never build anything that adds a step for a participant.** Not a form, not a survey, not a check-in, not an app to install. Their time is the scarcest resource in this building and we are already asking for all of it.
- **Instruction time is sacred.** Do not propose anything that takes classroom minutes.
- **Do not design around participants "catching up on their own time."** There is no such time.

## About participants' data

- **Signed confidentiality agreement** before any access. Least-privilege, task-scoped.
- **Develop against synthetic data.** We can produce a realistic fake cohort.
- **No scoring, ranking, or predicting participants.** Not completion likelihood, not employability, not risk of dropping out. We know exactly when people leave — weeks four to seven — and we know why, and it is money and childcare, not disposition. A model would tell us the same thing with a veneer of individual prediction, and then somebody would use it to decide who gets the childcare stipend. Not built here.
- **Identifiers are a compliance requirement, not a convenience.** We collect a date of birth and partial Social Security number because the state portal demands them. Anything you build must handle those as sensitive and reduce, never expand, where they travel. **We are aware they currently arrive by email into a shared inbox, and if you want to fix that we would be grateful.**

## On AI, for the project we are asking about

We are comfortable with this one, and we want to be precise about why: **it looks at public job postings, not at people.** That is a genuinely different risk category from most AI proposals and we do not want the caution appropriate to those imported here.

What we do care about:

- **A model's reading of the labor market must not decide what we teach.** This is the real risk in this project. If an extraction says employers want a particular tool, that is an input to a curriculum conversation with our instructors and our employer partners — not a signal to change a course. Labor-market data is noisy, postings are aspirational, and a job description is written by someone who copied the last one. **We have seen training programmes chase a keyword and produce graduates nobody wanted.**
- **Show us the postings, not just the conclusion.** Any finding must link back to the actual postings behind it so an instructor can read them and judge. A number we cannot trace is a number we will not act on.
- **Do not tell us what is "in demand" in a way that sounds authoritative.** Give us frequencies with counts and date ranges and let us draw the conclusion. If a chart makes a weak signal look strong, it is worse than no chart.
- **Respect the sources.** Whatever you gather, gather it in a way we would be comfortable explaining — honour robots directives and terms, throttle politely, use an API where one exists. We are not going to build something we would be embarrassed about.

## Working with us

- **Our director of programs is your contact.** Instructors are teaching evenings and weekends; you will get them in the daytime gaps and there are not many.
- **Remote is fine** for this project.
- **Storm season is real.** Late summer, expect schedules to move. Build in slack the way we do.
- **Handover:** nineteen staff, no developer, and our instructors teach IT — which does not mean they will maintain your code. **Anything requiring maintenance needs an owner agreed in advance, and "one of the instructors could probably figure it out" is not an owner.**

## One thing we would appreciate you noticing

Our development director left last November and we are still finding things that were registered to her email address. If you come across accounts, subscriptions, or portal registrations in her name while you are working, **please tell us rather than assuming somebody knows.**

We have already had one consequence from this that we would rather not repeat.

## What we would say no to

- Anything asking more of participants.
- Any model that scores or predicts individuals.
- A curriculum recommendation engine that we are expected to act on directly.
- Scraping that we would not want to explain.
