---
name: gd-winui-3
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review WinUI 3 engineering work for Windows App SDK lifecycle, XAML behavior, binding, dispatcher and asynchronous work, activation, navigation, resources, accessibility, packaging, identity, and deployment."
---

# WinUI 3 GrumpyDev review

## Quick checks

- Inspect Windows App SDK and target settings, XAML, view models, bindings,
  activation registration, windows, dispatch queues, resources, manifests,
  identity, packaging, bootstrapper, and deployment output.

Watch especially for packaged and unpackaged identity differences, activation
paths that assume one window, dispatcher access after teardown, compiled and
runtime binding differences, UWP lifecycle rules incorrectly applied to WinUI 3,
and XAML resources resolved only in one packaging mode.

- Inspect an identity or deployment mismatch that prevents launch, unsafe
  activation, inaccessible primary workflow, or state loss during ordinary
  lifecycle events.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the WinUI 3 specialist.

- [Focused rules](references/activation-identity-and-deployment.md):
  Read when the work changes launch or activation kinds,
  multiple instances, multiple
  windows, package identity, packaged versus unpackaged execution, Windows App SDK
  runtime initialization, file or protocol activation, native dependencies, signing,
  installation, update, rollback, repair, or uninstall behavior.

## Verdict context

State the Windows App SDK lifecycle, XAML, dependency properties, binding,
dispatcher and async behavior, windows, activation, navigation, resources,
accessibility, packaging, and deployment, supporting evidence, deployment or
recovery limits, and unresolved material assumptions.
