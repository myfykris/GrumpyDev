---
name: gd-powershell
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review PowerShell engineering work for object-pipeline behavior, quoting, remoting, credentials, error semantics, platform differences, idempotency, and automation safety."
---

# PowerShell GrumpyDev review

## Quick checks

- Read module manifests, required PowerShell editions and versions, parameter
  declarations, remoting setup, execution policy assumptions, and tests.

- Trace object and string conversion, native command invocation, credentials,
  temporary files, retries, partial changes, and cleanup.

Watch especially for formatted text mistaken for pipeline objects,
non-terminating errors treated as success, quoting and interpolation changes
across local and remote execution, scalar and array unrolling, remoting
serialization that strips behavior, and scope or preference variables inherited
implicitly.

- Assess command injection, credential exposure, destructive wildcard targeting,
  or ignored terminating failure under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the PowerShell
specialist.

## Verdict context

State supported hosts, error policy, mutation and rollback behavior, credential
handling, encoding assumptions, and cross-platform evidence.
