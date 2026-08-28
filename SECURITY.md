# Security Policy

## Reporting a vulnerability

**Please do not open a public issue.** A report in the issue tracker is visible
to everyone, including to whoever would use it before a fix exists.

Two private channels, either is fine:

- **GitHub** — open the *Security* tab of the affected repository and choose
  **Report a vulnerability**. This creates a private advisory only you and the
  maintainers can see, and it is where the fix is coordinated.
- **Email** — [security@fapost.in](mailto:security@fapost.in).

Please include enough to reproduce it: the affected version or commit, the
configuration it needs, and what an attacker gets out of it. A proof of concept
helps more than a description, and it stays private.

## What happens next

| | |
|---|---|
| Acknowledgement | within 3 working days |
| Initial assessment | within 10 working days — whether it reproduces, and how severe |
| Fix and advisory | coordinated with you before anything is published |

This is a small project, not a company with an on-call rota. If you have not
heard back within the acknowledgement window, please send a reminder rather than
assume the report was ignored.

We will credit you in the advisory unless you would rather stay anonymous. There
is no bug bounty.

## Supported versions

Until the first stable release, only the latest release and the `main` branch
receive fixes. Once tagged releases exist, this section will name the versions
that still get them.

## Scope

In scope are the repositories under [`fapost-lab`](https://github.com/fapost-lab)
— the platform, the packages it publishes, and the installer.

Out of scope, because they are not ours to fix, are vulnerabilities in
third-party dependencies (report them upstream; tell us if FaPost is affected),
and findings against an installation you do not operate.

### Worth knowing before reporting

A few designs are deliberate rather than oversights:

- **The installer is a shell script served over HTTPS and run by the operator.**
  That is the accepted model for this kind of tool; the mitigation is that the
  script is short, versioned, and meant to be read before it is run.
- **Webhook signatures are verified over the exact bytes received.** Anything in
  front of the application that rewrites request bodies breaks verification by
  design.
- **A self-hosted installation is as exposed as its operator makes it.** A
  missing TLS certificate or a database published to the internet is a
  configuration issue, documented in the deployment guide, not a platform
  vulnerability.
