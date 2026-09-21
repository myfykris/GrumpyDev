---
name: gd-swiftui
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review SwiftUI engineering work for state ownership, view identity, navigation, asynchronous work, persistence, accessibility, performance, and application lifecycle risks."
---

# SwiftUI GrumpyDev review

## Quick checks

- Establish the exact Swift, SwiftUI, OS, device, and deployment-target
  versions.

- Read platform targets, app entry points, observation approach, environment
  values, navigation, persistence, concurrency, previews, and UI tests.

Watch especially for unstable view identity, competing state owners, tasks that
survive view replacement, main-actor violations, side effects triggered by body
recomputation, navigation state that cannot restore, and newer APIs used below
the declared OS target.

- Assess cross-user data exposure, lost critical persisted state, or an
  inaccessible core flow under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the SwiftUI specialist.

## Verdict context

State view and model ownership, concurrency lifecycle, navigation and
restoration contract, accessibility, persistence behavior, and device evidence.
