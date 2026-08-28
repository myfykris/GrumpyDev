# AppKit sandbox, entitlements, and file access

Read this reference when the reviewed work directly or indirectly changes sandboxing,
entitlements, privacy permissions,
security-scoped URLs, helper access, filesystem access, automation, hardware access, or
denied permission behavior.

## Review requirements

- Match sandbox entitlements and privacy purpose strings to actual file,
  network, hardware, automation, and helper access. More entitlement is not a
  substitute for a coherent access workflow.

## Verify the claims

- Test sandboxed file selection, persistent security-scoped access, helpers,
  entitlements, and denied permissions.
