# WinUI 3 activation, identity, and deployment

Read this reference when the reviewed work directly or indirectly changes launch or
activation kinds, multiple
instances, multiple windows, package identity, packaged versus unpackaged execution,
Windows App SDK runtime initialization, file or protocol activation, native
dependencies, signing, installation, update, rollback, repair, or uninstall behavior.

## Review requirements

- Distinguish desktop WinUI lifecycle from UWP assumptions. Define launch,
  activation, multiple instances, multiple windows, background behavior, close,
  unexpected termination, and state persistence without relying on automatic
  suspension callbacks.

- Choose packaged, packaged-with-external-location, or unpackaged deployment
  deliberately. Trace package identity, Windows App SDK runtime initialization,
  dependencies, file and protocol activation, storage APIs, updates, and
  uninstall semantics for that exact model.

- Define activation routing and single- or multi-instance behavior for launch,
  files, protocols, notifications, and command-line input. Validate and
  authorize activation payloads before navigation or side effects.

- Verify architecture-specific native dependencies, runtime packaging, signing,
  installer behavior, updates, repair, rollback, and compatibility with the
  declared Windows minimum.

## Verify the claims

- Test packaged and unpackaged assumptions on clean machines without development
  runtimes.

- Inspect produced package identity, manifest, architecture payloads, runtime
  dependencies, signatures, update, rollback, and uninstall behavior.
