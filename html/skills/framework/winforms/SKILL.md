---
name: winforms
description: Review Windows Forms plans for control lifetime, UI-thread behavior, events, data binding, scaling, resources, asynchronous work, native interoperability, accessibility, configuration, and deployment. Use when a Windows desktop plan changes WinForms applications or controls.
---

# Windows Forms plan review

Apply this guidance alongside the core GrumpyDev review and the `csharp`,
`windows`, `application-security`, and `testing-strategy` skills. Select only
companions that match the plan's real boundaries. Verify behavior against the
project's declared targets; do not silently substitute the newest version, a
development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect target frameworks, forms and controls, designer files, event wiring,
  data bindings, synchronization contexts, resources, manifests, DPI settings,
  native interop, installers, and update configuration.
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

## Challenge the plan

### Recurring traps

Watch especially for synchronous Invoke deadlocks, event subscriptions retaining
controls, async-void failures, DPI and layout assumptions baked into designer
output, resources drifting across localization, and deployment bitness that
breaks native interop.

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
- Check P/Invoke, COM, ActiveX, window handles, architecture, calling
  convention, string encoding, ownership, registration, and installer scope
  across x86, x64, and Arm64 targets.
- Keep user, machine, roaming, and application configuration separate, version
  migrations restartable, secrets out of ordinary settings, and updates
  compatible with in-use files and rollback.

## Verify the claims

- Exercise create/show/hide/close/dispose sequences while background work,
  timers, bindings, and native callbacks are active.
- Test supported Windows versions, architectures, DPI configurations, fonts,
  languages, high contrast, keyboard use, and screen readers.
- Run clean-machine installation, update, rollback, repair, uninstall, and
  per-user or per-machine scenarios.
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

- Treat cross-thread corruption, inaccessible primary UI, destructive
  configuration migration, or deployment behavior that prevents safe startup or
  recovery as critical or high according to blast radius and realistic
  likelihood.
- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the plan depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
control and window lifetime, UI thread, message loop, events, data binding,
scaling, resources, async work, interoperability, accessibility, configuration,
and deployment, verification evidence, deployment and recovery limits, and any
material assumption that remains unresolved.
