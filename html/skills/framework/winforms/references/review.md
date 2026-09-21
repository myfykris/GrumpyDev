# Windows Forms full-review guidance

## Operating conditions

Establish the project target: .NET and WinForms versions, Windows targets,
architecture, DPI and localization targets, packaging, deployment, native
interop, and support constraints. The changed boundary must define: Control and
window lifetime, UI thread, message loop, events, data binding, scaling,
resources, async work, interop, accessibility, configuration, and deployment.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise create/show/hide/close/dispose sequences while background work,
  timers, bindings, and native callbacks are active.
- Test supported Windows versions, architectures, DPI configurations, fonts,
  languages, high contrast, keyboard use, and screen readers.
- Stress native boundaries and inspect handle, GDI object, memory, event, and
  control leaks.
