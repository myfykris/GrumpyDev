---
name: gd-android
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Android engineering work for component lifecycle, process death, permissions, storage, background work, compatibility, signing, packaging, accessibility, and release behavior."
---

# Android GrumpyDev review

## Quick checks

- Read minimum and target SDK, Android plugin, Gradle, language, UI toolkit, architecture, and
  dependency versions.

- Trace activity, fragment, service, receiver, provider, application, task, and process
  lifecycle behavior.

Watch especially for process death treated as logout, implicit exported
components, broad storage or notification permissions, background work assumed
continuous, pending intents with unsafe mutability, WebView bridges exposing
native power, and signing ownership left informal.

- Assess exposed privileged components, unsafe WebView bridges, signing compromise, or
  cross-account data leakage under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Android specialist.

## Verdict context

State supported Android matrix, lifecycle and data owners, external surface, background
guarantees, signing owner, and release evidence.
