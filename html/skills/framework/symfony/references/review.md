# Symfony full-review guidance

## Operating conditions

Establish the project target: Symfony and PHP versions, runtime and SAPI,
Doctrine providers, Messenger transports, cache, authentication, worker
topology, and deployment process. The changed boundary must define: Container
compilation, request and kernel events, configuration, Doctrine, validation,
security voters, messenger, cache, console, workers, and deployment.

## Failure patterns

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

## Verification to run or specify in the plan

- Boot the warmed production container and exercise firewall, access-control,
  and voter decisions with different identities. Check environment-specific
  services and shared state across repeated requests.
- Fail Doctrine transactions and redeliver Messenger messages to long-running
  workers. Verify idempotency, failure transport handling, cleared worker
  state, and compatibility during worker restarts.
