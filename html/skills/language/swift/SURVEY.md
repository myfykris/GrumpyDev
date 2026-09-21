# Swift survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Swift code, artifacts, or runtime behavior.

## Inspect

- Read package or project settings, Swift and platform targets, concurrency
  checks, entitlements, generated code, bridging headers, and representative
  tests.

## Ask when unresolved

- Which Swift language, compiler, OS, deployment target, package, and
  concurrency versions apply?

- How do actors, tasks, cancellation, sendability, ownership, errors, and
  Objective-C interop cross the boundary?

- Which runtime or deployment differences are material for future reviews:
  Apple OS versions, architectures, runtime availability, app or server
  process, concurrency runtime, sandbox, entitlements, signing, packaging, and
  distribution?

## Record

Map durable Swift version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
