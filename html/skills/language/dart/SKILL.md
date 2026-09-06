---
name: dart
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Dart engineering work for null safety, asynchronous execution, isolates, package compatibility, serialization, platform differences, and release-build risks."
---

# Dart GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read pubspec files, lockfiles, SDK constraints, analyzer settings, generated
  code configuration, platform targets, and representative tests.

- Trace futures, streams, isolates, cancellation or disposal, serialization,
  platform channels, and application lifecycle boundaries.

Watch especially for unawaited futures, errors escaping asynchronous zones,
stream subscriptions that are never cancelled, isolate messages that cannot
serialize or preserve identity, null-safety assumptions at dynamic boundaries,
and generated code drifting from its source declarations.

Lean mode is insufficient when this material severity condition may apply:

- Treat lost asynchronous errors, cross-isolate contract failure, or lifecycle
  work that corrupts durable state as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Dart evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the Dart and platform targets, async ownership, generated-code
assumptions, serialization boundaries, and release-mode evidence.
