---
name: gd-qt
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Qt engineering work for QObject ownership, signal and slot threading, event loops, model-view contracts, platform behavior, native resources, and deployment risks."
---

# Qt GrumpyDev review

## Quick checks

- Read Qt and compiler versions, object trees, signal and slot connections,
  thread use, models, QML boundaries, resource packaging, target platforms, and
  tests.

- Trace QObject lifetime, event-loop affinity, queued connections, workers,
  native handles, settings, files, and application shutdown.

Watch especially for QObject parentage and deferred deletion mistakes, direct
versus queued signal delivery across threads, event-loop blocking, references
invalidated by implicit sharing or container changes, and platform-plugin
differences hidden by one desktop environment.

- Assess cross-thread UI access, double ownership, or lifecycle failure that
  corrupts persistent data under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Qt specialist.

## Verdict context

State object and thread ownership, event ordering, model-view invariants, QML or
native boundaries, platform targets, and packaged-app evidence.
