# SwiftUI full-review guidance

## Operating conditions

Establish the project target: Swift and Xcode versions, target platforms and
minimum OS versions, observation and navigation model, concurrency mode,
persistence, and distribution targets. The changed boundary must define: View
identity, state wrappers, observation, rendering, navigation, tasks, actors,
persistence, platform lifecycle, accessibility, previews, and OS availability.

## Failure patterns

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

## Verification to run or specify in the plan

- Change view identity, navigate rapidly, and dismiss views while tasks
  finish. Verify observable state retains its intended owner and canceled or
  stale work cannot update the wrong screen.
- Test deep links and restoration after process termination on supported OS
  targets. Exercise affected flows with Dynamic Type and VoiceOver, and use
  device release builds for rendering and memory claims.
