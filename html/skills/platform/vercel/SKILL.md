---
name: gd-vercel
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Vercel engineering work for build output, runtimes, regions, Fluid compute, functions, caching, environment variables, domains, previews, observability, and rollout."
---

# Vercel GrumpyDev review

## Quick checks

- Read framework, Vercel project, build, output, function runtime, region, route, cache,
  domain, and environment configuration.

- Classify code across build, static asset, Node function, edge runtime, middleware,
  background, cron, and browser execution.

Watch especially for request data stored in process globals, automatic scaling
overwhelming databases, regions far from state, preview builds treated as
production proof, cache directives leaking private data, and dashboard settings
silently overriding or being overridden by code.

- Assess cross-user global or cache leakage, exposed production secrets, or unbounded scale
  against stateful dependencies under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Vercel specialist.

## Verdict context

State runtime and region choices, concurrency and connection bounds, cache policy, configuration
sources, preview differences, and production evidence.
