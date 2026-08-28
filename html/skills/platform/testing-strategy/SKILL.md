---
name: testing-strategy
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review testing plans and other engineering artifacts for risk coverage, realistic boundaries, determinism, fixtures, contract evidence, failure paths, mutation resistance, and maintenance cost. Project applicability: the project relies on automated tests as implementation evidence or has material test-strategy decisions."
---

# Testing strategy GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the relevant
language, framework, storage, and platform skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read risk claims, test layers, fixtures, fakes, mocks, property tests,
  integration environments, contract tests, failure injection, and CI results.

- Map each high-cost failure mode to the cheapest test that exercises the real
  boundary capable of causing it.

Watch especially for mock-only confidence, retries disguising flaky behavior,
assertions that prove execution but not outcome, shared state making order
matter, nondeterministic time or concurrency, coverage used as a quality proxy,
and no test exercising failure, rollback, or recovery.

Lean mode is insufficient when this material severity condition may apply:

- Treat missing evidence for a high-impact irreversible path or tests that
  cannot fail when behavior regresses as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Testing strategy evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State risk-to-test coverage, denied authorization and hostile-input coverage,
which boundaries are real, determinism controls, missing exceptional paths, and
confidence supported by evidence.
