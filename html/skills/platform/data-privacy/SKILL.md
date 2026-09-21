---
name: gd-data-privacy
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review data-privacy engineering work for purpose, minimization, consent, access, retention, deletion, export, residency, vendor flow, and incident scope."
---

# Data privacy GrumpyDev review

## Quick checks

- Read the data inventory, purposes, classifications, consent and notice, access
  paths, retention, deletion, exports, subprocessors, logs, and backups.

- Trace one person's data from collection through derivation, replication,
  analytics, support access, export, deletion, backup expiry, and incident
  response.

Watch especially for purpose creep, collecting fields without a defined use,
retention that excludes backups or derived data, identifiers leaking through
logs, consent used where another lawful basis actually governs, deletion that
cannot reach downstream copies, and cross-border processing left implicit.

- Assess unlawful collection, undeletable sensitive data, uncontrolled
  disclosure, or unknown vendor propagation under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Data privacy
specialist.

## Verdict context

State data purpose and minimization, access controls, retention and deletion
coverage, external flow, incident scope, and unresolved legal review.
