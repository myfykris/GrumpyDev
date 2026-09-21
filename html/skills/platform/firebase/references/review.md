# Firebase full-review guidance

## Operating conditions

Establish the project target: Firebase products and SDKs, projects per environment,
Authentication providers and tenant model, Security Rules ownership and versions, Admin SDK
boundaries, Firestore model and indexes, offline policy, functions runtime and region, Storage
layout, quotas, and deployment process.

## Failure patterns

- Prove deny-by-default rules for each collection, document, Storage path, operation, field
  constraint, and tenant boundary.
- Test every planned query against rules and indexes; reject assumptions that unauthorized
  results will simply be filtered out.
- Define custom-claim refresh, account disable, role change, token revocation, App Check
  limits, and privileged service behavior.
- Reconcile offline conflicts, retries, transactions, listeners, local cache exposure, and data
  deletion on shared devices.
- Make Functions and trigger effects idempotent and bound regions, concurrency, cold starts,
  quotas, and downstream connections.
- Separate projects, service accounts, rules, indexes, secrets, billing alerts, backups, and
  rollback for every environment.

## Verification to run or specify in the plan

- Run emulator rule tests for allowed and denied reads, writes, queries, field changes, tenant
  crossing, and Storage access.
- Exercise offline edits, reconnect conflicts, duplicate triggers, stale claims, disabled
  accounts, quota pressure, and migrations.
- Compare emulator results with a controlled representative project for product behavior the
  emulator does not reproduce.
