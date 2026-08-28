---
name: domain-driven-design
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review domain-driven design plans and other engineering artifacts for bounded contexts, aggregate invariants, language drift, data ownership, integration boundaries, and unjustified ceremony. Project applicability: the project models a complex business domain with domain-driven design concepts."
---

# Domain-driven design GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed architecture and storage specialists for the proposed boundaries.

## Lean review

- Read domain language, context maps, aggregate boundaries, invariants,
  commands, events, repositories, and integration contracts.

- Compare the proposed model with actual workflows, ownership, transaction
  boundaries, and terms used by domain experts.

Watch especially for anemic models carrying names but no invariants, aggregates
made too large for transactional convenience, bounded contexts that still share
one mutable model, domain events emitted before commitment, repositories leaking
persistence behavior, and team boundaries mistaken for domain boundaries.

Lean mode is insufficient when this material severity condition may apply:

- Treat a boundary that permits conflicting ownership or cannot enforce a core
  business invariant as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Domain-driven design evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State the domain boundaries, protected invariants, ownership model, translation
points, and any ceremony that lacks payoff.
