---
name: angular
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Angular plans and other engineering artifacts for dependency injection scope, signals and RxJS ownership, change detection, routing, forms, rendering, accessibility, and build risks. Project applicability: the project uses or materially depends on Angular."
---

# Angular GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `typescript` and
`javascript` skills.

## Lean review

- Read Angular and TypeScript versions, bootstrap and provider configuration,
  routes, state and data libraries, rendering mode, forms, build targets, and
  tests.

- Trace service lifetimes, signals, observables, subscriptions, navigation,
  server and browser boundaries, and loading or error states.

Watch especially for mutable singleton-service state, duplicated providers with
surprising scope, leaked subscriptions, change-detection assumptions that fail
outside the expected zone or signal boundary, and route guards mistaken for
server-side authorization.

Lean mode is insufficient when this material severity condition may apply:

- Treat client-side authorization as the only control, leaked long-lived
  subscriptions, or broken core hydration as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Angular evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State provider and state ownership, reactive cleanup, routing and rendering
assumptions, user-visible failure states, and production-build evidence.
