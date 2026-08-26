---
name: appkit
description: Review AppKit plans for application and window lifecycle, responder routing, controllers, bindings, drawing, threading, accessibility, sandboxing, state restoration, and termination risks. Use when a macOS desktop plan changes AppKit UI or application behavior.
---

# AppKit plan review

Apply this guidance alongside the core GrumpyDev review and the `swift`,
`objective-c`, `macos`, `application-security`, and `testing-strategy` skills.
Select only companions that match the plan's real boundaries. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect application delegates, scene or window controllers, responders, menus,
  bindings, document controllers, view code, drawing layers, concurrency
  boundaries, entitlements, and distribution settings.
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

Establish the project target: AppKit and macOS deployment targets, Swift or
Objective-C use, lifecycle model, document model, sandbox and entitlements,
persistence, accessibility targets, and distribution. The changed boundary must
define: Application and window lifecycle, responder chain, controllers,
bindings, document architecture, drawing, concurrency, accessibility, state
restoration, SwiftUI interop, sandboxing, and termination.

Assign lifecycle, state, dependency, persistence, and security ownership for
Application and window lifecycle, responder chain, controllers, bindings,
document architecture, drawing. Prove concurrency, accessibility, state
restoration, SwiftUI interop, sandboxing, termination through startup, invalid
or denied work, cancellation, background execution, mixed versions, shutdown,
rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for responder-chain behavior that hides mutations, bindings or
observers that outlive their owners, AppKit access off the main thread,
persistence deferred until a termination callback that may never run, and stale
security-scoped file access.

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
- For document apps, prove open, autosave, conflict, coordination,
  security-scoped access, undo, close, and recovery semantics. Preserve user
  data through version changes and interrupted writes.
- Check layout, backing scale, color spaces, text, focus, keyboard operation,
  accessibility names and actions, reduced motion, localization expansion, and
  multiple displays with real system settings.
- Keep AppKit and SwiftUI state ownership unambiguous at hosting boundaries.
  Verify object lifetime, environment propagation, navigation, focus, commands,
  and observation in both directions.
- Match sandbox entitlements and privacy purpose strings to actual file,
  network, hardware, automation, and helper access. More entitlement is not a
  substitute for a coherent access workflow.

## Verify the claims

- Exercise cold launch, reopen, multiple windows, close during work,
  termination, crash recovery, and state restoration.
- Run UI and accessibility tests with keyboard-only input, VoiceOver, scaling,
  localization, dark mode, reduced motion, and multiple displays.
- Test sandboxed file selection, persistent security-scoped access, helpers,
  entitlements, and denied permissions.
- Profile main-thread stalls, drawing, memory, retain cycles, and cancellation
  through window teardown.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: AppKit and macOS
deployment targets, Swift or Objective-C use, lifecycle model, document model,
sandbox and entitlements, persistence, accessibility targets, and distribution.
For the changed boundary, ask only about unresolved Application and window
lifecycle, responder chain, controllers, bindings, document architecture,
drawing, concurrency, accessibility, state restoration, SwiftUI interop,
sandboxing, and termination when the answer can change the verdict or
implementation.

## Calibrate findings

- Treat user-data loss, an unsandboxed privilege boundary, an inaccessible core
  workflow, or lifecycle behavior that makes recovery impossible as critical or
  high according to blast radius and realistic likelihood.
- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the plan depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
application and window lifecycle, responder chain, controllers, bindings,
document architecture, drawing, concurrency, accessibility, state restoration,
SwiftUI interoperability, sandboxing, and termination, verification evidence,
deployment and recovery limits, and any material assumption that remains
unresolved.
