# AppKit full-review guidance

## Operating conditions

Establish the project target: AppKit and macOS deployment targets, Swift or
Objective-C use, lifecycle model, document model, sandbox and entitlements,
persistence, accessibility targets, and distribution. The changed boundary must
define: Application and window lifecycle, responder chain, controllers,
bindings, document architecture, drawing, concurrency, accessibility, state
restoration, SwiftUI interop, sandboxing, and termination.

## Failure patterns

- Trace launch, activation, reopening, window creation, window close,
  application termination, sudden termination, and state restoration. Do not
  assume a final callback will run after crash, kill, logout, or power loss.
- Review first-responder and target-action routing, validation, menus, key
  equivalents, field editors, sheets, and modal sessions. Hidden responder-chain
  behavior can make authorization and state mutations occur somewhere other than
  the visible controller.
- Define ownership among windows, controllers, views, delegates, data sources,
  bindings, notifications, and observations. Avoid cycles and observers that
  outlive their owner or receive changes during teardown.
- Confine AppKit objects and UI mutations to the main thread. Move expensive
  work off it, then make cancellation and actor or queue hops explicit when
  windows close or selections change.
- Check layout, backing scale, color spaces, text, focus, keyboard operation,
  accessibility names and actions, reduced motion, localization expansion, and
  multiple displays with real system settings.
- Keep AppKit and SwiftUI state ownership unambiguous at hosting boundaries.
  Verify object lifetime, environment propagation, navigation, focus, commands,
  and observation in both directions.

## Verification to run or specify in the plan

- Run UI and accessibility tests with keyboard-only input, VoiceOver, scaling,
  localization, dark mode, reduced motion, and multiple displays.
- Profile main-thread stalls, drawing, memory, retain cycles, and cancellation
  through window teardown.
