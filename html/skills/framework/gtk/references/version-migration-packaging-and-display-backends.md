# GTK version migration, packaging, and display backends

Read this reference when the reviewed work directly or indirectly changes GTK 3 versus
GTK 4 behavior, GLib or language-binding compatibility, installed resources,
schemas, translations, loaders, plugins,
packaging, X11, Wayland, headless execution, clipboard, drag and drop, input, or
compositor behavior.

## Review requirements

- Treat GTK 3 to GTK 4 as an architectural migration, not a namespace update.
  Check removed container, event, rendering, action, menu, accessibility, and
  windowing behavior against the declared target.

- Package resources, icons, schemas, translations, loaders, and plugins so
  installed paths and sandboxed formats work. Development-tree paths are not
  installation contracts.

- Keep display-backend and compositor assumptions explicit for X11, Wayland,
  headless tests, clipboard, drag and drop, global positioning, input, and
  window activation.

## Verify the claims

- Build and test against every supported GTK, GLib, binding, distribution, and
  display-backend combination.

- Install the built package into a clean environment and verify resources,
  schemas, translations, plugins, and startup.
