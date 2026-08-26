# gRPC and Protocol Buffers survey contribution

## Applicability

Apply this contribution when services communicate through gRPC or protobuf
contracts. Skip it when gRPC and Protocol Buffers does not constrain a supported
build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For gRPC and Protocol Buffers, inspect version declarations, effective
configuration sources, rendered artifacts, infrastructure and identity policy,
build and deployment workflows, service objectives, operational runbooks, and
project documentation. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Protobuf and gRPC versions, language runtimes,
  code-generation ownership, transport and proxy topology, retry policy, schema
  registry, and compatibility window.
- Review doctrine for: Field evolution, presence, unknown fields, services,
  deadlines, cancellation, retries, streaming, status mapping, metadata, load
  balancing, and generated code.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Client and server versions, proxies or gateways,
  load balancing, TLS and identity, retry policy, deadlines, streaming limits,
  generated artifact rollout, and mixed schemas.

## Ask only when materially unresolved

- Which client, server, and schema versions overlap during rollout or replay?
- What deadlines, retry rules, message limits, streaming termination, and status
  details apply at each call boundary?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Client and server versions, proxies or
  gateways, load balancing, TLS and identity, retry policy, deadlines,
  streaming limits, generated artifact rollout, and mixed schemas? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record gRPC and Protocol Buffers answers in project technology, runtime,
security, deployment, verification, and operational doctrine. Preserve source
and scope. Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed gRPC and Protocol Buffers deployment facts on the affected
`DEP-###` profile. Use a referenced `INF-###` entry for a material component
shared by several profiles. Preserve separate state, support, ownership,
confidence, source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable gRPC and
Protocol Buffers doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey gRPC and Protocol Buffers when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
