# C# survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with C# or .NET code, artifacts, or runtime behavior.

## Inspect

- Read project and solution files, target frameworks, nullable settings, package
  locks, analyzers, publish settings, dependency registration, and
  representative tests.

## Ask when unresolved

- Which C# language, .NET runtime, nullable context, target framework, and
  deployment versions apply?

- What project conventions govern async cancellation, disposal, dependency
  lifetimes, serialization, and concurrency across components?

- Which runtime or deployment differences materially change future reviews:
  .NET runtime, Windows or cross-platform target, architecture, framework-
  dependent versus self-contained deployment, trimming or AOT, service or
  desktop process model, and native dependencies?

## Record

Map durable C# version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
