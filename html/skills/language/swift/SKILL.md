---
name: swift
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Swift plans and other engineering artifacts for ownership, concurrency, actor isolation, optionals, error handling, platform availability, Objective-C interoperability, and application lifecycle risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Swift code, artifacts, or runtime behavior."
---

# Swift GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read package or project settings, Swift and platform targets, concurrency
  checks, entitlements, generated code, bridging headers, and representative
  tests.

- Trace tasks, actors, continuations, delegates, resources, application
  lifecycle, persistence, and Objective-C or C boundaries.

Watch especially for ARC cycles, copy-on-write values assumed to be cheap or
isolated, actor isolation bypassed at legacy boundaries, tasks that ignore
cancellation, forced optionals on external data, availability checks that miss
linked symbols, and bridging that changes ownership or nullability.

Lean mode is insufficient when this material severity condition may apply:

- Treat actor isolation violation, use-after-lifetime through interop, or
  cancellation that corrupts durable state as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Swift evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State platform targets, concurrency and actor model, unsafe interoperability
boundaries, lifecycle guarantees, and device-level evidence.
