---
name: nextjs
description: Review Next.js plans for server and client boundaries, caching, rendering mode, routing, data mutation, runtime selection, authentication, and deployment risks. Use when a TypeScript or JavaScript plan changes Next.js routes, components, server actions, middleware, or deployment.
---

# Next.js plan review

Apply this guidance alongside the core GrumpyDev review and the `react`,
`javascript`, and `typescript` skills.

## Inspect evidence

- Read Next.js and React versions, app or pages router, route configuration,
  server and client components, caching directives, middleware, runtime targets,
  and tests.
- Trace data reads and mutations through rendering, caches, revalidation,
  cookies, authentication, navigation, streaming, and deployment.

## Establish the operating model

Establish the project target: Next.js, React and Node versions, router,
rendering modes, edge or Node runtime, cache and revalidation policy, hosting
target, build output, and browser support. The changed boundary must define: App
and pages routers, server and client components, rendering and caching modes,
actions, middleware, route handlers, hydration, runtimes, assets, and
deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for App
and pages routers, server and client components, rendering and caching modes,
actions, middleware. Prove route handlers, hydration, runtimes, assets,
deployment through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for server and client boundaries crossed accidentally, stale or
over-broad cache and revalidation behavior, route runtimes that lack required
APIs, secrets included in client bundles, hydration differences, and build-time
data assumed to remain current. Also watch for server actions treated as private
functions, user-specific results entering shared caches, and remote fetch or
redirect input becoming an SSRF or open-redirect path.

- Require an explicit server or client boundary and prevent secrets, server-only
  modules, or privileged data from entering client bundles.
- Define cache scope, key, lifetime, invalidation, personalization, and stale
  behavior for every cached read or rendered route.
- Treat server actions and route handlers as public endpoints with validation,
  object and action authorization, CSRF considerations, body and work limits,
  idempotency, safe errors, and audit behavior. Validate every invocation even
  when only generated client code is expected to call it.
- Keep cache keys, tags, revalidation paths, and rendered output within the
  current identity and tenant boundary. Do not let user input invalidate
  arbitrary content or let privileged fetch results enter a public cache.
- Constrain server-side fetches, image or metadata URLs, preview endpoints,
  redirects, rewrites, and callback destinations to approved schemes and
  origins. Apply the full SSRF policy before following redirects or returning
  fetched content.
- Treat middleware as an early filter, not the sole authorization boundary.
  Recheck permission at the route, action, resolver, or data operation that
  performs the sensitive effect.
- Audit values exposed through public environment variables, React Server
  Component serialization, page data, source maps, errors, and build output.
- Check Node versus edge runtime APIs, streaming, dynamic rendering triggers,
  middleware limits, and deployment-specific behavior.
- Test production builds, direct URL loads, navigation, hydration,
  authentication transitions, cache invalidation, and rolling releases.

## Verify the claims

- Verify these behaviors through the actual Next.js lifecycle and production
  pipeline: App and pages routers, server and client components, rendering and
  caching modes, actions, middleware. Use the actual framework pipeline and
  production build with representative services and configuration.
- Exercise failure and edge behavior for: route handlers, hydration, runtimes,
  assets, deployment. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.
- Call route handlers and server actions directly with missing, stale,
  cross-tenant, malformed, oversized, and duplicate input. Verify denial at the
  authoritative data or effect boundary.
- Exercise personalized cache reads, revalidation, redirects, remote fetches,
  preview or draft access, production error handling, and client bundle
  inspection with the deployed runtime configuration.

## Ask when evidence is missing

- Which Next.js, React, router, rendering mode, cache mode, and deployment
  runtime apply?
- Where do authentication, server actions, route handlers, revalidation,
  serialization, and client state cross boundaries?

## Calibrate findings

- Treat server-only data exposure, cache leakage across users, or unsafe
  mutation authorization as critical.
- Downgrade when exact rendering and cache semantics, auth boundaries, and mixed
  navigation behavior are tested.

## Add to the verdict

State rendering and runtime modes, server-client trust boundary, route and
action authorization, cache and revalidation scope, outbound fetch policy,
mutation contracts, authentication behavior, and production evidence.
