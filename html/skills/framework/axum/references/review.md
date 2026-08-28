# Axum standard review

## Inspect additional evidence

- Trace request data, blocking work, spawned tasks, streaming, cancellation,
  error conversion, timeouts, and shutdown.

## Establish the operating model

Establish the project target: Axum, Tokio and tower versions, runtime topology,
state ownership, proxy and TLS arrangement, request limits, and deployment
target. The changed boundary must define: Router and extractor behavior, state
and tower layers, async blocking, errors, body limits, streaming, cancellation,
graceful shutdown, and proxy trust.

Assign lifecycle, state, dependency, persistence, and security ownership for
Router and extractor behavior, state and tower layers, async blocking, errors,
body limits. Prove streaming, cancellation, graceful shutdown, proxy trust
through startup, invalid or denied work, cancellation, background execution,
mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

- Require thread-safe state with explicit ownership and reject locks held across
  await points.
- Check Tower layer order, timeout coverage, concurrency limits, backpressure,
  tracing, and authentication placement.
- Bound bodies, decompression, extractors, streams, and fan-out before untrusted
  input reaches expensive work.
- Require typed but non-sensitive error mapping and ownership for disconnected
  clients, spawned tasks, and websockets.
- Test production serving, proxy headers, graceful drain, dependency failure,
  and runtime saturation.

## Verify the claims

- Verify these behaviors through the actual Axum lifecycle and production
  pipeline: Router and extractor behavior, state and tower layers, async
  blocking, errors, body limits. Use the actual framework pipeline and
  production build with representative services and configuration.
- Exercise failure and edge behavior for: streaming, cancellation, graceful
  shutdown, proxy trust. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Axum, Rust, Tokio, Tower, and HTTP stack versions apply?
- How do router state, extractors, layers, blocking work, cancellation, limits,
  and shutdown interact?

## Calibrate findings

- Downgrade when version-specific layer order, state ownership, limits, and
  shutdown behavior are tested.
