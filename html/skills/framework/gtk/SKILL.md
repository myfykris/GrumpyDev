---
name: gtk
description: Review GTK plans for GObject ownership, widget lifecycle, signals, main-loop and threading behavior, models, actions, resources, styling, accessibility, rendering, and GTK version compatibility. Use when a Linux or cross-platform desktop plan changes GTK UI code.
---

# GTK plan review

Apply this guidance alongside the core GrumpyDev review and the applicable
language, `linux`, `application-security`, and `testing-strategy` skills. Select
only companions that match the plan's real boundaries. Verify behavior against
the project's declared targets; do not silently substitute the newest version, a
development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect GTK and GLib versions, UI definitions, GObject types, ownership
  annotations, widget trees, signal connections, list models, actions,
  resources, CSS, main-context use, and packaging metadata.
- Inspect generated and rendered artifacts in addition to source. Templates,
  designers, metadata, conventions, and lifecycle callbacks can own behavior
  that is invisible in the main code path.
- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: GTK version, language binding, GLib version,
desktop targets, display backends, packaging, theme and accessibility
requirements, and supported distributions. The changed boundary must define:
GObject ownership, widget lifecycle, signals, main loop, threading, list and
model behavior, actions, resources, styling, accessibility, rendering, and GTK 3
to 4 differences.

Assign lifecycle, state, dependency, persistence, and security ownership for
GObject ownership, widget lifecycle, signals, main loop, threading, list and
model behavior. Prove actions, resources, styling, accessibility, rendering, GTK
3 to 4 differences through startup, invalid or denied work, cancellation,
background execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for incorrect GObject reference ownership, signals left
connected through teardown, main-loop blocking or off-thread widget access, GTK
3 behavior assumed under GTK 4, invalidated model positions, and theme-dependent
layout or contrast.

- Apply the ownership conventions of the exact C API or language binding.
  Distinguish borrowed, floating, full, and container ownership, and verify when
  references are sunk, retained, disconnected, or finalized.
- Keep GTK objects on the main thread unless the specific object is documented
  as thread-safe. Marshal results through the intended GLib main context and
  cancel background work when its widget or model disappears.
- Match signal connection lifetime, detail, accumulator, ordering, and
  reentrancy to the object graph. Prevent callbacks into finalized state and
  avoid handlers that accidentally trigger their own mutation recursively.
- Review widget disposal, parenting, templates, list-item factories, recycling,
  selection models, and bindings. Reused list items must not retain stale model
  state or leaked handlers.
- Treat GTK 3 to GTK 4 as an architectural migration, not a namespace update.
  Check removed container, event, rendering, action, menu, accessibility, and
  windowing behavior against the declared target.
- Package resources, icons, schemas, translations, loaders, and plugins so
  installed paths and sandboxed formats work. Development-tree paths are not
  installation contracts.
- Validate semantics, focus, shortcuts, accessibility roles and relations,
  scaling, text direction, themes, contrast, reduced motion, and custom widgets
  under the real desktop environments.
- Keep display-backend and compositor assumptions explicit for X11, Wayland,
  headless tests, clipboard, drag and drop, global positioning, input, and
  window activation.

## Verify the claims

- Build and test against every supported GTK, GLib, binding, distribution, and
  display-backend combination.
- Run ownership and leak diagnostics plus main-thread and reentrancy tests
  around signal and model teardown.
- Exercise keyboard and assistive technology workflows, scaling, themes,
  localization, and custom widgets.
- Install the built package into a clean environment and verify resources,
  schemas, translations, plugins, and startup.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: GTK version,
language binding, GLib version, desktop targets, display backends, packaging,
theme and accessibility requirements, and supported distributions. For the
changed boundary, ask only about unresolved GObject ownership, widget lifecycle,
signals, main loop, threading, list and model behavior, actions, resources,
styling, accessibility, rendering, and GTK 3 to 4 differences when the answer
can change the verdict or implementation.

## Calibrate findings

- Treat use-after-free, persistent data loss, an inaccessible primary workflow,
  or a display/backend assumption that makes the application unusable as
  critical or high according to blast radius and realistic likelihood.
- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the plan depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
GObject ownership, widget lifecycle, signals, main loop, threading, list and
model behavior, actions, resources, styling, accessibility, rendering, and GTK 3
to 4 differences, verification evidence, deployment and recovery limits, and any
material assumption that remains unresolved.
