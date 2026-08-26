---
name: express
description: Review Express plans for middleware order, async error propagation, request validation, authorization, resource limits, proxy behavior, and shutdown risks. Use when a JavaScript or TypeScript plan changes Express applications, routers, middleware, or HTTP handlers.
---

# Express plan review

Apply this guidance alongside the core GrumpyDev review and the `javascript` or
`typescript` skill.

## Inspect evidence

- Read application setup, Express and Node versions, routers, middleware order,
  validation, authentication, proxy settings, server timeouts, and integration
  tests.
- Trace request data, async handlers, errors, streams, uploads, downstream
  calls, background work, and shutdown.

## Establish the operating model

Establish the project target: Express and Node versions, module system, proxy
topology, session store, body limits, worker or cluster model, process manager,
and deployment platform. The changed boundary must define: Middleware and error
order, request lifecycle, async failures, body parsing, proxy trust, sessions,
streaming, shutdown, Node event loop, and security boundaries.

Assign lifecycle, state, dependency, persistence, and security ownership for
Middleware and error order, request lifecycle, async failures, body parsing,
proxy trust. Prove sessions, streaming, shutdown, Node event loop, security
boundaries through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for middleware that falls through or sends twice, rejected
promises or callback failures that are not forwarded under the selected Express
version and wrapper conventions, global request state, body and proxy defaults
treated as security controls, and CPU or synchronous I/O blocking the event
loop.

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

## Verify the claims

- Verify these behaviors through the actual Express lifecycle and production
  pipeline: Middleware and error order, request lifecycle, async failures, body
  parsing, proxy trust. Use the actual framework pipeline and production build
  with representative services and configuration.
- Exercise failure and edge behavior for: sessions, streaming, shutdown, Node
  event loop, security boundaries. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Node.js and Express versions, module mode, proxy topology, and server
  runtime apply?
- How do middleware order, trust proxy, body limits, async errors,
  authentication, and shutdown behave?

## Calibrate findings

- Treat auth bypass, spoofed client identity, unhandled async failure, or
  unbounded request input as critical.
- Downgrade when the deployment boundary, middleware order, error path, limits,
  and shutdown are integration-tested.

## Add to the verdict

State middleware and validation boundaries, async error behavior, resource
limits, proxy assumptions, shutdown behavior, and HTTP integration evidence.
