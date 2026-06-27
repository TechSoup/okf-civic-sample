# Contributing

This is a reference bundle and an open invitation. Two kinds of contribution are especially welcome:

1. **Adopt the pattern.** Publish your own OKF bundle for your resources or programs. Tell us — we'd like to point to a growing set of civil-society examples.
2. **Shape the civic profile.** The proposed [`x-civic` profile](docs/civic-profile.md) is a draft. Open an issue to debate a field, propose a shared vocabulary for `capability`/`category`, or discuss how it should relate to [Open Referral / HSDS](https://openreferral.org).

## How

- Open an **issue** to propose conventions, report a broken link, or ask a question.
- Open a **pull request** for new sample records, fixes, or tooling.

## Validating the bundle

This repo ships a validator (`scripts/validate.py`) that checks frontmatter, conformance to [`schemas/civic_schema.json`](schemas/civic_schema.json), the `civic/0.3` profile declaration, and that each record's `x-civic.relations` matches its prose link-title edges (reciprocally).

```sh
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python scripts/validate.py            # validate every record
./venv/bin/python scripts/validate.py --write    # regenerate relations from prose links
```

**Edges are authored as prose links only** — the `[Title](file.md "complements: …")` link-title token (per OKF issue #101) is the source of truth. Run `--write` to regenerate the `x-civic.relations` blocks; never edit them by hand.

**Before you push**, run `python3 scripts/validate.py` — every record must pass. To run it automatically, install the provided git hook (it isn't auto-installed):

```sh
ln -s ../../scripts/pre-push .git/hooks/pre-push
```

## Licensing of contributions

By contributing, you agree that your contributions are offered under **CC BY-SA 4.0** (see [LICENSE](LICENSE)).

This project relates to Google's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf); contributions to the upstream standard are encouraged there.
