---
name: htmx
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review htmx engineering work for hypermedia contracts, fragment and full-page responses, swaps, request ordering, history, caching, security, and accessibility."
---

# htmx GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `html-css`, `web-accessibility`
and `application-security` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
