---
name: nestjs
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review NestJS engineering work for module boundaries, provider scope, dependency cycles, validation, guards, interceptors, asynchronous work, and deployment risks."
---

# NestJS GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
