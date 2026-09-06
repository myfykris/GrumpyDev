---
name: vue
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Vue engineering work for reactive state ownership, composable lifecycle, routing, rendering, asynchronous work, accessibility, and build risks."
---

# Vue GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
