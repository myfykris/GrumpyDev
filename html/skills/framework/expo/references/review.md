# Expo full-review guidance

## Operating conditions

Establish the project target: Expo SDK and React Native versions, target platforms, workflow,
native directories, EAS profiles, signing ownership, update channels and runtime policy, router,
plugins, permissions, and minimum OS versions.

## Failure patterns

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

## Verification to run or specify in the plan

- Produce representative local or EAS-equivalent release builds for every platform and inspect
  generated native configuration.
- Test updates against each supported installed binary, including incompatible updates,
  rollback, offline launch, and failed startup.
- Use development builds or release binaries for native modules and permissions rather than
  relying only on Expo Go.
