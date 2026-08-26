---
name: linux
description: Review Linux plans for process, identity, filesystem, signal, service, socket, namespace, resource-limit, packaging, dynamic-linking, desktop-session, logging, update, and recovery risks. Use when behavior depends on a Linux host or desktop environment.
---

# Linux plan review

Apply this guidance alongside the core GrumpyDev review and the implementation
language, framework, packaging, `application-security`, and deployment skills.
Select only companions that match the plan's real boundaries. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect distribution and kernel targets, architecture and libc, packages,
  service units, users and groups, capabilities, filesystem layout, permissions,
  sockets, namespaces, limits, security modules, logs, crash handling, and
  update scripts.
- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.
- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: Distributions and versions, architectures, libc,
init and service manager, package format, filesystem and security modules,
desktop environment when applicable, and deployment targets. The changed
boundary must define: Processes, users and capabilities, filesystems,
permissions, signals, services, sockets, namespaces, limits, packaging, dynamic
linking, desktop sessions, logging, updates, and recovery.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Processes, users and capabilities, filesystems,
permissions, signals, services, sockets, namespaces. Prove limits, packaging,
dynamic linking, desktop sessions, logging, updates, recovery through rotation,
overload, partial rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for mode bits confused with effective capabilities or ACLs,
service-manager environments differing from shells, signals not reaching the
real process, atomic filesystem behavior assumed across mounts, temporary-file
or symlink races, and one distribution or libc standing in for every target.

- Verify against the supported distribution, kernel, libc, architecture, init
  system, security modules, and packaging policy. "Linux" is not one ABI or
  operating contract.
- Define process ownership, user/group identity, supplementary groups,
  capabilities, ambient authority, umask, working directory, environment,
  file-descriptor inheritance, and privilege transitions.
- Trace service readiness, dependencies, ordering, restart policy, watchdog,
  signals, process groups, child reaping, daemonization assumptions, graceful
  stop, and state after repeated crash loops.
- Validate filesystem types and mount options, case sensitivity, atomic rename
  scope, durability, symlinks, temporary files, permissions, ACLs, quotas,
  read-only roots, network filesystems, and full-disk behavior.
- Budget CPU, memory, swap, file descriptors, processes, threads, sockets,
  ephemeral ports, disk, inodes, and cgroup or service limits. A host with free
  resources can still reject a process at its configured limit.
- Check socket activation, Unix socket ownership, address binding, namespaces,
  firewall rules, DNS, resolver behavior, proxy settings, and forwarded identity
  across host and container boundaries.
- Package all runtime libraries, loaders, plugins, locales, certificates,
  resources, and service definitions. Verify dynamic linkage and avoid depending
  on undeclared files from a developer machine.
- Define update, configuration migration, restart, rollback, crash dump,
  logging, rotation, time synchronization, backup, rescue access, and recovery
  behavior under partial package or disk failure.

## Verify the claims

- Build and run on each supported distribution, architecture, libc, filesystem,
  security-module, and desktop/server mode.
- Test clean installation, upgrade, interrupted upgrade, rollback, uninstall,
  reboot, service crash loop, graceful stop, and recovery.
- Exercise low disk, inode, memory, descriptor, process, permission, DNS,
  socket, and dependency-failure conditions.
- Inspect package contents, dynamic dependencies, service hardening,
  permissions, capabilities, logs, crash artifacts, and restoration procedures.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Distributions and
versions, architectures, libc, init and service manager, package format,
filesystem and security modules, desktop environment when applicable, and
deployment targets. For the changed boundary, ask only about unresolved
Processes, users and capabilities, filesystems, permissions, signals, services,
sockets, namespaces, limits, packaging, dynamic linking, desktop sessions,
logging, updates, and recovery when the answer can change the verdict or
implementation.

## Calibrate findings

- Treat privilege escalation, data corruption, an unrecoverable update, or
  platform assumptions that prevent startup across supported systems as critical
  or high according to blast radius and realistic likelihood.
- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the plan depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
processes, users and capabilities, filesystems, permissions, signals, services,
sockets, namespaces, limits, packaging, dynamic linking, desktop sessions,
logging, updates, and recovery, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
