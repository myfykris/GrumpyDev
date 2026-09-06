---
name: scala
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Scala engineering work for effect ownership, concurrency, type-level assumptions, Java interoperability, serialization, build compatibility, and distributed runtime risks."
---

# Scala GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
