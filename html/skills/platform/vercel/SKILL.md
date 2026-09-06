---
name: vercel
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Vercel engineering work for build output, runtimes, regions, Fluid compute, functions, caching, environment variables, domains, previews, observability, and rollout."
---

# Vercel GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `serverless`, `nextjs` and
`observability` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read framework, Vercel project, build, output, function runtime, region, route, cache,
  domain, and environment configuration.

- Classify code across build, static asset, Node function, edge runtime, middleware,
  background, cron, and browser execution.

Watch especially for request data stored in process globals, automatic scaling
overwhelming databases, regions far from state, preview builds treated as
production proof, cache directives leaking private data, and dashboard settings
silently overriding or being overridden by code.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-user global or cache leakage, exposed production secrets, or unbounded scale
  against stateful dependencies as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Vercel evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State runtime and region choices, concurrency and connection bounds, cache policy, configuration
sources, preview differences, and production evidence.
