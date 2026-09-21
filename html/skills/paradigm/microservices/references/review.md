# Microservices full-review guidance

## Operating conditions

Establish the project target: Service and team ownership, data stores,
protocols, deployment units, consistency expectations, platform capabilities,
SLOs, and incident ownership. The changed boundary must define: Service
boundaries, ownership, data separation, contracts, partial failure, deployment
independence, observability, versioning, testing, and operational cost.

## Failure patterns

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

## Verification to run or specify in the plan

- Deploy or roll back one changed service while its consumers remain on
  supported older versions. Verify the contract and data ownership do not
  require coordinated releases or direct writes to another service's storage.
- Delay or lose responses after remote effects succeed. Check retry identity,
  compensation, and reconciliation, and verify an operator can trace the
  business operation across services.
