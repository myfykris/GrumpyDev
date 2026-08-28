# Node.js filesystem, child processes, and workers

Read this reference when the reviewed work directly or indirectly changes paths,
permissions, symlinks, temporary files,
durability, file descriptors, child processes, shell use, process arguments, stdio,
worker threads, shared memory, message transfer, restart, or orphan prevention.

## Review requirements

- Validate paths, permissions, symlinks, temporary files, atomicity, durability,
  file descriptor lifetime, child-process arguments, shell use, environment,
  stdio, exit, and cross-platform signal differences.

- For worker threads and child processes, define ownership, message
  serialization or transfer, shared memory synchronization, startup failure,
  health, restart, capacity, shutdown, and orphan prevention.
