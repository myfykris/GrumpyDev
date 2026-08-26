# Microservices survey contribution

## Applicability

Apply this contribution when a system is split into independently deployed
network services. Skip it when Microservices does not constrain a supported
build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Microservices, inspect architecture records, module or service maps,
dependency rules, schemas and contracts, enforcement tests, deployment
definitions, ownership documents, service objectives, and recovery runbooks.
Read existing `.grump` doctrine and project documentation before treating a
durable fact as unresolved.

## Durable project facts

- Target and operating model: Service and team ownership, data stores,
  protocols, deployment units, consistency expectations, platform capabilities,
  SLOs, and incident ownership.
- Review doctrine for: Service boundaries, ownership, data separation,
  contracts, partial failure, deployment independence, observability,
  versioning, testing, and operational cost.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Service placement, discovery, network, ingress,
  identity, data ownership, regions, service mesh, deployment independence,
  observability, and incident ownership.

## Ask only when materially unresolved

- What independent ownership, scaling, deployment, or failure requirement
  justifies each service boundary?
- How are data ownership, cross-service workflows, compatibility, observability,
  and operator recovery handled?
- Align existing domain questions with this deployment guidance when it is
  material: Service placement, discovery, network, ingress, identity, data
  ownership, regions, service mesh, deployment independence, observability, and
  incident ownership. Do not repeat the core profile confirmation.

## Record in .grump

Record Microservices answers in project architecture, data ownership,
integration, deployment, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Map existing Microservices survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep unaccepted proposed boundaries, temporary team assignments, one incident
snapshot, and plan-only design choices out of durable Microservices doctrine. Do
not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Microservices when business invariants, ownership boundaries, data
authority, module or service map, integration model, deployment units,
consistency requirements, or operational responsibility materially change, when
evidence conflicts with saved doctrine, or when the user requests a context
refresh.
