# Schema evolution full-review guidance

## Operating conditions

Establish the project target: Schema systems and registries, compatibility
policy, owners, deployment overlap, retention and replay, code generation,
migration tooling, and deprecation windows. The changed boundary must define:
Compatibility modes, producer and consumer overlap, defaults, unknown fields,
migrations, backfills, dual reads or writes, contracts, rollout, and rollback.

## Failure patterns

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

## Verification to run or specify in the plan

- Run every supported old-new producer and consumer combination against old,
  partially migrated, new and replayed data or messages. Verify unknown fields,
  defaults, nullability and semantic meaning.
- Interrupt and resume backfills, duplicate or reorder events, fail dual writes,
  and validate counts, checks and repair procedures at production-shaped scale.
- Roll forward and roll back application and schema versions at each stage,
  proving the documented rollback boundary before any irreversible step.
