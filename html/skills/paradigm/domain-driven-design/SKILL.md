---
name: gd-domain-driven-design
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review domain-driven design engineering work for bounded contexts, aggregate invariants, language drift, data ownership, integration boundaries, and unjustified ceremony."
---

# Domain-driven design GrumpyDev review

## Quick checks

- Read domain language, context maps, aggregate boundaries, invariants,
  commands, events, repositories, and integration contracts.

- Compare the proposed model with actual workflows, ownership, transaction
  boundaries, and terms used by domain experts.

Watch especially for anemic models carrying names but no invariants, aggregates
made too large for transactional convenience, bounded contexts that still share
one mutable model, domain events emitted before commitment, repositories leaking
persistence behavior, and team boundaries mistaken for domain boundaries.

- Assess a boundary that permits conflicting ownership or cannot enforce a core
  business invariant under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Domain-driven
design specialist.

## Verdict context

State the domain boundaries, protected invariants, ownership model, translation
points, and any ceremony that lacks payoff.
