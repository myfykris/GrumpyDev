# Windows packaging, signing, updates, and recovery

Read this reference when the reviewed work directly or indirectly changes package
identity, packaged or unpackaged
execution, Store, installer, portable or managed distribution, architecture, runtime
dependencies, activation, signing, repair, uninstall, per-user or per-machine scope,
updates, locked files, migration, rollback, event logs, dumps, or offline recovery.

## Review requirements

- Choose packaged, unpackaged, installer, Store, portable, or managed
  distribution deliberately. Trace identity, capabilities, registration,
  file/protocol activation, runtime dependencies, signing, repair, uninstall,
  and per-user versus per-machine scope.

- Make updates transactional where possible and define compatibility, process
  shutdown, locked-file handling, settings/data migrations, interrupted
  installation, rollback, signing-key continuity, event logging, dumps, and
  offline recovery.

## Verify the claims

- Test every supported Windows version, edition, architecture, identity,
  privilege, and installation scope on clean machines.

- Exercise install, repair, upgrade, interrupted upgrade, rollback, uninstall,
  reboot, service recovery, activation, and multiple-user scenarios.

- Inspect manifests, package identity, capabilities, signatures, ACLs, service
  settings, dependencies, event logs, crash dumps, and recovery media or
  procedures.
