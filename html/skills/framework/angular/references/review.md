# Angular standard review

## Establish the operating model

Establish the project target: Angular, TypeScript, Node and RxJS versions,
rendering mode, browser targets, build system, state approach, deployment base
path, and CSP constraints. The changed boundary must define: Standalone and
module boundaries, dependency injection scopes, change detection, signals, RxJS
lifecycle, routing, SSR and hydration, forms, security, bundles, and upgrades.

Assign lifecycle, state, dependency, persistence, and security ownership for
Standalone and module boundaries, dependency injection scopes, change detection,
signals, RxJS lifecycle, routing. Prove SSR and hydration, forms, security,
bundles, upgrades through startup, invalid or denied work, cancellation,
background execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the actual Angular lifecycle and production
  pipeline: Standalone and module boundaries, dependency injection scopes,
  change detection, signals, RxJS lifecycle, routing. Use the actual framework
  pipeline and production build with representative services and configuration.
- Exercise failure and edge behavior for: SSR and hydration, forms, security,
  bundles, upgrades. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Angular, TypeScript, RxJS, rendering, router, and change-detection
  versions or modes apply?
- Who owns subscriptions, forms, server state, errors, hydration, and
  route-level authorization?

## Calibrate findings

- Downgrade when lifecycle, server enforcement, rendering, and user-flow tests
  cover the supported browser matrix.
