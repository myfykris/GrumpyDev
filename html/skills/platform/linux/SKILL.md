---
name: gd-linux
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Linux engineering work for process, identity, filesystem, signal, service, socket, namespace, resource-limit, packaging, dynamic-linking, desktop-session, logging, update, and recovery risks."
---

# Linux GrumpyDev review

## Quick checks

- Inspect distribution and kernel targets, architecture and libc, packages,
  service units, users and groups, capabilities, filesystem layout, permissions,
  sockets, namespaces, limits, security modules, logs, crash handling, and
  update scripts.

Watch especially for mode bits confused with effective capabilities or ACLs,
service-manager environments differing from shells, signals not reaching the
real process, atomic filesystem behavior assumed across mounts, temporary-file
or symlink races, and one distribution or libc standing in for every target.

- Inspect privilege escalation, data corruption, an unrecoverable update, or
  platform assumptions that prevent startup across supported systems.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Linux specialist.

- [Focused rules](references/services-processes-and-resource-limits.md):
  Read when the work changes services, init or
  service-manager behavior, users or
  groups, capabilities, signals, process groups, child reaping, watchdogs, restart
  policy, sockets, namespaces, cgroups, CPU, memory, descriptors, ports, or other
  process limits.
- [Focused rules](references/packaging-updates-and-recovery.md):
  Read when the work changes distributions, libc,
  architecture, dynamic linking, package
  formats, runtime libraries, plugins, locales, certificates, service definitions,
  installation, upgrade, rollback, logging, crash dumps, backup, rescue access, or host
  recovery.

## Verdict context

State the processes, users and capabilities, filesystems, permissions, signals,
services, sockets, namespaces, limits, packaging, dynamic linking, desktop
sessions, logging, updates, and recovery, supporting evidence, deployment or
recovery limits, and unresolved material assumptions.
