# Realtime web survey contribution

## Applies when

Apply this contribution when the project uses WebSockets, server-sent events, long
polling, or similar live client connections.

## Inspect

- Read handshake and authentication, connection registry, message protocol,
  sequence handling, buffers, heartbeat, fan-out, reconnect, and load tests.

## Ask when unresolved

- What connection identity, authorization refresh, ordering, reconnect, and
  state-recovery contract applies?

- How are slow clients, fan-out, presence expiry, deploys, and regional or
  broker failure bounded?

- Which runtime or deployment differences materially change future reviews:
  WebSocket, SSE, or other transport; proxy and timeout behavior; connection
  routing; shared state; regions; backpressure; reconnect; scaling; and drain?

## Record

Map durable Realtime web requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
