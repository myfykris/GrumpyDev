# Concurrent systems survey contribution

## Applies when

Apply this contribution when work runs in parallel across threads, processes, tasks,
actors, or workers.

## Inspect

- Read ownership boundaries, synchronization primitives, queues, pools,
  cancellation paths, timeouts, and concurrency tests.

## Ask when unresolved

- Which task owns each mutable resource, and which synchronization or message
  boundary orders access?

- What progress, cancellation, fairness, timeout, and failure behavior applies
  under contention?

- Which runtime or deployment differences materially change future reviews:
  Process, thread, actor, coroutine, or device model; scheduler; core count;
  shared memory; clock; cancellation; resource limits; and failure isolation?

## Record

Map accepted Concurrent systems choices to `Accepted decisions`,
binding boundaries to `Requirements` or `Constraints`, and material gaps to
`Unknowns`.
