# Distributed partial failure, retries, and overload

Read this reference when the reviewed work directly or indirectly changes remote calls,
timeouts, retries, hedging,
backoff, circuit breaking, overload behavior, admission control, cancellation, uncertain
outcomes, or dependency failure.

## Partial failure and uncertain outcomes

- Reject reasoning that treats a remote call like a local function. The server
  may commit after the caller times out, the response may be lost, or a retry
  may race the original request.
- Require an explicit response to ambiguous completion: query by stable
  operation identity, retry an idempotent command, reconcile later, or surface
  an honest unknown state. Blind retry is not a general answer.
- Trace partial success across databases, queues, object stores, caches, and
  external APIs. State which state becomes authoritative and how abandoned or
  duplicate effects are detected and repaired.
- Challenge distributed transactions and sagas equally. A transaction protocol
  needs coordinator and blocking-failure analysis; a saga needs compensation
  semantics, ordering, irreversibility, and human-repair behavior.

## Timeouts, retries, and overload

- Require bounded timeouts at connection, request, stream, lock, lease, and
  overall-operation layers. Defaults can be infinite or misaligned across
  proxies, clients, servers, and queues.
- Assign one retry owner when possible. Multiply attempts across clients,
  gateways, services, SDKs, queues, and operators to expose retry amplification.
- Use exponential backoff, jitter, retry budgets, deadlines, and circuit or
  admission control where they match the failure mode. Retrying overload can
  turn a degraded dependency into a full outage.
- Retry only errors and operations proven safe to retry. Preserve a stable
  idempotency identity across attempts and define its scope, retention,
  concurrency behavior, result replay, and payload-conflict rule.
- Include backpressure and load shedding. Bounded queues, concurrency limits,
  and admission rules must preserve the work and tenants that matter most.
