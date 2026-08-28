# Domain-driven design survey contribution

## Applicability

Apply this contribution when the project models a complex business domain with
domain-driven design concepts.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Domain-driven design, inspect architecture records, module or service maps,
dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Domain boundaries and owners, authoritative
  terminology, aggregate and transaction boundaries, integration relationships,
  decision records, and accepted context mappings.
- Review doctrine for: Bounded contexts, ubiquitous language, aggregates,
  invariants, transactions, domain events, anti-corruption layers, ownership,
  and model evolution.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Conditional deployment boundary: Ask only when bounded contexts map to
  separate processes, data stores, teams, deployments, or consistency
  boundaries. Do not add a generic hosting question.

## Ask only when materially unresolved

- Which business invariant and language define each proposed bounded context and
  aggregate boundary?
- Where do translations, ownership, transactions, and eventual consistency cross
  contexts?
- Do not add a standing infrastructure question for this specialist. Ask only
  when bounded contexts map to separate processes, data stores, teams,
  deployments, or consistency boundaries. Do not add a generic hosting
  question.

## Record in .grump

Record Domain-driven design answers in project architecture, data ownership,
integration, deployment, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

If the Domain-driven design boundary becomes material, record it on the
affected `DEP-###` profile or referenced `INF-###` component. Preserve separate
state, support, ownership, confidence, source, and scope fields. Otherwise add
no infrastructure doctrine for this contribution.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Domain-driven design
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Domain-driven design when business invariants, ownership boundaries,
data authority, module or service map, integration model, deployment units,
consistency requirements, or operational responsibility materially change, when
evidence conflicts with saved doctrine, or when the user requests a context
refresh.
