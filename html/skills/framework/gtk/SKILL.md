---
name: gd-gtk
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review GTK engineering work for GObject ownership, widget lifecycle, signals, main-loop and threading behavior, models, actions, resources, styling, accessibility, rendering, and GTK version compatibility."
---

# GTK GrumpyDev review

## Quick checks

- Inspect GTK and GLib versions, UI definitions, GObject types, ownership
  annotations, widget trees, signal connections, list models, actions,
  resources, CSS, main-context use, and packaging metadata.

Watch especially for incorrect GObject reference ownership, signals left
connected through teardown, main-loop blocking or off-thread widget access, GTK
3 behavior assumed under GTK 4, invalidated model positions, and theme-dependent
layout or contrast.

- Inspect use-after-free, persistent data loss, an inaccessible primary workflow,
  or a display/backend assumption that makes the application unusable.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the GTK specialist.

- [Focused rules](references/version-migration-packaging-and-display-backends.md):
  Read when the work changes GTK 3 versus GTK 4
  behavior, GLib or language-binding
  compatibility, installed resources, schemas, translations, loaders, plugins,
  packaging, X11, Wayland, headless execution, clipboard, drag and drop, input, or
  compositor behavior.

## Verdict context

State the GObject ownership, widget lifecycle, signals, main loop, threading,
list and model behavior, actions, resources, styling, accessibility, rendering,
and GTK 3 to 4 differences, supporting evidence, deployment or recovery limits,
and unresolved material assumptions.
