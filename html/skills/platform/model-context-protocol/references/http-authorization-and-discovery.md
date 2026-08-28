# MCP HTTP authorization and discovery

Read this reference when the reviewed work directly or indirectly uses Streamable HTTP,
remote transport, OAuth,
protected-resource metadata, authorization-server discovery, dynamic client metadata,
redirect URIs, tokens, scopes, Origin validation, DNS, localhost binding, TLS,
downstream APIs, or SSRF-sensitive metadata retrieval.

## Review requirements

- For HTTP, validate Origin, bind local services to loopback, authenticate connections, use
  HTTPS remotely, and validate token audience.

- Never pass an MCP access token through to a downstream API. Obtain and store a separate token
  for the downstream resource, validate issuer and audience, minimize scopes, and prevent the MCP
  server from acting as a confused deputy.

- Restrict authorization-server discovery, protected-resource metadata, client metadata,
  redirect URIs, and any fetched registration document to expected schemes, hosts, redirects,
  addresses, response sizes, and timeouts. Apply SSRF controls before and after redirects and DNS
  resolution.

## Verify the claims

- Run interoperability tests against the selected client, server, protocol, SDK, transport, and
  authorization combination.
