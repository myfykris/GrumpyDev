---
name: linux
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Linux plans and other engineering artifacts for process, identity, filesystem, signal, service, socket, namespace, resource-limit, packaging, dynamic-linking, desktop-session, logging, update, and recovery risks. Project applicability: behavior depends on a Linux host or desktop environment."
---

# Linux GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the implementation
language, framework, packaging, `application-security`, and deployment skills.
Every installed companion that remains applicable to the project participates;
the reviewed target does not select the roster. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Lean review

- Inspect distribution and kernel targets, architecture and libc, packages,
  service units, users and groups, capabilities, filesystem layout, permissions,
  sockets, namespaces, limits, security modules, logs, crash handling, and
  update scripts.

- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.

Watch especially for mode bits confused with effective capabilities or ACLs,
service-manager environments differing from shells, signals not reaching the
real process, atomic filesystem behavior assumed across mounts, temporary-file
or symlink races, and one distribution or libc standing in for every target.

Lean mode is insufficient when this material severity condition may apply:

- Treat privilege escalation, data corruption, an unrecoverable update, or
  platform assumptions that prevent startup across supported systems as critical
  or high according to blast radius and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/services-processes-and-resource-limits.md):
  Read when the reviewed work directly or indirectly changes services, init or
  service-manager behavior, users or
  groups, capabilities, signals, process groups, child reaping, watchdogs, restart
  policy, sockets, namespaces, cgroups, CPU, memory, descriptors, ports, or other
  process limits.
- [Focused rules](references/packaging-updates-and-recovery.md):
  Read when the reviewed work directly or indirectly changes distributions, libc,
  architecture, dynamic linking, package
  formats, runtime libraries, plugins, locales, certificates, service definitions,
  installation, upgrade, rollback, logging, crash dumps, backup, rescue access, or host
  recovery.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
processes, users and capabilities, filesystems, permissions, signals, services,
sockets, namespaces, limits, packaging, dynamic linking, desktop sessions,
logging, updates, and recovery, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
