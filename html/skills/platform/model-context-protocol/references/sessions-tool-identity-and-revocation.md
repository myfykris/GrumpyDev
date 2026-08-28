# MCP sessions, tool identity, and revocation

Read this reference when the reviewed work directly or indirectly changes session
identity, reconnect or resumption,
duplicate requests, cancellation, negotiated capabilities, tool or resource identity,
schema drift, description changes, confusable names, approval binding, server
revocation, or compatibility behavior.

## Review requirements

- Pin or negotiate supported protocol and SDK versions and define behavior for unknown
  capabilities, messages, and version mismatch.

- Bind consent and approval to the exact server identity, tool identity, arguments, scopes,
  target resource, and external effect. Reconfirm when a server changes tool descriptions,
  schemas, capabilities, ownership, or requested permissions.

- Reject duplicate or confusable tool identities, schema drift, unknown fields where unsafe,
  oversized messages, hostile content in errors or annotations, and tool results that request a
  second action without normal authorization.

- Define session identity, reconnect, resumption, duplicate requests, cancellation, timeout,
  logging redaction, and server revocation.

## Verify the claims

- Inspect network binding, process environment, logs, token storage, negotiated capabilities,
  and user-visible approval behavior.


## Ask when evidence is missing

- Which MCP protocol and SDK versions, roles, capabilities, transports, sessions, and
  deployment topology apply?

- How are authorization, token audience and exchange, discovery fetches, origins, local binding,
  tool identity and authority, untrusted content, compatibility, and revocation handled?
