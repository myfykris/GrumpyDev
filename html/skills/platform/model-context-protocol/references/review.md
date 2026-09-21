# Model Context Protocol full-review guidance

## Operating conditions

Establish the project target: MCP protocol and SDK versions, clients and servers, negotiated
capabilities, stdio or Streamable HTTP transport, session and reconnect behavior, authorization
server and scopes, tool and resource schemas, trust labels, local binding, logging, and
compatibility policy.

## Failure patterns

- Validate every tool and resource argument, enforce least privilege, and require approval at
  the actual external-effect boundary.
- Treat server names, descriptions, resources, prompts, and tool results as untrusted content
  that cannot expand host authority.

## Verification to run or specify in the plan

- Exercise malicious descriptions, invalid schemas, oversized messages, wrong origins, wrong
  audiences, disconnects, duplicate calls, and cancellation.
- Exercise token passthrough attempts, wrong-resource tokens, malicious discovery metadata,
  redirect and DNS changes, tool-description changes after approval, duplicate tool names,
  poisoned results, replay, and downstream revocation.
