# Schema evolution survey contribution

## Applies when

Apply this contribution when the project has persistent, message, API, file, or
configuration schemas that can evolve.

## Inspect

- Read old and new schemas, serializers, validators, migrations, consumers,
  deployment order, backfills, compatibility tests, and repair tooling.

## Ask when unresolved

- Which readers and writers overlap, and which old data or messages can
  reappear during rollout, retry, or replay?

- What transform, backfill, validation, rollback, and repair behavior applies
  to irreversible fields?

- Which runtime or deployment differences materially change future reviews:
  Migration runner, database topology, application replicas, old and new
  version overlap, lock and resource limits, backfill workers, rollout order,
  and rollback authority?

## Record

Map durable Schema evolution requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
