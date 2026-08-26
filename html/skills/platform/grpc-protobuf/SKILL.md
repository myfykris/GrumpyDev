---
name: grpc-protobuf
description: Review gRPC and Protocol Buffers plans for schema compatibility, deadlines, retries, streaming, status details, metadata, limits, security, and rollout. Use when services communicate through gRPC or protobuf contracts.
---

# gRPC and Protocol Buffers plan review

Apply this guidance alongside the core GrumpyDev review and the
`distributed-systems` and `schema-evolution` skills.

## Inspect evidence

- Read proto files, field history, generated-code versions, interceptors,
  deadlines, retry policy, streaming handlers, limits, security, and
  compatibility tests.
- Trace unary and streaming calls through cancellation, partial messages, retry,
  backpressure, load balancing, and mixed-version rollout.

## Establish the operating model

Establish the project target: Protobuf and gRPC versions, language runtimes,
code-generation ownership, transport and proxy topology, retry policy, schema
registry, and compatibility window. The changed boundary must define: Field
evolution, presence, unknown fields, services, deadlines, cancellation, retries,
streaming, status mapping, metadata, load balancing, and generated code.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Field evolution, presence, unknown fields, services,
deadlines, cancellation. Prove retries, streaming, status mapping, metadata,
load balancing, generated code through rotation, overload, partial rollout,
drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for field numbers reused, presence confused with default
values, unknown fields discarded during read-modify-write, deadlines or
cancellation not propagated, retries enabled for non-idempotent calls, streams
without backpressure, and generated clients built from different schemas.

- Never reuse removed field numbers or names, and require intentional presence,
  default, enum, oneof, and unknown-field behavior.
- Propagate deadlines and cancellation across handlers and downstream calls; a
  client timeout must not leave expensive work running.
- Retry only idempotent operations with bounded budgets and account for
  transparent retries plus load-balancer behavior.
- Define stream flow control, message-size limits, half-close, reconnect,
  resume, and resource cleanup under slow peers.
- Standardize status codes and structured error details, secure transport and
  service identity, and test mixed generated clients and servers.

## Verify the claims

- Verify these behaviors through the effective gRPC and Protocol Buffers
  configuration and runtime topology: Field evolution, presence, unknown fields,
  services, deadlines, cancellation. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: retries, streaming, status mapping,
  metadata, load balancing, generated code. Exercise startup, readiness, normal
  load, overload, dependency loss, rotation, graceful drain, forced stop,
  failover, and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which client, server, and schema versions overlap during rollout or replay?
- What deadlines, retry rules, message limits, streaming termination, and status
  details apply at each call boundary?

## Calibrate findings

- Treat wire incompatibility, retry-amplified side effects, or unbounded
  streaming resource use as critical.
- Downgrade when compatibility tests, bounded calls, and idempotent retry
  behavior cover the supported version matrix.

## Add to the verdict

State protobuf compatibility, deadline and retry behavior, streaming bounds,
error contract, identity, and mixed-version evidence.
