---
name: realtime-web
description: Review realtime web plans for connection lifecycle, authentication, ordering, backpressure, reconnect, fan-out, presence, state recovery, and capacity. Use when a plan uses WebSockets, server-sent events, long polling, or similar live client connections.
---

# Realtime web plan review

Apply this guidance alongside the core GrumpyDev review and the
`distributed-systems`, `application-security`, and `performance-capacity`
skills.

## Inspect evidence

- Read handshake and authentication, connection registry, message protocol,
  sequence handling, buffers, heartbeat, fan-out, reconnect, and load tests.
- Trace token expiry, network flap, duplicate message, slow client, process
  restart, deploy drain, regional loss, and state resynchronization.

## Establish the operating model

Establish the project target: Transport choices, connection scale, proxy and
timeout limits, authentication, message size and ordering, resume policy,
regional topology, and client support. The changed boundary must define:
WebSocket, SSE and polling semantics, connection lifecycle, authentication,
ordering, heartbeats, backpressure, reconnect, resume, fan-out, proxies, and
draining.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for WebSocket, SSE and polling semantics, connection
lifecycle, authentication, ordering, heartbeats. Prove backpressure, reconnect,
resume, fan-out, proxies, draining through rotation, overload, partial rollout,
drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for reconnect storms, duplicate or out-of-order messages,
authorization that expires while a connection remains open, connection state
pinned to one instance, unbounded outbound buffers, heartbeat intervals
incompatible with proxies, resume tokens that replay unauthorized data,
cross-site WebSocket handshakes, and one authenticated connection assumed to
authorize every topic and message.

- Define authentication refresh, authorization changes, origin checks,
  connection limits, and revocation for long-lived sessions.
- Authorize each subscribe, publish, command, resource, and delivered event
  against the current user and tenant. Recheck permissions after role changes,
  token refresh, resume, and backend reconnect rather than trusting connection
  establishment forever.
- Validate the browser Origin where applicable, require an explicit protocol and
  schema, and bound frame, message, decompression, nesting, topic count, and
  per-identity rate before allocation or fan-out.
- Specify ordering and delivery scope with sequence identifiers so reconnect can
  detect gaps, duplicates, and stale state.
- Bound per-connection and shared buffers, apply backpressure, and disconnect
  slow consumers before memory becomes the queue.
- Separate ephemeral presence from durable state and make reconnect use
  snapshots or replay with an explicit retention window.
- Prove fan-out, heartbeat, proxy timeouts, load-balancer behavior, rolling
  deploys, and connection storms at expected concurrency.

## Verify the claims

- Verify these behaviors through the effective Realtime web configuration and
  runtime topology: WebSocket, SSE and polling semantics, connection lifecycle,
  authentication, ordering, heartbeats. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: backpressure, reconnect, resume,
  fan-out, proxies, draining. Exercise startup, readiness, normal load,
  overload, dependency loss, rotation, graceful drain, forced stop, failover,
  and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.
- Exercise hostile origins, guessed topics, cross-tenant subscriptions, stale
  roles, oversized and compressed messages, malformed frames, publish floods,
  revocation during a connection, and replay after permissions change.

## Ask when evidence is missing

- What connection identity, authorization refresh, ordering, reconnect, and
  state-recovery contract applies?
- How are slow clients, fan-out, presence expiry, deploys, and regional or
  broker failure bounded?

## Calibrate findings

- Treat cross-user data leakage, unbounded fan-out, or unrecoverable client
  state divergence as critical.
- Downgrade when connections are low-scale and bounded or replay, auth refresh,
  and backpressure are demonstrated.

## Add to the verdict

State connection identity, origin and per-message authorization, delivery and
resync contract, parser and buffer bounds, presence authority, lifecycle
behavior, and capacity evidence.
