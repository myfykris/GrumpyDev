# GTK survey contribution

## Applies when

Apply this contribution when the project uses GTK or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect GTK and GLib versions, UI definitions, GObject types, ownership
  annotations, widget trees, signal connections, list models, actions,
  resources, CSS, main-context use, and packaging metadata.

## Ask when unresolved

- Which of these durable facts materially change future reviews: GTK version,
  language binding, GLib version, desktop targets, display backends, packaging,
  theme and accessibility requirements, and supported distributions?

- Which runtime or deployment differences are material for future reviews: GTK
  and GLib versions, display backend, desktop and distribution targets, sandbox
  or portal use, packaging, native dependencies, accessibility, and update
  channel?

## Record

Map durable GTK version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
