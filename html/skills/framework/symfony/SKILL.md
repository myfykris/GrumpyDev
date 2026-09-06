---
name: symfony
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Symfony engineering work for service scope, event ordering, Doctrine behavior, validation, security, messaging, caching, and deployment risks."
---

# Symfony GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `php` skill.

## Lean review

- Read bundle and framework configuration, service definitions, event
  subscribers, routes, security firewalls and voters, Doctrine mappings and
  migrations, Messenger, cache, and tests.

- Trace requests and messages through validation, authorization, transactions,
  events, retries, serialization, and deployment.

Watch especially for compiled-container and cache behavior differing by
environment, listener priority and ordering, Doctrine unit-of-work assumptions,
Messenger retries without idempotency, migrations that block production data,
and firewall or access-control rules with unintended scope.

Lean mode is insufficient when this material severity condition may apply:

- Treat authorization bypass, shared mutable service state, or duplicate
  irreversible message effects as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Symfony evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State service and event ownership, Doctrine and migration safety, authorization
coverage, message guarantees, cache behavior, and production evidence.
