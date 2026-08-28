# Vue standard review

## Establish the operating model

Establish the project target: Vue, TypeScript and Node versions, composition or
options API, SSR framework, router and state tools, browser targets, bundler,
and deployment form. The changed boundary must define: Reactivity, refs and
proxies, component lifecycle, composables, watchers, state ownership, routing,
SSR and hydration, forms, security, and bundles.

Assign lifecycle, state, dependency, persistence, and security ownership for
Reactivity, refs and proxies, component lifecycle, composables, watchers, state
ownership. Prove routing, SSR and hydration, forms, security, bundles through
startup, invalid or denied work, cancellation, background execution, mixed
versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the actual Vue lifecycle and production
  pipeline: Reactivity, refs and proxies, component lifecycle, composables,
  watchers, state ownership. Use the actual framework pipeline and production
  build with representative services and configuration.
- Exercise failure and edge behavior for: routing, SSR and hydration, forms,
  security, bundles. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Vue, JavaScript or TypeScript, build tool, router, state library,
  rendering mode, and browser versions apply?
- Who owns reactive state, effects, async work, hydration, errors,
  authorization, and accessibility behavior?

## Calibrate findings

- Downgrade when state isolation, rendering, failure, accessibility, and
  navigation are covered by representative tests.
