# Vapor standard review

## Establish the operating model

Establish the project target: Vapor and Swift versions, event-loop topology,
database drivers, queues, proxy and TLS, container or host deployment, and
supported operating systems. The changed boundary must define: Event loops,
async and blocking work, request lifecycle, content decoding, authentication,
Fluent transactions, queues, WebSockets, shutdown, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Event loops, async and blocking work, request lifecycle, content decoding,
authentication. Prove Fluent transactions, queues, WebSockets, shutdown,
deployment through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

- Keep blocking filesystem, SDK, cryptographic, or database work off event-loop
  threads and bound any thread-pool use.
- Require request-scoped ownership and cancellation for tasks, clients, streams,
  websockets, and temporary resources.
- Check Content decoding, validation, over-posting, authentication, object
  authorization, body limits, and error-detail exposure.
- Analyze Fluent migrations, transactions, eager loading, constraints,
  concurrency, and old or new application overlap.
- Test the production server and proxy for timeouts, forwarded headers, TLS
  assumptions, graceful drain, migrations, and release builds.

## Verify the claims

- Verify these behaviors through the actual Vapor lifecycle and production
  pipeline: Event loops, async and blocking work, request lifecycle, content
  decoding, authentication. Use the actual framework pipeline and production
  build with representative services and configuration.
- Exercise failure and edge behavior for: Fluent transactions, queues,
  WebSockets, shutdown, deployment. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Swift, Vapor, SwiftNIO, database driver, and deployment versions apply?
- How do event-loop affinity, async work, request state, authentication,
  transactions, errors, and shutdown interact?

## Calibrate findings

- Downgrade when exact-version concurrency, auth, transaction, and shutdown
  behavior are integration-tested.
