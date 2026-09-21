# Performance and capacity full-review guidance

## Operating conditions

Establish the project target: SLOs, traffic and growth, workload mix, peak
factors, capacity budgets, test environments, autoscaling, resource limits, and
cost constraints. The changed boundary must define: Workload model, latency
distributions, throughput, concurrency, saturation, queuing, caches, load tests,
profiling, limits, scaling, and degradation.

## Failure patterns

- Require percentile budgets and workload distributions; averages hide the users
  who wait longest.
- Benchmark production-sized data, realistic concurrency, cache states, network
  latency, payloads, and downstream behavior.
- Identify the first saturated resource, queue growth, admission control,
  timeouts, backpressure, and load-shedding policy.
- Separate microbenchmark gains from end-to-end impact and include startup,
  allocation, garbage collection, and contention costs.
- Prove scaling speed, safe maximum capacity, degraded-mode behavior, recovery
  after overload, and cost per useful unit.

## Verification to run or specify in the plan

- Measure production-shaped request and data mixes at idle, expected, peak and
  beyond-peak concurrency, reporting latency distributions, throughput, queues,
  errors and every constrained resource.
- Test cold and warm caches, burst arrival, uneven tenants, slow dependencies,
  scaling delay, quota exhaustion and the first bottleneck. Verify bounded
  queues, admission control and degradation protect critical work.
- Compare old and new versions at equal workload, including mixed-version
  rollout, drain and rollback, without hiding warmup or background work.
