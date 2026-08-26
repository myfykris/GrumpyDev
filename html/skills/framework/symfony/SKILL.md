---
name: symfony
description: Review Symfony plans for service scope, event ordering, Doctrine behavior, validation, security, messaging, caching, and deployment risks. Use when a PHP plan changes Symfony controllers, services, entities, messages, listeners, or operations.
---

# Symfony plan review

Apply this guidance alongside the core GrumpyDev review and the `php` skill.

## Inspect evidence

- Read bundle and framework configuration, service definitions, event
  subscribers, routes, security firewalls and voters, Doctrine mappings and
  migrations, Messenger, cache, and tests.
- Trace requests and messages through validation, authorization, transactions,
  events, retries, serialization, and deployment.

## Establish the operating model

Establish the project target: Symfony and PHP versions, runtime and SAPI,
Doctrine providers, Messenger transports, cache, authentication, worker
topology, and deployment process. The changed boundary must define: Container
compilation, request and kernel events, configuration, Doctrine, validation,
security voters, messenger, cache, console, workers, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Container compilation, request and kernel events, configuration, Doctrine,
validation, security voters. Prove messenger, cache, console, workers,
deployment through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for compiled-container and cache behavior differing by
environment, listener priority and ordering, Doctrine unit-of-work assumptions,
Messenger retries without idempotency, migrations that block production data,
and firewall or access-control rules with unintended scope.

- Check container scope, shared mutable services, lazy proxies, autowiring
  ambiguity, compiler passes, and environment-specific configuration.
- Verify firewall order, access control, voters, object authorization, CSRF
  policy, user providers, and error redaction.
- Analyze Doctrine unit-of-work, lazy loading, cascades, transaction boundaries,
  migrations, and long-running worker state.
- Define Messenger idempotency, retry and failure transports, transaction
  interaction, serialization, and worker restart.
- Test warmed production containers and caches, proxy headers, migrations,
  workers, assets, and mixed-version rollout.

## Verify the claims

- Verify these behaviors through the actual Symfony lifecycle and production
  pipeline: Container compilation, request and kernel events, configuration,
  Doctrine, validation, security voters. Use the actual framework pipeline and
  production build with representative services and configuration.
- Exercise failure and edge behavior for: messenger, cache, console, workers,
  deployment. Exercise invalid input, denied access, cancellation, dependency
  failure, concurrent work, shutdown, and mixed-version deployment where
  plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which PHP, Symfony, runtime, container, database, cache, and Messenger
  versions or transports apply?
- How do service scopes, security voters, validation, transactions, messages,
  retries, and migrations interact?

## Calibrate findings

- Treat authorization bypass, shared mutable service state, or duplicate
  irreversible message effects as critical.
- Downgrade when container scope, security, transport semantics, transactions,
  and migration behavior are feature-tested.

## Add to the verdict

State service and event ownership, Doctrine and migration safety, authorization
coverage, message guarantees, cache behavior, and production evidence.
