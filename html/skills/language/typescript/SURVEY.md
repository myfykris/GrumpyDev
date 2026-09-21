# TypeScript survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with TypeScript code, artifacts, or runtime behavior.

## Inspect

- Read `package.json`, the lockfile, `tsconfig` variants, bundler/runtime
  config, package exports, lint rules, and representative tests.

## Ask when unresolved

- Which TypeScript version, tsconfig strictness, module mode, runtime, and
  generated-type sources apply?

- Where do untyped inputs, assertions, narrowing, serialization, async work,
  and JavaScript consumers cross the boundary?

- Which runtime or deployment differences are material for future reviews:
  Runtime after compilation, compiler and module mode, bundler, browser or
  server targets, generated output, environment injection, source maps, and
  deployment artifact?

## Record

Map durable TypeScript version and compatibility requirements to `Requirements`
or `Constraints`, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
