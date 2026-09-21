---
name: gd-performance-capacity
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review performance and capacity engineering work for measurable budgets, representative load, bottlenecks, queueing, saturation, tail latency, scaling, and degradation."
---

# Performance and capacity GrumpyDev review

## Quick checks

- Read workload shape, latency and throughput targets, profiles, query plans,
  resource metrics, load tests, autoscaling, and cost models.

- Trace a representative request at steady state, burst, saturation, dependency
  slowdown, cold start, and recovery.

Watch especially for microbenchmarks extrapolated to systems, averages hiding
tail latency, coordinated omission, warm-cache-only tests, load generators
becoming the bottleneck, one saturated dependency hidden by aggregate CPU, and
throughput gains purchased by unacceptable queue growth.

- Assess an unbounded queue, hard capacity cliff, or unsupported claim on a
  critical path under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Performance and
capacity specialist.

## Verdict context

State measurable budgets, workload realism, bottleneck evidence, saturation
controls, scaling limits, and cost impact.
