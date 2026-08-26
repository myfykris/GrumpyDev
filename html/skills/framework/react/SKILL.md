---
name: react
description: Review React engineering plans for state ownership, effect lifecycle, rendering, accessibility, performance, hydration, and user-experience failure risks. Use when a plan creates or changes React components, hooks, routes, data flows, or frontend architecture.
---

# React plan review

Apply this guidance alongside the core GrumpyDev review, the `javascript` or
`typescript` skill, and `application-security` when untrusted content,
authentication, or sensitive browser state changes.

## Inspect evidence

- Identify the React and framework versions, rendering mode, routing, data
  library, form approach, styling system, tests, and supported browsers.
- Trace ownership for server data, URL state, form state, local interaction
  state, cached state, and cross-page state.
- Inspect representative components, hooks, loading/error UI, accessibility
  patterns, and any server/client boundary.
- Inventory untrusted HTML, Markdown, URLs, styles, script-capable properties,
  browser storage, third-party widgets, and values serialized into hydration.

## Establish the operating model

Establish the project target: React version, renderer and framework, server or
client rendering, browser targets, state and data libraries, bundler, test
renderer, and deployment form. The changed boundary must define: Render purity,
state ownership, effects, concurrency, transitions, suspense, server rendering,
hydration, context, forms, accessibility, performance, and library boundaries.

Assign lifecycle, state, dependency, persistence, and security ownership for
Render purity, state ownership, effects, concurrency, transitions, suspense,
server rendering. Prove hydration, context, forms, accessibility, performance,
library boundaries through startup, invalid or denied work, cancellation,
background execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for stale closures and incomplete effect dependencies,
duplicated derived state, unstable list keys, asynchronous results applied after
ownership changes, Strict Mode exposing non-idempotent effects, and client-side
checks mistaken for authorization. Also watch for unsafe HTML or URL sinks,
secrets in browser state or bundles, and server-rendered data crossing users
through caches or hydration.

- Reject duplicated state whose synchronization is left to effects. Prefer one
  owner and derive values during render when possible.
- Inspect every proposed effect for a real external synchronization target,
  dependency correctness, cancellation, cleanup, race handling, and development
  double-invocation behavior.
- Require complete loading, empty, error, stale, offline, unauthorized, and
  retry states for user-visible data flows.
- Check keyboard behavior, focus management, semantic structure, labels,
  contrast, reduced motion, and screen-reader announcements for dynamic UI.
- Check hydration and serialization assumptions when server rendering or server
  components apply. Identify browser-only APIs and time/randomness differences.
- Treat all client-side authorization as presentation behavior. Enforce object,
  property, and action permissions on the authoritative server and avoid
  serializing inaccessible records or secrets merely because the UI hides them.
- Keep normal text in React's escaped rendering path. Require a reviewed
  sanitizer and explicit policy for intentionally rendered HTML or Markdown;
  constrain URL schemes, iframe and navigation targets, CSS or style input, and
  direct DOM sinks used by components or third-party libraries.
- Keep credentials and sensitive personal data out of source maps, client
  environment values, error payloads, analytics, browser storage, and cached
  state unless the architecture explicitly requires and protects that exposure.
- Use browser security controls such as Content Security Policy, frame policy,
  safe cookie attributes, and trusted origin rules as defense in depth matched
  to the actual deployment and third-party script model.
- Treat memoization and state libraries as costs that require measured need.
  Flag render churn only with a plausible scale or interaction consequence.
- Require tests at the behavior boundary. Do not accept implementation-detail
  snapshots as the sole evidence for critical flows.

## Verify the claims

- Verify these behaviors through the actual React lifecycle and production
  pipeline: Render purity, state ownership, effects, concurrency, transitions,
  suspense, server rendering. Use the actual framework pipeline and production
  build with representative services and configuration.
- Exercise failure and edge behavior for: hydration, context, forms,
  accessibility, performance, library boundaries. Exercise invalid input, denied
  access, cancellation, dependency failure, concurrent work, shutdown, and
  mixed-version deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.
- Exercise stored, reflected, and DOM-based hostile content through text, HTML,
  Markdown, URL, navigation, hydration, error, analytics, and widget boundaries.
- Inspect production bundles, source maps, storage, network calls, and rendered
  DOM for secrets, cross-user data, dangerous schemes, and executable markup.

## Ask when evidence is missing

- Which React version, JavaScript or TypeScript version, framework, rendering
  mode, and supported browsers apply?
- Who owns server data, URL state, form state, effects, hydration, errors, and
  accessibility behavior?

## Calibrate findings

- Treat cross-user hydration leakage, missing authorization at the server
  boundary, or an inaccessible core flow as critical.
- Downgrade when state has one owner and rendering, failure, accessibility, and
  interaction behavior are tested.

## Add to the verdict

State the state owner for each changed flow, the server/client and trust
boundaries, untrusted rendering and browser-storage policy, all user-visible
failure states, accessibility evidence, and the test that proves the interaction
works.
