# Microservices survey contribution

## Applies when

Apply this contribution when a system is split into independently deployed network
services.

## Inspect

- Read service responsibilities, data stores, APIs and events, dependency graph,
  deployment units, ownership, observability, and incident history.

## Ask when unresolved

- What independent ownership, scaling, deployment, or failure requirement
  justifies each service boundary?

- How are data ownership, cross-service workflows, compatibility,
  observability, and operator recovery handled?

- Which runtime or deployment differences are material for future reviews:
  Service placement, discovery, network, ingress, identity, data ownership,
  regions, service mesh, deployment independence, observability, and incident
  ownership?

## Record

Map accepted Microservices architecture choices to `Accepted decisions`,
binding boundaries to `Requirements` or `Constraints`, and material gaps to
`Unknowns`.
