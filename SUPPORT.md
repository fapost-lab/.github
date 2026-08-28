# Getting help

## Start with the documentation

[docs.fapost.in](https://docs.fapost.in) is the source of truth and is kept in
step with the code. The pages that answer most questions:

- [Docker Compose](https://docs.fapost.in/self-hosting/docker-compose) — installation, start to finish
- [Troubleshooting](https://docs.fapost.in/self-hosting/troubleshooting) — failures actually encountered, not imagined ones
- [Concepts](https://docs.fapost.in/using/concepts) — what a tenant, a flow and a session are, and how they relate

## Then the issue tracker

Search [existing issues](https://github.com/fapost-lab/core/issues?q=is%3Aissue)
first — an installation problem is rarely unique.

If nothing matches, open one. A question is a perfectly good issue; if the answer
turns out to be in the documentation, that usually means the documentation was
not findable, which is itself worth fixing.

**What makes an answer possible:** the version you are running, how you installed
it, what you did, what happened, and what you expected instead. Logs beat
descriptions:

```bash
docker compose logs app --tail 50
docker compose logs horizon --tail 50
docker compose exec app php artisan about
```

Redact tokens and passwords before pasting. `php artisan about` prints
configuration, not secrets, but channel logs can contain both.

## Not here

**Security vulnerabilities** — see [SECURITY.md](SECURITY.md). Please do not open
a public issue.

**Questions about your own deployment's data** — nobody here can see your
installation. It is self-hosted, on your database, and no telemetry is sent
anywhere.

## Response times

This is an open-source project maintained by a small team. Issues are read, and
most get a reply within a few days. There is no support contract and no SLA. A
polite reminder on a stale issue is welcome rather than annoying.
