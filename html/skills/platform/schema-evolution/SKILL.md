---
name: schema-evolution
description: Review schema-evolution plans for compatibility, sequencing, backfills, mixed versions, defaults, validation, rollback, and data repair. Use when a plan changes persistent, message, API, file, or configuration schemas.
---

# Schema evolution plan review

Apply this guidance alongside the core GrumpyDev review and the applicable
installed storage, API-contract, or `event-driven-architecture` skill.

## Inspect evidence

- Read old and new schemas, serializers, validators, migrations, consumers,
  deployment order, backfills, compatibility tests, and repair tooling.
- Trace old data through new code and new data through old code during deploy,
  rollback, replay, replication, and delayed processing.

## Establish the operating model

Establish the project target: Schema systems and registries, compatibility
policy, owners, deployment overlap, retention and replay, code generation,
migration tooling, and deprecation windows. The changed boundary must define:
Compatibility modes, producer and consumer overlap, defaults, unknown fields,
migrations, backfills, dual reads or writes, contracts, rollout, and rollback.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Compatibility modes, producer and consumer overlap,
defaults, unknown fields, migrations. Prove backfills, dual reads or writes,
contracts, rollout, rollback through rotation, overload, partial rollout, drain,
forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for destructive changes combined into one deployment, backfills
holding locks or exhausting capacity, old and new code unable to coexist,
defaults rewriting large tables, renames implemented as delete-and-add, rollback
requiring discarded data, and schema validation that ignores stored history.

- Classify reader and writer compatibility explicitly; "optional" fields still
  have default, null, and semantic consequences.
- Use expand, migrate, contract sequencing when independent components or stored
  data cannot change atomically.
- Bound backfill duration, write amplification, lock risk, throttling, retries,
  and correctness checks on production-sized data.
- Preserve stable identifiers, numeric precision, timestamps, enums, unknown
  fields, and encoding across every serializer boundary.
- Define rollback when irreversible data has already been written and provide
  reconciliation plus manual repair for partial completion.

## Verify the claims

- Verify these behaviors through the effective Schema evolution configuration
  and runtime topology: Compatibility modes, producer and consumer overlap,
  defaults, unknown fields, migrations. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: backfills, dual reads or writes,
  contracts, rollout, rollback. Exercise startup, readiness, normal load,
  overload, dependency loss, rotation, graceful drain, forced stop, failover,
  and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which readers and writers overlap, and which old data or messages can reappear
  during rollout, retry, or replay?
- What transform, backfill, validation, rollback, and repair behavior applies to
  irreversible fields?

## Calibrate findings

- Treat unreadable retained data, incompatible mixed versions, or irreversible
  transformation without recovery as critical.
- Downgrade when the schema is ephemeral or compatibility, backfill, and repair
  are proven across the full overlap window.

## Add to the verdict

State compatibility mode, deployment sequence, mixed-version behavior, backfill
controls, encoding contract, and repair evidence.
