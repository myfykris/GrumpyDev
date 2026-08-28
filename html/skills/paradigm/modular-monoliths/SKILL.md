---
name: modular-monoliths
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review modular-monolith plans and other engineering artifacts for enforceable boundaries, dependency direction, data ownership, transaction scope, deployment coupling, and extraction seams. Project applicability: one deployable system contains intentionally isolated business modules."
---

# Modular monolith GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed language, framework, and storage specialists for the module
boundaries.

## Lean review

- Read module APIs, dependency rules, build layout, database ownership,
  transaction boundaries, background work, and architecture tests.

- Trace calls and data access that cross modules, including shortcuts through
  shared helpers, tables, and internal types.

Watch especially for package names without enforceable boundaries, cyclic
dependencies, shared mutable tables with no owning module, framework-wide
dependency injection bypassing module APIs, global events with unclear delivery
rules, and speculative extraction driving needless indirection.

Lean mode is insufficient when this material severity condition may apply:

- Treat cyclic ownership or unenforced writes that allow modules to violate core
  invariants as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Modular monolith evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State module boundaries, enforcement mechanism, data ownership, allowed
coupling, transaction scope, and realistic extraction seams.
