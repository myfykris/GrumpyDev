---
name: kotlin
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Kotlin engineering work for nullability, coroutine ownership, Java interoperability, serialization, multiplatform differences, dependency compatibility, and lifecycle risks."
---

# Kotlin GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read Gradle configuration, Kotlin and JVM targets, compiler options, coroutine
  usage, serialization settings, platform source sets, and representative tests.

- Trace coroutine scopes, dispatchers, cancellation, flows, Java calls, nullable
  platform types, resources, and application lifecycle.

Watch especially for nullable Java platform types, coroutine scopes detached
from their owner, cancellation swallowed as an ordinary exception, blocking
calls on constrained dispatchers, data-class equality used for mutable identity,
and JVM interop changing default or overload behavior.

Lean mode is insufficient when this material severity condition may apply:

- Treat lost cancellation, blocking on a constrained dispatcher, unsafe platform
  types, or incompatible serialization as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Kotlin evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State platform targets, coroutine ownership, Java boundary risks, serialization
contract, lifecycle behavior, and platform-specific evidence.
