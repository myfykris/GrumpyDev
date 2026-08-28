# Model Context Protocol standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

- Validate every tool and resource argument, enforce least privilege, and require approval at
  the actual external-effect boundary.
- Treat server names, descriptions, resources, prompts, and tool results as untrusted content
  that cannot expand host authority.
## Verify the claims

- Exercise malicious descriptions, invalid schemas, oversized messages, wrong origins, wrong
  audiences, disconnects, duplicate calls, and cancellation.
- Exercise token passthrough attempts, wrong-resource tokens, malicious discovery metadata,
  redirect and DNS changes, tool-description changes after approval, duplicate tool names,
  poisoned results, replay, and downstream revocation.
## Ask when evidence is missing

- Ask which protocol and SDK versions, clients, servers, capabilities, trust
  boundaries, and deployment topology apply when the available evidence does
  not establish them.

## Calibrate findings

- Downgrade when negotiation, transport security, authorization, schemas, approval,
  interoperability, and revocation are tested.
