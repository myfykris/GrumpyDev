# Linux packaging, updates, and recovery

Read this reference when the reviewed work directly or indirectly changes distributions,
libc, architecture, dynamic
linking, package formats, runtime libraries, plugins, locales, certificates, service
definitions, installation, upgrade, rollback, logging, crash dumps, backup, rescue
access, or host recovery.

## Review requirements

- Verify against the supported distribution, kernel, libc, architecture, init
  system, security modules, and packaging policy. "Linux" is not one ABI or
  operating contract.

- Package all runtime libraries, loaders, plugins, locales, certificates,
  resources, and service definitions. Verify dynamic linkage and avoid depending
  on undeclared files from a developer machine.

- Define update, configuration migration, restart, rollback, crash dump,
  logging, rotation, time synchronization, backup, rescue access, and recovery
  behavior under partial package or disk failure.

## Verify the claims

- Test clean installation, upgrade, interrupted upgrade, rollback, uninstall,
  reboot, service crash loop, graceful stop, and recovery.

- Inspect package contents, dynamic dependencies, service hardening,
  permissions, capabilities, logs, crash artifacts, and restoration procedures.
