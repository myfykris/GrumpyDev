# Dart survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Dart code, artifacts, or runtime behavior.

## Inspect

- Read pubspec files, lockfiles, SDK constraints, analyzer settings, generated
  code configuration, platform targets, and representative tests.

## Ask when unresolved

- Which Dart version, target runtime, null-safety mode, package constraints,
  and isolate model apply?

- How do futures, streams, cancellation, serialization, errors, and mutable
  state cross isolates or UI lifecycles?

- Which runtime or deployment differences materially change future reviews:
  Dart VM, AOT, Flutter, browser, server, isolate, architecture, packaging, and
  platform service boundaries?

## Record

Map durable Dart version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
