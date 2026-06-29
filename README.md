# OKF Civic Sample — Civil-Society Knowledge as an Open Knowledge Format Bundle

> A reference example of representing civil-society knowledge — community resources and nonprofit tech offers — in the Open Knowledge Format (OKF).

![license: CC BY-SA 4.0](https://img.shields.io/badge/license-CC_BY--SA_4.0-blue)
![format: OKF v0.1](https://img.shields.io/badge/format-OKF_v0.1-success)
![civic profile: v0.5](https://img.shields.io/badge/civic_profile-v0.5-orange)
![maintained by TechSoup Global Network](https://img.shields.io/badge/maintained_by-TechSoup_Global_Network-7B2FBE)

**[Learn more about TechSoup](https://about.techsoup.org/) · [Support TechSoup](https://www.every.org/techsoup)**

A small, open **reference bundle** showing how civil-society knowledge — community resources, services, and the intelligence needed to use them — can be represented in Google's [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf).

It is also a working **Obsidian vault**: clone it, open the folder in [Obsidian](https://obsidian.md), and you can read, link, and explore the knowledge the same way a human maintainer would. The format is just markdown + YAML — no database, no platform, no lock-in.

> **This is a sample, not a catalog.** The meal-site records are a real sample from [Range](https://www.rangeapp.org/) (Caravan Studios, a division of TechSoup); the offers are an abstracted sample from TechSoup's Verbose Knowledge Base. The point is the *method* and the *shape* — not the full corpus.

## Why this exists

The nonprofit sector runs on knowledge that is scattered across incompatible systems — directories, spreadsheets, wikis, and people's heads. OKF offers a portable, vendor-neutral way to represent that knowledge so it is readable by humans *and* by AI agents, and so it can be shared and federated across organizations without anyone owning the pipe.

TechSoup is adopting OKF for exactly this. This repo demonstrates the pattern for **civil society** specifically — the first such reference we're aware of — and proposes a lightweight **civic profile** (see [`docs/civic-profile.md`](docs/civic-profile.md)) for the things the sector needs that core OKF leaves open: eligibility, lifecycle/status, relationships between resources, provenance, and trust signals.

## How it maps to OKF

- **Files are the knowledge.** Each resource is a markdown file with YAML frontmatter. The directory *is* the bundle.
- **`type` is the only required field.** Everything else is recommended or a producer extension.
- **`okf_version`** is declared in the root [`index.md`](index.md).
- **Links are graph edges.** Resources reference each other with normal markdown links (referral partners, alternatives, capabilities), and the *type* of each edge is carried in the link title (`alternative`, `complements`) following OKF issue [#101](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/101) — so the edges are machine-readable, not just prose.
- **`index.md` files** give progressive disclosure as an agent (or a person) walks the tree — each is a plain listing (a map of its directory's contents), with no frontmatter except the bundle-root index.
- **Extensions are namespaced** under `x-civic:` so they're clearly additive to core OKF (see the civic profile).

## Relationship to Open Referral / HSDS

For human-services directory data, the sector's established standard is **[Open Referral / HSDS](https://docs.openreferral.org/)** (Human Services Data Specification, v3.0.1). This bundle doesn't compete with it: HSDS is the structured *data-exchange* layer (normalized objects, JSON Schema, an API); OKF + the `x-civic` profile is the human- and AI-readable *knowledge* layer that sits alongside it. The meal-site fields map directly onto HSDS objects — see the [crosswalk in the civic profile](docs/civic-profile.md).

## How to use it

- **As a reader/agent:** browse on GitHub, or `git clone` and read the markdown.
- **As a maintainer:** open the folder as an Obsidian vault — frontmatter shows in the Properties panel, links power the graph view, and templates make new records easy.
- **To check conformance:** a standalone `okf-validate` tool (checks every doc has a `type` and reports link health) is in the works — link coming once it's published.

## Licensing

Licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](LICENSE) — deliberately viral, so derivatives stay open and credit the source. Use it, fork it, build on it; just credit the source and keep your derivatives open.

## Contributing & contact

Built at TechSoup; maintained in the open. We'd love to see this pattern adopted and the civic profile debated — see [`CONTRIBUTING.md`](CONTRIBUTING.md). Issues and pull requests welcome.

## Acknowledgments

This reference bundle was developed with AI assistance: drafted and structured in collaboration with Anthropic's **Claude (Opus 4.8)**, using **Claude Code**. The direction, data choices, civic-profile design, and review were human (TechSoup) — the AI scaffolded; a person decided. We name it in the spirit of transparency and showing the work.
