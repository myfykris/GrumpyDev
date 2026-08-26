# Testing strategy survey contribution

## Applicability

Apply this contribution when a plan adds or changes automated test strategy or
relies on tests as implementation evidence. Skip it when Testing strategy does
not constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Testing strategy, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Test frameworks, CI environments, supported
  platforms, fixture and data policy, external dependency strategy, coverage
  expectations, performance tests, and ownership.
- Review doctrine for: Risk model, test boundaries, determinism, fixtures,
  contracts, property tests, concurrency, failure injection, coverage meaning,
  environments, and maintenance.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Test environment parity, service substitutes,
  architecture and browser matrix, network and failure simulation, data
  isolation, resources, CI runners, and production-only gaps.

## Ask only when materially unresolved

- Which concrete failure risks must the tests detect, and at which boundary can
  each be observed reliably?
- How are fixtures, time, randomness, concurrency, external systems, and failure
  injection made representative and deterministic?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Test environment parity, service
  substitutes, architecture and browser matrix, network and failure simulation,
  data isolation, resources, CI runners, and production-only gaps? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Testing strategy answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Testing strategy deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Testing
strategy doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Testing strategy when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
