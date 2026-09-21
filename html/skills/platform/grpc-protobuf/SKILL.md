---
name: gd-grpc-protobuf
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review gRPC and Protocol Buffers engineering work for schema compatibility, deadlines, retries, streaming, status details, metadata, limits, security, and rollout."
---

# gRPC and Protocol Buffers GrumpyDev review

## Quick checks

- Read proto files, field history, generated-code versions, interceptors,
  deadlines, retry policy, streaming handlers, limits, security, and
  compatibility tests.

- Trace unary and streaming calls through cancellation, partial messages, retry,
  backpressure, load balancing, and mixed-version rollout.

Watch especially for field numbers reused, presence confused with default
values, unknown fields discarded during read-modify-write, deadlines or
cancellation not propagated, retries enabled for non-idempotent calls, streams
without backpressure, and generated clients built from different schemas.

- Assess wire incompatibility, retry-amplified side effects, or unbounded
  streaming resource use under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the gRPC and Protocol
Buffers specialist.

## Verdict context

State protobuf compatibility, deadline and retry behavior, streaming bounds,
error contract, identity, and mixed-version evidence.
