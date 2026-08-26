---
name: event-sourcing-cqrs
description: Review event sourcing and CQRS plans for immutable history, projection rebuilds, command invariants, event evolution, consistency lag, and operational burden. Use when events are the source of truth or reads and writes use distinct models.
---

# Event sourcing and CQRS plan review

Apply this guidance alongside the core GrumpyDev review and the
`event-driven-architecture`, `schema-evolution`, and applicable installed
storage skills.

## Inspect evidence

- Read command handlers, aggregate reconstruction, event store guarantees,
  snapshots, projections, checkpoints, and rebuild tooling.
- Trace a command through validation, event append, projection lag, failure,
  replay, correction, and data erasure requirements.

## Establish the operating model

Establish the project target: Event store and versions, stream boundaries,
command and projection topology, consistency expectations, snapshot policy,
replay scale, and deletion constraints. The changed boundary must define: Event
immutability, aggregate streams, expected versions, projections, snapshots,
commands, consistency, rebuilds, corrections, privacy, and migrations.

Name the invariants, authorities, owners, and enforcement for Event
immutability, aggregate streams, expected versions, projections, snapshots,
commands. Prove consistency, rebuilds, corrections, privacy, migrations under
concurrency, partial failure, incompatible versions, operational response,
rollback, and repair, and justify the added complexity.

## Challenge the plan

### Recurring traps

Watch especially for rewriting historical events, projections treated as
immediately consistent, replay triggering live side effects, command retries
without idempotency, snapshots treated as a correctness boundary, event schemas
that cannot evolve, and deletion obligations with no workable policy.

- Demand a concrete need for historical reconstruction or independent read
  models; CRUD with extra steps is a bad trade.
- Require optimistic concurrency and invariant enforcement at the append
  boundary.
- Define how old events remain readable as code, schemas, identifiers, and
  business meanings change.
- Prove projections can rebuild deterministically, resume idempotently, and
  expose their freshness to callers.
- Address corrections, privacy deletion, snapshot invalidation, storage growth,
  and operator tooling before committing to immutable history.

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Event immutability, aggregate streams, expected versions,
  projections, snapshots, commands. Use dependency, architecture, contract,
  schema, or ownership tests that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: consistency, rebuilds, corrections,
  privacy, migrations. Exercise the material invariant under concurrency, delay,
  duplication, partial failure, incompatible versions, rollback, and repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- Which log is authoritative, and which event versions must rebuild every
  supported projection?
- How are command concurrency, event evolution, snapshots, projection lag,
  replay, and correction handled?

## Calibrate findings

- Treat unrebuildable history, conflicting aggregate writes, or a projection
  used beyond its consistency contract as critical.
- Downgrade when the log is non-authoritative or versioned replay, concurrency
  control, and reconciliation are proven.

## Add to the verdict

State why the pattern is justified, append guarantees, event evolution,
projection recovery, consistency lag, and operational cost.
