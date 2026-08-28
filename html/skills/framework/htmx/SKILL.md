---
name: htmx
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review htmx plans and other engineering artifacts for hypermedia contracts, fragment and full-page responses, swaps, request ordering, history, caching, security, and accessibility. Project applicability: the project uses or materially depends on htmx."
---

# htmx GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `html-css`, `web-accessibility`
and `application-security` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read the htmx version, extensions, configuration, server framework, template system, and
  response conventions.

- Map each request to its trigger, method, parameters, target, swap, synchronization,
  validation, and failure behavior.

Watch especially for the same URL caching both fragments and full pages,
race-prone requests overwriting newer state, sensitive HTML entering history
storage, injected htmx attributes becoming executable behavior, and swaps losing
focus or form errors.

Lean mode is insufficient when this material severity condition may apply:

- Treat stored sensitive fragments, forged state-changing requests, or executable untrusted
  HTML as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete htmx evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State fragment and full-page contracts, request ordering, cache keys, history policy, security
controls, focus behavior, and browser tests.
