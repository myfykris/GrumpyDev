# Domain-driven design full-review guidance

## Operating conditions

Establish the project target: Domain boundaries and owners, authoritative
terminology, aggregate and transaction boundaries, integration relationships,
decision records, and accepted context mappings. The changed boundary must
define: Bounded contexts, ubiquitous language, aggregates, invariants,
transactions, domain events, anti-corruption layers, ownership, and model
evolution.

## Failure patterns

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

## Verification to run or specify in the plan

- Test business invariants through aggregate operations, including competing
  updates and failed transactions. Check that domain events cannot claim a
  state change that did not commit.
- Exercise translations between bounded contexts with values whose meanings
  differ. Verify a model change in one context does not silently alter another
  context's rules or bypass the owning aggregate.
