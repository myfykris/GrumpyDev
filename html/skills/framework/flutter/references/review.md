# Flutter full-review guidance

## Operating conditions

Establish the project target: Flutter and Dart versions, target platforms and
minimum versions, state and navigation libraries, build flavors, plugin set,
signing boundary, and distribution channels. The changed boundary must define:
Widget and element lifecycle, state ownership, async context, navigation,
isolates, plugins, platform channels, rendering, accessibility, persistence, and
release modes.

## Failure patterns

- Require one owner for each state value and dispose controllers, subscriptions,
  focus nodes, animations, and platform resources.
- Check stale BuildContext use, work after disposal, duplicate requests,
  navigation restoration, and app background or resume behavior.
- Verify plugin support, permissions, storage, networking, and platform-channel
  contracts on every target platform.
- Require complete loading, empty, stale, offline, denied, error, and retry
  states with keyboard and screen-reader behavior.
- Use profile or release evidence for frame time, memory, startup, binary size,
  tree shaking, and native build behavior.

## Verification to run or specify in the plan

- Navigate away while requests and platform calls are pending, then background
  and resume the app. Verify disposed state is not updated and navigation or
  persisted state restores as promised.
- Exercise plugins and permission denial on each supported platform. Use
  profile or release builds for frame-time and memory claims, and test
  affected flows with keyboard and screen-reader input.
