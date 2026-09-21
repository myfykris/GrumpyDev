# Angular survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Angular.

## Inspect

- Read Angular and TypeScript versions, bootstrap and provider configuration,
  routes, state and data libraries, rendering mode, forms, build targets, and
  tests.

## Ask when unresolved

- Which Angular, TypeScript, RxJS, rendering, router, and change-detection
  versions or modes apply?

- Who owns subscriptions, forms, server state, errors, hydration, and route-
  level authorization?

- Which runtime or deployment differences materially change future reviews:
  Browser targets, SSR or client-only mode, Node build or server runtime, base
  path, proxy, static hosting, cache, content security policy, and deployment
  artifact?

## Record

Map durable Angular version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
