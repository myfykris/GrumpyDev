# REST authorization, input, and abuse

Read this reference when the reviewed work directly or indirectly changes
authentication, object or property
authorization, tenant isolation, mutable fields, validation, bulk operations, uploads,
body or decompression limits, expensive filters, automation-sensitive business flows,
rate limits, or abuse controls.

## Review requirements

- Check authorization for every object, property, function, and state
  transition, not only authentication at the route. Apply request property
  allowlists and response filtering at the server; include identifier
  enumeration, cross-tenant access, bulk operations, and stale permissions.

- Bound request bytes, decompression, parsing, result size, page size, uploaded
  files, expensive filters, concurrent work, and downstream cost by authenticated
  actor and tenant where possible. An IP-only rate limit is not an abuse model.

- Identify business flows whose value can be abused through automation, such as
  reservations, invitations, recovery, signup, or purchases. Define economic,
  identity, sequence, and velocity controls in addition to transport rate limits.

## Verify the claims

- Run an authorization matrix across actor, tenant, object, property, function,
  and state, including bulk requests and identifiers obtained from another
  account.


## Ask when evidence is missing

- What idempotency, object and property authorization, business-flow abuse,
  resource limits, upstream trust, pagination, caching, and compatibility
  behavior applies?
