# Express full-review guidance

## Operating conditions

Establish the project target: Express and Node versions, module system, proxy
topology, session store, body limits, worker or cluster model, process manager,
and deployment platform. The changed boundary must define: Middleware and error
order, request lifecycle, async failures, body parsing, proxy trust, sessions,
streaming, shutdown, Node event loop, and security boundaries.

## Failure patterns

- Verify async errors reach one controlled error handler for the actual Express
  version and wrapper conventions.
- Check middleware and router order for authentication, authorization, parsing,
  CORS, compression, logging, and error handling.
- Bound bodies, files, decompression, query complexity, concurrency, downstream
  time, and response buffering.
- Treat req.body, params, query, headers, and proxy-derived identity as
  untrusted until validated and normalized.
- Require server timeout, keep-alive, drain, connection, and signal handling
  tests under the production proxy.

## Verification to run or specify in the plan

- Throw synchronous errors and reject asynchronous handlers through the
  configured Express version and middleware chain. Verify one controlled
  response, including failures after response streaming begins.
- Send spoofed proxy headers and oversized or malformed bodies through
  protected routes. Test keep-alive connections and slow streams during
  shutdown behind the actual proxy configuration.
