# Schema evolution survey contribution

## Applicability

Apply this contribution when a plan changes persistent, message, API, file, or
configuration schemas. Skip it when Schema evolution does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Schema evolution, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Schema systems and registries, compatibility
  policy, owners, deployment overlap, retention and replay, code generation,
  migration tooling, and deprecation windows.
- Review doctrine for: Compatibility modes, producer and consumer overlap,
  defaults, unknown fields, migrations, backfills, dual reads or writes,
  contracts, rollout, and rollback.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Migration runner, database topology, application
  replicas, old and new version overlap, lock and resource limits, backfill
  workers, rollout order, and rollback authority.

## Ask only when materially unresolved

- Which readers and writers overlap, and which old data or messages can reappear
  during rollout, retry, or replay?
- What transform, backfill, validation, rollback, and repair behavior applies to
  irreversible fields?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Migration runner, database topology,
  application replicas, old and new version overlap, lock and resource limits,
  backfill workers, rollout order, and rollback authority? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Schema evolution answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Schema evolution deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Schema
evolution doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Schema evolution when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
