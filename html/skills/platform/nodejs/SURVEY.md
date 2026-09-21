# Node.js survey contribution

## Applies when

Apply this contribution when the project uses Node.js or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Establish Node and package-manager versions, module mode, lock policy,
  process topology, native addons, runtime flags, operating targets, and the
  deployed artifact.

## Ask when unresolved

- Which of these durable facts materially change future reviews: Node.js
  versions, LTS policy, module mode, package manager, lock policy, worker and
  process topology, OS and architecture, native addons, runtime flags, and
  deployment form?

- Which runtime or deployment differences are material for future reviews:
  Node.js version, module mode, process and worker topology, event loop, native
  add-ons, runtime flags, proxy, filesystem, signals, packaging, and deployment
  coverage?

## Record

Map durable Node.js requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
