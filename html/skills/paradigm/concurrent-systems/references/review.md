# Concurrent systems full-review guidance

## Operating conditions

Establish the project target: Concurrency model, thread or process limits,
synchronization primitives, scheduler assumptions, latency targets,
race-detection tools, and failure policy. The changed boundary must define:
Memory ordering, races, deadlocks, starvation, cancellation, ownership,
synchronization, work queues, backpressure, scheduling, and deterministic
evidence.

## Failure patterns

- Require an explicit happens-before story for shared state; thread safety by
  reputation is not evidence.
- Check lock ordering, nested waits, bounded queues, pool exhaustion,
  starvation, and priority inversion under peak load.
- Define cancellation and shutdown propagation so abandoned work cannot leak
  resources or commit after the caller gives up.
- Treat retries and parallel consumers as sources of duplication and reordering;
  require idempotency where effects can repeat.
- Demand stress, race, timeout, and deterministic scheduling tests around the
  actual coordination boundaries.

## Verification to run or specify in the plan

- Force competing operations to pause around lock acquisition, shared-state
  reads, and commits. Use race detection or controlled scheduling where
  available to test the claimed ordering and invariant.
- Saturate worker pools and queues, then cancel callers and begin shutdown.
  Check bounded waiting, deadlock recovery, released resources, and whether
  abandoned work can still commit.
