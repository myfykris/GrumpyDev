---
name: object-oriented-design
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review object-oriented design plans and other engineering artifacts for ownership, invariants, mutability, inheritance, polymorphism, dependency direction, and test seams. Project applicability: objects and collaborating types are the primary structure of a design."
---

# Object-oriented design GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed language or framework specialist for the object model in use.

## Lean review

- Read object responsibilities, constructors, state transitions, public methods,
  inheritance trees, interfaces, dependencies, and tests.

- Trace who owns mutable state, who may change it, and how invariants survive
  callbacks, exceptions, persistence, and concurrency.

Watch especially for inheritance used only for reuse, god objects, mutable
aliases crossing ownership boundaries, subtype behavior that violates caller
expectations, temporal coupling hidden behind setters, domain behavior displaced
into services, and accessors that trigger surprising I/O.

Lean mode is insufficient when this material severity condition may apply:

- Treat split ownership or polymorphism that can violate a core invariant or
  resource lifecycle as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Object-oriented design evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State object ownership, protected invariants, mutation boundaries, polymorphism
justification, dependency direction, and test evidence.
