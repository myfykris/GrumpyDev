---
name: gd-windows
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Windows engineering work for process, service, identity, ACL, registry, filesystem, COM and WinRT, application identity, packaging, activation, architecture, update, logging, crash, and recovery risks."
---

# Windows GrumpyDev review

## Quick checks

- Inspect supported Windows versions and architectures, manifests, services,
  users and service accounts, ACLs, registry use, files, COM/WinRT registration,
  package identity, installers, signatures, updates, event logs, dumps, and
  recovery runbooks.

Watch especially for ACLs evaluated under the wrong identity, path normalization
and case assumptions, services interacting with an absent desktop session,
registry-view differences by architecture, UAC virtualization hiding writes, COM
apartment violations, and installers unable to recover from partial updates.

- Inspect privilege escalation, arbitrary code loading, cross-user data exposure,
  destructive update, or platform/identity assumptions that prevent recovery.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Windows specialist.

- [Focused rules](references/services-com-and-process-identity.md):
  Read when the work changes Windows services, service
  accounts, tokens, impersonation,
  privileges, sessions, job objects, child processes, UAC, COM, WinRT, apartment models,
  marshaling, registration, process boundaries, service recovery, or shutdown.
- [Focused rules](references/packaging-signing-updates-and-recovery.md):
  Read when the work changes package identity, packaged
  or unpackaged execution, Store,
  installer, portable or managed distribution, architecture, runtime dependencies,
  activation, signing, repair, uninstall, per-user or per-machine scope, updates, locked
  files, migration, rollback, event logs, dumps, or offline recovery.

## Verdict context

State the processes, services, identity, ACLs, registry, filesystems, COM and
WinRT, application identity, packaging, activation, architecture, updates,
logging, crash handling, and recovery, supporting evidence, deployment or
recovery limits, and unresolved material assumptions.
