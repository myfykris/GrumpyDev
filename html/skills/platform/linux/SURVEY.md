# Linux survey contribution

## Applies when

Apply this contribution when the project uses Linux or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect distribution and kernel targets, architecture and libc, packages,
  service units, users and groups, capabilities, filesystem layout, permissions,
  sockets, namespaces, limits, security modules, logs, crash handling, and
  update scripts.

## Ask when unresolved

- Which of these durable facts materially change future reviews: Distributions
  and versions, architectures, libc, init and service manager, package format,
  filesystem and security modules, desktop environment when applicable, and
  deployment targets?

- Which runtime or deployment differences are material for future reviews:
  distribution, kernel, architecture, libc, service manager, user,
  capabilities, filesystem, security modules, packages, sockets, limits,
  updates, and recovery?

## Record

Map durable Linux requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
