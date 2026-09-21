---
name: gd-go
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Go engineering work for goroutine ownership, context propagation, interfaces, error handling, memory behavior, modules, concurrency, and service lifecycle risks."
---

# Go GrumpyDev review

## Quick checks

- Read go.mod, go.sum, build tags, generated code, entry points, interface
  boundaries, race-test configuration, and representative tests.

- Trace goroutine creation, channel ownership, contexts, timers, network
  clients, shutdown, retry behavior, and shared mutable state.

Watch especially for goroutines without stop conditions, contexts not propagated
to blocking work, channels closed by the wrong owner, typed nil values hidden in
interfaces, loop-capture assumptions that ignore the declared Go version, and
races masked by happy-path tests. Also watch for `text/template` used for HTML,
unbounded response reads, archive traversal, and command options controlled by
untrusted input.

- Assess a reachable data race, goroutine leak, deadlock, or lost cancellation on
  a critical path under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Go specialist.

## Verdict context

State goroutine and channel ownership, cancellation behavior, concurrency
hazards, module and build assumptions, and race or leak evidence.
