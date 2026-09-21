# Echo full-review guidance

## Operating conditions

Establish the project target: Echo and Go versions, server topology, middleware
stack, trusted proxies, request limits, validation, TLS termination, and
deployment target. The changed boundary must define: Middleware order, context
lifetime, binder and validator behavior, error handling, concurrency, streaming,
shutdown, proxy trust, and deployment.

## Failure patterns

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

## Verification to run or specify in the plan

- Send malformed, oversized, and privileged fields through the real binder,
  validator, and route middleware. Verify denial and error handling before
  effects occur.
- Reuse connections under concurrent load, cancel requests, and interrupt
  streams. Check that goroutines do not retain pooled Echo contexts and that
  server shutdown drains only within its declared deadline.
