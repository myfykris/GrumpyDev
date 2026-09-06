---
name: concurrent-systems
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review concurrent-system engineering work for shared-state races, ordering, cancellation, backpressure, starvation, deadlocks, and deterministic testing."
---

# Concurrent systems GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed language or framework specialist for the concurrency model in use.

## Lean review

- Read ownership boundaries, synchronization primitives, queues, pools,
  cancellation paths, timeouts, and concurrency tests.

- Trace shared mutable state and every operation that can block, retry, reorder,
  duplicate, or outlive its caller.

Watch especially for inconsistent lock ordering, lost wakeups, check-then-act
races, operations described as atomic but implemented in stages, cancellation
that strands ownership, starvation hidden by throughput averages, and tests that
cannot force the dangerous interleaving.

Lean mode is insufficient when this material severity condition may apply:

- Treat a reachable data race, deadlock, livelock, or duplicate irreversible
  effect as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Concurrent systems evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State state ownership, ordering guarantees, blocking and backpressure limits,
cancellation behavior, and concurrency evidence.
