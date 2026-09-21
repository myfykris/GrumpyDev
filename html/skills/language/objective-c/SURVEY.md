# Objective-C survey contribution

## Applies when

Apply this contribution when the project contains or builds Objective-C or
Objective-C++ source, exposes an Objective-C ABI, or uses generated bindings or
a bridge whose correctness depends on Objective-C runtime semantics. Do not
apply it merely because the project targets an Apple platform, imports Apple
frameworks, or contains Swift code.

## Inspect

- Inspect compiler and target settings, headers, module maps, ownership
  annotations, bridging headers, categories, blocks, observers, native
  boundaries, and build products.

## Ask when unresolved

- Which of these durable facts materially change future reviews: compiler and
  language mode, ARC policy, target Apple platform and operating-system
  versions, frameworks, Swift bridging, Objective-C++ use, architectures, and
  deployment form?

- Which runtime or deployment differences are material for future reviews:
  macOS or iOS targets, architectures, runtime and framework versions, app or
  helper process, sandbox, entitlements, signing, packaging, and Swift or C++
  interop?

## Record

Map durable Objective-C version and compatibility requirements to
`Requirements` or `Constraints`, runtime facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
