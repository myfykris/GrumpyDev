# Rust survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Rust code, artifacts, or runtime behavior.

## Inspect

- Establish the Rust edition, minimum supported Rust version, Cargo version,
  target toolchains, and supported feature combinations.

## Ask when unresolved

- Which Rust edition, minimum supported Rust version, Cargo version, target
  toolchain, and feature set apply?

- Where do unsafe code, FFI, pinning, async cancellation, shared state, and
  resource lifetime cross the boundary?

- Which runtime or deployment differences materially change future reviews:
  Rust target triple, libc or static linkage, architecture, feature set, native
  libraries, service or embedded process, packaging, and FFI runtime boundary?

## Record

Map durable Rust version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
