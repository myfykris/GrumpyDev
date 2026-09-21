# Testing strategy survey contribution

## Applies when

Apply this contribution when the project relies on automated tests as implementation
evidence or has material test-strategy decisions.

## Inspect

- Read risk claims, test layers, fixtures, fakes, mocks, property tests,
  integration environments, contract tests, failure injection, and CI results.

## Ask when unresolved

- Which concrete failure risks must the tests detect, and at which boundary can
  each be observed reliably?

- How are fixtures, time, randomness, concurrency, external systems, and
  failure injection made representative and deterministic?

- Which runtime or deployment differences materially change future reviews:
  Test environment parity, service substitutes, architecture and browser
  matrix, network and failure simulation, data isolation, resources, CI
  runners, and production-only gaps?

## Record

Map durable Testing strategy requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
