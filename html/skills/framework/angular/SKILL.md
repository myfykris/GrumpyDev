---
name: angular
description: Review Angular plans for dependency injection scope, signals and RxJS ownership, change detection, routing, forms, rendering, accessibility, and build risks. Use when a plan changes Angular applications, libraries, components, services, or routes.
---

# Angular plan review

Apply this guidance alongside the core GrumpyDev review and the `typescript` and
`javascript` skills.

## Inspect evidence

- Read Angular and TypeScript versions, bootstrap and provider configuration,
  routes, state and data libraries, rendering mode, forms, build targets, and
  tests.
- Trace service lifetimes, signals, observables, subscriptions, navigation,
  server and browser boundaries, and loading or error states.

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

## Challenge the plan

### Recurring traps

Watch especially for mutable singleton-service state, duplicated providers with
surprising scope, leaked subscriptions, change-detection assumptions that fail
outside the expected zone or signal boundary, and route guards mistaken for
server-side authorization.

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

- Treat client-side authorization as the only control, leaked long-lived
  subscriptions, or broken core hydration as critical.
- Downgrade when lifecycle, server enforcement, rendering, and user-flow tests
  cover the supported browser matrix.

## Add to the verdict

State provider and state ownership, reactive cleanup, routing and rendering
assumptions, user-visible failure states, and production-build evidence.
