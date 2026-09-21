# Linux full-review guidance

## Operating conditions

Establish the project target: Distributions and versions, architectures, libc,
init and service manager, package format, filesystem and security modules,
desktop environment when applicable, and deployment targets. The changed
boundary must define: Processes, users and capabilities, filesystems,
permissions, signals, services, sockets, namespaces, limits, packaging, dynamic
linking, desktop sessions, logging, updates, and recovery.

## Failure patterns

- Validate filesystem types and mount options, case sensitivity, atomic rename
  scope, durability, symlinks, temporary files, permissions, ACLs, quotas,
  read-only roots, network filesystems, and full-disk behavior.

## Verification to run or specify in the plan

- Build and run on each supported distribution, architecture, libc, filesystem,
  security-module, and desktop/server mode.
- Exercise low disk, inode, memory, descriptor, process, permission, DNS,
  socket, and dependency-failure conditions.
