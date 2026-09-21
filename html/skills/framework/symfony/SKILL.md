---
name: gd-symfony
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Symfony engineering work for service scope, event ordering, Doctrine behavior, validation, security, messaging, caching, and deployment risks."
---

# Symfony GrumpyDev review

## Quick checks

- Read bundle and framework configuration, service definitions, event
  subscribers, routes, security firewalls and voters, Doctrine mappings and
  migrations, Messenger, cache, and tests.

- Trace requests and messages through validation, authorization, transactions,
  events, retries, serialization, and deployment.

Watch especially for compiled-container and cache behavior differing by
environment, listener priority and ordering, Doctrine unit-of-work assumptions,
Messenger retries without idempotency, migrations that block production data,
and firewall or access-control rules with unintended scope.

- Assess authorization bypass, shared mutable service state, or duplicate
  irreversible message effects under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Symfony specialist.

## Verdict context

State service and event ownership, Doctrine and migration safety, authorization
coverage, message guarantees, cache behavior, and production evidence.
