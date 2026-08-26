---
name: winui-3
description: Review WinUI 3 plans for Windows App SDK lifecycle, XAML behavior, binding, dispatcher and asynchronous work, activation, navigation, resources, accessibility, packaging, identity, and deployment. Use when a Windows desktop plan changes WinUI 3 applications.
---

# WinUI 3 plan review

Apply this guidance alongside the core GrumpyDev review and the `csharp` or
`cpp`, `windows`, `application-security`, and `testing-strategy` skills. Select
only companions that match the plan's real boundaries. Verify behavior against
the project's declared targets; do not silently substitute the newest version, a
development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect Windows App SDK and target settings, XAML, view models, bindings,
  activation registration, windows, dispatch queues, resources, manifests,
  identity, packaging, bootstrapper, and deployment output.
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

Establish the project target: Windows App SDK and WinUI versions, C# or C++,
Windows minimums, packaged or unpackaged deployment, architectures, app
lifecycle, identity, and distribution. The changed boundary must define: Windows
App SDK lifecycle, XAML, dependency properties, binding, dispatcher and async
behavior, windows, activation, navigation, resources, accessibility, packaging,
and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Windows App SDK lifecycle, XAML, dependency properties, binding, dispatcher and
async behavior, windows. Prove activation, navigation, resources, accessibility,
packaging, deployment through startup, invalid or denied work, cancellation,
background execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for packaged and unpackaged identity differences, activation
paths that assume one window, dispatcher access after teardown, compiled and
runtime binding differences, UWP lifecycle rules incorrectly applied to WinUI 3,
and XAML resources resolved only in one packaging mode.

- Distinguish desktop WinUI lifecycle from UWP assumptions. Define launch,
  activation, multiple instances, multiple windows, background behavior, close,
  unexpected termination, and state persistence without relying on automatic
  suspension callbacks.
- Choose packaged, packaged-with-external-location, or unpackaged deployment
  deliberately. Trace package identity, Windows App SDK runtime initialization,
  dependencies, file and protocol activation, storage APIs, updates, and
  uninstall semantics for that exact model.
- Keep XAML dependency-property precedence, bindings, converters, compiled
  binding, resources, themes, and visual-state ownership understandable. Silent
  binding failure is not acceptable for required state.
- Confine UI objects to the owning dispatcher and define cancellation when
  windows, pages, or navigation entries disappear. Avoid sync waits and
  background callbacks into closed windows.
- Define activation routing and single- or multi-instance behavior for launch,
  files, protocols, notifications, and command-line input. Validate and
  authorize activation payloads before navigation or side effects.
- Review navigation state, window lifetime, back behavior, restoration, and
  unsaved-data handling across crash, update, restart, and multiple windows.
- Validate keyboard, focus, accessibility names and patterns, text scaling, high
  contrast, themes, localization, input methods, and custom controls through UI
  Automation.
- Verify architecture-specific native dependencies, runtime packaging, signing,
  installer behavior, updates, repair, rollback, and compatibility with the
  declared Windows minimum.

## Verify the claims

- Exercise every activation kind, instance redirection path, window lifecycle,
  close-during-work path, crash, restart, and state restore.
- Test packaged and unpackaged assumptions on clean machines without development
  runtimes.
- Run accessibility, keyboard, theme, high-contrast, text-scale, localization,
  and mixed-DPI tests.
- Inspect produced package identity, manifest, architecture payloads, runtime
  dependencies, signatures, update, rollback, and uninstall behavior.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Windows App SDK and
WinUI versions, C# or C++, Windows minimums, packaged or unpackaged deployment,
architectures, app lifecycle, identity, and distribution. For the changed
boundary, ask only about unresolved Windows App SDK lifecycle, XAML, dependency
properties, binding, dispatcher and async behavior, windows, activation,
navigation, resources, accessibility, packaging, and deployment when the answer
can change the verdict or implementation.

## Calibrate findings

- Treat an identity or deployment mismatch that prevents launch, unsafe
  activation, inaccessible primary workflow, or state loss during ordinary
  lifecycle events as critical or high according to blast radius and realistic
  likelihood.
- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the plan depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
Windows App SDK lifecycle, XAML, dependency properties, binding, dispatcher and
async behavior, windows, activation, navigation, resources, accessibility,
packaging, and deployment, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
