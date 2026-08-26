# Event-driven architecture survey contribution

## Applicability

Apply this contribution when services communicate or trigger work through events
or messages. Skip it when Event-driven architecture does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Event-driven architecture, inspect architecture records, module or service
maps, dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Brokers, delivery and ordering guarantees, event
  ownership, schema governance, retention and replay, consumer topology, and
  failure handling.
- Review doctrine for: Event ownership, notification versus fact semantics,
  ordering, delivery, schemas, idempotency, consumers, dead letters, replay,
  observability, and evolution.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Broker or transport, delivery and acknowledgement,
  partitions, ordering, retention, dead letters, consumer topology, replay,
  regions, and operational owner.

## Ask only when materially unresolved

- Is each message an event, command, or data stream, and who owns its meaning
  and handling?
- What delivery, ordering, acknowledgement, duplication, evolution, replay, and
  recovery semantics apply?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Broker or transport, delivery and
  acknowledgement, partitions, ordering, retention, dead letters, consumer
  topology, replay, regions, and operational owner? Ask only when evidence and
  the core profile confirmation do not resolve them.

## Record in .grump

Record Event-driven architecture answers in project architecture, data
ownership, integration, deployment, and operational doctrine. Preserve source
and scope. Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Event-driven architecture deployment facts on the affected
`DEP-###` profile. Use a referenced `INF-###` entry for a material component
shared by several profiles. Preserve separate state, support, ownership,
confidence, source, and scope fields.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Event-driven architecture
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Event-driven architecture when business invariants, ownership
boundaries, data authority, module or service map, integration model, deployment
units, consistency requirements, or operational responsibility materially
change, when evidence conflicts with saved doctrine, or when the user requests a
context refresh.
