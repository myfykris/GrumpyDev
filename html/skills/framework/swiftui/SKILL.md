---
name: swiftui
description: Review SwiftUI plans for state ownership, view identity, navigation, asynchronous work, persistence, accessibility, performance, and application lifecycle risks. Use when a Swift plan changes SwiftUI views, models, navigation, data flow, or app structure.
---

# SwiftUI plan review

Apply this guidance alongside the core GrumpyDev review and the `swift` skill.

## Inspect evidence

- Establish the exact Swift, SwiftUI, OS, device, and deployment-target
  versions.
- Read platform targets, app entry points, observation approach, environment
  values, navigation, persistence, concurrency, previews, and UI tests.
- Trace state ownership, bindings, view identity, tasks, cancellation, scene
  transitions, navigation restoration, and data errors.

## Establish the operating model

Establish the project target: Swift and Xcode versions, target platforms and
minimum OS versions, observation and navigation model, concurrency mode,
persistence, and distribution targets. The changed boundary must define: View
identity, state wrappers, observation, rendering, navigation, tasks, actors,
persistence, platform lifecycle, accessibility, previews, and OS availability.

Assign lifecycle, state, dependency, persistence, and security ownership for
View identity, state wrappers, observation, rendering, navigation, tasks. Prove
actors, persistence, platform lifecycle, accessibility, previews, OS
availability through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for unstable view identity, competing state owners, tasks that
survive view replacement, main-actor violations, side effects triggered by body
recomputation, navigation state that cannot restore, and newer APIs used below
the declared OS target.

- Choose the correct owner for each state value and reject duplicated or
  recreated observable state caused by view identity changes.
- Check task cancellation, actor isolation, stale responses, work after view
  disappearance, and main-thread updates.
- Verify navigation deep links, restoration, modal ownership, back behavior, and
  state after process termination.
- Require loading, empty, stale, offline, denied, error, and retry states with
  Dynamic Type, VoiceOver, focus, and reduced motion.
- Use device and release evidence for rendering cost, list identity, memory,
  persistence migration, and lifecycle transitions.

## Verify the claims

- Verify these behaviors through the actual SwiftUI lifecycle and production
  pipeline: View identity, state wrappers, observation, rendering, navigation,
  tasks. Use the actual framework pipeline and production build with
  representative services and configuration.
- Exercise failure and edge behavior for: actors, persistence, platform
  lifecycle, accessibility, previews, OS availability. Exercise invalid input,
  denied access, cancellation, dependency failure, concurrent work, shutdown,
  and mixed-version deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Swift, SwiftUI, OS versions, device classes, and concurrency model
  apply?
- Who owns observable state, navigation, task cancellation, persistence,
  accessibility, and scene restoration?

## Calibrate findings

- Treat cross-user data exposure, lost critical persisted state, or an
  inaccessible core flow as critical.
- Downgrade when version-specific state, navigation, concurrency, restoration,
  and accessibility are tested on supported devices.

## Add to the verdict

State view and model ownership, concurrency lifecycle, navigation and
restoration contract, accessibility, persistence behavior, and device evidence.
