# Microservices standard review

## Establish the operating model

Establish the project target: Service and team ownership, data stores,
protocols, deployment units, consistency expectations, platform capabilities,
SLOs, and incident ownership. The changed boundary must define: Service
boundaries, ownership, data separation, contracts, partial failure, deployment
independence, observability, versioning, testing, and operational cost.

Name the invariants, authorities, owners, and enforcement for Service
boundaries, ownership, data separation, contracts, partial failure. Prove
deployment independence, observability, versioning, testing, operational cost
under concurrency, partial failure, incompatible versions, operational response,
rollback, and repair, and justify the added complexity.

## Challenge the reviewed work

### Recurring traps

- Demand a reason each network boundary must be independently deployed; team
  charts and future scale are not enough.
- Reject shared-database ownership, lockstep releases, generated-client churn,
  and chatty call graphs that preserve monolith coupling remotely.
- Define consistency and compensation where one business operation crosses
  service-owned data.
- Account for discovery, identity, authorization, secrets, telemetry, capacity,
  on-call ownership, and local development cost per service.
- Prefer a modular monolith until evidence shows one boundary needs independent
  scale, reliability, release cadence, or ownership.

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Service boundaries, ownership, data separation, contracts, partial
  failure. Use dependency, architecture, contract, schema, or ownership tests
  that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: deployment independence,
  observability, versioning, testing, operational cost. Exercise the material
  invariant under concurrency, delay, duplication, partial failure, incompatible
  versions, rollback, and repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- What independent ownership, scaling, deployment, or failure requirement
  justifies each service boundary?
- How are data ownership, cross-service workflows, compatibility, observability,
  and operator recovery handled?

## Calibrate findings

- Downgrade when the split is already operationally mature or autonomy,
  contracts, failure handling, and ownership are proven.
