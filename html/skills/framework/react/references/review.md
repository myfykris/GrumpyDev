# React standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

- Reject duplicated state whose synchronization is left to effects. Prefer one
  owner and derive values during render when possible.
- Inspect every proposed effect for a real external synchronization target,
  dependency correctness, cancellation, cleanup, race handling, and development
  double-invocation behavior.
- Require complete loading, empty, error, stale, offline, unauthorized, and
  retry states for user-visible data flows.
- Check keyboard behavior, focus management, semantic structure, labels,
  contrast, reduced motion, and screen-reader announcements for dynamic UI.
- Treat memoization and state libraries as costs that require measured need.
  Flag render churn only with a plausible scale or interaction consequence.
- Require tests at the behavior boundary. Do not accept implementation-detail
  snapshots as the sole evidence for critical flows.

## Verify the claims

- Exercise failure and edge behavior for: hydration, context, forms,
  accessibility, performance, library boundaries. Exercise invalid input, denied
  access, cancellation, dependency failure, concurrent work, shutdown, and
  mixed-version deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.
## Ask when evidence is missing

- Which React version, JavaScript or TypeScript version, framework, rendering
  mode, and supported browsers apply?
## Calibrate findings

- Downgrade when state has one owner and rendering, failure, accessibility, and
  interaction behavior are tested.
