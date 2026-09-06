---
name: c
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review C engineering work for memory safety, ownership, ABI, undefined behavior, concurrency, portability, build, and native dependency risks."
---

# C GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
