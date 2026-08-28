# Linux standard review

## Inspect additional evidence

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

Identify the supported distributions and architectures, package and dynamic
library sources, service manager, process identity and capabilities, filesystem
and socket ownership, namespaces, limits, logging, update path, and recovery
owner. Prove installation and service behavior on the supported targets under
ordinary privileges, missing dependencies, signal-driven shutdown, resource
exhaustion, restart, and package rollback.

## Challenge the reviewed work

### Recurring traps

- Validate filesystem types and mount options, case sensitivity, atomic rename
  scope, durability, symlinks, temporary files, permissions, ACLs, quotas,
  read-only roots, network filesystems, and full-disk behavior.
## Verify the claims

- Build and run on each supported distribution, architecture, libc, filesystem,
  security-module, and desktop/server mode.
- Exercise low disk, inode, memory, descriptor, process, permission, DNS,
  socket, and dependency-failure conditions.
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

- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the reviewed work depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
