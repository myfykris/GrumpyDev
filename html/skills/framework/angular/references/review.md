# Angular full-review guidance

## Operating conditions

Establish the project target: Angular, TypeScript, Node and RxJS versions,
rendering mode, browser targets, build system, state approach, deployment base
path, and CSP constraints. The changed boundary must define: Standalone and
module boundaries, dependency injection scopes, change detection, signals, RxJS
lifecycle, routing, SSR and hydration, forms, security, bundles, and upgrades.

## Failure patterns

- Require explicit provider scope and reject accidental shared state caused by
  root or route injector placement.
- Check subscription ownership, teardown, higher-order observable cancellation,
  retry loops, and signal or observable duplication.
- Verify guards are not treated as server authorization and that route data
  handles reload, deep links, and failed navigation.
- Check hydration, browser-only APIs, change-detection cost, template escaping,
  accessibility, and complete UI states.
- Demand production-build and browser tests for lazy chunks, configuration
  replacement, service workers, and deployment base paths.

## Verification to run or specify in the plan

- Navigate repeatedly between affected routes while requests resolve out of
  order. Check provider state isolation, observable teardown, signal updates,
  and form errors after component destruction.
- Serve the production build at the deployment base path. Exercise direct URLs
  and failed lazy-chunk loads; where SSR or service workers are used, check
  hydration and stale asset updates.
