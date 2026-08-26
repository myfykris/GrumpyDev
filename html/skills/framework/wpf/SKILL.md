---
name: wpf
description: Review WPF plans for application and dispatcher lifecycle, dependency properties, binding, resources, commands, threading, rendering, DPI, accessibility, interoperability, and deployment. Use when a Windows desktop plan changes WPF applications or controls.
---

# WPF plan review

Apply this guidance alongside the core GrumpyDev review and the `csharp`,
`windows`, `application-security`, and `testing-strategy` skills. Select only
companions that match the plan's real boundaries. Verify behavior against the
project's declared targets; do not silently substitute the newest version, a
development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect target frameworks, XAML, dependency properties, bindings, resources,
  styles, templates, commands, dispatchers, windows, native interop, manifests,
  packaging, and deployment configuration.
- Inspect generated and rendered artifacts in addition to source. Templates,
  designers, metadata, conventions, and lifecycle callbacks can own behavior
  that is invisible in the main code path.
- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: .NET and WPF versions, Windows targets,
architecture, packaging, deployment, DPI and localization targets, interop, and
application lifecycle. The changed boundary must define: Application and
dispatcher lifecycle, dependency properties, binding, resources, templates,
commands, threading, async behavior, rendering, DPI, accessibility, interop, and
deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Application and dispatcher lifecycle, dependency properties, binding, resources,
templates, commands, threading. Prove async behavior, rendering, DPI,
accessibility, interop, deployment through startup, invalid or denied work,
cancellation, background execution, mixed versions, shutdown, rollback, and
recovery.

## Challenge the plan

### Recurring traps

Watch especially for silent binding failures, inherited DataContext changing
unexpectedly, dispatcher deadlocks, dependency-property metadata with unintended
scope, dynamic-resource lookup differences, virtualization disabled by
templates, and async-void command failures.

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
- Verify P/Invoke, COM, HWND hosting, architecture, trimming or deployment mode,
  signing, installer, updates, settings migration, rollback, repair, and
  uninstall.

## Verify the claims

- Run binding and resource diagnostics and treat required-path errors as
  failures.
- Exercise windows, navigation, cancellation, shutdown, crash recovery, multiple
  dispatchers if used, and native callbacks.
- Test supported Windows, architectures, DPI, themes, high contrast, text
  scaling, localization, keyboard, and screen readers.
- Install, update, roll back, repair, and uninstall on clean machines with the
  declared runtime and native dependencies.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: .NET and WPF
versions, Windows targets, architecture, packaging, deployment, DPI and
localization targets, interop, and application lifecycle. For the changed
boundary, ask only about unresolved Application and dispatcher lifecycle,
dependency properties, binding, resources, templates, commands, threading, async
behavior, rendering, DPI, accessibility, interop, and deployment when the answer
can change the verdict or implementation.

## Calibrate findings

- Treat persistent state loss, cross-thread corruption, inaccessible core
  interaction, or a packaging/update failure that prevents safe recovery as
  critical or high according to blast radius and realistic likelihood.
- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the plan depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
application and dispatcher lifecycle, dependency properties, binding, resources,
templates, commands, threading, async behavior, rendering, DPI, accessibility,
interoperability, and deployment, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
