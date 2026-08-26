---
name: actix-web
description: Review Actix Web plans for worker state, extractor behavior, async blocking, middleware order, cancellation, error responses, and graceful shutdown risks. Use when a Rust plan changes Actix Web applications, handlers, middleware, or server configuration.
---

# Actix Web plan review

Apply this guidance alongside the core GrumpyDev review and the `rust` skill.

## Inspect evidence

- Establish the exact Actix Web, Rust, Tokio, and target-platform versions.
- Read application construction, worker configuration, shared state types,
  extractors, middleware, route registration, server settings, and integration
  tests.
- Trace request data, blocking work, database clients, spawned tasks,
  cancellation, error conversion, streaming bodies, and shutdown.

## Establish the operating model

Establish the project target: Actix and Rust versions, Tokio runtime, worker
counts, proxy and TLS termination, payload limits, state ownership, and
deployment model. The changed boundary must define: Extractor limits,
application and worker state, async blocking, middleware ordering, error
mapping, streaming, shutdown, TLS and proxy behavior.

Assign lifecycle, state, dependency, persistence, and security ownership for
Extractor limits, application and worker state, async blocking, middleware
ordering. Prove error mapping, streaming, shutdown, TLS and proxy behavior
through startup, invalid or denied work, cancellation, background execution,
mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for synchronous work blocking Actix workers, extractors that
turn domain errors into accidental responses, shared-state locks held across
await points, middleware ordering changes, and shutdown paths that abandon
in-flight work.

- Verify whether application data is shared or constructed per worker and
  whether its synchronization model is sound.
- Move CPU or blocking I/O off async workers and require bounds for pools, body
  sizes, concurrency, and timeouts.
- Check extractor limits, middleware order, authentication coverage, error
  mapping, and sensitive response details.
- Require ownership and cancellation for spawned tasks, streams, websockets, and
  long-running handlers.
- Test graceful drain, worker restart, client disconnect, dependency timeout,
  and production TLS or proxy behavior.

## Verify the claims

- Verify these behaviors through the actual Actix Web lifecycle and production
  pipeline: Extractor limits, application and worker state, async blocking,
  middleware ordering. Use the actual framework pipeline and production build
  with representative services and configuration.
- Exercise failure and edge behavior for: error mapping, streaming, shutdown,
  TLS and proxy behavior. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Actix Web, Rust, and Tokio versions and worker model apply to the
  service?
- How do extractors, shared state, blocking work, errors, limits, and graceful
  shutdown behave?

## Calibrate findings

- Treat blocking or unbounded work on workers, unsafe shared state, or shutdown
  data loss as critical.
- Downgrade when the path is bounded and framework-version-specific concurrency,
  limits, and shutdown tests cover it.

## Add to the verdict

State worker and state ownership, blocking boundaries, middleware and extractor
controls, shutdown behavior, and end-to-end server evidence.
