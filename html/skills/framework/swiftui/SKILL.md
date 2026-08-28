---
name: swiftui
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review SwiftUI plans and other engineering artifacts for state ownership, view identity, navigation, asynchronous work, persistence, accessibility, performance, and application lifecycle risks. Project applicability: the project uses or materially depends on SwiftUI."
---

# SwiftUI GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `swift` skill.

## Lean review

- Establish the exact Swift, SwiftUI, OS, device, and deployment-target
  versions.

- Read platform targets, app entry points, observation approach, environment
  values, navigation, persistence, concurrency, previews, and UI tests.

Watch especially for unstable view identity, competing state owners, tasks that
survive view replacement, main-actor violations, side effects triggered by body
recomputation, navigation state that cannot restore, and newer APIs used below
the declared OS target.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-user data exposure, lost critical persisted state, or an
  inaccessible core flow as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete SwiftUI evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State view and model ownership, concurrency lifecycle, navigation and
restoration contract, accessibility, persistence behavior, and device evidence.
