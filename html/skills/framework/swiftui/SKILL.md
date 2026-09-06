---
name: swiftui
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review SwiftUI engineering work for state ownership, view identity, navigation, asynchronous work, persistence, accessibility, performance, and application lifecycle risks."
---

# SwiftUI GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
