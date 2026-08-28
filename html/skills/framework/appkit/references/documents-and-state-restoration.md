# AppKit documents and state restoration

Read this reference when the reviewed work directly or indirectly changes document
architecture, opening, autosave,
undo, conflict handling, coordinated access, state restoration, close behavior, or
document recovery.

## Review requirements

- For document apps, prove open, autosave, conflict, coordination,
  security-scoped access, undo, close, and recovery semantics. Preserve user
  data through version changes and interrupted writes.

## Verify the claims

- Exercise cold launch, reopen, multiple windows, close during work,
  termination, crash recovery, and state restoration.
