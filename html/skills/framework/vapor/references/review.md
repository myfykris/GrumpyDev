# Vapor full-review guidance

## Operating conditions

Establish the project target: Vapor and Swift versions, event-loop topology,
database drivers, queues, proxy and TLS, container or host deployment, and
supported operating systems. The changed boundary must define: Event loops,
async and blocking work, request lifecycle, content decoding, authentication,
Fluent transactions, queues, WebSockets, shutdown, and deployment.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise Content decoding and object authorization with malformed and
  privileged fields. Run concurrent handlers with slow dependencies to check
  event-loop responsiveness and pool bounds.
- Disconnect streams and WebSockets during work and stop the server during
  Fluent transactions. Check cleanup, rollback, and request draining in the
  release build behind the configured proxy.
