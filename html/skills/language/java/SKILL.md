---
name: java
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Java engineering work for JVM compatibility, concurrency, resource management, serialization, dependency resolution, reflection, memory, and deployment risks."
---

# Java GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read Maven or Gradle configuration, toolchains, dependency locks, module
  settings, JVM flags, serialization mappings, and representative tests.

- Trace thread pools, futures, transactions, resources, class loading,
  reflection, shutdown hooks, and data crossing service boundaries.

Watch especially for nullability assumptions at framework boundaries,
inconsistent identity and equality semantics, mutable shared state, resources
that escape structured cleanup, thread-local state under pooled or virtual
threads, class-loader leaks, XML external entities, dynamic expression or class
loading, and unsafe deserialization.

Lean mode is insufficient when this material severity condition may apply:

- Treat a reachable data race, thread starvation, lost interruption, or
  incompatible persisted serialization as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Java evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State JVM and bytecode targets, executor and resource ownership, serialization
compatibility, memory assumptions, and deployed-runtime evidence.
