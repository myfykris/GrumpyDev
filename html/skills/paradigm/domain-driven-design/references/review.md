# Domain-driven design standard review

## Establish the operating model

Establish the project target: Domain boundaries and owners, authoritative
terminology, aggregate and transaction boundaries, integration relationships,
decision records, and accepted context mappings. The changed boundary must
define: Bounded contexts, ubiquitous language, aggregates, invariants,
transactions, domain events, anti-corruption layers, ownership, and model
evolution.

Name the invariants, authorities, owners, and enforcement for Bounded contexts,
ubiquitous language, aggregates, invariants, transactions. Prove domain events,
anti-corruption layers, ownership, model evolution under concurrency, partial
failure, incompatible versions, operational response, rollback, and repair, and
justify the added complexity.

## Challenge the reviewed work

### Recurring traps

- Reject entities, services, repositories, or events added only to imitate a
  pattern; require a domain problem each abstraction solves.
- Keep aggregates small enough for one consistency boundary and require the
  aggregate root to enforce real invariants.
- Check that bounded contexts follow different meanings and ownership, not team
  preferences or arbitrary folders.
- Define translations at context boundaries so one model does not silently leak
  into another.
- Distinguish domain rules from orchestration and infrastructure, then test
  rules without requiring the entire runtime.

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Bounded contexts, ubiquitous language, aggregates, invariants,
  transactions. Use dependency, architecture, contract, schema, or ownership
  tests that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: domain events, anti-corruption layers,
  ownership, model evolution. Exercise the material invariant under concurrency,
  delay, duplication, partial failure, incompatible versions, rollback, and
  repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- Which business invariant and language define each proposed bounded context and
  aggregate boundary?
- Where do translations, ownership, transactions, and eventual consistency cross
  contexts?

## Calibrate findings

- Downgrade when the distinction is organizational only or domain evidence,
  ownership, and translation rules are explicit.
