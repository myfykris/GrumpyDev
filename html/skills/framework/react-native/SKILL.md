---
name: gd-react-native
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review React Native engineering work for architecture compatibility, native bridges, lifecycle, navigation, state, permissions, performance, accessibility, and release behavior."
---

# React Native GrumpyDev review

## Quick checks

- Read React Native, React, platform, engine, native module, navigation, and state-library
  versions.

- Identify New Architecture support, code generation, bridged or bridgeless modules, native
  build settings, and minimum OS levels.

Watch especially for old native modules assumed compatible with the New
Architecture, JavaScript-thread stalls hidden by simulators, lifecycle work lost
in background state, navigation state duplicated, and platform permission
differences ignored.

- Assess unsafe native memory behavior, secret exposure, inaccessible core flows, or lost
  committed data under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the React Native
specialist.

## Verdict context

State the architecture matrix, native boundaries, lifecycle and state owners, platform
differences, accessibility, and release evidence.
