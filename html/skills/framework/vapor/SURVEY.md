# Vapor survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Vapor.

## Inspect

- Read Vapor, Swift, and dependency versions, application configuration, routes,
  middleware, content models, Fluent schemas and migrations, clients, and tests.

## Ask when unresolved

- Which Swift, Vapor, SwiftNIO, database driver, and deployment versions apply?

- How do event-loop affinity, async work, request state, authentication,
  transactions, errors, and shutdown interact?

- Which runtime or deployment differences materially change future reviews:
  Swift and Vapor versions, event-loop and worker sizing, proxy, TLS, files,
  database pool, queues, executable platform, signals, drain, and deployment?

## Record

Map durable Vapor version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
