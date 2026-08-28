---
name: qt
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Qt plans and other engineering artifacts for QObject ownership, signal and slot threading, event loops, model-view contracts, platform behavior, native resources, and deployment risks. Project applicability: the project uses or materially depends on Qt."
---

# Qt GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `cpp` skill.

## Lean review

- Read Qt and compiler versions, object trees, signal and slot connections,
  thread use, models, QML boundaries, resource packaging, target platforms, and
  tests.

- Trace QObject lifetime, event-loop affinity, queued connections, workers,
  native handles, settings, files, and application shutdown.

Watch especially for QObject parentage and deferred deletion mistakes, direct
versus queued signal delivery across threads, event-loop blocking, references
invalidated by implicit sharing or container changes, and platform-plugin
differences hidden by one desktop environment.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-thread UI access, double ownership, or lifecycle failure that
  corrupts persistent data as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Qt evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State object and thread ownership, event ordering, model-view invariants, QML or
native boundaries, platform targets, and packaged-app evidence.
