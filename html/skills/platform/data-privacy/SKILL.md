---
name: data-privacy
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review data-privacy plans and other engineering artifacts for purpose, minimization, consent, access, retention, deletion, export, residency, vendor flow, and incident scope. Project applicability: the project collects, derives, stores, shares, exports, retains, or deletes personal or sensitive data."
---

# Data privacy GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill, and applicable installed storage or explicitly
selected integration specialists.

## Lean review

- Read the data inventory, purposes, classifications, consent and notice, access
  paths, retention, deletion, exports, subprocessors, logs, and backups.

- Trace one person's data from collection through derivation, replication,
  analytics, support access, export, deletion, backup expiry, and incident
  response.

Watch especially for purpose creep, collecting fields without a defined use,
retention that excludes backups or derived data, identifiers leaking through
logs, consent used where another lawful basis actually governs, deletion that
cannot reach downstream copies, and cross-border processing left implicit.

Lean mode is insufficient when this material severity condition may apply:

- Treat unlawful collection, undeletable sensitive data, uncontrolled
  disclosure, or unknown vendor propagation as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Data privacy evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State data purpose and minimization, access controls, retention and deletion
coverage, external flow, incident scope, and unresolved legal review.
