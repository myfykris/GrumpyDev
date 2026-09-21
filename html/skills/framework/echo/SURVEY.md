# Echo survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Echo.

## Inspect

- Establish the exact Go, Echo, server, and deployment versions or modes.

## Ask when unresolved

- Which Go and Echo versions, server settings, middleware order, and binder
  behavior apply?

- How are validation, authentication, request limits, cancellation, errors, and
  graceful shutdown handled?

- Which runtime or deployment differences materially change future reviews: Go
  and Echo versions, worker process, reverse proxy and trusted addresses, TLS,
  body and timeout limits, filesystem, signals, drain, and cross-compilation
  target?

## Record

Map durable Echo version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
