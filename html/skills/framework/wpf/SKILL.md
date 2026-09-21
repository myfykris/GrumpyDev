---
name: gd-wpf
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review WPF engineering work for application and dispatcher lifecycle, dependency properties, binding, resources, commands, threading, rendering, DPI, accessibility, interoperability, and deployment."
---

# WPF GrumpyDev review

## Quick checks

- Inspect target frameworks, XAML, dependency properties, bindings, resources,
  styles, templates, commands, dispatchers, windows, native interop, manifests,
  packaging, and deployment configuration.

Watch especially for silent binding failures, inherited DataContext changing
unexpectedly, dispatcher deadlocks, dependency-property metadata with unintended
scope, dynamic-resource lookup differences, virtualization disabled by
templates, and async-void command failures.

- Inspect persistent state loss, cross-thread corruption, inaccessible core
  interaction, or a packaging/update failure that prevents safe recovery.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the WPF specialist.

- [Focused rules](references/native-interop-packaging-and-updates.md):
  Read when the work changes P/Invoke, COM, HWND
  hosting, native callbacks,
  architecture, trimming, deployment mode, runtime dependencies, signing, installers,
  settings migration, update, rollback, repair, or uninstall behavior.

## Verdict context

State the application and dispatcher lifecycle, dependency properties, binding,
resources, templates, commands, threading, async behavior, rendering, DPI,
accessibility, interoperability, and deployment, supporting evidence,
deployment or recovery limits, and unresolved material assumptions.
