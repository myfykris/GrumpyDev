---
name: ios
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review iOS and iPadOS engineering work for application lifecycle, permissions, entitlements, data protection, background work, signing, accessibility, compatibility, and release behavior."
---

# iOS and iPadOS GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `swift`, `swiftui` and
`application-security` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read minimum OS, Xcode, SDK, language, UI framework, dependency, build setting, and
  supported-device versions.

- Trace scene and application lifecycle, state restoration, background transitions,
  termination, memory pressure, and multitasking.

Watch especially for background time assumed unlimited, privacy prompts without
denial behavior, sensitive files left with weak protection or backup enabled,
keychain groups shared too broadly, universal links trusted without validation,
and signing ownership undocumented.

Lean mode is insufficient when this material severity condition may apply:

- Treat signing compromise, entitlement overreach, credential leakage, or cross-account
  protected-data exposure as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete iOS and iPadOS evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State the Apple platform matrix, lifecycle and state owners, permission and entitlement surface,
signing owner, and release evidence.
