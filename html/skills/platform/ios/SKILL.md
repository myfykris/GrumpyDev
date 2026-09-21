---
name: gd-ios
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review iOS and iPadOS engineering work for application lifecycle, permissions, entitlements, data protection, background work, signing, accessibility, compatibility, and release behavior."
---

# iOS and iPadOS GrumpyDev review

## Quick checks

- Read minimum OS, Xcode, SDK, language, UI framework, dependency, build setting, and
  supported-device versions.

- Trace scene and application lifecycle, state restoration, background transitions,
  termination, memory pressure, and multitasking.

Watch especially for background time assumed unlimited, privacy prompts without
denial behavior, sensitive files left with weak protection or backup enabled,
keychain groups shared too broadly, universal links trusted without validation,
and signing ownership undocumented.

- Assess signing compromise, entitlement overreach, credential leakage, or cross-account
  protected-data exposure under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the iOS and iPadOS
specialist.

## Verdict context

State the Apple platform matrix, lifecycle and state owners, permission and entitlement surface,
signing owner, and release evidence.
