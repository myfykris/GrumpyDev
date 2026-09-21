# C++ survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with C++ code, artifacts, or runtime behavior.

## Inspect

- Read build definitions, compiler and language-standard settings, public
  headers, dependency configuration, sanitizer settings, and representative
  tests.

## Ask when unresolved

- Which C++ standard, compiler, standard library, target ABI, and exception or
  RTTI settings apply?

- Who owns each object and resource across move, exception, concurrency, and
  binary boundaries?

- Which runtime or deployment differences materially change future reviews:
  Compiler and standard library, ABI, architecture, runtime linkage, allocator,
  plugin boundary, packaging, and supported operating targets?

## Record

Map durable C++ version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
