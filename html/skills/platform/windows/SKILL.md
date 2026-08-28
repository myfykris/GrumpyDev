---
name: windows
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Windows plans and other engineering artifacts for process, service, identity, ACL, registry, filesystem, COM and WinRT, application identity, packaging, activation, architecture, update, logging, crash, and recovery risks. Project applicability: software depends on Windows desktop or server behavior."
---

# Windows GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the implementation
language, UI framework, `application-security`, packaging, and deployment
skills. Every installed companion that remains applicable to the project
participates; the reviewed target does not select the roster. Verify
behavior against the project's declared targets; do not silently substitute the
newest version, a development default, or a neighboring product's semantics.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Inspect supported Windows versions and architectures, manifests, services,
  users and service accounts, ACLs, registry use, files, COM/WinRT registration,
  package identity, installers, signatures, updates, event logs, dumps, and
  recovery runbooks.

- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.

Watch especially for ACLs evaluated under the wrong identity, path normalization
and case assumptions, services interacting with an absent desktop session,
registry-view differences by architecture, UAC virtualization hiding writes, COM
apartment violations, and installers unable to recover from partial updates.

Lean mode is insufficient when this material severity condition may apply:

- Treat privilege escalation, arbitrary code loading, cross-user data exposure,
  destructive update, or platform/identity assumptions that prevent recovery as
  critical or high according to blast radius and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/services-com-and-process-identity.md):
  Read when the reviewed work directly or indirectly changes Windows services, service
  accounts, tokens, impersonation,
  privileges, sessions, job objects, child processes, UAC, COM, WinRT, apartment models,
  marshaling, registration, process boundaries, service recovery, or shutdown.
- [Focused rules](references/packaging-signing-updates-and-recovery.md):
  Read when the reviewed work directly or indirectly changes package identity, packaged
  or unpackaged execution, Store,
  installer, portable or managed distribution, architecture, runtime dependencies,
  activation, signing, repair, uninstall, per-user or per-machine scope, updates, locked
  files, migration, rollback, event logs, dumps, or offline recovery.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
processes, services, identity, ACLs, registry, filesystems, COM and WinRT,
application identity, packaging, activation, architecture, updates, logging,
crash handling, and recovery, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
