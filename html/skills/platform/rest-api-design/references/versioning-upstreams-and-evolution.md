# REST versioning, upstreams, and evolution

Read this reference when the reviewed work directly or indirectly changes public
contracts, independently deployed
clients, versions, deprecation, compatibility, error formats, third-party or upstream
responses, redirects, exposed routes, administrative surfaces, retirement, mixed
versions, or rollout sequencing.

## Review requirements

- Analyze backward and forward compatibility across independently deployed
  clients. Adding a required field or tightening validation is a breaking
  change.

- Treat upstream and third-party API data as untrusted. Validate its schema and
  semantics, bound response and decompression size, set timeouts, restrict
  redirects, and prevent returned URLs or fields from bypassing local policy.

- Inventory every exposed version, host, route, method, documentation endpoint,
  administrative surface, and debug mode. Define owners and retirement dates so
  an obsolete endpoint cannot silently escape current controls.
