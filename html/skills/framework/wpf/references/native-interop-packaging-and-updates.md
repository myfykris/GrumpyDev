# WPF native interop, packaging, and updates

Read this reference when the reviewed work directly or indirectly changes P/Invoke, COM,
HWND hosting, native callbacks,
architecture, trimming, deployment mode, runtime dependencies, signing, installers,
settings migration, update, rollback, repair, or uninstall behavior.

## Review requirements

- Verify P/Invoke, COM, HWND hosting, architecture, trimming or deployment mode,
  signing, installer, updates, settings migration, rollback, repair, and
  uninstall.

## Verify the claims

- Exercise windows, navigation, cancellation, shutdown, crash recovery, multiple
  dispatchers if used, and native callbacks.

- Install, update, roll back, repair, and uninstall on clean machines with the
  declared runtime and native dependencies.
