# Quarkus full-review guidance

## Operating conditions

Establish the project target: Quarkus and Java versions, JVM or native mode,
extensions, reactive stack, build tool, configuration sources, container
platform, and database drivers. The changed boundary must define: CDI scopes,
build-time augmentation, reactive and imperative boundaries, transactions,
configuration, native image, extensions, dev services, startup, and deployment.

## Failure patterns

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

## Verification to run or specify in the plan

- Boot the packaged application without dev services and verify which settings
  were fixed at build time. Exercise CDI initialization, transaction context,
  and blocking work under concurrent requests.
- If native output is shipped, run that artifact through reflection,
  serialization, resource loading, and TLS paths. Check health and shutdown
  behavior with unavailable dependencies.
