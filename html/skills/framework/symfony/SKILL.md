---
name: symfony
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Symfony plans and other engineering artifacts for service scope, event ordering, Doctrine behavior, validation, security, messaging, caching, and deployment risks. Project applicability: the project uses or materially depends on Symfony."
---

# Symfony GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
