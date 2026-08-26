# Realtime web survey contribution

## Applicability

Apply this contribution when a plan uses WebSockets, server-sent events, long
polling, or similar live client connections. Skip it when Realtime web does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Realtime web, inspect version declarations, effective configuration sources,
rendered artifacts, infrastructure and identity policy, build and deployment
workflows, service objectives, operational runbooks, and project documentation.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Transport choices, connection scale, proxy and
  timeout limits, authentication, message size and ordering, resume policy,
  regional topology, and client support.
- Review doctrine for: WebSocket, SSE and polling semantics, connection
  lifecycle, authentication, ordering, heartbeats, backpressure, reconnect,
  resume, fan-out, proxies, and draining.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: WebSocket, SSE, or other transport; proxy and
  timeout behavior; connection routing; shared state; regions; backpressure;
  reconnect; scaling; and drain.

## Ask only when materially unresolved

- What connection identity, authorization refresh, ordering, reconnect, and
  state-recovery contract applies?
- How are slow clients, fan-out, presence expiry, deploys, and regional or
  broker failure bounded?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: WebSocket, SSE, or other transport;
  proxy and timeout behavior; connection routing; shared state; regions;
  backpressure; reconnect; scaling; and drain? Ask only when evidence and the
  core profile confirmation do not resolve them.

## Record in .grump

Record Realtime web answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Realtime web deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Realtime
web doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Realtime web when product or protocol version, topology, environment,
identity, trust boundary, resource model, configuration authority, deployment
process, or recovery objectives materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
