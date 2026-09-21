---
name: gd-expo
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Expo engineering work for SDK and React Native compatibility, native configuration, EAS builds, updates, permissions, plugins, routing, and release safety."
---

# Expo GrumpyDev review

## Quick checks

- Read Expo SDK, React Native, React, router, module, config-plugin, and native project
  versions.

- Identify managed or prebuild workflow, development builds, EAS Build profiles, credentials,
  channels, and runtime versions.

Watch especially for Expo Go treated as production evidence, config plugins that
mutate native projects unpredictably, over-the-air updates crossing native
compatibility, secrets placed in public app config, and permissions tested on
only one platform.

- Assess signing compromise, secret exposure, incompatible updates that brick a core flow, or
  unsafe permission use under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Expo specialist.

## Verdict context

State the SDK and native matrix, workflow, generated changes, update compatibility, permission
behavior, signing owner, and release evidence.
