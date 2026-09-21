# Axum full-review guidance

## Operating conditions

Establish the project target: Axum, Tokio and tower versions, runtime topology,
state ownership, proxy and TLS arrangement, request limits, and deployment
target. The changed boundary must define: Router and extractor behavior, state
and tower layers, async blocking, errors, body limits, streaming, cancellation,
graceful shutdown, and proxy trust.

## Failure patterns

- Identify state ownership and the actual synchronization primitive. Blocking
  locks across await points can deadlock or block runtime threads; async mutexes
  can legitimately span awaits. Check lock duration, unnecessary serialization,
  cancellation, and ownership rather than rejecting every such lock.
- Check Tower layer order, timeout coverage, concurrency limits, backpressure,
  tracing, and authentication placement.
- Bound bodies, decompression, extractors, streams, and fan-out before untrusted
  input reaches expensive work.
- Require typed but non-sensitive error mapping and ownership for disconnected
  clients, spawned tasks, and websockets.
- Test production serving, proxy headers, graceful drain, dependency failure,
  and runtime saturation.

## Verification to run or specify in the plan

- Exercise extractor rejection, authentication, body limits, and timeouts
  through the actual router and Tower layer order. Saturate shared state to
  check lock contention and backpressure.
- Disconnect streams and stop the server during pending work. Verify
  cancellation, task cleanup, and graceful drain without blocking runtime
  threads.
