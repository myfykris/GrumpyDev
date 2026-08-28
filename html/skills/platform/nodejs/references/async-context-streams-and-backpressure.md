# Node.js async context, streams, and backpressure

Read this reference when the reviewed work directly or indirectly changes promises,
callbacks, events, timers, async
iterators, AsyncLocalStorage, abort signals, streams, buffers, pipelines, backpressure,
half-close, encoding, slow peers, or unbounded in-memory accumulation.

## Review requirements

- Trace promises, timers, callbacks, events, async iterators, AsyncLocalStorage,
  abort signals, and unhandled rejection or exception policy. Async context and
  cancellation must survive the actual library boundaries.

- Design streams for backpressure, errors, abort, half-close, encoding, buffer
  bounds, pipeline cleanup, and slow peers. Do not concatenate unbounded
  request, file, or child-process output in memory.
