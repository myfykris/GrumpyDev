# Qt full-review guidance

## Operating conditions

Establish the project target: Qt and compiler versions, widgets or QML, target
OS and architectures, static or dynamic linking, plugin and graphics stack,
packaging, and accessibility targets. The changed boundary must define: QObject
ownership, parent-child lifetime, signals and slots, thread affinity, event
loops, QML and C++ boundaries, models, resources, plugins, and packaging.

## Failure patterns

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

## Verification to run or specify in the plan

- Destroy objects with queued signals and callbacks pending, and close windows
  while worker threads run. Check QObject ownership, thread affinity, and
  deferred deletion with the actual event loops.
- Exercise model inserts, removals, and resets through affected views. Launch
  the packaged application on supported platforms to verify QML resources,
  plugins, translations, high DPI, and shutdown.
