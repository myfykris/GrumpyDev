# Firebase standard review

## Inspect additional evidence

- Map data models, queries, transactions, offline persistence, last-write-wins behavior,
  listeners, indexes, and migrations.
- Inspect Storage paths, callable and HTTP functions, triggers, retries, regions, quotas,
  billing, logs, and environment separation.

## Establish the operating model

Establish the project target: Firebase products and SDKs, projects per environment,
Authentication providers and tenant model, Security Rules ownership and versions, Admin SDK
boundaries, Firestore model and indexes, offline policy, functions runtime and region, Storage
layout, quotas, and deployment process.

Client SDK calls are authorized by deployed Security Rules, while trusted Admin SDK code
bypasses those rules. Query rules are not post-query filters, so planned queries must satisfy
their authorization constraints.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Run emulator rule tests for allowed and denied reads, writes, queries, field changes, tenant
  crossing, and Storage access.
- Exercise offline edits, reconnect conflicts, duplicate triggers, stale claims, disabled
  accounts, quota pressure, and migrations.
- Compare emulator results with a controlled representative project for product behavior the
  emulator does not reproduce.

## Ask when evidence is missing

- Which Firebase products, SDKs, projects, identity providers, tenant model, rules, and Admin
  SDK boundaries apply?
- How are queries, indexes, offline conflicts, functions retries, Storage, quotas, backups,
  deployment, and rollback handled?

## Calibrate findings

- Downgrade when rules, queries, offline behavior, privileged paths, retries, quotas, and
  project separation are tested.
