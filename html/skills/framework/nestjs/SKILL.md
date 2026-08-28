---
name: nestjs
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review NestJS plans and other engineering artifacts for module boundaries, provider scope, dependency cycles, validation, guards, interceptors, asynchronous work, and deployment risks. Project applicability: the project uses or materially depends on NestJS."
---

# NestJS GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `typescript` and
`javascript` skills.

## Lean review

- Establish the exact Node.js, NestJS, TypeScript, adapter, transport, and
  deployment versions.

- Read modules, imports and exports, provider scopes, controllers, pipes,
  guards, interceptors, exception filters, transport setup, and tests.

Watch especially for provider-scope mistakes, circular dependencies hidden by
forward references, guard and interceptor ordering, validation transforms that
coerce hostile input, lifecycle hooks that do not await completion, and
request-scoped providers multiplying cost.

Lean mode is insufficient when this material severity condition may apply:

- Treat guard bypass, request data in singleton state, or transport retries
  causing irreversible effects as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete NestJS evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State module and provider ownership, validation and authorization pipeline,
initialization and shutdown behavior, transport guarantees, and built-runtime
evidence.
