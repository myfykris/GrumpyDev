---
name: gd-model-context-protocol
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Model Context Protocol engineering work for capability negotiation, transports, authorization, tool schemas, resource trust, sessions, versioning, and local-server security."
---

# Model Context Protocol GrumpyDev review

## Quick checks

- Read MCP protocol and SDK versions, client and server roles, capabilities, transports,
  initialization, and session behavior.

- Inventory tools, resources, prompts, roots, sampling, elicitation, notifications, and any
  external effects or credentials.

Watch especially for local HTTP servers bound to all interfaces, missing Origin
validation, OAuth tokens accepted for the wrong audience, stdout logs corrupting
stdio messages, tool descriptions treated as trusted policy, client tokens
passed through to downstream APIs, authorization metadata used as an
unrestricted server-side fetch, broad filesystem roots, tool identity changing
after approval, and protocol-version drift.

- Assess remote access to an unauthenticated local server, token confusion, credential leakage,
  or unauthorized tool effects under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Model Context
Protocol specialist.

- [Focused rules](references/http-authorization-and-discovery.md):
  Read when the work uses Streamable HTTP, remote
  transport, OAuth, protected-resource
  metadata, authorization-server discovery, dynamic client metadata, redirect URIs,
  tokens, scopes, Origin validation, DNS, localhost binding, TLS, downstream APIs, or
  SSRF-sensitive metadata retrieval.
- [Focused rules](references/stdio-process-lifecycle.md):
  Read when the work uses stdio, launches or supervises
  a local server process, passes
  an environment, handles stdout or stderr, cancellation, exit, restart, or local
  credentials.
- [Focused rules](references/sessions-tool-identity-and-revocation.md):
  Read when the work changes session identity, reconnect
  or resumption, duplicate
  requests, cancellation, negotiated capabilities, tool or resource identity, schema
  drift, description changes, confusable names, approval binding, server revocation, or
  compatibility behavior.

## Verdict context

State versions, roles, transport, capabilities, token and downstream-resource boundaries,
discovery policy, tool identity and authority, local security, compatibility, and interop
evidence.
