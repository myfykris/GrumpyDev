# WPF survey contribution

## Applies when

Apply this contribution when the project uses WPF or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect target frameworks, XAML, dependency properties, bindings, resources,
  styles, templates, commands, dispatchers, windows, native interop, manifests,
  packaging, and deployment configuration.

## Ask when unresolved

- Which of these durable facts materially change future reviews: .NET and WPF
  versions, Windows targets, architecture, packaging, deployment, DPI and
  localization targets, interop, and application lifecycle?

- Which runtime or deployment differences are material for future reviews:
  Windows and .NET versions, architecture, desktop session, native interop,
  rendering mode, installer, signing, configuration, update, and file access?

## Record

Map durable WPF version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
