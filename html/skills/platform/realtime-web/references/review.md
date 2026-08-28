# Realtime web standard review

## Establish the operating model

Establish the project target: Transport choices, connection scale, proxy and
timeout limits, authentication, message size and ordering, resume policy,
regional topology, and client support. The changed boundary must define:
WebSocket, SSE and polling semantics, connection lifecycle, authentication,
ordering, heartbeats, backpressure, reconnect, resume, fan-out, proxies, and
draining.

Identify the connection and session authority, authentication refresh,
subscription and authorization owner, message ordering and resume token,
heartbeat and idle policy, buffer limits, fan-out topology, proxy timeouts,
reconnect behavior, and deployment drain. Prove disconnects, duplicated or
missed messages, slow clients, expired credentials, proxy resets and mixed
server versions preserve the documented client contract.

## Challenge the reviewed work

### Recurring traps

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

- Exercise handshake, authentication refresh, subscribe, publish, idle,
  heartbeat, reconnect, resume and close through the production proxy and
  routing topology.
- Inject slow clients, full buffers, duplicate and missing messages, proxy
  resets, expired credentials, revoked access, fan-out overload and regional or
  process loss while checking ordering and resume contracts.
- Drain and roll back old and new server versions with long-lived connections
  active, verifying clients reconnect without cross-tenant data or silent gaps.
- Exercise hostile origins, guessed topics, cross-tenant subscriptions, stale
  roles, oversized and compressed messages, malformed frames, publish floods,
  revocation during a connection, and replay after permissions change.

## Ask when evidence is missing

- What connection identity, authorization refresh, ordering, reconnect, and
  state-recovery contract applies?
- How are slow clients, fan-out, presence expiry, deploys, and regional or
  broker failure bounded?

## Calibrate findings

- Downgrade when connections are low-scale and bounded or replay, auth refresh,
  and backpressure are demonstrated.
