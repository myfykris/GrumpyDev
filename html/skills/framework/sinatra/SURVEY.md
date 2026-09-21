# Sinatra survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Sinatra.

## Inspect

- Establish the exact Ruby, Sinatra, Rack, server, and deployment versions or
  modes.

## Ask when unresolved

- Which Ruby, Sinatra, Rack, server, concurrency, and deployment versions or
  modes apply?

- How do middleware, shared state, sessions, authentication, errors, blocking
  work, and shutdown behave?

- Which runtime or deployment differences materially change future reviews:
  Ruby implementation, Rack and server, process and thread model, middleware,
  proxy, sessions, static files, timeouts, signals, and production deployment?

## Record

Map durable Sinatra version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
