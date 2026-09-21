# WPF full-review guidance

## Operating conditions

Establish the project target: .NET and WPF versions, Windows targets,
architecture, packaging, deployment, DPI and localization targets, interop, and
application lifecycle. The changed boundary must define: Application and
dispatcher lifecycle, dependency properties, binding, resources, templates,
commands, threading, async behavior, rendering, DPI, accessibility, interop, and
deployment.

## Failure patterns

- Trace application, dispatcher, window, navigation, resource, view-model, and
  shutdown lifetime. Define behavior for multiple windows, hidden last windows,
  session ending, crash, and restart.
- Analyze dependency-property precedence, metadata, inheritance, coercion,
  validation, default-value sharing, and change callbacks. Prevent recursive
  updates and mutable defaults shared across instances.
- Keep binding source ownership, update triggers, validation, converters,
  collection views, current item, commands, and error reporting explicit.
  Required state cannot depend on silent binding failures.
- Keep DispatcherObject access on its owning thread. Make async cancellation,
  dispatcher priority, collection synchronization, progress, window close, and
  shutdown races explicit; avoid sync-over-async deadlocks.
- Review merged dictionaries, dynamic versus static resources, theme lookup,
  templates, styles, and resource URIs across libraries and packaging. Prevent
  runtime-only missing resources and accidental global overrides.
- Test layout, per-monitor DPI, text scaling, fonts, localization expansion,
  right-to-left layout, high contrast, hardware rendering fallback, large visual
  trees, and virtualization.
- Provide Automation peers, names, roles, states, focus, keyboard navigation,
  error announcements, and patterns for custom controls and templated
  interactions.

## Verification to run or specify in the plan

- Run binding and resource diagnostics and treat required-path errors as
  failures.
- Test supported Windows, architectures, DPI, themes, high contrast, text
  scaling, localization, keyboard, and screen readers.
