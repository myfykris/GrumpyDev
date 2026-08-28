# Functional programming survey contribution

## Applicability

Apply this contribution when the project architecture or correctness materially depends
on functional programming concepts or language features.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Functional programming, inspect architecture records, module or service
maps, dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Language and effect libraries, purity boundaries,
  runtime evaluation model, error conventions, state and I/O adapters, and team
  constraints that affect the design.
- Review doctrine for: Effects, purity boundaries, immutability, algebraic data,
  error modeling, recursion, laziness, resource safety, concurrency, and
  interoperability.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Conditional deployment boundary: Ask only when evaluation strategy, parallel
  runtime, process model, or resource limits materially affect correctness or
  performance.

## Ask only when materially unresolved

- Where do effects, mutable state, failure, cancellation, and resource lifetime
  enter the proposed functional boundary?
- Which evaluation, recursion, allocation, or parallelism assumptions affect
  correctness or scale?
- Do not add a standing infrastructure question for this specialist. Ask only
  when evaluation strategy, parallel runtime, process model, or resource limits
  materially affect correctness or performance.

## Record in .grump

Record Functional programming answers in project architecture, data ownership,
integration, deployment, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

If the Functional programming boundary becomes material, record it on the
affected `DEP-###` profile or referenced `INF-###` component. Preserve separate
state, support, ownership, confidence, source, and scope fields. Otherwise add
no infrastructure doctrine for this contribution.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Functional programming
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Functional programming when business invariants, ownership boundaries,
data authority, module or service map, integration model, deployment units,
consistency requirements, or operational responsibility materially change, when
evidence conflicts with saved doctrine, or when the user requests a context
refresh.
