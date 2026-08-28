# Application security survey contribution

## Applicability

Apply this contribution when the project exposes security-sensitive application
behavior, trust boundaries, untrusted input, or attack surface.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Application security, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Security requirements, data sensitivity, threat
  actors, identity providers, trust zones, compliance constraints, secret
  handling, scanning, and incident ownership.
- Review doctrine for: Trust boundaries, threat modeling, input handling,
  output contexts, authentication, object and function authorization, sessions,
  injection, SSRF, file and upload handling, deserialization, exceptional
  failure, crypto use, abuse, dependencies, logging, and incident response.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Trust zones, internet exposure, identities, service
  accounts, tenant boundaries, TLS termination, proxy trust, egress, secret
  sources, logging, and security ownership.

## Ask only when materially unresolved

- Which actors cross each changed trust boundary, and where are object,
  property, function, tenant, and state-change permissions enforced?
- Which hostile input or output context, abuse case, exceptional failure,
  credential failure, or incident response path can change the design?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Trust zones, internet exposure,
  identities, service accounts, tenant boundaries, TLS termination, proxy
  trust, egress, secret sources, logging, and security ownership? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Application security answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Application security deployment facts on the affected
`DEP-###` profile. Use a referenced `INF-###` entry for a material component
shared by several profiles. Preserve separate state, support, ownership,
confidence, source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable
Application security doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey Application security when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
