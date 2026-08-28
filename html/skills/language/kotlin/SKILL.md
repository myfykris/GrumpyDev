---
name: kotlin
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Kotlin plans and other engineering artifacts for nullability, coroutine ownership, Java interoperability, serialization, multiplatform differences, dependency compatibility, and lifecycle risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Kotlin code, artifacts, or runtime behavior."
---

# Kotlin GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
