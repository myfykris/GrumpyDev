---
name: concurrent-systems
description: Review concurrent-system plans for shared-state races, ordering, cancellation, backpressure, starvation, deadlocks, and deterministic testing. Use when work runs in parallel across threads, processes, tasks, actors, or workers.
---

# Concurrent systems plan review

Apply this guidance alongside the core GrumpyDev review and the applicable
installed language or framework specialist for the concurrency model in use.

## Inspect evidence

- Read ownership boundaries, synchronization primitives, queues, pools,
  cancellation paths, timeouts, and concurrency tests.
- Trace shared mutable state and every operation that can block, retry, reorder,
  duplicate, or outlive its caller.

## Establish the operating model

Establish the project target: Concurrency model, thread or process limits,
synchronization primitives, scheduler assumptions, latency targets,
race-detection tools, and failure policy. The changed boundary must define:
Memory ordering, races, deadlocks, starvation, cancellation, ownership,
synchronization, work queues, backpressure, scheduling, and deterministic
evidence.

Name the invariants, authorities, owners, and enforcement for Memory ordering,
races, deadlocks, starvation, cancellation, ownership. Prove synchronization,
work queues, backpressure, scheduling, deterministic evidence under concurrency,
partial failure, incompatible versions, operational response, rollback, and
repair, and justify the added complexity.

## Challenge the plan

### Recurring traps

Watch especially for inconsistent lock ordering, lost wakeups, check-then-act
races, operations described as atomic but implemented in stages, cancellation
that strands ownership, starvation hidden by throughput averages, and tests that
cannot force the dangerous interleaving.

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

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Memory ordering, races, deadlocks, starvation, cancellation,
  ownership. Use dependency, architecture, contract, schema, or ownership tests
  that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: synchronization, work queues,
  backpressure, scheduling, deterministic evidence. Exercise the material
  invariant under concurrency, delay, duplication, partial failure, incompatible
  versions, rollback, and repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- Which task owns each mutable resource, and which synchronization or message
  boundary orders access?
- What progress, cancellation, fairness, timeout, and failure behavior applies
  under contention?

## Calibrate findings

- Treat a reachable data race, deadlock, livelock, or duplicate irreversible
  effect as critical.
- Downgrade when state is isolated or ownership, synchronization, and stress
  evidence prove safety and progress.

## Add to the verdict

State state ownership, ordering guarantees, blocking and backpressure limits,
cancellation behavior, and concurrency evidence.
