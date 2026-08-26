---
name: qt
description: Review Qt plans for QObject ownership, signal and slot threading, event loops, model-view contracts, platform behavior, native resources, and deployment risks. Use when a C++ plan changes Qt desktop, embedded, or cross-platform applications.
---

# Qt plan review

Apply this guidance alongside the core GrumpyDev review and the `cpp` skill.

## Inspect evidence

- Read Qt and compiler versions, object trees, signal and slot connections,
  thread use, models, QML boundaries, resource packaging, target platforms, and
  tests.
- Trace QObject lifetime, event-loop affinity, queued connections, workers,
  native handles, settings, files, and application shutdown.

## Establish the operating model

Establish the project target: Qt and compiler versions, widgets or QML, target
OS and architectures, static or dynamic linking, plugin and graphics stack,
packaging, and accessibility targets. The changed boundary must define: QObject
ownership, parent-child lifetime, signals and slots, thread affinity, event
loops, QML and C++ boundaries, models, resources, plugins, and packaging.

Assign lifecycle, state, dependency, persistence, and security ownership for
QObject ownership, parent-child lifetime, signals and slots, thread affinity,
event loops. Prove QML and C++ boundaries, models, resources, plugins, packaging
through startup, invalid or denied work, cancellation, background execution,
mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for QObject parentage and deferred deletion mistakes, direct
versus queued signal delivery across threads, event-loop blocking, references
invalidated by implicit sharing or container changes, and platform-plugin
differences hidden by one desktop environment.

- Require explicit QObject ownership and prevent dangling callbacks, double
  deletion, or deleteLater calls without a live event loop.
- Check thread affinity and connection type; direct and queued signals have
  different ordering and safety guarantees.
- Validate model notifications, indexes, proxy models, and view updates against
  Qt model-view invariants.
- Treat QML and C++ boundaries, variants, JavaScript, URLs, resources, and user
  input as runtime validation boundaries.
- Test packaging, plugins, translations, high DPI, permissions, native dialogs,
  and shutdown on every supported platform.

## Verify the claims

- Verify these behaviors through the actual Qt lifecycle and production
  pipeline: QObject ownership, parent-child lifetime, signals and slots, thread
  affinity, event loops. Use the actual framework pipeline and production build
  with representative services and configuration.
- Exercise failure and edge behavior for: QML and C++ boundaries, models,
  resources, plugins, packaging. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Qt, C++ compiler, platform, rendering backend, and ownership model
  apply?
- How do parent ownership, signals, threads, event loops, shutdown,
  accessibility, and native resources interact?

## Calibrate findings

- Treat cross-thread UI access, double ownership, or lifecycle failure that
  corrupts persistent data as critical.
- Downgrade when thread affinity, ownership, platform behavior, and shutdown are
  covered by native tests.

## Add to the verdict

State object and thread ownership, event ordering, model-view invariants, QML or
native boundaries, platform targets, and packaged-app evidence.
