# Kubernetes health, lifecycle, and rollouts

Read this reference when the reviewed work directly or indirectly changes probes,
startup, readiness, liveness,
termination, pre-stop behavior, disruption budgets, Deployment or StatefulSet rollout
strategy, draining, mixed versions, migration order, rollback, or controller
replacement.

## Health, lifecycle, and rollout

- Give startup, readiness, and liveness probes distinct jobs. Startup probes
  protect slow initialization; readiness controls traffic; liveness is only for
  states where restarting is the correct recovery. Bad probes manufacture
  outages and restart loops.
- Verify probe endpoints under overload and dependency loss. A readiness probe
  that requires every optional dependency can remove all replicas at once; a
  liveness probe that fails on a remote dependency amplifies that outage.
- Align `preStop`, signal handling, endpoint removal, load-balancer behavior,
  queue visibility, connection draining, and `terminationGracePeriodSeconds`.
  Confirm the process actually receives and honors the expected signal.
- Check rollout surge, unavailable capacity, progress deadlines, min-ready time,
  disruption budgets, and existing headroom together. Individually valid
  settings can deadlock an upgrade or exceed node capacity.
- Prove old/new application, worker, message, cache, and schema compatibility.
  Kubernetes rollback only changes workload objects; it does not reverse data
  migrations, external effects, or already-consumed messages.

## Verify the claims

- Observe cold start, readiness transitions, steady load, overload, dependency
  loss, graceful termination, forced termination, rolling updates, and rollback.
