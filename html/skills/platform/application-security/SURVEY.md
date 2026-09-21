# Application security survey contribution

## Applies when

Apply this contribution when the project exposes security-sensitive application
behavior, trust boundaries, untrusted input, or attack surface.

## Inspect

For Application security, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation.

## Ask when unresolved

- Which actors cross the project's trust boundaries, and where are object,
  property, function, tenant, and state-change permissions enforced?

- Which hostile input or output context, abuse case, exceptional failure,
  credential failure, or incident response path can change the design?

- Which runtime or deployment differences materially change future reviews:
  Trust zones, internet exposure, identities, service accounts, tenant
  boundaries, TLS termination, proxy trust, egress, secret sources, logging,
  and security ownership?

## Record

Map durable Application security requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
