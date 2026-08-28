# Schema evolution standard review

## Establish the operating model

Establish the project target: Schema systems and registries, compatibility
policy, owners, deployment overlap, retention and replay, code generation,
migration tooling, and deprecation windows. The changed boundary must define:
Compatibility modes, producer and consumer overlap, defaults, unknown fields,
migrations, backfills, dual reads or writes, contracts, rollout, and rollback.

Identify the schema authority, every producer and consumer, compatibility mode,
overlap window, unknown-field and default behavior, migration and backfill
owner, validation signal, rollback limit, and repair path. Prove old data,
replayed messages, old and new binaries, interrupted backfills and partial dual
reads or writes coexist without corrupting meaning or making rollback
impossible.

## Challenge the reviewed work

### Recurring traps

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

- Run every supported old-new producer and consumer combination against old,
  partially migrated, new and replayed data or messages. Verify unknown fields,
  defaults, nullability and semantic meaning.
- Interrupt and resume backfills, duplicate or reorder events, fail dual writes,
  and validate counts, checks and repair procedures at production-shaped scale.
- Roll forward and roll back application and schema versions at each stage,
  proving the documented rollback boundary before any irreversible step.

## Ask when evidence is missing

- Which readers and writers overlap, and which old data or messages can reappear
  during rollout, retry, or replay?
- What transform, backfill, validation, rollback, and repair behavior applies to
  irreversible fields?

## Calibrate findings

- Downgrade when the schema is ephemeral or compatibility, backfill, and repair
  are proven across the full overlap window.
