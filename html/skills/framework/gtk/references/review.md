# GTK standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

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
## Verify the claims

- Run ownership and leak diagnostics plus main-thread and reentrancy tests
  around signal and model teardown.
- Exercise keyboard and assistive technology workflows, scaling, themes,
  localization, and custom widgets.
## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: GTK version,
language binding, GLib version, desktop targets, display backends, packaging,
theme and accessibility requirements, and supported distributions. For the
changed boundary, ask only about unresolved GObject ownership, widget lifecycle,
signals, main loop, threading, list and model behavior, actions, resources,
styling, accessibility, rendering, and GTK 3 to 4 differences when the answer
can change the verdict or implementation.

## Calibrate findings

- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the reviewed work depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
