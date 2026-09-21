---
name: gd-elixir
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Elixir engineering work for supervision, process ownership, message ordering, backpressure, fault recovery, distribution, state, and release risks."
---

# Elixir GrumpyDev review

## Quick checks

- Establish the exact Elixir, Erlang/OTP, release-target, and dependency
  versions.

- Read mix files, supervision trees, process registries, GenServer state, queue
  or stream configuration, clustering, release configuration, and tests.

Watch especially for unbounded mailboxes, GenServer callbacks doing slow work,
incorrect links or monitors, supervision restart loops that amplify failure,
dynamically created atoms from external input, ETS tables whose owner dies, and
retries that repeat side effects.

- Assess unsupervised critical work, mailbox exhaustion, or incompatible rolling
  release behavior under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Elixir specialist.

## Verdict context

State the supervision and state model, overload controls, delivery guarantees,
cluster assumptions, release sequence, and recovery evidence.
