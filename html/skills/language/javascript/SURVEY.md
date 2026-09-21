# JavaScript survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with JavaScript code, artifacts, or runtime behavior.

## Inspect

- Read package metadata, lockfiles, runtime and browser targets, module type,
  bundler settings, lint rules, generated artifacts, and representative tests.

## Ask when unresolved

- Which ECMAScript, Node.js or browser versions, module mode, package
  resolution, and runtime globals apply?

- How do promises, cancellation, event-loop work, coercion, serialization, and
  untrusted input cross the boundary?

- Which runtime or deployment differences are material for future reviews:
  Browser, Node.js, edge, worker, embedded, or build-only execution; supported
  engines; event-loop ownership; bundling; environment injection; and
  deployment artifact?

## Record

Map durable JavaScript version and compatibility requirements to `Requirements`
or `Constraints`, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
