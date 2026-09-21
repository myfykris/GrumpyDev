# SwiftUI survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on SwiftUI.

## Inspect

- Establish the exact Swift, SwiftUI, OS, device, and deployment-target
  versions.

## Ask when unresolved

- Which Swift, SwiftUI, OS versions, device classes, and concurrency model
  apply?

- Who owns observable state, navigation, task cancellation, persistence,
  accessibility, and scene restoration?

- Which runtime or deployment differences are material for future reviews:
  Apple OS range, architectures, app lifecycle, sandbox, entitlements, state
  restoration, helpers, signing, packaging, update, and distribution?

## Record

Map durable SwiftUI version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
