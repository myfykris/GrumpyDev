---
name: swift
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Swift engineering work for ownership, concurrency, actor isolation, optionals, error handling, platform availability, Objective-C interoperability, and application lifecycle risks."
---

# Swift GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
