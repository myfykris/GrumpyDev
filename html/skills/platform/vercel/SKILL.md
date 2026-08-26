---
name: vercel
description: Review Vercel plans for build output, runtimes, regions, Fluid compute, functions, caching, environment variables, domains, previews, observability, and rollout. Use when an application builds or runs on Vercel.
---

# Vercel plan review

Apply this guidance alongside the core GrumpyDev review and the `serverless`, `nextjs` and
`observability` skills.

## Inspect evidence

- Read framework, Vercel project, build, output, function runtime, region, route, cache,
  domain, and environment configuration.
- Classify code across build, static asset, Node function, edge runtime, middleware,
  background, cron, and browser execution.
- Trace function concurrency, instance reuse, mutable globals, connections, timeouts, payloads,
  streaming, retries, and downstream limits.
- Inspect preview and production differences, secrets, protection, aliases, redirects, headers,
  observability, and rollback controls.

## Establish the operating model

Establish the project target: Vercel projects and teams, framework and build command, output
mode, function runtimes and regions, Fluid compute behavior, concurrency and limits, cache and
revalidation ownership, environment variables, previews, domains, protection, observability, and
rollout.

A function instance may serve concurrent requests and reuse global state, but it is not a
durable singleton. Region, runtime, cache, and production build behavior must match data
location and framework assumptions.

## Challenge the plan

### Recurring traps

Watch especially for request data stored in process globals, automatic scaling overwhelming
databases, regions far from state, preview builds treated as production proof, cache directives
leaking private data, and dashboard settings silently overriding or being overridden by code.

- Select runtime and region based on framework support, data location, latency, security, and
  required APIs rather than defaults.
- Make global connection reuse concurrency-safe while keeping request and user state strictly
  scoped to each invocation.
- Bound function concurrency against database pools and vendor quotas, and define timeout,
  cancellation, retry, and partial effects.
- Specify cache keys, revalidation, private-data exclusion, purge, mixed-version behavior, and
  ownership across framework and platform.
- Reconcile code, vercel configuration, project settings, environment variables, domains, and
  preview differences with clear precedence.
- Test production bytecode and output, cold and warm starts, concurrent requests, region
  failure, rollback, and observability.

## Verify the claims

- Build with the actual production command and inspect functions, static output, routes,
  regions, runtimes, and bundle limits.
- Exercise concurrent requests, instance reuse, connection pressure, timeouts, streaming, cache
  variation, and old and new versions.
- Compare preview and production configuration, protection, environment values, domains,
  observability, and rollback behavior.

## Ask when evidence is missing

- Which Vercel projects, framework, runtimes, regions, Fluid settings, limits, build output,
  and data locations apply?
- How are concurrency, global reuse, connections, caches, environments, previews, domains,
  rollout, and rollback handled?

## Calibrate findings

- Treat cross-user global or cache leakage, exposed production secrets, or unbounded scale
  against stateful dependencies as critical.
- Downgrade when runtimes, regions, limits, concurrency, cache scope, configuration precedence,
  and production output are tested.

## Add to the verdict

State runtime and region choices, concurrency and connection bounds, cache policy, configuration
sources, preview differences, and production evidence.
