---
name: expo
description: Review Expo plans for SDK and React Native compatibility, native configuration, EAS builds, updates, permissions, plugins, routing, and release safety. Use when a plan builds or operates an Expo application.
---

# Expo plan review

Apply this guidance alongside the core GrumpyDev review and the `react-native`, `javascript` and
`typescript` skills.

## Inspect evidence

- Read Expo SDK, React Native, React, router, module, config-plugin, and native project
  versions.
- Identify managed or prebuild workflow, development builds, EAS Build profiles, credentials,
  channels, and runtime versions.
- Trace permissions, deep links, push tokens, background work, secure storage, assets, native
  modules, and platform differences.
- Inspect app configuration, generated native changes, update settings, environment values,
  signing, and store metadata.

## Establish the operating model

Establish the project target: Expo SDK and React Native versions, target platforms, workflow,
native directories, EAS profiles, signing ownership, update channels and runtime policy, router,
plugins, permissions, and minimum OS versions.

The plan must distinguish JavaScript updates from native binary changes. Runtime version policy
must prevent an update from loading on an incompatible binary.

## Challenge the plan

### Recurring traps

Watch especially for Expo Go treated as production evidence, config plugins that mutate native
projects unpredictably, over-the-air updates crossing native compatibility, secrets placed in
public app config, and permissions tested on only one platform.

- Require a compatibility matrix for Expo SDK, React Native, React, native modules, and
  supported operating systems.
- Treat config plugins and prebuild output as code changes; review generated entitlements,
  manifests, permissions, and native dependencies.
- Define runtime versions, channels, rollback, rollout percentage, failed-update recovery, and
  binary-to-update compatibility.
- Separate build-time public configuration from server secrets and assume packaged application
  values are readable by users.
- Exercise deep links, notifications, background and resumed state, offline startup, denied
  permissions, and store release variants.

## Verify the claims

- Produce representative local or EAS-equivalent release builds for every platform and inspect
  generated native configuration.
- Test updates against each supported installed binary, including incompatible updates,
  rollback, offline launch, and failed startup.
- Use development builds or release binaries for native modules and permissions rather than
  relying only on Expo Go.

## Ask when evidence is missing

- Which Expo SDK, React Native version, platforms, workflow, native modules, EAS profiles, and
  minimum OS versions apply?
- What runtime-version, channel, rollout, rollback, signing, permission, and
  generated-native-code policy applies?

## Calibrate findings

- Treat signing compromise, secret exposure, incompatible updates that brick a core flow, or
  unsafe permission use as critical.
- Downgrade when native compatibility, generated configuration, updates, rollback, and
  real-device release builds are proven.

## Add to the verdict

State the SDK and native matrix, workflow, generated changes, update compatibility, permission
behavior, signing owner, and release evidence.
