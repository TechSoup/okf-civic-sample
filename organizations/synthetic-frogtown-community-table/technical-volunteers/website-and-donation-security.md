---
type: volunteer-request
title: A donation channel we can trust, and somebody who has the keys
description: Get $70K/year of online giving off unmaintained self-hosted WordPress with an abandoned payment plugin, establish credential ownership, and change nothing about how the site looks.
tags: [technical-volunteers, request, synthetic, security, website]
synthetic: true
status: draft
generated: { by: claude-code/claude-opus-5, at: 2026-07-29T00:00:00Z }
sources:
  - id: inventory
    resource: ../technology/inventory.md
    title: This organization's technology inventory
  - id: constraints
    resource: constraints.md
    title: This organization's volunteer constraints
x-civic:
  profile: civic/0.6
  project_shape: website-security-remediation
---

# Volunteer project — Website & donation channel security

> **⚠ Synthetic.** A fabricated project request in a fabricated bundle. `status: draft` is core OKF v0.2 §5.4 and it is accurate: **the organization owns this and has not blessed it.** Nothing should be posted from a draft.

Note the two `sources` entries. Both point at documents *inside this bundle* rather than at external material, which OKF §5.1 permits and which makes the derivation edge explicit: this request was scoped from [the inventory](../technology/inventory.md)[^inventory] and [the constraints](constraints.md).[^constraints] That is the whole method — read what the organization has, read what it will not accept, and propose something inside both.

## The need, in the org's words

A volunteer built our website in 2018. He was generous, he did a good job, and then he moved away.

Since then: WordPress core has not been updated in a long time, the donation plugin hasn't had a release in over three years and we think the person who made it has stopped, the theme licence lapsed, and — the part that worries us most — **we are not confident anyone here can log into the admin panel.** Our executive director has a password that may or may not work; nobody has tried in about a year.

That form takes about **$70,000 a year** from people who trust us. It is a sixth of our budget and it is the only way to give to us online.

We would also like to know whose credit card our domain is renewing on, because we don't think it's ours.

## What this project is not

**It is not a website redesign.** Per [constraints.md](constraints.md), and the organization is direct about having been offered one twice.

The site looks dated. The photographs are old. **Neither of those is the problem.** The problem is an unmaintained payment-adjacent system that nobody owns. A volunteer who fixes that and changes nothing visual has done exactly the right job. A volunteer who arrives with a design concept has replaced the organization's problem with a more interesting one.

## Confirm first — and the first item may change everything

1. **Can anyone log in?** Establish this on day one. If nobody has working admin credentials, this becomes a recovery project before it becomes a remediation project — via the host, the domain registrar, or worst case a rebuild from what is publicly visible. **Everything below assumes access; check the assumption first.**
2. **Who owns the domain, and whose payment method renews it?** The organization suspects a card belonging to someone who left. A lapsed domain would take down the site and the email addresses that depend on it, and this is a more common way small organizations lose a website than compromise is.
3. **Where does the money actually go?** Which payment processor, whose account, who receives the notifications, and how the organization reconciles online gifts today. There may be a third number here that neither the donor database nor the accounting system matches.
4. **Has the site already been compromised?** Nobody has looked. Assume it may have been and check before treating anything on it as trustworthy. If it has, the response changes shape and the organization's donors may need to be told — which is the executive director's decision and a board conversation, not a volunteer's call.
5. **Can online giving move to a hosted service?** Per [constraints.md](constraints.md) the organization can pay for hosting and would rather pay than accept something fragile. A managed donation platform removes the maintenance burden permanently, which is worth more here than any amount of careful patching.

## What a volunteer would do (roughly 2–4 weeks)

1. **Establish access and ownership.** Admin credentials, host account, domain registrar, payment processor — all in the **organization's name**, on an **organizational payment method**, documented somewhere the board chair can find. This is the deliverable the organization says it cares most about.
2. **Check for compromise** before trusting anything. If found, stop and escalate rather than quietly cleaning up.
3. **Move the donation channel to a managed platform.** Recommended over patching for one reason: patching leaves the organization owning a maintenance obligation it cannot meet, and in three years someone will write this request again. A hosted donation page with the organization's branding, PCI handled by the vendor, and nothing to update is the answer that stays fixed. Confirm the fee structure — for a small organization the difference between platforms is real money.
4. **Then deal with the site itself**, whichever way is cheapest to keep safe: update core, theme, and plugins if the site can carry it, or move the handful of static pages to managed hosting and retire the self-hosted installation. **Visual output should be essentially unchanged.**
5. **Strip what should not be there.** No shopper-facing data collection of any kind — no visit registration, no intake form, no email capture on the shelf pages. And **remove any photograph of a shopper the organization cannot produce a permission for.**
6. **Reconcile the three numbers** — website donations, donor database, accounting — for the last twelve months, and say so if they do not agree. This may be the most useful hour in the project.
7. Leave a **plain-language handover**: where everything lives, how to log in, how to get back in if the password is lost, who to call about the payment platform, and when the domain renews. Written for a non-technical executive director with two hours a week.

**Definition of done:** online giving runs on a platform nobody at the organization has to maintain; the organization owns every credential and the domain on its own payment method; the handover document has been walked through with the executive director and she has successfully logged in while you watched; and the site looks the same as it did.

## What the volunteer should bring

- **Practical web security** for small sites — not penetration testing, but the judgment to assess an unmaintained WordPress, recognize a compromise, and know when patching is the wrong answer.
- **Credential and account hygiene discipline.** Half this project is the unglamorous work of getting things into the right name.
- **Familiarity with nonprofit donation platforms**, and honest views on fee structures at $70K/year of small gifts.
- **The restraint not to redesign anything.** The crux, and the reason two previous offers did not fit.
- Willingness to write **documentation for a non-technical reader** and then sit with her while she uses it.

Per [constraints.md](constraints.md): **no redesign**, **do not migrate the donor database**, **nothing connecting shelf data to anything**, **no translate widget** (the site is for donors, not shoppers), and **no solution that requires a volunteer's continued involvement.**

## Capacity gained

The organization stops having a sixth of its revenue running through software nobody owns. If a password is lost, it can be recovered. If the domain is about to lapse, someone knows. And when the executive director needs to change a paragraph on the site, she can.

The thing that would be genuinely new: **the organization would no longer be one departed volunteer away from a problem it cannot diagnose.** That is worth more than the technical fix, and it is why the handover is the real deliverable.

## Data sensitivity

**Low for most of the work, sharp in two places.**

Website content and configuration are not sensitive. Most of this project touches nothing confidential.

The two exceptions: **donor payment information**, which is why the recommendation is to move to a platform where neither the organization nor its volunteers handle card data at all; and **photographs of shoppers**, which are more sensitive than they look. An image of an identifiable person at an immigrant-serving food shelf, on a public website, is a disclosure of that person's food insecurity and possibly of their presence in the country. Anything without a documented permission comes down.

**Nothing in this project should touch shelf data**, and the site should be left in a state where it cannot collect any. That is a deliberate design outcome the organization has asked for, and it is worth preserving actively rather than merely not violating.

[^inventory]: This organization's technology inventory
[^constraints]: This organization's volunteer constraints
