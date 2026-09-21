# Gin full-review guidance

## Operating conditions

Establish the project target: Gin and Go versions, middleware, trusted proxies,
binding and validation approach, request limits, server topology, and deployment
target. The changed boundary must define: Middleware order, context reuse,
binding and validation, errors, goroutine safety, streaming, shutdown, proxy
trust, and server configuration.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise route groups with denied access, malformed bodies, and attempts to
  bind privileged fields. Check that middleware aborts prevent later handlers
  from performing effects.
- Run concurrent and canceled requests with the race detector where supported.
  Verify detached work does not retain pooled Gin contexts, and test
  trusted-proxy handling and shutdown with open connections.
