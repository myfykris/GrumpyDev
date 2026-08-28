---
name: ios
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review iOS and iPadOS plans and other engineering artifacts for application lifecycle, permissions, entitlements, data protection, background work, signing, accessibility, compatibility, and release behavior. Project applicability: software targets Apple mobile devices."
---

# iOS and iPadOS GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `swift`, `swiftui` and
`application-security` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
