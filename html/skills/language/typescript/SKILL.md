---
name: gd-typescript
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review TypeScript engineering work for runtime validation, type-safety gaps, module boundaries, build configuration, dependency, and asynchronous failure risks."
---

# TypeScript GrumpyDev review

## Quick checks

- Read `package.json`, the lockfile, `tsconfig` variants, bundler/runtime
  config, package exports, lint rules, and representative tests.

- Identify actual execution targets: browser, Node, edge runtime, worker, test
  runner, CommonJS, ESM, or multiple outputs.

Watch especially for erased types treated as runtime validation, any or
assertions silencing uncertainty, structural compatibility accepting
semantically wrong objects, excess-property checks applied inconsistently,
module-resolution differences, and promises whose rejection path is missing.

- Assess trusted static types at an unvalidated runtime boundary or unsafe
  assertion on security-critical input under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the TypeScript
specialist.

## Verdict context

State the runtime targets, validation boundaries, compiler guarantees actually
enabled, compatibility assumptions, and evidence that built artifacts work for
their real consumers.
