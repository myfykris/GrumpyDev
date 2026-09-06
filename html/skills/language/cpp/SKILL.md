---
name: cpp
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review C++ engineering work for ownership, lifetime, exception safety, templates, ABI, concurrency, build configuration, and native dependency risks."
---

# C++ GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
