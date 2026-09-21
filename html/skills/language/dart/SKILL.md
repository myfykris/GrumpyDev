---
name: gd-dart
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Dart engineering work for null safety, asynchronous execution, isolates, package compatibility, serialization, platform differences, and release-build risks."
---

# Dart GrumpyDev review

## Quick checks

- Read pubspec files, lockfiles, SDK constraints, analyzer settings, generated
  code configuration, platform targets, and representative tests.

- Trace futures, streams, isolates, cancellation or disposal, serialization,
  platform channels, and application lifecycle boundaries.

Watch especially for unawaited futures, errors escaping asynchronous zones,
stream subscriptions that are never cancelled, isolate messages that cannot
serialize or preserve identity, null-safety assumptions at dynamic boundaries,
and generated code drifting from its source declarations.

- Assess lost asynchronous errors, cross-isolate contract failure, or lifecycle
  work that corrupts durable state under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Dart specialist.

## Verdict context

State the Dart and platform targets, async ownership, generated-code
assumptions, serialization boundaries, and release-mode evidence.
