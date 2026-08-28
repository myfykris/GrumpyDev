# Elixir standard review

## Inspect additional evidence

- Trace process startup, ownership, mailbox growth, crash propagation, restart
  behavior, external calls, and node membership changes.

## Establish the operating model

Establish the project target: Elixir and OTP versions, release tooling, node
topology, clustering and discovery, deployment model, scheduler and resource
limits, and persistence dependencies. The changed boundary must define: BEAM
processes, supervision, linking and monitoring, mailbox growth, OTP behaviors,
fault isolation, clustering, distribution, hot upgrades, persistence boundaries,
and releases.

Define ownership, errors, cancellation, and concurrency for BEAM processes,
supervision, linking and monitoring, mailbox growth, OTP behaviors, fault
isolation. Verify version, package, native, serialization, and artifact
compatibility for clustering, distribution, hot upgrades, persistence
boundaries, releases across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared Elixir compiler and runtime
  targets: BEAM processes, supervision, linking and monitoring, mailbox growth,
  OTP behaviors, fault isolation. Use the real compiler or interpreter and
  supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: clustering, distribution, hot
  upgrades, persistence boundaries, releases. Exercise boundary values,
  encoding, cancellation, resource exhaustion, concurrency, dependency failure,
  and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which Elixir, Erlang/OTP, release target, and dependency versions define
  runtime behavior?
- Which process owns state and work, and how do supervision, messages, timeouts,
  overload, and upgrades behave?

## Calibrate findings

- Downgrade when process lifecycles are bounded and supervision, overload,
  failure, and release tests prove recovery.
