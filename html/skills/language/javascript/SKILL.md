---
name: javascript
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review JavaScript engineering work for runtime coercion, asynchronous control flow, module compatibility, dependency behavior, browser or Node differences, validation, and build risks."
---

# JavaScript GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read package metadata, lockfiles, runtime and browser targets, module type,
  bundler settings, lint rules, generated artifacts, and representative tests.

- Trace external data, promises, events, timers, shared state, cleanup, module
  loading, and browser or Node API usage.

Watch especially for coercion and truthiness changing control flow, promises
that are neither awaited nor returned, shared mutation across callbacks, CPU
work blocking the event loop, prototype or property-name hazards, floating-point
assumptions, catastrophic regular expressions, dynamic code evaluation, and
local-time conversions.

Lean mode is insufficient when this material severity condition may apply:

- Treat unhandled async failure, prototype or input abuse, event-loop
  starvation, or cross-user state leakage as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete JavaScript evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State runtime targets, validation boundaries, async ownership, module format,
compatibility assumptions, and built-artifact evidence.
