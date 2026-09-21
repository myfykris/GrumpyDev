# Axum survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Axum.

## Inspect

- Establish the exact Axum, Rust, Tokio, Tower, and target-platform versions.

## Ask when unresolved

- Which Axum, Rust, Tokio, Tower, and HTTP stack versions apply?

- How do router state, extractors, layers, blocking work, cancellation, limits,
  and shutdown interact?

- Which runtime or deployment differences materially change future reviews:
  Tokio runtime, blocking boundaries, worker threads, reverse proxy, TLS, body
  and timeout limits, process manager, signals, drain, and executable target?

## Record

Map durable Axum version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
