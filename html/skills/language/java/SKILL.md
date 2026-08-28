---
name: java
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Java plans and other engineering artifacts for JVM compatibility, concurrency, resource management, serialization, dependency resolution, reflection, memory, and deployment risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Java, JVM bytecode, or JVM runtime behavior."
---

# Java GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
