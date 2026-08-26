---
name: performance-capacity
description: Review performance and capacity plans for measurable budgets, representative load, bottlenecks, queueing, saturation, tail latency, scaling, and degradation. Use when a plan claims or changes latency, throughput, resource, or scale behavior.
---

# Performance and capacity plan review

Apply this guidance alongside the core GrumpyDev review, the `observability`
skill, and applicable installed runtime, storage, and deployment-platform
specialists.

## Inspect evidence

- Read workload shape, latency and throughput targets, profiles, query plans,
  resource metrics, load tests, autoscaling, and cost models.
- Trace a representative request at steady state, burst, saturation, dependency
  slowdown, cold start, and recovery.

## Establish the operating model

Establish the project target: SLOs, traffic and growth, workload mix, peak
factors, capacity budgets, test environments, autoscaling, resource limits, and
cost constraints. The changed boundary must define: Workload model, latency
distributions, throughput, concurrency, saturation, queuing, caches, load tests,
profiling, limits, scaling, and degradation.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Workload model, latency distributions, throughput,
concurrency, saturation, queuing. Prove caches, load tests, profiling, limits,
scaling, degradation through rotation, overload, partial rollout, drain, forced
stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for microbenchmarks extrapolated to systems, averages hiding
tail latency, coordinated omission, warm-cache-only tests, load generators
becoming the bottleneck, one saturated dependency hidden by aggregate CPU, and
throughput gains purchased by unacceptable queue growth.

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

- Verify these behaviors through the effective Performance and capacity
  configuration and runtime topology: Workload model, latency distributions,
  throughput, concurrency, saturation, queuing. Use effective rendered
  configuration and deployable artifacts in a representative identity, topology,
  capacity, and policy boundary.
- Exercise failure and edge behavior for: caches, load tests, profiling, limits,
  scaling, degradation. Exercise startup, readiness, normal load, overload,
  dependency loss, rotation, graceful drain, forced stop, failover, and recovery
  where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- What measured latency, throughput, concurrency, resource, and tail-percentile
  budget defines success?
- Which representative load shape, bottleneck, saturation point, and degraded
  mode support the capacity claim?

## Calibrate findings

- Treat an unbounded queue, hard capacity cliff, or unsupported claim on a
  critical path as critical.
- Downgrade when load is bounded and representative measurements demonstrate
  headroom and controlled degradation.

## Add to the verdict

State measurable budgets, workload realism, bottleneck evidence, saturation
controls, scaling limits, and cost impact.
