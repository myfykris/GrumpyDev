# Go survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Go code, artifacts, or runtime behavior.

## Inspect

- Read go.mod, go.sum, build tags, generated code, entry points, interface
  boundaries, race-test configuration, and representative tests.

## Ask when unresolved

- Which Go language version in go.mod, toolchain version, target, build tags,
  and module graph apply?

- Who owns each goroutine, channel, context, timer, and shared value, including
  the exact loop form for captures?

- Which runtime or deployment differences materially change future reviews: Go
  version, OS and architecture matrix, CGO and libc, build tags, static or
  dynamic linkage, container or host process, signals, and executable
  packaging?

## Record

Map durable Go version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
