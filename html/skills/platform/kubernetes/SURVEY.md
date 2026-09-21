# Kubernetes survey contribution

## Applies when

Apply this contribution when the project deploys workloads to Kubernetes or depends on
Kubernetes-specific behavior in development, testing, or operations.

## Inspect

- Inspect rendered objects, admission effects, controllers, field ownership,
  cluster versions, workload type, identity, networking, volumes, probes,
  resources, scaling, disruption, and termination.

## Ask when unresolved

- Which durable cluster versions, render and apply authority, tenancy, workload
  identity, ingress and network-policy implementation, shutdown, capacity,
  stateful recovery, or emergency-access facts govern the project?

- Which runtime or deployment differences are material for future reviews:
  cluster, provider, versions, nodes, namespaces, controllers, ingress,
  identity, network policy, storage, resources, scaling, rollout, drain, and
  failure-domain coverage?

## Record

Map durable Kubernetes requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
