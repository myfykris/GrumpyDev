# Actix Web survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Actix Web.

## Inspect

- Establish the exact Actix Web, Rust, Tokio, and target-platform versions.

## Ask when unresolved

- Which Actix Web, Rust, and Tokio versions and worker model apply to the
  service?

- How do extractors, shared state, blocking work, errors, limits, and graceful
  shutdown behave?

- Which runtime or deployment differences materially change future reviews:
  Rust and Actix versions, worker count, async runtime, blocking pool, reverse
  proxy, TLS, body and timeout limits, process manager, drain, and shutdown?

## Record

Map durable Actix Web version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
