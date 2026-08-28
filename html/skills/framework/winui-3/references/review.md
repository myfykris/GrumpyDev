# WinUI 3 standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

- Keep XAML dependency-property precedence, bindings, converters, compiled
  binding, resources, themes, and visual-state ownership understandable. Silent
  binding failure is not acceptable for required state.
- Confine UI objects to the owning dispatcher and define cancellation when
  windows, pages, or navigation entries disappear. Avoid sync waits and
  background callbacks into closed windows.
- Review navigation state, window lifetime, back behavior, restoration, and
  unsaved-data handling across crash, update, restart, and multiple windows.
- Validate keyboard, focus, accessibility names and patterns, text scaling, high
  contrast, themes, localization, input methods, and custom controls through UI
  Automation.
## Verify the claims

- Exercise every activation kind, instance redirection path, window lifecycle,
  close-during-work path, crash, restart, and state restore.
- Run accessibility, keyboard, theme, high-contrast, text-scale, localization,
  and mixed-DPI tests.
## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Windows App SDK and
WinUI versions, C# or C++, Windows minimums, packaged or unpackaged deployment,
architectures, app lifecycle, identity, and distribution. For the changed
boundary, ask only about unresolved Windows App SDK lifecycle, XAML, dependency
properties, binding, dispatcher and async behavior, windows, activation,
navigation, resources, accessibility, packaging, and deployment when the answer
can change the verdict or implementation.

## Calibrate findings

- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the reviewed work depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
