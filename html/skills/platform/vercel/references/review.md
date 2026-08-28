# Vercel standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when runtimes, regions, limits, concurrency, cache scope, configuration precedence,
  and production output are tested.
