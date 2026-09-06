---
name: flutter
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Flutter engineering work for widget and application state, lifecycle, navigation, asynchronous work, platform plugins, accessibility, performance, and release risks."
---

# Flutter GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
