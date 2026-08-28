# Linux services, processes, and resource limits

Read this reference when the reviewed work directly or indirectly changes services, init
or service-manager behavior,
users or groups, capabilities, signals, process groups, child reaping, watchdogs,
restart policy, sockets, namespaces, cgroups, CPU, memory, descriptors, ports, or other
process limits.

## Review requirements

- Define process ownership, user/group identity, supplementary groups,
  capabilities, ambient authority, umask, working directory, environment,
  file-descriptor inheritance, and privilege transitions.

- Trace service readiness, dependencies, ordering, restart policy, watchdog,
  signals, process groups, child reaping, daemonization assumptions, graceful
  stop, and state after repeated crash loops.

- Budget CPU, memory, swap, file descriptors, processes, threads, sockets,
  ephemeral ports, disk, inodes, and cgroup or service limits. A host with free
  resources can still reject a process at its configured limit.

- Check socket activation, Unix socket ownership, address binding, namespaces,
  firewall rules, DNS, resolver behavior, proxy settings, and forwarded identity
  across host and container boundaries.
