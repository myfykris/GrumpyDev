# Symfony standard review

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when container scope, security, transport semantics, transactions,
  and migration behavior are feature-tested.
