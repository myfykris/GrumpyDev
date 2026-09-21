# GTK full-review guidance

## Operating conditions

Establish the project target: GTK version, language binding, GLib version,
desktop targets, display backends, packaging, theme and accessibility
requirements, and supported distributions. The changed boundary must define:
GObject ownership, widget lifecycle, signals, main loop, threading, list and
model behavior, actions, resources, styling, accessibility, rendering, and GTK 3
to 4 differences.

## Failure patterns

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
- Validate semantics, focus, shortcuts, accessibility roles and relations,
  scaling, text direction, themes, contrast, reduced motion, and custom widgets
  under the real desktop environments.

## Verification to run or specify in the plan

- Run ownership and leak diagnostics plus main-thread and reentrancy tests
  around signal and model teardown.
- Exercise keyboard and assistive technology workflows, scaling, themes,
  localization, and custom widgets.
