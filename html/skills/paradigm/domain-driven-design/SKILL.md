---
name: domain-driven-design
description: Review domain-driven design plans for bounded contexts, aggregate invariants, language drift, data ownership, integration boundaries, and unjustified ceremony. Use when a plan models a complex business domain with DDD concepts.
---

# Domain-driven design plan review

Apply this guidance alongside the core GrumpyDev review and the applicable
installed architecture and storage specialists for the proposed boundaries.

## Inspect evidence

- Read domain language, context maps, aggregate boundaries, invariants,
  commands, events, repositories, and integration contracts.
- Compare the proposed model with actual workflows, ownership, transaction
  boundaries, and terms used by domain experts.

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

## Challenge the plan

### Recurring traps

Watch especially for anemic models carrying names but no invariants, aggregates
made too large for transactional convenience, bounded contexts that still share
one mutable model, domain events emitted before commitment, repositories leaking
persistence behavior, and team boundaries mistaken for domain boundaries.

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

- Treat a boundary that permits conflicting ownership or cannot enforce a core
  business invariant as critical.
- Downgrade when the distinction is organizational only or domain evidence,
  ownership, and translation rules are explicit.

## Add to the verdict

State the domain boundaries, protected invariants, ownership model, translation
points, and any ceremony that lacks payoff.
