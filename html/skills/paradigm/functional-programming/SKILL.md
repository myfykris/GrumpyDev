---
name: functional-programming
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review functional-programming engineering work for effect boundaries, immutable data, error modeling, recursion, laziness, concurrency, and interop."
---

# Functional programming GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed language specialist for the effect model in use.

## Lean review

- Read data types, effect wrappers, pure core boundaries, state transitions,
  error channels, recursion, evaluation strategy, and tests.

- Trace input, validation, effects, failure, cancellation, resource cleanup, and
  conversion at imperative or foreign interfaces.

Watch especially for hidden effects behind pure-looking interfaces, lazy
evaluation retaining unbounded memory, recursion without a safe execution
strategy, persistent structures used outside their performance envelope,
abstractions obscuring failure context, and error accumulation confused with
short-circuiting.

Lean mode is insufficient when this material severity condition may apply:

- Treat hidden effects that can duplicate irreversible work or resource behavior
  that exhausts a critical path as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Functional programming evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State effect boundaries, state and error models, evaluation and memory risks,
interop escape hatches, and test evidence.
