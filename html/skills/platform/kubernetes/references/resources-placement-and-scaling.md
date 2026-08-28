# Kubernetes resources, placement, and scaling

Read this reference when the reviewed work directly or indirectly changes requests,
limits, CPU or memory behavior,
scheduling, affinity, topology spread, taints, priorities, quotas, autoscaling, cluster
scaling, capacity, or overload behavior.

## Resources, placement, and scaling

- Derive CPU and memory requests from observed normal and peak use plus startup
  behavior. Requests drive scheduling; limits change runtime behavior and can
  cause throttling or termination.
- Account for ephemeral storage, process counts, file descriptors, huge pages,
  GPUs, local volumes, and sidecars where applicable. Sidecars and init
  containers participate in capacity and lifecycle decisions.
- Review replica minimums, zone and node spread, anti-affinity, taints,
  tolerations, priorities, preemption, and disruption budgets as one
  availability design. Rules that cannot be scheduled do not improve safety.
- Validate autoscaling signals, stabilization, minimums, maximums, cold-start
  time, queue or request backlog, downstream capacity, and scale-to-zero
  behavior. CPU scaling cannot fix a serial bottleneck and can overload a
  database.
- Include cluster autoscaler latency, quota, node-pool maximums, image pull
  time, and zonal capacity. A pod maximum above available node capacity is not a
  capacity plan.

## Verify the claims

- Load test resource and autoscaling assumptions through startup and peak,
  including downstream limits and cluster scaling latency.
