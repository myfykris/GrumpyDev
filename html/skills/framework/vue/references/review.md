# Vue full-review guidance

## Operating conditions

Establish the project target: Vue, TypeScript and Node versions, composition or
options API, SSR framework, router and state tools, browser targets, bundler,
and deployment form. The changed boundary must define: Reactivity, refs and
proxies, component lifecycle, composables, watchers, state ownership, routing,
SSR and hydration, forms, security, and bundles.

## Failure patterns

- Require one owner for each state value and reject duplicated props, store,
  route, and local state synchronized by watchers.
- Check watcher flush timing, deep reactivity, stale closures, cleanup, aborted
  requests, and effects after component disposal.
- Verify route guards are not treated as server authorization and that deep
  links, reloads, and failed navigation work.
- Check SSR and hydration, browser-only APIs, template escaping, accessibility,
  and complete loading or error states.
- Demand production-build and browser tests for chunks, environment variables,
  base paths, plugins, hydration, and deployment.

## Verification to run or specify in the plan

- Change routes and reactive inputs while requests resolve out of order. Check
  watcher cleanup, state ownership, and that disposed components cannot apply
  stale updates.
- Serve the production build under its actual base path and test direct links,
  failed chunks, and forms. If SSR is used, compare server and client state
  across identities and check hydration.
