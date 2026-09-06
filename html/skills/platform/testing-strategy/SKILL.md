---
name: testing-strategy
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review testing engineering work for risk coverage, realistic boundaries, determinism, fixtures, contract evidence, failure paths, mutation resistance, and maintenance cost."
---

# Testing strategy GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the relevant
language, framework, storage, and platform skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
