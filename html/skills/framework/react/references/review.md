# React full-review guidance

## Operating conditions

Establish the project target: React version, renderer and framework, server or
client rendering, browser targets, state and data libraries, bundler, test
renderer, and deployment form. The changed boundary must define: Render purity,
state ownership, effects, concurrency, transitions, suspense, server rendering,
hydration, context, forms, accessibility, performance, and library boundaries.

## Failure patterns

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

## Verification to run or specify in the plan

- Change props and navigate away while effects or requests are pending.
  Resolve responses out of order and check cleanup, state ownership, and
  protection against stale updates.
- Exercise loading, failure, retry, and form flows through visible behavior
  with keyboard and screen-reader input. Measure claimed render improvements
  in the relevant build instead of relying on memoization alone.
