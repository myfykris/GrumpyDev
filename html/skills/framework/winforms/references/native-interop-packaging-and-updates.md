# Windows Forms native interop, packaging, and updates

Read this reference when the reviewed work directly or indirectly changes P/Invoke, COM,
ActiveX, handles, native
ownership, architecture, string encoding, registration, application settings migration,
packaging, signing, install scope, repair, update, rollback, or uninstall behavior.

## Review requirements

- Check P/Invoke, COM, ActiveX, window handles, architecture, calling
  convention, string encoding, ownership, registration, and installer scope
  across x86, x64, and Arm64 targets.

- Keep user, machine, roaming, and application configuration separate, version
  migrations restartable, secrets out of ordinary settings, and updates
  compatible with in-use files and rollback.

## Verify the claims

- Run clean-machine installation, update, rollback, repair, uninstall, and
  per-user or per-machine scenarios.
