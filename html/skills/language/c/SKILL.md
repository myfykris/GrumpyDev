---
name: c
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review C plans and other engineering artifacts for memory safety, ownership, ABI, undefined behavior, concurrency, portability, build, and native dependency risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with C code, artifacts, or runtime behavior."
---

# C GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read build files, compiler flags, target platforms, public headers, allocation
  conventions, sanitizer settings, and representative tests.

- Trace ownership, lifetime, bounds, error returns, cleanup paths, thread
  interaction, and data crossing ABI or hardware boundaries.

Watch especially for undefined behavior from lifetime, bounds, alignment,
aliasing, or signed arithmetic; silent integer conversions; ownership that
changes across error paths; struct layout assumed across ABI boundaries; and
signal handlers calling unsafe operations.

Lean mode is insufficient when this material severity condition may apply:

- Treat reachable undefined behavior, memory corruption, integer-controlled
  allocation, or unsafe concurrency as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete C evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the ownership model, ABI assumptions, supported toolchains and targets,
undefined-behavior risks, cleanup behavior, and evidence from native tests or
analysis.
