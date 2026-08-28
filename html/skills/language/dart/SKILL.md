---
name: dart
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Dart plans and other engineering artifacts for null safety, asynchronous execution, isolates, package compatibility, serialization, platform differences, and release-build risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with Dart code, artifacts, or runtime behavior."
---

# Dart GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
