# Performance and capacity survey contribution

## Applies when

Apply this contribution when the project has material latency, throughput, resource,
scale, availability, or cost requirements.

## Inspect

- Read workload shape, latency and throughput targets, profiles, query plans,
  resource metrics, load tests, autoscaling, and cost models.

## Ask when unresolved

- What measured latency, throughput, concurrency, resource, and tail-percentile
  budget defines success?

- Which representative load shape, bottleneck, saturation point, and degraded
  mode support the capacity claim?

- Which runtime or deployment differences materially change future reviews:
  Instance and resource limits, replicas, autoscaling, quotas, downstream
  ceilings, network path, cold start, failure domains, load-test environment,
  and capacity owner?

## Record

Map durable Performance and capacity requirements and constraints to the
matching doctrine sections, runtime facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
