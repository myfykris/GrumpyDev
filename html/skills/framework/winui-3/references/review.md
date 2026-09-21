# WinUI 3 full-review guidance

## Operating conditions

Establish the project target: Windows App SDK and WinUI versions, C# or C++,
Windows minimums, packaged or unpackaged deployment, architectures, app
lifecycle, identity, and distribution. The changed boundary must define: Windows
App SDK lifecycle, XAML, dependency properties, binding, dispatcher and async
behavior, windows, activation, navigation, resources, accessibility, packaging,
and deployment.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise every activation kind, instance redirection path, window lifecycle,
  close-during-work path, crash, restart, and state restore.
- Run accessibility, keyboard, theme, high-contrast, text-scale, localization,
  and mixed-DPI tests.
