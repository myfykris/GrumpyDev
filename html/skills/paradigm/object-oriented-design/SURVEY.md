# Object-oriented design survey contribution

## Applicability

Apply this contribution when objects and collaborating types are the primary structure
of a design. Skip it when Object-oriented design does not constrain a supported build,
runtime, client, data, deployment, or operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Object-oriented design, inspect architecture records, module or service
maps, dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Domain object conventions, framework lifecycle
  constraints, mutability policy, dependency injection approach, persistence
  mapping, and accepted inheritance or composition rules.
- Review doctrine for: Identity, state and invariants, composition, inheritance,
  substitutability, encapsulation, mutation, lifecycle, dependency direction,
  and test seams.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Conditional deployment boundary: No standing infrastructure question. Ask
  only when object identity, serialization, remote proxies, plugin loading, or
  lifecycle crosses a process or deployment boundary.

## Ask only when materially unresolved

- Which object owns each invariant, mutable resource, and lifecycle transition?
- Which substitution, identity, concurrency, persistence, or failure assumptions
  must callers respect?
- Do not add a standing infrastructure question for this specialist. Ask only
  when object identity, serialization, remote proxies, plugin loading, or
  lifecycle crosses a process or deployment boundary.

## Record in .grump

Record Object-oriented design answers in project architecture, data ownership,
integration, deployment, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

If the Object-oriented design boundary becomes material, record it on the
affected `DEP-###` profile or referenced `INF-###` component. Preserve separate
state, support, ownership, confidence, source, and scope fields. Otherwise add
no infrastructure doctrine for this contribution.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Object-oriented design
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Object-oriented design when business invariants, ownership boundaries,
data authority, module or service map, integration model, deployment units,
consistency requirements, or operational responsibility materially change, when
evidence conflicts with saved doctrine, or when the user requests a context
refresh.
