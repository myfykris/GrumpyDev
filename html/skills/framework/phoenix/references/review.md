# Phoenix standard review

## Establish the operating model

Establish the project target: Phoenix, Elixir and OTP versions, LiveView use,
database, PubSub and cluster topology, session and proxy setup, release tooling,
and deployment environment. The changed boundary must define: Endpoint and plug
order, LiveView lifecycle, channels, PubSub, Ecto transactions, supervision,
sessions, presence, clustering, releases, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Endpoint and plug order, LiveView lifecycle, channels, PubSub, Ecto
transactions, supervision. Prove sessions, presence, clustering, releases,
deployment through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the actual Phoenix lifecycle and production
  pipeline: Endpoint and plug order, LiveView lifecycle, channels, PubSub, Ecto
  transactions, supervision. Use the actual framework pipeline and production
  build with representative services and configuration.
- Exercise failure and edge behavior for: sessions, presence, clustering,
  releases, deployment. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Elixir, Erlang/OTP, Phoenix, LiveView, and deployment versions apply?
- How do process ownership, supervision, socket state, PubSub, transactions,
  reconnect, and release rollout interact?

## Calibrate findings

- Downgrade when process lifecycles, authorization, reconnect, and release
  compatibility are integration-tested.
