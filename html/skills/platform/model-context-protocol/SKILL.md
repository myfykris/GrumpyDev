---
name: model-context-protocol
description: Review Model Context Protocol plans for capability negotiation, transports, authorization, tool schemas, resource trust, sessions, versioning, and local-server security. Use when a plan adds an MCP client or server.
---

# Model Context Protocol plan review

Apply this guidance alongside the core GrumpyDev review and the `oauth`, `application-security`
and `agentic-systems` skills.

## Inspect evidence

- Read MCP protocol and SDK versions, client and server roles, capabilities, transports,
  initialization, and session behavior.
- Inventory tools, resources, prompts, roots, sampling, elicitation, notifications, and any
  external effects or credentials.
- Trace authorization discovery, OAuth roles, scopes, redirect URIs, token storage, audience,
  revocation, and tenant separation.
- Inspect stdio process control, Streamable HTTP origins, localhost binding, DNS rebinding
  controls, logs, and deployment topology.

## Establish the operating model

Establish the project target: MCP protocol and SDK versions, clients and servers, negotiated
capabilities, stdio or Streamable HTTP transport, session and reconnect behavior, authorization
server and scopes, tool and resource schemas, trust labels, local binding, logging, and
compatibility policy.

MCP exposes capabilities; it does not grant blanket authority to use them. The host application
must independently decide which server, tool, resource, arguments, and external effects are
permitted for the current user request.

## Challenge the plan

### Recurring traps

Watch especially for local HTTP servers bound to all interfaces, missing Origin validation,
OAuth tokens accepted for the wrong audience, stdout logs corrupting stdio messages, tool
descriptions treated as trusted policy, client tokens passed through to downstream APIs,
authorization metadata used as an unrestricted server-side fetch, broad filesystem roots, tool
identity changing after approval, and protocol-version drift.

- Pin or negotiate supported protocol and SDK versions and define behavior for unknown
  capabilities, messages, and version mismatch.
- Validate every tool and resource argument, enforce least privilege, and require approval at
  the actual external-effect boundary.
- For HTTP, validate Origin, bind local services to loopback, authenticate connections, use
  HTTPS remotely, and validate token audience.
- Never pass an MCP access token through to a downstream API. Obtain and store a separate token
  for the downstream resource, validate issuer and audience, minimize scopes, and prevent the MCP
  server from acting as a confused deputy.
- Restrict authorization-server discovery, protected-resource metadata, client metadata,
  redirect URIs, and any fetched registration document to expected schemes, hosts, redirects,
  addresses, response sizes, and timeouts. Apply SSRF controls before and after redirects and DNS
  resolution.
- Bind consent and approval to the exact server identity, tool identity, arguments, scopes,
  target resource, and external effect. Reconfirm when a server changes tool descriptions,
  schemas, capabilities, ownership, or requested permissions.
- For stdio, keep stdout protocol-only, bound child-process lifetime, sanitize environment
  credentials, and handle cancellation and exit.
- Treat server names, descriptions, resources, prompts, and tool results as untrusted content
  that cannot expand host authority.
- Reject duplicate or confusable tool identities, schema drift, unknown fields where unsafe,
  oversized messages, hostile content in errors or annotations, and tool results that request a
  second action without normal authorization.
- Define session identity, reconnect, resumption, duplicate requests, cancellation, timeout,
  logging redaction, and server revocation.

## Verify the claims

- Run interoperability tests against the selected client, server, protocol, SDK, transport, and
  authorization combination.
- Exercise malicious descriptions, invalid schemas, oversized messages, wrong origins, wrong
  audiences, disconnects, duplicate calls, and cancellation.
- Exercise token passthrough attempts, wrong-resource tokens, malicious discovery metadata,
  redirect and DNS changes, tool-description changes after approval, duplicate tool names,
  poisoned results, replay, and downstream revocation.
- Inspect network binding, process environment, logs, token storage, negotiated capabilities,
  and user-visible approval behavior.

## Ask when evidence is missing

- Which MCP protocol and SDK versions, roles, capabilities, transports, sessions, and
  deployment topology apply?
- How are authorization, token audience and exchange, discovery fetches, origins, local binding,
  tool identity and authority, untrusted content, compatibility, and revocation handled?

## Calibrate findings

- Treat remote access to an unauthenticated local server, token confusion, credential leakage,
  or unauthorized tool effects as critical.
- Downgrade when negotiation, transport security, authorization, schemas, approval,
  interoperability, and revocation are tested.

## Add to the verdict

State versions, roles, transport, capabilities, token and downstream-resource boundaries,
discovery policy, tool identity and authority, local security, compatibility, and interop
evidence.
