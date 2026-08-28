---
name: cpp
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review C++ plans and other engineering artifacts for ownership, lifetime, exception safety, templates, ABI, concurrency, build configuration, and native dependency risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with C++ code, artifacts, or runtime behavior."
---

# C++ GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read build definitions, compiler and language-standard settings, public
  headers, dependency configuration, sanitizer settings, and representative
  tests.

- Trace object ownership, move and copy behavior, exception boundaries, thread
  use, shared state, and C or other-language interfaces.

Watch especially for mixed raw and smart ownership, iterator or reference
invalidation, objects used outside their lifetime, static initialization order,
exceptions crossing incompatible boundaries, unsynchronized shared state, and
one-definition-rule violations across builds.

Lean mode is insufficient when this material severity condition may apply:

- Treat reachable undefined behavior, ownership corruption, ABI mismatch, or
  data race as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete C++ evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the ownership and exception model, ABI and toolchain constraints,
concurrency hazards, compatibility impact, and native evidence required for
approval.
