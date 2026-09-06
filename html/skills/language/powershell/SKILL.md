---
name: powershell
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review PowerShell engineering work for object-pipeline behavior, quoting, remoting, credentials, error semantics, platform differences, idempotency, and automation safety."
---

# PowerShell GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read module manifests, required PowerShell editions and versions, parameter
  declarations, remoting setup, execution policy assumptions, and tests.

- Trace object and string conversion, native command invocation, credentials,
  temporary files, retries, partial changes, and cleanup.

Watch especially for formatted text mistaken for pipeline objects,
non-terminating errors treated as success, quoting and interpolation changes
across local and remote execution, scalar and array unrolling, remoting
serialization that strips behavior, and scope or preference variables inherited
implicitly.

Lean mode is insufficient when this material severity condition may apply:

- Treat command injection, credential exposure, destructive wildcard targeting,
  or ignored terminating failure as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete PowerShell evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State supported hosts, error policy, mutation and rollback behavior, credential
handling, encoding assumptions, and cross-platform evidence.
