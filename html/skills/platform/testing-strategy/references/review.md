# Testing strategy full-review guidance

## Operating conditions

Establish the project target: Test frameworks, CI environments, supported
platforms, fixture and data policy, external dependency strategy, coverage
expectations, performance tests, and ownership. The changed boundary must
define: Risk model, test boundaries, determinism, fixtures, contracts, property
tests, concurrency, failure injection, coverage meaning, environments, and
maintenance.

## Failure patterns

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

## Verification to run or specify in the plan

- Demonstrate that each named risk causes a test to fail when the protected
  behavior is deliberately broken, and that the assertion observes the real
  contract rather than an implementation detail.
- Run with controlled time, randomness, locale, timezone, encoding, scheduling
  and external dependencies, then vary concurrency and inject the failures the
  design claims to survive.
- Execute the relevant suite in the actual CI environments and supported
  platforms, checking isolation, order dependence, flake rate, fixture cleanup,
  runtime and failure diagnostics.
