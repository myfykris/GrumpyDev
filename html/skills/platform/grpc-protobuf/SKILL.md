---
name: grpc-protobuf
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review gRPC and Protocol Buffers plans and other engineering artifacts for schema compatibility, deadlines, retries, streaming, status details, metadata, limits, security, and rollout. Project applicability: services communicate through gRPC or protobuf contracts."
---

# gRPC and Protocol Buffers GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the
`distributed-systems` and `schema-evolution` skills.

## Lean review

- Read proto files, field history, generated-code versions, interceptors,
  deadlines, retry policy, streaming handlers, limits, security, and
  compatibility tests.

- Trace unary and streaming calls through cancellation, partial messages, retry,
  backpressure, load balancing, and mixed-version rollout.

Watch especially for field numbers reused, presence confused with default
values, unknown fields discarded during read-modify-write, deadlines or
cancellation not propagated, retries enabled for non-idempotent calls, streams
without backpressure, and generated clients built from different schemas.

Lean mode is insufficient when this material severity condition may apply:

- Treat wire incompatibility, retry-amplified side effects, or unbounded
  streaming resource use as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete gRPC and Protocol Buffers evidence, operating model,
failure, verification, question, and calibration guidance. Never load
`SURVEY.md` during an ordinary review.

## Add to the verdict

State protobuf compatibility, deadline and retry behavior, streaming bounds,
error contract, identity, and mixed-version evidence.
