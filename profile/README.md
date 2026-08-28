# FaPost

Open-source platform for conversational assistants and flow automation.

Assistants that hold a conversation across channels, a visual builder for the
flows behind them, and the runtime that executes those flows reliably — queued,
retried, and isolated per tenant. Self-hosted, on your own database, under
Apache-2.0.

```bash
sh -c "$(curl -fsSL https://get.fapost.in/install.sh)"
```

**[Documentation](https://docs.fapost.in)** · **[fapost.in](https://fapost.in)**

## Repositories

| | |
|---|---|
| [**core**](https://github.com/fapost-lab/core) | The platform: flow engine, channels, assistants, admin panel |
| [**install**](https://github.com/fapost-lab/install) | One-command installer — [get.fapost.in](https://get.fapost.in) |
| [**foundation**](https://github.com/fapost-lab/foundation) | Public contracts and DTOs that Solutions and Plugins build against |
| [**support**](https://github.com/fapost-lab/support) | Reusable Eloquent primitives, with no dependency on Core |
| [**website**](https://github.com/fapost-lab/website) | fapost.in |

`foundation` and `support` are deliberately separate and deliberately do not
depend on Core: anything extending the platform compiles against the contracts,
not against the implementation behind them.

## Built with

PHP 8.4 · Laravel 12 · PostgreSQL with schema-per-tenant isolation · Redis and
Horizon for queues · Filament for the admin panel · Inertia and Vue for the flow
builder · an optional Go gateway in front of webhook ingress.

## Contributing

Issues and pull requests are welcome. Start with
[local setup](https://docs.fapost.in/contributing/local-setup), then
[pull requests](https://docs.fapost.in/contributing/pull-requests) for what a
change is expected to carry — including the CLA, which every contribution is
subject to.

Reporting a security problem is different: please do not open an issue. See
[SECURITY.md](https://github.com/fapost-lab/.github/blob/main/SECURITY.md).
