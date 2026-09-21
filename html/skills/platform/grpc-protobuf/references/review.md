# gRPC and Protocol Buffers full-review guidance

## Operating conditions

Establish the project target: Protobuf and gRPC versions, language runtimes,
code-generation ownership, transport and proxy topology, retry policy, schema
registry, and compatibility window. The changed boundary must define: Field
evolution, presence, unknown fields, services, deadlines, cancellation, retries,
streaming, status mapping, metadata, load balancing, and generated code.

## Failure patterns

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

## Verification to run or specify in the plan

- Generate every supported client and server from the reviewed proto set and
  run old-new combinations through serialization, unknown fields, presence,
  default values, status mapping and metadata handling.
- Exercise deadlines, cancellation, retry after an ambiguous result, partial
  and long-lived streams, oversized messages, backpressure, connection loss and
  endpoint movement through the actual proxy and load balancer.
- Roll out and roll back client and server versions while calls and streams are
  active, verifying removed fields or methods are not reused incompatibly.
