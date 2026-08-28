---
name: powershell
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review PowerShell plans and other engineering artifacts for object-pipeline behavior, quoting, remoting, credentials, error semantics, platform differences, idempotency, and automation safety. Project applicability: the project contains, builds, deploys, operates, or interoperates with PowerShell code, artifacts, or runtime behavior."
---

# PowerShell GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
