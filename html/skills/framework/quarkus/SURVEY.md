# Quarkus survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Quarkus.

## Inspect

- Read Quarkus, Java, and extension versions, build configuration, CDI scopes,
  REST stack, persistence, messaging, native-image settings, and tests.

## Ask when unresolved

- Which Java, Quarkus, build mode, native-image toolchain, extension, and
  deployment versions apply?

- How do dependency injection scopes, reactive and blocking work,
  configuration, transactions, and startup differ by mode?

- Which runtime or deployment differences are material for future reviews: JVM
  versus native image, build-time versus runtime configuration, container
  limits, HTTP or reactive worker model, generated resources, packaging, and
  startup or shutdown?

## Record

Map durable Quarkus version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
