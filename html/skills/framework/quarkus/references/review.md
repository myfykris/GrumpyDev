# Quarkus standard review

## Establish the operating model

Establish the project target: Quarkus and Java versions, JVM or native mode,
extensions, reactive stack, build tool, configuration sources, container
platform, and database drivers. The changed boundary must define: CDI scopes,
build-time augmentation, reactive and imperative boundaries, transactions,
configuration, native image, extensions, dev services, startup, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for CDI
scopes, build-time augmentation, reactive and imperative boundaries,
transactions, configuration. Prove native image, extensions, dev services,
startup, deployment through startup, invalid or denied work, cancellation,
background execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

- Distinguish build-time from runtime configuration and reject plans that expect
  runtime changes to alter build-fixed behavior.
- Keep blocking work off event-loop threads and verify worker-pool, transaction,
  and context propagation.
- Check CDI scopes, proxyability, initialization order, dev-mode assumptions,
  and lifecycle callbacks.
- Require native-image registration and native tests for reflection, resources,
  proxies, serialization, TLS, and dynamic loading.
- Test JVM and native artifacts under production configuration, health checks,
  rolling deployment, and dependency failure.

## Verify the claims

- Verify these behaviors through the actual Quarkus lifecycle and production
  pipeline: CDI scopes, build-time augmentation, reactive and imperative
  boundaries, transactions, configuration. Use the actual framework pipeline and
  production build with representative services and configuration.
- Exercise failure and edge behavior for: native image, extensions, dev
  services, startup, deployment. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Java, Quarkus, build mode, native-image toolchain, extension, and
  deployment versions apply?
- How do dependency injection scopes, reactive and blocking work, configuration,
  transactions, and startup differ by mode?

## Calibrate findings

- Downgrade when JVM and native modes, extension versions, transactions, and
  lifecycle are both tested where supported.
