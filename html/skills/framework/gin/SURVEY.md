# Gin survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Gin.

## Inspect

- Establish the exact Go, Gin, server, and deployment versions or modes.

## Ask when unresolved

- Which Go and Gin versions, server configuration, middleware order, and
  binding rules apply?

- How are validation, authentication, limits, cancellation, errors, shared
  state, and shutdown handled?

- Which runtime or deployment differences materially change future reviews: Go
  and Gin versions, proxy trust, worker process, limits, timeouts, file
  serving, signals, drain, and deployment architecture?

## Record

Map durable Gin version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
