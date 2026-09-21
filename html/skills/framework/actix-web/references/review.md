# Actix Web full-review guidance

## Operating conditions

Establish the project target: Actix and Rust versions, Tokio runtime, worker
counts, proxy and TLS termination, payload limits, state ownership, and
deployment model. The changed boundary must define: Extractor limits,
application and worker state, async blocking, middleware ordering, error
mapping, streaming, shutdown, TLS and proxy behavior.

## Failure patterns

- Verify whether application data is shared or constructed per worker and
  whether its synchronization model is sound.
- Move CPU or blocking I/O off async workers and require bounds for pools, body
  sizes, concurrency, and timeouts.
- Check extractor limits, middleware order, authentication coverage, error
  mapping, and sensitive response details.
- Require ownership and cancellation for spawned tasks, streams, websockets, and
  long-running handlers.
- Test graceful drain, worker restart, client disconnect, dependency timeout,
  and production TLS or proxy behavior.

## Verification to run or specify in the plan

- Send concurrent requests across multiple workers and verify the intended
  sharing of application data. Exercise oversized bodies, extractor failures,
  and denied requests through the real middleware chain.
- Disconnect streaming clients and stop workers with requests in flight. Check
  task ownership, bounded blocking work, and drain behavior behind the
  deployment proxy.
