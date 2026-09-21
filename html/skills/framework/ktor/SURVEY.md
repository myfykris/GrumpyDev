# Ktor survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Ktor.

## Inspect

- Read application modules, installed plugins and order, routing, content
  negotiation, authentication, coroutine dispatchers, client configuration, and
  tests.

## Ask when unresolved

- Which Kotlin, Ktor, engine, coroutine, serialization, and deployment versions
  apply?

- How do plugin order, authentication, cancellation, blocking work, errors,
  limits, and shutdown interact?

- Which runtime or deployment differences materially change future reviews:
  Kotlin and JVM or native target, server engine, coroutine dispatchers, proxy,
  TLS, serialization, worker model, packaging, resource limits, and shutdown?

## Record

Map durable Ktor version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
