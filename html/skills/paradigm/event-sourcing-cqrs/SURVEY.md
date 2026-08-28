# Event sourcing and CQRS survey contribution

## Applicability

Apply this contribution when events are the source of truth or reads and writes use
distinct models. Skip it when Event sourcing and CQRS do not constrain a supported
build, runtime, client, data, deployment, or operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Event sourcing and CQRS, inspect architecture records, module or service
maps, dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Event store and versions, stream boundaries,
  command and projection topology, consistency expectations, snapshot policy,
  replay scale, and deletion constraints.
- Review doctrine for: Event immutability, aggregate streams, expected versions,
  projections, snapshots, commands, consistency, rebuilds, corrections, privacy,
  and migrations.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Event store, command and projection runtimes,
  consistency lag, replay environment, snapshot storage, partitioning, backup,
  restore, and deployment compatibility.

## Ask only when materially unresolved

- Which log is authoritative, and which event versions must rebuild every
  supported projection?
- How are command concurrency, event evolution, snapshots, projection lag,
  replay, and correction handled?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Event store, command and projection
  runtimes, consistency lag, replay environment, snapshot storage,
  partitioning, backup, restore, and deployment compatibility? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Event sourcing and CQRS answers in project architecture, data ownership,
integration, deployment, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Event sourcing and CQRS deployment facts on the affected
`DEP-###` profile. Use a referenced `INF-###` entry for a material component
shared by several profiles. Preserve separate state, support, ownership,
confidence, source, and scope fields.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Event sourcing and CQRS
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Event sourcing and CQRS when business invariants, ownership
boundaries, data authority, module or service map, integration model, deployment
units, consistency requirements, or operational responsibility materially
change, when evidence conflicts with saved doctrine, or when the user requests a
context refresh.
