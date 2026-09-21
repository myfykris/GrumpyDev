---
name: gd-winforms
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Windows Forms engineering work for control lifetime, UI-thread behavior, events, data binding, scaling, resources, asynchronous work, native interoperability, accessibility, configuration, and deployment."
---

# Windows Forms GrumpyDev review

## Quick checks

- Inspect target frameworks, forms and controls, designer files, event wiring,
  data bindings, synchronization contexts, resources, manifests, DPI settings,
  native interop, installers, and update configuration.

Watch especially for synchronous Invoke deadlocks, event subscriptions retaining
controls, async-void failures, DPI and layout assumptions baked into designer
output, resources drifting across localization, and deployment bitness that
breaks native interop.

- Inspect cross-thread corruption, inaccessible primary UI, destructive
  configuration migration, or deployment behavior that prevents safe startup or
  recovery.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Windows Forms
specialist.

- [Focused rules](references/native-interop-packaging-and-updates.md):
  Read when the work changes P/Invoke, COM, ActiveX,
  handles, native ownership,
  architecture, string encoding, registration, application settings migration,
  packaging, signing, install scope, repair, update, rollback, or uninstall behavior.

## Verdict context

State the control and window lifetime, UI thread, message loop, events, data
binding, scaling, resources, async work, interoperability, accessibility,
configuration, and deployment, supporting evidence, deployment or recovery
limits, and unresolved material assumptions.
