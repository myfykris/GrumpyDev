---
name: gin
description: Review Gin plans for middleware order, request binding, validation, context lifetime, concurrency, error responses, and graceful shutdown risks. Use when a Go plan changes Gin HTTP services, handlers, middleware, or server configuration.
---

# Gin plan review

Apply this guidance alongside the core GrumpyDev review and the `go` skill.

## Inspect evidence

- Establish the exact Go, Gin, server, and deployment versions or modes.
- Read engine setup, routes and groups, middleware order, binders and
  validators, limits, dependency clients, server settings, and integration
  tests.
- Trace request data, context propagation, authentication, errors, goroutines,
  streaming, timeouts, and shutdown.

## Establish the operating model

Establish the project target: Gin and Go versions, middleware, trusted proxies,
binding and validation approach, request limits, server topology, and deployment
target. The changed boundary must define: Middleware order, context reuse,
binding and validation, errors, goroutine safety, streaming, shutdown, proxy
trust, and server configuration.

Assign lifecycle, state, dependency, persistence, and security ownership for
Middleware order, context reuse, binding and validation, errors, goroutine
safety. Prove streaming, shutdown, proxy trust, server configuration through
startup, invalid or denied work, cancellation, background execution, mixed
versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for binding without explicit validation, mass assignment into
privileged fields, request contexts used from later goroutines, middleware-order
changes, abort and response-write sequencing, and client addresses accepted from
untrusted proxy headers.

- Do not retain or use Gin contexts after the request; copy required values
  before starting owned asynchronous work.
- Check binding and validation for content type, duplicate fields, unknown
  fields, body size, over-posting, and sensitive errors.
- Verify middleware and route-group coverage for authentication, authorization,
  recovery, CORS, logging, and limits.
- Require propagated standard contexts, bounded goroutines, server timeouts, and
  graceful draining.
- Test proxy headers, trusted-proxy configuration, path handling, client
  cancellation, dependency failure, and shutdown.

## Verify the claims

- Verify these behaviors through the actual Gin lifecycle and production
  pipeline: Middleware order, context reuse, binding and validation, errors,
  goroutine safety. Use the actual framework pipeline and production build with
  representative services and configuration.
- Exercise failure and edge behavior for: streaming, shutdown, proxy trust,
  server configuration. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Go and Gin versions, server configuration, middleware order, and binding
  rules apply?
- How are validation, authentication, limits, cancellation, errors, shared
  state, and shutdown handled?

## Calibrate findings

- Treat auth-order bypass, unsafe binding, data races, or unbounded request work
  as critical.
- Downgrade when exact binding, middleware, concurrency, limits, and shutdown
  behavior are tested.

## Add to the verdict

State request and context ownership, middleware coverage, binding controls,
proxy trust, shutdown behavior, and HTTP integration evidence.
