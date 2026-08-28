# Qt standard review

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when thread affinity, ownership, platform behavior, and shutdown are
  covered by native tests.
