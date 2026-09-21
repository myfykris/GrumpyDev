# Windows Forms survey contribution

## Applies when

Apply this contribution when the project uses Windows Forms or when its behavior
constrains a supported build, deployment, client, or operating environment.

## Inspect

- Inspect target frameworks, forms and controls, designer files, event wiring,
  data bindings, synchronization contexts, resources, manifests, DPI settings,
  native interop, installers, and update configuration.

## Ask when unresolved

- Which of these durable facts materially change future reviews: .NET and
  WinForms versions, Windows targets, architecture, DPI and localization
  targets, packaging, deployment, native interop, and support constraints?

- Which runtime or deployment differences are material for future reviews:
  Windows and .NET versions, architecture, desktop session, native interop,
  DPI, installer, signing, update, configuration, file access, and support
  channel?

## Record

Map durable Windows Forms version and behavior requirements to `Requirements`
or `Constraints`, lifecycle and deployment facts to `Runtime and deployment`,
and material gaps to `Unknowns`.
