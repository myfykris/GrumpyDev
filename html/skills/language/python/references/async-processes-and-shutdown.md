# Python async, processes, and shutdown

Read this reference when the reviewed work directly or indirectly changes an event loop,
async framework, threads,
processes, executors, workers, GIL assumptions, task ownership, cancellation, signals,
fork behavior, cleanup, retries, or graceful shutdown.

## Review requirements

- Require a defined ownership and shutdown path for sessions, files, processes,
  executors, tasks, and async clients.

- Test whether blocking work enters the event loop and whether async work is
  incorrectly treated as parallel CPU execution.

- Find retry loops without deadlines, idempotency, bounded backoff, or exception
  classification.

- Check mutable defaults, import-time side effects, global client state, and
  fork/thread safety where the execution model makes them material.

- Require tests for error paths, cancellation, cleanup, serialization edges,
  time behavior, and dependency failures - not only happy-path unit tests.
