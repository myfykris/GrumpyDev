# Event sourcing and CQRS survey contribution

## Applies when

Apply this contribution when events are the source of truth or reads and writes use
distinct models.

## Inspect

- Read command handlers, write and read models, authoritative storage, and any
  synchronization between stores. Determine whether events are authoritative
  before inspecting event logs, replay, or snapshots.

## Ask when unresolved

- Does the project use CQRS, event sourcing, or both? CQRS alone does not require
  an event log or separate databases.

- What enforces command invariants and retry safety, and how current must reads
  be? If models use separate stores, how are they synchronized and repaired?

- If events are authoritative, which store and event versions must remain
  readable, and how are replay, correction, and deletion handled? Ask about
  snapshots only if used or proposed.

- Which storage, runtime, backup, restore, or deployment constraints affect
  these guarantees? Include replay environments only for event-sourced state.

## Record

Map accepted Event sourcing and CQRS architecture choices to `Accepted
decisions`, binding boundaries to `Requirements` or `Constraints`, and material
gaps to `Unknowns`.
