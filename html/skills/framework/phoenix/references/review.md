# Phoenix full-review guidance

## Operating conditions

Establish the project target: Phoenix, Elixir and OTP versions, LiveView use,
database, PubSub and cluster topology, session and proxy setup, release tooling,
and deployment environment. The changed boundary must define: Endpoint and plug
order, LiveView lifecycle, channels, PubSub, Ecto transactions, supervision,
sessions, presence, clustering, releases, and deployment.

## Failure patterns

- Verify router pipeline and plug order for sessions, CSRF, authentication,
  authorization, parsing, and proxy behavior.
- Keep authorization at context or resource boundaries instead of trusting
  routes, assigns, or client events.
- Check LiveView and channel process lifetime, reconnect behavior, stale state,
  mailbox growth, temporary assigns, and upload limits.
- Require Ecto migration, transaction, constraint, query, and mixed-version
  safety with explicit backfill behavior.
- Test clustered PubSub, node loss, rolling releases, socket reconnect, job
  retries, and graceful drain.

## Verification to run or specify in the plan

- Reconnect LiveViews and channels while state changes and permissions expire.
  Check event authorization, duplicate submissions, mailbox growth, and
  restoration rather than relying on existing assigns.
- Exercise Ecto operations and migrations with competing writes and
  overlapping releases. Where clustered PubSub is used, lose a node during
  delivery and verify the application's resynchronization path.
