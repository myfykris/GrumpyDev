---
name: performance-capacity
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review performance and capacity engineering work for measurable budgets, representative load, bottlenecks, queueing, saturation, tail latency, scaling, and degradation."
---

# Performance and capacity GrumpyDev review

Apply this guidance alongside the core GrumpyDev review, the `observability`
skill, and applicable installed runtime, storage, and deployment-platform
specialists.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read workload shape, latency and throughput targets, profiles, query plans,
  resource metrics, load tests, autoscaling, and cost models.

- Trace a representative request at steady state, burst, saturation, dependency
  slowdown, cold start, and recovery.

Watch especially for microbenchmarks extrapolated to systems, averages hiding
tail latency, coordinated omission, warm-cache-only tests, load generators
becoming the bottleneck, one saturated dependency hidden by aggregate CPU, and
throughput gains purchased by unacceptable queue growth.

Lean mode is insufficient when this material severity condition may apply:

- Treat an unbounded queue, hard capacity cliff, or unsupported claim on a
  critical path as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Performance and capacity evidence, operating model,
failure, verification, question, and calibration guidance. Never load
`SURVEY.md` during an ordinary review.

## Add to the verdict

State measurable budgets, workload realism, bottleneck evidence, saturation
controls, scaling limits, and cost impact.
