# Next.js full-review guidance

## Operating conditions

Establish the project target: Next.js, React and Node versions, router,
rendering modes, edge or Node runtime, cache and revalidation policy, hosting
target, build output, and browser support. The changed boundary must define: App
and pages routers, server and client components, rendering and caching modes,
actions, middleware, route handlers, hydration, runtimes, assets, and
deployment.

## Failure patterns

- Require an explicit server or client boundary and prevent secrets, server-only
  modules, or privileged data from entering client bundles.
- Test production builds, direct URL loads, navigation, hydration,
  authentication transitions, cache invalidation, and rolling releases.

## Verification to run or specify in the plan

- Inspect production client bundles and serialized page data for server-only
  modules, secrets, and privileged fields. Verify affected routes in the
  selected runtime rather than only in the development server.
- During a rolling release, exercise direct URLs and client navigation using
  old browser assets against the new server. Check the fallback for
  incompatible assets or requests.
