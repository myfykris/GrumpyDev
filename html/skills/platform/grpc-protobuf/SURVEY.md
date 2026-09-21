# gRPC and Protocol Buffers survey contribution

## Applies when

Apply this contribution when services communicate through gRPC or protobuf contracts.

## Inspect

- Read proto files, field history, generated-code versions, interceptors,
  deadlines, retry policy, streaming handlers, limits, security, and
  compatibility tests.

## Ask when unresolved

- Which client, server, and schema versions overlap during rollout or replay?

- What deadlines, retry rules, message limits, streaming termination, and
  status details apply at each call boundary?

- Which runtime or deployment differences materially change future reviews:
  Client and server versions, proxies or gateways, load balancing, TLS and
  identity, retry policy, deadlines, streaming limits, generated artifact
  rollout, and mixed schemas?

## Record

Map durable gRPC and Protocol Buffers requirements and constraints to the
matching doctrine sections, runtime facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
