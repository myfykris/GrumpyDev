# Serverless standard review

## Inspect additional evidence

- Trace cold start, duplicate event, partial effect, timeout, throttling,
  dependency slowdown, deployment, and regional failure.

## Establish the operating model

Establish the project target: Provider and runtimes, regions, triggers,
concurrency and timeout limits, network attachment, identity, packaging,
deployment tool, and local-test limits. The changed boundary must define:
Invocation lifecycle, concurrency, cold starts, timeouts, retries, events,
idempotency, state, networking, IAM, packaging, observability, and deployment.

Identify the exact trigger contract, delivery and retry semantics, function
identity, concurrency and timeout limits, package and runtime, network path,
ephemeral and durable state, downstream quotas, regional behavior, deployment
owner and recovery path. Prove duplicates, cold starts, throttling, timeout after
a partial effect, dependency loss and mixed function revisions preserve
idempotency and stay within downstream capacity.

## Challenge the reviewed work

### Recurring traps

- Design handlers for duplicate and out-of-order delivery with idempotency at
  the side-effect boundary.
- Bound concurrency against databases and downstream quotas; automatic scale can
  automate an outage.
- Include cold start, package size, initialization, connection reuse, execution
  duration, and memory in latency evidence.
- Keep durable state outside ephemeral execution and make timeout, cancellation,
  continuation, and poison-event handling explicit.
- Model request, duration, transfer, logging, provisioned capacity, and idle
  alternatives before claiming lower cost.

## Verify the claims

- Deploy the real package and configuration to a representative isolated
  environment and measure cold and warm startup, memory, duration, network,
  identity and initialization behavior.
- Inject duplicate and out-of-order events, throttling, timeout before and after
  effects, dependency slowdown, downstream quota exhaustion, poison events and
  regional or service failure.
- Run old and new function revisions together and roll back while events are in
  flight, verifying idempotency, payload compatibility, observability and state
  recovery.

## Ask when evidence is missing

- Which provider, service, runtime version, deployment mode, trigger, and
  regional limits apply?
- What delivery, concurrency, timeout, retry, state, networking, permission, and
  cost behavior follows from that platform?

## Calibrate findings

- Downgrade when the exact provider semantics are known and load, idempotency,
  limits, and recovery are tested.
