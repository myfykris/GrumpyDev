---
name: vue
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Vue plans and other engineering artifacts for reactive state ownership, composable lifecycle, routing, rendering, asynchronous work, accessibility, and build risks. Project applicability: the project uses or materially depends on Vue."
---

# Vue GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `javascript` or
`typescript` skill.

## Lean review

- Read Vue and build-tool versions, component API style, router, store and data
  libraries, rendering mode, plugins, configuration, and tests.

- Trace props, emits, reactive state, watchers, composables, subscriptions,
  navigation, data requests, and component disposal.

Watch especially for reactivity lost through destructuring, watchers or effects
that outlive their owner, computed values with side effects, unstable keys,
server-rendered state leaking between requests, hydration mismatches, and store
state duplicated outside its authority.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-user SSR state leakage, client-only authorization, or an
  inaccessible core flow as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Vue evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State reactive state ownership, lifecycle cleanup, routing and rendering
assumptions, user-visible failure states, and production-build evidence.
