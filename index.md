---
okf_version: "0.2"
---

# Civic Knowledge Sample — collection listing

**⚠ Every organization in this collection is fabricated.** See [README.md](README.md), which is the canonical record for the collection.

# Start here

* [README.md](README.md) - what this collection is, how to use it, and what is deliberately broken
* [organizations/](organizations/README.md) - the fifteen organization bundles, all in one folder
* [organizations/synthetic-frogtown-community-table/](organizations/synthetic-frogtown-community-table/index.md) - the worked reference bundle; read this one first

# The specification

* [docs/civic-profile.md](docs/civic-profile.md) - the `x-civic` civic profile, v0.6. Five required fields
* [docs/use-cases.md](docs/use-cases.md) - what the graph makes answerable, with the queries written out
* [docs/data-dictionary.md](docs/data-dictionary.md) - lookup tables for every file and frontmatter field in a bundle

# Organization bundles

All fifteen live under one folder.

* [organizations/](organizations/README.md) - the canonical record for the org set: what they are for, what is in a bundle, what is deliberately broken
* [organizations/synthetic-black-mountain-workforce-partnership/](organizations/synthetic-black-mountain-workforce-partnership/index.md) - workforce training, Letcher County, Kentucky
* [organizations/synthetic-central-valley-farmworker-law-center/](organizations/synthetic-central-valley-farmworker-law-center/index.md) - legal aid, Fresno County, California
* [organizations/synthetic-corporacion-rio-vivo/](organizations/synthetic-corporacion-rio-vivo/index.md) - environmental justice, Cali, Colombia
* [organizations/synthetic-crescent-city-career-lab/](organizations/synthetic-crescent-city-career-lab/index.md) - workforce training, New Orleans. **Lapsed determination**
* [organizations/synthetic-cumberland-gap-health-cooperative/](organizations/synthetic-cumberland-gap-health-cooperative/index.md) - rural health, Letcher County, Kentucky
* [organizations/synthetic-eastside-harvest-collective/](organizations/synthetic-eastside-harvest-collective/index.md) - food security, Detroit. **Unreconciled budget**
* [organizations/synthetic-frogtown-community-table/](organizations/synthetic-frogtown-community-table/index.md) - food security, Saint Paul. **The worked reference**
* [organizations/synthetic-fundacja-prawo-i-schronienie/](organizations/synthetic-fundacja-prawo-i-schronienie/index.md) - legal aid, Warsaw, Poland
* [organizations/synthetic-gulf-corridor-justice-project/](organizations/synthetic-gulf-corridor-justice-project/index.md) - environmental justice, New Orleans
* [organizations/synthetic-motor-city-trades-institute/](organizations/synthetic-motor-city-trades-institute/index.md) - workforce training, Detroit
* [organizations/synthetic-north-star-immigrant-defense/](organizations/synthetic-north-star-immigrant-defense/index.md) - legal aid, Saint Paul
* [organizations/synthetic-nyando-community-health-trust/](organizations/synthetic-nyando-community-health-trust/index.md) - rural health, Kisumu County, Kenya. **Insufficient evidence**
* [organizations/synthetic-riverbend-air-alliance/](organizations/synthetic-riverbend-air-alliance/index.md) - environmental justice, Detroit
* [organizations/synthetic-sierra-foothills-community-health/](organizations/synthetic-sierra-foothills-community-health/index.md) - rural health, Fresno County, California
* [organizations/synthetic-valle-verde-food-network/](organizations/synthetic-valle-verde-food-network/index.md) - food security, Fresno County, California

# Shared nodes

* [_shared/](_shared/index.md) - classification and place nodes. One required layer (PCS), three optional ones

# Tooling

* [schemas/civic_schema.json](schemas/civic_schema.json) - JSON Schema for the profile
* [scripts/validate.py](scripts/validate.py) - conformance checker for both levels
* [scripts/build_hubs.py](scripts/build_hubs.py) - regenerates every hub membership list from the org frontmatter
* [scripts/extract_pcs.py](scripts/extract_pcs.py) - vendors the attributed Candid PCS subset
* [scripts/generate_org_json.py](scripts/generate_org_json.py) - consolidates one organization's frontmatter into a single JSON file
* [scripts/generate_mapped_json.py](scripts/generate_mapped_json.py) - re-expresses an organization's frontmatter against another schema (e.g. [Philanthropy Data Commons](https://philanthropydatacommons.org/base-fields-list/)) via `scripts/mappings/`; see [scripts/README.md](scripts/README.md)
