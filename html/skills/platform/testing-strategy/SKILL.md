---
name: gd-testing-strategy
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review testing engineering work for risk coverage, realistic boundaries, determinism, fixtures, contract evidence, failure paths, mutation resistance, and maintenance cost."
---

# Testing strategy GrumpyDev review

## Quick checks

- Read risk claims, test layers, fixtures, fakes, mocks, property tests,
  integration environments, contract tests, failure injection, and CI results.

- Map each high-cost failure mode to the cheapest test that exercises the real
  boundary capable of causing it.

Watch especially for mock-only confidence, retries disguising flaky behavior,
assertions that prove execution but not outcome, shared state making order
matter, nondeterministic time or concurrency, coverage used as a quality proxy,
and no test exercising failure, rollback, or recovery.

- Assess missing evidence for a high-impact irreversible path or tests that
  cannot fail when behavior regresses under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Testing strategy
specialist.

## Verdict context

State risk-to-test coverage, denied authorization and hostile-input coverage,
which boundaries are real, determinism controls, missing exceptional paths, and
confidence supported by evidence.
