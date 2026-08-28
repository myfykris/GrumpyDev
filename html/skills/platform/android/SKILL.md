---
name: android
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Android plans and other engineering artifacts for component lifecycle, process death, permissions, storage, background work, compatibility, signing, packaging, accessibility, and release behavior. Project applicability: software targets Android devices."
---

# Android GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `kotlin`, `jetpack-compose` and
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

- Read minimum and target SDK, Android plugin, Gradle, language, UI toolkit, architecture, and
  dependency versions.

- Trace activity, fragment, service, receiver, provider, application, task, and process
  lifecycle behavior.

Watch especially for process death treated as logout, implicit exported
components, broad storage or notification permissions, background work assumed
continuous, pending intents with unsafe mutability, WebView bridges exposing
native power, and signing ownership left informal.

Lean mode is insufficient when this material severity condition may apply:

- Treat exposed privileged components, unsafe WebView bridges, signing compromise, or
  cross-account data leakage as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Android evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State supported Android matrix, lifecycle and data owners, external surface, background
guarantees, signing owner, and release evidence.
