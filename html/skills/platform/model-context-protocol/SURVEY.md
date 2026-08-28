# Model Context Protocol survey contribution

## Applicability

Apply this contribution when the project includes or materially depends on a Model
Context Protocol client or server.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for Model Context Protocol. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: MCP protocol and SDK versions, clients and servers, negotiated
  capabilities, stdio or Streamable HTTP transport, session and reconnect behavior,
  authorization server and scopes, tool and resource schemas, trust labels, local binding,
  logging, and compatibility policy.
- Review doctrine: MCP exposes capabilities; it does not grant blanket authority to use them.
  The host application must independently decide which server, tool, resource, arguments, and
  external effects are permitted for the current user request. MCP access tokens must not be
  passed through to downstream APIs, and remote metadata remains an SSRF boundary.
- Deployment-profile facts: MCP protocol and SDK versions, client and server topology,
  transports, bind addresses, origins, TLS, authorization metadata, token audiences, process
  environment, capability allowlists, timeouts, logs, and disable controls.

## Ask only when materially unresolved

- Which MCP protocol and SDK versions, roles, capabilities, transports, sessions, and
  deployment topology apply?
- How are authorization, token audience and exchange, discovery fetches, origins, local binding,
  tool identity and authority, untrusted content, compatibility, and revocation handled?

## Record in .grump

Record confirmed Model Context Protocol answers as project technology, architecture, security,
deployment, verification, and operational doctrine. Preserve source, scope, confidence, and
environment differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Model Context Protocol doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Model Context Protocol when the protocol version, client or server roster,
transport, tool or resource surface, authentication method, trust boundary, consent
policy, or capability-negotiation behavior materially changes. Also re-survey when
evidence conflicts with saved doctrine or the user requests a context refresh.
