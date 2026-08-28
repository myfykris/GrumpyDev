# Performance and capacity standard review

## Establish the operating model

Establish the project target: SLOs, traffic and growth, workload mix, peak
factors, capacity budgets, test environments, autoscaling, resource limits, and
cost constraints. The changed boundary must define: Workload model, latency
distributions, throughput, concurrency, saturation, queuing, caches, load tests,
profiling, limits, scaling, and degradation.

Identify the workload model and owner, user-visible latency and throughput
objectives, concurrency and burst assumptions, resource and downstream budgets,
queue limits, scaling delay, cache behavior, degradation policy, and measurement
source. Prove the first saturated resource and the system's response before,
at, and beyond the expected peak rather than extrapolating from an average or a
single-component benchmark.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Measure production-shaped request and data mixes at idle, expected, peak and
  beyond-peak concurrency, reporting latency distributions, throughput, queues,
  errors and every constrained resource.
- Test cold and warm caches, burst arrival, uneven tenants, slow dependencies,
  scaling delay, quota exhaustion and the first bottleneck. Verify bounded
  queues, admission control and degradation protect critical work.
- Compare old and new versions at equal workload, including mixed-version
  rollout, drain and rollback, without hiding warmup or background work.

## Ask when evidence is missing

- What measured latency, throughput, concurrency, resource, and tail-percentile
  budget defines success?
- Which representative load shape, bottleneck, saturation point, and degraded
  mode support the capacity claim?

## Calibrate findings

- Downgrade when load is bounded and representative measurements demonstrate
  headroom and controlled degradation.
