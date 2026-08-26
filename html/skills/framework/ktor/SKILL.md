---
name: ktor
description: Review Ktor plans for plugin order, coroutine ownership, request validation, serialization, authentication, client and server lifecycle, and deployment risks. Use when a Kotlin plan changes Ktor servers, clients, routes, plugins, or services.
---

# Ktor plan review

Apply this guidance alongside the core GrumpyDev review and the `kotlin` skill.

## Inspect evidence

- Read application modules, installed plugins and order, routing, content
  negotiation, authentication, coroutine dispatchers, client configuration, and
  tests.
- Trace calls, cancellation, blocking work, resources, serialization, errors,
  streaming, background tasks, and shutdown.

## Establish the operating model

Establish the project target: Ktor, Kotlin and JDK versions, engine,
serialization, authentication, coroutine and dispatcher policy, proxy topology,
and deployment environment. The changed boundary must define: Plugin order,
coroutine context, routing, content negotiation, authentication, serialization,
client and server engines, streaming, shutdown, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Plugin order, coroutine context, routing, content negotiation, authentication.
Prove serialization, client and server engines, streaming, shutdown, deployment
through startup, invalid or denied work, cancellation, background execution,
mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for plugin installation order, coroutine scopes that outlive
requests or the application, blocking I/O on constrained dispatchers,
content-negotiation mismatches, route-scoped authentication gaps, and shutdown
that cancels work without reconciliation.

- Verify plugin order and route coverage for authentication, status handling,
  content negotiation, compression, CORS, and observability.
- Keep blocking work off constrained dispatchers and require structured
  ownership for launched coroutines and background services.
- Check serializer configuration, polymorphism, defaults, unknown fields,
  content type, and contract evolution.
- Bound request bodies, streams, concurrency, client pools, timeouts, retries,
  and decompression.
- Test the actual engine and deployment for proxy headers, graceful shutdown,
  connection drain, and mixed-version clients.

## Verify the claims

- Verify these behaviors through the actual Ktor lifecycle and production
  pipeline: Plugin order, coroutine context, routing, content negotiation,
  authentication. Use the actual framework pipeline and production build with
  representative services and configuration.
- Exercise failure and edge behavior for: serialization, client and server
  engines, streaming, shutdown, deployment. Exercise invalid input, denied
  access, cancellation, dependency failure, concurrent work, shutdown, and
  mixed-version deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Kotlin, Ktor, engine, coroutine, serialization, and deployment versions
  apply?
- How do plugin order, authentication, cancellation, blocking work, errors,
  limits, and shutdown interact?

## Calibrate findings

- Treat auth plugin bypass, blocked event loops, or lost structured cancellation
  on a critical path as critical.
- Downgrade when engine-specific plugin order, coroutine ownership, limits, and
  shutdown are integration-tested.

## Add to the verdict

State plugin ordering, coroutine and resource ownership, serialization contract,
resource limits, engine assumptions, and deployment evidence.
