---
name: typescript
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review TypeScript plans and other engineering artifacts for runtime validation, type-safety gaps, module boundaries, build configuration, dependency, and asynchronous failure risks. Project applicability: the project contains, builds, deploys, operates, or interoperates with TypeScript code, artifacts, or runtime behavior."
---

# TypeScript GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read `package.json`, the lockfile, `tsconfig` variants, bundler/runtime
  config, package exports, lint rules, and representative tests.

- Identify actual execution targets: browser, Node, edge runtime, worker, test
  runner, CommonJS, ESM, or multiple outputs.

Watch especially for erased types treated as runtime validation, any or
assertions silencing uncertainty, structural compatibility accepting
semantically wrong objects, excess-property checks applied inconsistently,
module-resolution differences, and promises whose rejection path is missing.

Lean mode is insufficient when this material severity condition may apply:

- Treat trusted static types at an unvalidated runtime boundary or unsafe
  assertion on security-critical input as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete TypeScript evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State the runtime targets, validation boundaries, compiler guarantees actually
enabled, compatibility assumptions, and evidence that built artifacts work for
their real consumers.
