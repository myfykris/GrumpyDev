---
name: model-context-protocol
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Model Context Protocol plans and other engineering artifacts for capability negotiation, transports, authorization, tool schemas, resource trust, sessions, versioning, and local-server security. Project applicability: the project includes or materially depends on a Model Context Protocol client or server."
---

# Model Context Protocol GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `oauth`, `application-security`
and `agentic-systems` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat remote access to an unauthenticated local server, token confusion, credential leakage,
  or unauthorized tool effects as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/http-authorization-and-discovery.md):
  Read when the reviewed work directly or indirectly uses Streamable HTTP, remote
  transport, OAuth, protected-resource
  metadata, authorization-server discovery, dynamic client metadata, redirect URIs,
  tokens, scopes, Origin validation, DNS, localhost binding, TLS, downstream APIs, or
  SSRF-sensitive metadata retrieval.
- [Focused rules](references/stdio-process-lifecycle.md):
  Read when the reviewed work directly or indirectly uses stdio, launches or supervises
  a local server process, passes
  an environment, handles stdout or stderr, cancellation, exit, restart, or local
  credentials.
- [Focused rules](references/sessions-tool-identity-and-revocation.md):
  Read when the reviewed work directly or indirectly changes session identity, reconnect
  or resumption, duplicate
  requests, cancellation, negotiated capabilities, tool or resource identity, schema
  drift, description changes, confusable names, approval binding, server revocation, or
  compatibility behavior.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State versions, roles, transport, capabilities, token and downstream-resource boundaries,
discovery policy, tool identity and authority, local security, compatibility, and interop
evidence.
