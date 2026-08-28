---
name: scala
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Scala plans and other engineering artifacts for effect ownership, concurrency, type-level assumptions, Java interoperability, serialization, build compatibility, and distributed runtime risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Scala code, artifacts, or runtime behavior."
---

# Scala GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read sbt or build configuration, Scala and JVM versions, effect or actor
  libraries, serialization settings, generated code, and representative tests.

- Trace effects, execution contexts, futures or fibers, blocking work, Java
  boundaries, implicits or givens, state, and shutdown.

Watch especially for surprising implicit or given resolution, lazy
initialization under concurrency, futures using an unsuitable execution context,
strict and lazy collection behavior being confused, erased runtime types,
variance hiding unsafe assumptions, and binary incompatibility across library
versions.

Lean mode is insufficient when this material severity condition may apply:

- Treat binary incompatibility, lost effect cancellation, dispatcher starvation,
  or unsafe shared state as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Scala evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State Scala and JVM targets, effect and execution model, binary compatibility,
serialization assumptions, and distributed failure evidence.
