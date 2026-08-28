---
name: flutter
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Flutter plans and other engineering artifacts for widget and application state, lifecycle, navigation, asynchronous work, platform plugins, accessibility, performance, and release risks. Project applicability: the project uses or materially depends on Flutter."
---

# Flutter GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `dart` skill.

## Lean review

- Read Flutter and Dart versions, supported platforms, navigation, state and
  data libraries, plugin configuration, persistence, permissions, and tests.

- Trace widget and app lifecycle, state ownership, futures and streams,
  background work, platform channels, navigation, and offline or error states.

Watch especially for side effects during build, use of a stale BuildContext
after asynchronous work, undisposed controllers and subscriptions, two state
owners for the same value, and mobile-only testing that misses desktop, web,
accessibility, or restoration behavior.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-user state leakage, lost critical offline data, or a core flow
  inaccessible on a supported platform as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Flutter evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State platform targets, state and lifecycle ownership, plugin boundaries,
user-visible failure states, accessibility, and release evidence.
