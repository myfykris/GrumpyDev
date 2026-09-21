# CI/CD survey contribution

## Applies when

Apply this contribution when the project uses automation to build, test, release,
promote, or deploy software.

## Inspect

- Read workflow definitions, triggers, permissions, runners, caches, artifacts,
  environments, gates, deployment strategy, and rollback procedures.

## Ask when unresolved

- Which triggers can run untrusted changes, and which credentials or protected
  environments can those runs reach?

- Is one verified artifact promoted across environments, and what restores
  service after a failed release?

- Which runtime or deployment differences are material for future reviews:
  Runner location and trust, identities, environments, artifact flow, caches,
  approvals, concurrency, secret boundaries, deployment method, rollback, and
  ownership?

## Record

Map durable CI/CD requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
