---
name: gd-appkit
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review AppKit engineering work for application and window lifecycle, responder routing, controllers, bindings, drawing, threading, accessibility, sandboxing, state restoration, and termination risks."
---

# AppKit GrumpyDev review

## Quick checks

- Inspect application delegates, scene or window controllers, responders, menus,
  bindings, document controllers, view code, drawing layers, concurrency
  boundaries, entitlements, and distribution settings.

Watch especially for responder-chain behavior that hides mutations, bindings or
observers that outlive their owners, AppKit access off the main thread,
persistence deferred until a termination callback that may never run, and stale
security-scoped file access.

- Inspect user-data loss, an unsandboxed privilege boundary, an inaccessible core
  workflow, or lifecycle behavior that makes recovery impossible.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the AppKit specialist.

- [Focused rules](references/documents-and-state-restoration.md):
  Read when the work changes document architecture,
  opening, autosave, undo, conflict
  handling, coordinated access, state restoration, close behavior, or document recovery.
- [Focused rules](references/sandbox-entitlements-and-file-access.md):
  Read when the work changes sandboxing, entitlements,
  privacy permissions, security-scoped URLs, helper access, filesystem access,
  automation, hardware access, or denied
  permission behavior.

## Verdict context

State the application and window lifecycle, responder chain, controllers,
bindings, document architecture, drawing, concurrency, accessibility, state
restoration, SwiftUI interoperability, sandboxing, and termination, supporting
evidence, deployment or recovery limits, and unresolved material assumptions.
