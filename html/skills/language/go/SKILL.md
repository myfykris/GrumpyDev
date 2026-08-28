---
name: go
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Go plans and other engineering artifacts for goroutine ownership, context propagation, interfaces, error handling, memory behavior, modules, concurrency, and service lifecycle risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Go code, artifacts, or runtime behavior."
---

# Go GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
