---
name: data-privacy
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review data-privacy engineering work for purpose, minimization, consent, access, retention, deletion, export, residency, vendor flow, and incident scope."
---

# Data privacy GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
