# Elixir full-review guidance

## Operating conditions

Establish the project target: Elixir and OTP versions, release tooling, node
topology, clustering and discovery, deployment model, scheduler and resource
limits, and persistence dependencies. The changed boundary must define: BEAM
processes, supervision, linking and monitoring, mailbox growth, OTP behaviors,
fault isolation, clustering, distribution, hot upgrades, persistence boundaries,
and releases.

## Failure patterns

- Require a deliberate supervisor strategy and restart intensity for every
  long-lived process.
- Check mailbox growth, unbounded tasks, caller timeouts, stale replies, message
  ordering, and overload behavior.
- Separate recoverable process crashes from corrupted or externally persisted
  state that restart cannot repair.
- Verify idempotency and delivery semantics across Oban, Broadway, queues,
  retries, and node failures when used.
- Test rolling releases, configuration at runtime, clustering partitions, and
  dependency outages rather than only happy-path process tests.

## Verification to run or specify in the plan

- Crash supervised children during in-flight work and verify restart behavior
  against persisted state. Delay replies and overload mailboxes to check
  timeout handling, bounded work, and protection against repeated external
  effects.
- Boot the packaged release with runtime configuration and interrupt its
  dependencies. If clustering applies, partition and rejoin nodes while
  checking recovery, message handling, and rolling-version compatibility.
