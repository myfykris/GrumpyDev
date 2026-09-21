# Blazor full-review guidance

## Operating conditions

Establish the project target: .NET and Blazor versions, render modes by route,
hosting and proxy, browser targets, authentication, trimming and AOT, CDN
prohibition or asset policy, and offline needs. The changed boundary must
define: Server, WebAssembly, auto and hybrid modes, circuit lifecycle,
prerendering, hydration, state persistence, JS interop, authentication,
payloads, and deployment.

## Failure patterns

- Require one declared rendering mode per route or component and account for
  code that runs during prerender and again after activation.
- Check circuit lifetime, scoped-service semantics, reconnection, stale state,
  concurrent events, and server memory limits.
- Treat browser and server authorization separately; never rely on hidden UI or
  client state as access control.
- Require disposal for timers, subscriptions, cancellation sources, and
  JavaScript references across component teardown.
- Test published output, navigation reloads, offline or disconnected states,
  accessibility, trimming, and supported browsers.

## Verification to run or specify in the plan

- Load each affected rendering mode from a fresh session. Check prerendering
  and activation for duplicate effects; where server circuits apply,
  disconnect and reconnect while verifying user-state isolation.
- Navigate away during JS interop or asynchronous work and verify disposal.
  Test direct server access independently of hidden UI, then exercise the
  published artifact for the configured trimming and browser targets.
