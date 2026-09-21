# Ruby survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Ruby code, artifacts, or runtime behavior.

## Inspect

- Read gem metadata, lockfiles, Ruby version files, native extensions, autoload
  configuration, process and worker settings, and representative tests.

## Ask when unresolved

- Which Ruby version and implementation, thread and process model, native
  extensions, and gem versions apply?

- How do mutable state, blocks, exceptions, fibers, threads, resources, and
  serialization cross the boundary?

- Which runtime or deployment differences materially change future reviews:
  Ruby implementation and version, application server, process and thread
  model, worker runtime, native extensions, OS, packaging, signals, and rolling
  restart behavior?

## Record

Map durable Ruby version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
