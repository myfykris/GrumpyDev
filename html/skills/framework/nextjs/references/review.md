# Next.js standard review

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

## Challenge the reviewed work

### Recurring traps

- Require an explicit server or client boundary and prevent secrets, server-only
  modules, or privileged data from entering client bundles.
- Test production builds, direct URL loads, navigation, hydration,
  authentication transitions, cache invalidation, and rolling releases.

## Verify the claims

- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.
## Ask when evidence is missing

- Ask which Next.js and React versions, router, execution runtime, hosting
  target, and production build apply when repository evidence does not establish
  them.

## Calibrate findings

- Downgrade when exact rendering and cache semantics, auth boundaries, and mixed
  navigation behavior are tested.
