# Python survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Python code, artifacts, or runtime behavior.

## Inspect

- Read `pyproject.toml`, lockfiles, supported Python versions, entry points,
  framework configuration, type-checker settings, and representative tests.

## Ask when unresolved

- Which Python version and implementation, target platforms, dependency
  resolver, and packaging mode apply?

- How do async and sync work, cancellation, typing boundaries, serialization,
  resources, and process concurrency interact?

- Which runtime or deployment differences materially change future reviews:
  Interpreter and version, WSGI or ASGI or worker runtime, process and thread
  model, event loop, native wheels, OS and architecture, packaging, environment
  management, and shutdown?

## Record

Map durable Python version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
