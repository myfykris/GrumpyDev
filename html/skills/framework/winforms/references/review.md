# Windows Forms standard review

## Inspect additional evidence

- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: .NET and WinForms versions, Windows targets,
architecture, DPI and localization targets, packaging, deployment, native
interop, and support constraints. The changed boundary must define: Control and
window lifetime, UI thread, message loop, events, data binding, scaling,
resources, async work, interop, accessibility, configuration, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Control and window lifetime, UI thread, message loop, events, data binding,
scaling. Prove resources, async work, interop, accessibility, configuration,
deployment through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

- Keep controls on their creating UI thread and make marshaling explicit. Async
  continuations, timers, events, background workers, and shutdown can race a
  disposed handle even when ordinary updates look serialized.
- Trace form, control, component, handle, event, timer, image, font, graphics,
  stream, and unmanaged-resource disposal. Designer ownership and application
  ownership are not interchangeable.
- Review event subscriptions, binding sources, validation, currency managers,
  error providers, and update modes for cycles, stale values, recursive updates,
  and commits that occur later than the visible edit.
- Declare per-monitor DPI awareness and test scaling after monitor changes, font
  changes, localization expansion, right-to-left layout, custom drawing, and
  mixed-DPI native controls. Pixel-perfect coordinates are not a layout
  strategy.
- Make cancellation and close behavior explicit for async work. Do not block the
  UI synchronization context waiting for a continuation that needs that same
  context.
- Validate accessibility names, roles, states, labels, tab order, keyboard
  access, focus visibility, high contrast, text scaling, and custom-control UI
  Automation behavior.
## Verify the claims

- Exercise create/show/hide/close/dispose sequences while background work,
  timers, bindings, and native callbacks are active.
- Test supported Windows versions, architectures, DPI configurations, fonts,
  languages, high contrast, keyboard use, and screen readers.
- Stress native boundaries and inspect handle, GDI object, memory, event, and
  control leaks.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: .NET and WinForms
versions, Windows targets, architecture, DPI and localization targets,
packaging, deployment, native interop, and support constraints. For the changed
boundary, ask only about unresolved Control and window lifetime, UI thread,
message loop, events, data binding, scaling, resources, async work, interop,
accessibility, configuration, and deployment when the answer can change the
verdict or implementation.

## Calibrate findings

- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the reviewed work depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
