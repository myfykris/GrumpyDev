# Application identity, sessions, and authorization

Read this reference when the reviewed work directly or indirectly changes
authentication, object or property
authorization, tenant isolation, session creation or rotation, cookies, CSRF, CORS,
account recovery, revocation, role changes, or security-sensitive state transitions.

## Review requirements

- Require authorization at every object, property, function, and state-change
  boundary. Test anonymous, lower-privilege, cross-tenant, stale-role, and
  guessed-identifier requests; a hidden button or authenticated route is not
  access control.

- Define session rotation, revocation, CSRF, CORS, cookie flags, rate limits,
  abuse detection, and account recovery explicitly.

## Verify the claims

- Exercise login, session creation, rotation, refresh, logout, revocation,
  account recovery and role or tenant changes through the effective identity,
  proxy, cookie and data-access path.

- Build an authorization matrix covering actor, tenant, object, property,
  function, and state. Run its denied cases through the real entry point and
  data boundary, not only a mocked policy function.


## Ask when evidence is missing

- Which actors cross each changed trust boundary, and where are object,
  property, function, tenant, and state-change permissions enforced?
