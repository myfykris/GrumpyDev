---
name: echo
description: Review Echo framework plans for middleware order, request binding, validation, context lifetime, concurrency, error responses, and graceful shutdown risks. Use when a Go plan changes Echo HTTP services, handlers, middleware, or server configuration.
---

# Echo plan review

Apply this guidance alongside the core GrumpyDev review and the `go` skill.

## Inspect evidence

- Establish the exact Go, Echo, server, and deployment versions or modes.
- Read server setup, routes, middleware order, binders and validators, context
  use, limits, dependency clients, shutdown, and integration tests.
- Trace request data, authentication, errors, goroutines, streaming, timeouts,
  client disconnects, and server lifecycle.

## Establish the operating model

Establish the project target: Echo and Go versions, server topology, middleware
stack, trusted proxies, request limits, validation, TLS termination, and
deployment target. The changed boundary must define: Middleware order, context
lifetime, binder and validator behavior, error handling, concurrency, streaming,
shutdown, proxy trust, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Middleware order, context lifetime, binder and validator behavior, error
handling, concurrency. Prove streaming, shutdown, proxy trust, deployment
through startup, invalid or denied work, cancellation, background execution,
mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for middleware-order changes, binders accepting fields that
callers must not control, request contexts retained after the request, blocking
handlers, partial responses followed by error handling, and proxy headers
trusted without an explicit proxy boundary.

- Do not retain or use Echo contexts outside the request lifecycle; copy only
  required immutable data.
- Check binding and validation against over-posting, body size, duplicate
  fields, content type, and sensitive error output.
- Verify middleware order and route coverage for authentication, authorization,
  recovery, CORS, logging, and rate limits.
- Require bounded goroutines, propagated contexts, server timeouts, and graceful
  shutdown for handlers and streams.
- Test behind the production proxy for headers, paths, TLS assumptions,
  cancellation, and draining.

## Verify the claims

- Verify these behaviors through the actual Echo lifecycle and production
  pipeline: Middleware order, context lifetime, binder and validator behavior,
  error handling, concurrency. Use the actual framework pipeline and production
  build with representative services and configuration.
- Exercise failure and edge behavior for: streaming, shutdown, proxy trust,
  deployment. Exercise invalid input, denied access, cancellation, dependency
  failure, concurrent work, shutdown, and mixed-version deployment where
  plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Go and Echo versions, server settings, middleware order, and binder
  behavior apply?
- How are validation, authentication, request limits, cancellation, errors, and
  graceful shutdown handled?

## Calibrate findings

- Treat mass assignment, auth-order bypass, unbounded input, or shutdown data
  loss as critical.
- Downgrade when explicit binding, middleware ordering, limits, and shutdown
  tests prove the boundary.

## Add to the verdict

State context and request ownership, middleware order, binding controls, timeout
and shutdown behavior, and end-to-end HTTP evidence.
