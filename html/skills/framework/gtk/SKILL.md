---
name: gtk
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review GTK plans and other engineering artifacts for GObject ownership, widget lifecycle, signals, main-loop and threading behavior, models, actions, resources, styling, accessibility, rendering, and GTK version compatibility. Project applicability: the project uses or materially depends on GTK."
---

# GTK GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the applicable
language, `linux`, `application-security`, and `testing-strategy` skills. Every
installed companion that remains applicable to the project participates; the
reviewed target does not select the roster. Verify behavior against
the project's declared targets; do not silently substitute the newest version, a
development default, or a neighboring product's semantics.

## Lean review

- Inspect GTK and GLib versions, UI definitions, GObject types, ownership
  annotations, widget trees, signal connections, list models, actions,
  resources, CSS, main-context use, and packaging metadata.

- Inspect generated and rendered artifacts in addition to source. Templates,
  designers, metadata, conventions, and lifecycle callbacks can own behavior
  that is invisible in the main code path.

Watch especially for incorrect GObject reference ownership, signals left
connected through teardown, main-loop blocking or off-thread widget access, GTK
3 behavior assumed under GTK 4, invalidated model positions, and theme-dependent
layout or contrast.

Lean mode is insufficient when this material severity condition may apply:

- Treat use-after-free, persistent data loss, an inaccessible primary workflow,
  or a display/backend assumption that makes the application unusable as
  critical or high according to blast radius and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/version-migration-packaging-and-display-backends.md):
  Read when the reviewed work directly or indirectly changes GTK 3 versus GTK 4
  behavior, GLib or language-binding
  compatibility, installed resources, schemas, translations, loaders, plugins,
  packaging, X11, Wayland, headless execution, clipboard, drag and drop, input, or
  compositor behavior.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
GObject ownership, widget lifecycle, signals, main loop, threading, list and
model behavior, actions, resources, styling, accessibility, rendering, and GTK 3
to 4 differences, verification evidence, deployment and recovery limits, and any
material assumption that remains unresolved.
