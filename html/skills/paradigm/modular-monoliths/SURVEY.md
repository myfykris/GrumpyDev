# Modular monolith survey contribution

## Applicability

Apply this contribution when one deployable system contains intentionally
isolated business modules. Skip it when Modular monolith does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Modular monolith, inspect architecture records, module or service maps,
dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Module map and owners, allowed dependencies, data
  ownership, transaction model, enforcement tooling, deployment unit, and
  extraction intentions.
- Review doctrine for: Module boundaries, dependency direction, encapsulation,
  transactions, shared database rules, internal contracts, extraction seams,
  build enforcement, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Conditional deployment boundary: Confirm the shared deployment and database
  boundary when it affects module ownership, migrations, failure isolation, or
  a future extraction claim.

## Ask only when materially unresolved

- Which module owns each invariant and data set, and what mechanism enforces
  dependency direction?
- How do transactions, background work, migrations, tests, and future extraction
  cross module boundaries?
- Do not add a standing infrastructure question for this specialist. Confirm
  the shared deployment and database boundary when it affects module ownership,
  migrations, failure isolation, or a future extraction claim.

## Record in .grump

Record Modular monolith answers in project architecture, data ownership,
integration, deployment, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

If the Modular monolith boundary becomes material, record it on the affected
`DEP-###` profile or referenced `INF-###` component. Preserve separate state,
support, ownership, confidence, source, and scope fields. Otherwise add no
infrastructure doctrine for this contribution.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Modular monolith doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Modular monolith when business invariants, ownership boundaries, data
authority, module or service map, integration model, deployment units,
consistency requirements, or operational responsibility materially change, when
evidence conflicts with saved doctrine, or when the user requests a context
refresh.
