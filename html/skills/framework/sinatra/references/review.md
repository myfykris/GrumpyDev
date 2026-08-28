# Sinatra standard review

## Inspect additional evidence

- Trace request data, global or class state, authentication, errors, streaming,
  background work, thread safety, and shutdown.

## Establish the operating model

Establish the project target: Sinatra and Ruby versions, Rack and server
versions, thread and worker model, middleware, sessions, proxy setup, and
deployment platform. The changed boundary must define: Request lifecycle,
settings and environments, middleware, thread safety, sessions, errors,
streaming, reloading, server behavior, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Request lifecycle, settings and environments, middleware, thread safety,
sessions. Prove errors, streaming, reloading, server behavior, deployment
through startup, invalid or denied work, cancellation, background execution,
mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the actual Sinatra lifecycle and production
  pipeline: Request lifecycle, settings and environments, middleware, thread
  safety, sessions. Use the actual framework pipeline and production build with
  representative services and configuration.
- Exercise failure and edge behavior for: errors, streaming, reloading, server
  behavior, deployment. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Ruby, Sinatra, Rack, server, concurrency, and deployment versions or
  modes apply?
- How do middleware, shared state, sessions, authentication, errors, blocking
  work, and shutdown behave?

## Calibrate findings

- Downgrade when the process model is single-threaded by contract or state,
  middleware, and concurrency are tested.
