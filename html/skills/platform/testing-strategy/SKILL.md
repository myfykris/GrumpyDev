---
name: testing-strategy
description: Review testing plans for risk coverage, realistic boundaries, determinism, fixtures, contract evidence, failure paths, mutation resistance, and maintenance cost. Use when a plan adds or changes automated test strategy or relies on tests as implementation evidence.
---

# Testing strategy plan review

Apply this guidance alongside the core GrumpyDev review and the relevant
language, framework, storage, and platform skills.

## Inspect evidence

- Read risk claims, test layers, fixtures, fakes, mocks, property tests,
  integration environments, contract tests, failure injection, and CI results.
- Map each high-cost failure mode to the cheapest test that exercises the real
  boundary capable of causing it.

## Establish the operating model

Establish the project target: Test frameworks, CI environments, supported
platforms, fixture and data policy, external dependency strategy, coverage
expectations, performance tests, and ownership. The changed boundary must
define: Risk model, test boundaries, determinism, fixtures, contracts, property
tests, concurrency, failure injection, coverage meaning, environments, and
maintenance.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Risk model, test boundaries, determinism, fixtures,
contracts, property tests. Prove concurrency, failure injection, coverage
meaning, environments, maintenance through rotation, overload, partial rollout,
drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for mock-only confidence, retries disguising flaky behavior,
assertions that prove execution but not outcome, shared state making order
matter, nondeterministic time or concurrency, coverage used as a quality proxy,
and no test exercising failure, rollback, or recovery.

- Test observable behavior and invariants; line coverage and mock call counts
  are not correctness.
- Keep unit tests fast, but cross real parsers, databases, protocols,
  serializers, clocks, and concurrency boundaries where semantics matter.
- Control time, randomness, scheduling, locale, timezone, encoding, filesystem,
  and network assumptions without hiding race conditions.
- Make fixtures minimal and legible, isolate test data, and prove failures
  cannot leak state into later tests.
- Require negative, recovery, migration, compatibility, and property-based cases
  for the risks happy-path examples miss.
- For security-sensitive changes, build denied-case matrices across anonymous,
  low-privilege, cross-tenant, stale-role, object, property, function, and state
  boundaries. Prove denial through the real parser, policy, and data or effect
  boundary rather than a mocked helper alone.
- Fuzz or generate cases for exposed parsers, encodings, path handling,
  archives, uploads, protocol frames, deserialization, query builders, and
  resource limits where malformed or adversarial structure can change safety.
- Test that exceptional paths fail closed: dependency errors, timeouts, partial
  commits, malformed upstream data, alert failure, revoked credentials, and
  resource exhaustion must preserve authorization and data invariants.

## Verify the claims

- Verify these behaviors through the effective Testing strategy configuration
  and runtime topology: Risk model, test boundaries, determinism, fixtures,
  contracts, property tests. Use effective rendered configuration and deployable
  artifacts in a representative identity, topology, capacity, and policy
  boundary.
- Exercise failure and edge behavior for: concurrency, failure injection,
  coverage meaning, environments, maintenance. Exercise startup, readiness,
  normal load, overload, dependency loss, rotation, graceful drain, forced stop,
  failover, and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which concrete failure risks must the tests detect, and at which boundary can
  each be observed reliably?
- How are fixtures, time, randomness, concurrency, external systems, and failure
  injection made representative and deterministic?

## Calibrate findings

- Treat missing evidence for a high-impact irreversible path or tests that
  cannot fail when behavior regresses as critical.
- Downgrade when lower layers or existing contract evidence already cover the
  risk with stable, representative assertions.

## Add to the verdict

State risk-to-test coverage, denied authorization and hostile-input coverage,
which boundaries are real, determinism controls, missing exceptional paths, and
confidence supported by evidence.
