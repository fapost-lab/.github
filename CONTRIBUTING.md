# Contributing

Thanks for considering it. This file is the short version; the working detail
lives in the [documentation](https://docs.fapost.in), which is the source of
truth and is kept current with the code.

## Before you write code

**Open an issue first for anything non-trivial.** A bug fix or a typo needs no
preamble. A new node type, a schema change, or anything that alters a public
contract does — the architecture has constraints that are not obvious from the
outside, and finding out about them in review costs you a rewrite.

## Getting set up

[Local setup](https://docs.fapost.in/contributing/local-setup) covers both paths:
Docker, which matches production, or a local PHP install if you already run one.

```bash
composer test          # the suite
composer run test:arch # architectural rules, enforced by PHPStan and PHPat
vendor/bin/pint        # formatting — run it before you push
```

## What the project expects of a change

These are enforced by tests rather than by review, so they fail fast:

- **Every PHP file declares `strict_types=1`**, classes are `final` by default,
  constructors use property promotion, and return types are explicit.
- **Tenant context is never assumed.** Core code fails fast when it is required
  and missing; there is no fallback to a default tenant and no branching on
  deployment shape.
- **Migrations do not read runtime state.** No `app()`, no `config()`, no tenant
  services in `up()` or `down()`.
- **`foundation` and `support` never depend on Core.** A contract needed by an
  external Solution or Plugin belongs in `foundation`.
- **Every change carries a test.** The narrowest one that would have caught the
  bug, run and passing.

The reasoning behind each is in
[conventions](https://docs.fapost.in/contributing/conventions) and the pages
beside it.

## Pull requests

See [pull requests](https://docs.fapost.in/contributing/pull-requests) for what
a change is expected to carry. In short: one concern per pull request, a
description that says why rather than restating the diff, and a green suite.

Documentation is part of the change, not a follow-up. If behaviour an operator
or user can observe is different, the page describing it changes in the same
pull request.

## Legal

Contributions are accepted under [Apache-2.0](https://github.com/fapost-lab/core/blob/main/LICENSE),
and every contributor signs a CLA — see
[legal](https://docs.fapost.in/contributing/legal). The name and logo are
trademarks and are not covered by the licence; the terms for using them are in
`TRADEMARK.md`.

## Security

Not here — see [SECURITY.md](SECURITY.md). Please do not open a public issue for
a vulnerability.
