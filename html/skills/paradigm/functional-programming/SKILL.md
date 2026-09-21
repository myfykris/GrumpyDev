---
name: gd-functional-programming
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review functional-programming engineering work for effect boundaries, immutable data, error modeling, recursion, laziness, concurrency, and interop."
---

# Functional programming GrumpyDev review

## Quick checks

- Read data types, effect wrappers, pure core boundaries, state transitions,
  error channels, recursion, evaluation strategy, and tests.

- Trace input, validation, effects, failure, cancellation, resource cleanup, and
  conversion at imperative or foreign interfaces.

Watch especially for hidden effects behind pure-looking interfaces, lazy
evaluation retaining unbounded memory, recursion without a safe execution
strategy, persistent structures used outside their performance envelope,
abstractions obscuring failure context, and error accumulation confused with
short-circuiting.

- Assess hidden effects that can duplicate irreversible work or resource behavior
  that exhausts a critical path under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Functional
programming specialist.

## Verdict context

State effect boundaries, state and error models, evaluation and memory risks,
interop escape hatches, and test evidence.
