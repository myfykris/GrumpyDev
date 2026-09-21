# WinUI 3 survey contribution

## Applies when

Apply this contribution when the project uses WinUI 3 or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect Windows App SDK and target settings, XAML, view models, bindings,
  activation registration, windows, dispatch queues, resources, manifests,
  identity, packaging, bootstrapper, and deployment output.

## Ask when unresolved

- Which of these durable facts materially change future reviews: Windows App
  SDK and WinUI versions, C# or C++, Windows minimums, packaged or unpackaged
  deployment, architectures, app lifecycle, identity, and distribution?

- Which runtime or deployment differences are material for future reviews:
  Windows App SDK, packaged or unpackaged identity, Windows versions,
  architecture, activation, app services, permissions, signing, installer or
  Store, and updates?

## Record

Map durable WinUI 3 version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
