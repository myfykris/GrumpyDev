---
name: gd-concurrent-systems
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review concurrent-system engineering work for shared-state races, ordering, cancellation, backpressure, starvation, deadlocks, and deterministic testing."
---

# Concurrent systems GrumpyDev review

## Quick checks

- Read ownership boundaries, synchronization primitives, queues, pools,
  cancellation paths, timeouts, and concurrency tests.

- Trace shared mutable state and every operation that can block, retry, reorder,
  duplicate, or outlive its caller.

Watch especially for inconsistent lock ordering, lost wakeups, check-then-act
races, operations described as atomic but implemented in stages, cancellation
that strands ownership, starvation hidden by throughput averages, and tests that
cannot force the dangerous interleaving.

- Assess a reachable data race, deadlock, livelock, or duplicate irreversible
  effect under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Concurrent systems
specialist.

## Verdict context

State state ownership, ordering guarantees, blocking and backpressure limits,
cancellation behavior, and concurrency evidence.
