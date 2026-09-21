# Vercel full-review guidance

## Operating conditions

Establish the project target: Vercel projects and teams, framework and build command, output
mode, function runtimes and regions, Fluid compute behavior, concurrency and limits, cache and
revalidation ownership, environment variables, previews, domains, protection, observability, and
rollout.

## Failure patterns

- Select runtime and region based on framework support, data location, latency, security, and
  required APIs rather than defaults.
- Make global connection reuse concurrency-safe while keeping request and user state strictly
  scoped to each invocation.
- Bound function concurrency against database pools and vendor quotas, and define timeout,
  cancellation, retry, and partial effects.
- Specify cache keys, revalidation, private-data exclusion, purge, mixed-version behavior, and
  ownership across framework and platform.
- Reconcile code, Vercel configuration, project settings, environment variables, domains, and
  preview differences with clear precedence.
- Test production bytecode and output, cold and warm starts, concurrent requests, region
  failure, rollback, and observability.

## Verification to run or specify in the plan

- Build with the actual production command and inspect functions, static output, routes,
  regions, runtimes, and bundle limits.
- Exercise concurrent requests, instance reuse, connection pressure, timeouts, streaming, cache
  variation, and old and new versions.
- Compare preview and production configuration, protection, environment values, domains,
  observability, and rollback behavior.
