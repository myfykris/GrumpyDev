# Sinatra full-review guidance

## Operating conditions

Establish the project target: Sinatra and Ruby versions, Rack and server
versions, thread and worker model, middleware, sessions, proxy setup, and
deployment platform. The changed boundary must define: Request lifecycle,
settings and environments, middleware, thread safety, sessions, errors,
streaming, reloading, server behavior, and deployment.

## Failure patterns

- Verify route and middleware order, method matching, error-handler coverage,
  and behavior under mounted or modular applications.
- Reject mutable global or class state unless it is safe under the actual
  threaded or multi-process server.
- Require validation and object-level authorization for params, body, sessions,
  headers, and uploaded files.
- Bound request bodies, streams, downstream calls, database pools, timeouts, and
  any work detached from the request.
- Test under the production Rack server and proxy for concurrency, path base,
  sessions, client disconnect, and graceful shutdown.

## Verification to run or specify in the plan

- Exercise mounted routes, method matching, session handling, and error
  handlers under the production Rack server. Send concurrent identities to
  detect mutable class or global state leaking between requests.
- Disconnect clients during streaming and fail downstream calls. Check
  connection release, bounded work, and shutdown behavior with the configured
  proxy paths and timeouts.
