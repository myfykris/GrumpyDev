---
name: gd-realtime-web
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review realtime web engineering work for connection lifecycle, authentication, ordering, backpressure, reconnect, fan-out, presence, state recovery, and capacity."
---

# Realtime web GrumpyDev review

## Quick checks

- Read handshake and authentication, connection registry, message protocol,
  sequence handling, buffers, heartbeat, fan-out, reconnect, and load tests.

- Trace token expiry, network flap, duplicate message, slow client, process
  restart, deploy drain, regional loss, and state resynchronization.

Watch especially for reconnect storms, duplicate or out-of-order messages,
authorization that expires while a connection remains open, connection state
pinned to one instance, unbounded outbound buffers, heartbeat intervals
incompatible with proxies, resume tokens that replay unauthorized data,
cross-site WebSocket handshakes, and one authenticated connection assumed to
authorize every topic and message.

- Assess cross-user data leakage, unbounded fan-out, or unrecoverable client
  state divergence under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Realtime web
specialist.

## Verdict context

State connection identity, origin and per-message authorization, delivery and
resync contract, parser and buffer bounds, presence authority, lifecycle
behavior, and capacity evidence.
