# Contributing

This is a reference implementation and an open invitation. Three kinds of contribution are especially welcome.

1. **Adopt the pattern.** Publish an OKF bundle for your own organization, or for the organizations you work with. Tell us — we would like to point at a growing set of civil-society examples.
2. **Argue with the profile.** [`docs/civic-profile.md`](docs/civic-profile.md) is a draft proposal. Four required fields is a deliberate, arguable choice. Open an issue if you think it should be three, or five, or bound to a different vocabulary. The open questions at the end of that document are the ones we most want help with.
3. **Break the sample.** Build something against the fifteen bundles and tell us where they were unrealistic, or where your tooling fell over. That is what they are for. [`docs/use-cases.md`](docs/use-cases.md) ends with a list of ways to try.

## The two things not to do

**Do not add a real organization to this collection.** Every folder carries a `synthetic-` prefix and every record carries `synthetic: true`, and that marking is the only thing keeping fabricated budgets and determinations out of real totals. A pull request that adds a real organization will be declined regardless of how good the record is.

**Do not fabricate a code in a real vocabulary.** PCS is Candid's, NTEE is the IRS's, SDG is the UN's. An invented-but-plausible code is worse than an empty field, because it breaks any downstream crosswalk that trusts it and it is harder to detect than an obvious gap. If no code fits, use a level-1 parent deliberately and say why in `org_type_note` or `classification_note` — that is what the Colombian and Kenyan bundles do. **An empty slot documented as empty is the intended state.**

The same applies to statistics about real places. The [situation nodes](_shared/situations/index.md) carry stubs naming the authoritative source rather than fabricated numbers, because a synthetic organization cannot be mistaken for real and a synthetic poverty rate for a real county can.

## Adding an organization

```sh
cp -R organizations/synthetic-frogtown-community-table organizations/synthetic-your-org
# rewrite the contents, then:
./venv/bin/python scripts/extract_pcs.py /path/to/PCS_Taxonomy_Definitions_2024.xlsx  # only if you used new codes
./venv/bin/python scripts/build_hubs.py
./venv/bin/python scripts/validate.py
```

`build_hubs.py` rebuilds every hub membership list, place roster, and `_shared/` index from your frontmatter. **Do not edit a `<!-- GENERATED -->` block by hand** — `validate.py` fails if one is stale.

The required frontmatter is four fields plus the profile declaration. Assign PCS codes from Candid's published taxonomy, not from memory:

```yaml
x-civic:
  profile: civic/0.6
  subject: [SS030601]          # PCS Subject
  population: [PG010000]       # PCS Population
  org_type: EA040000           # PCS OrgType
  registration_country: US     # ISO 3166-1 alpha-2
```

## Two conventions worth following

**Structural links are markdown links; emergent terms are wikilinks.** A wikilink that resolves to a file is a mistake and the validator says so — use a markdown link so a plain OKF consumer sees the edge. A wikilink that resolves to *nothing* is the point: it is a term the controlled vocabulary cannot carry, and OKF §6.1 explicitly permits it. See [the profile](docs/civic-profile.md) on why both layers exist, and `validate.py --terms` for what the collection currently reaches for.

**Attribute claims with footnotes, not parentheticals.** Declare a source in `sources` with an `id`, then cite it from the body as `[^id]` (OKF v0.2 §5.1). The join is keyed, so reordering the list cannot silently misattribute a claim.

## Validating

```sh
python3 -m venv venv
./venv/bin/pip install -r requirements.txt

./venv/bin/python scripts/validate.py             # both conformance levels + hub freshness
./venv/bin/python scripts/validate.py --quiet     # failures only
./venv/bin/python scripts/validate.py --terms     # the emergent vocabulary
./venv/bin/python scripts/validate.py --self-test # confirm the fixtures are rejected
```

The validator reports **two independent levels**, and it is worth understanding why before reading its output:

- **Core OKF v0.2 (§11)** — parseable frontmatter, a non-empty `type`, and correctly shaped `index.md`/`log.md`. This is all the format itself requires.
- **civic/0.6** — a promise a record opts into by declaring `x-civic.profile`. Failing it means your declaration is false; it does **not** mean your bundle is bad OKF.

Nothing under `x-civic` can make a bundle non-conformant with core OKF: §11 requires consumers to tolerate unknown keys. [`schemas/fixtures/missing-required-field.md`](schemas/fixtures/missing-required-field.md) exists to demonstrate exactly that case — valid core OKF, invalid profile.

**Before you push**, run the validator. To do it automatically:

```sh
ln -s ../../scripts/pre-push .git/hooks/pre-push
```

## How

- Open an **issue** to propose a convention, report a broken link, or challenge a required field.
- Open a **pull request** for new bundles, fixes, or tooling.

## Licensing of contributions

By contributing you agree that your contributions are offered under **CC BY-SA 4.0** (see [LICENSE](LICENSE)). PCS content remains © Candid under CC BY 4.0 — see [NOTICE](NOTICE).

This project relates to Google's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf); contributions to the upstream specification are encouraged there. Several things this profile used to carry are now core v0.2 fields, which is the outcome we were hoping for.
