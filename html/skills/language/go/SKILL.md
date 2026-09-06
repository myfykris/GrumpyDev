---
name: go
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Go engineering work for goroutine ownership, context propagation, interfaces, error handling, memory behavior, modules, concurrency, and service lifecycle risks."
---

# Go GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat a reachable data race, goroutine leak, deadlock, or lost cancellation on
  a critical path as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Go evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State goroutine and channel ownership, cancellation behavior, concurrency
hazards, module and build assumptions, and race or leak evidence.
