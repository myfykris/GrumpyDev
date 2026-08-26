# Windows survey contribution

## Applicability

Apply this contribution when the project uses Windows or when its behavior
constrains a supported build, deployment, client, or operating environment.
Combine it with the implementation language, UI framework,
`application-security`, packaging, and deployment skills. Deduplicate shared
version, runtime, architecture, identity, data, security, and deployment
questions.

## Inspect before asking

Inspect supported Windows versions and architectures, manifests, services, users
and service accounts, ACLs, registry use, files, COM/WinRT registration, package
identity, installers, signatures, updates, event logs, dumps, and recovery
runbooks, dependency declarations, build and deployment files, CI workflows,
runbooks, and project documentation. Distinguish a committed project fact from a
local-machine default or a transient environment value. Do not access or mutate
an external system merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- Windows versions and editions.
- Architectures.
- Desktop, service, packaged, unpackaged, or server application model.
- Packaging and identity.
- Installer or Store channel.
- Service use.
- Privilege requirements.
- Code-signing ownership.
- Update policy.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: versions and editions, architecture,
  app model, service or desktop session, identity, ACLs, filesystem, registry,
  packaging, signing, updates, logging, and recovery.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later Windows reviews. Candidate subjects are: Windows versions and
editions, architectures, app model, packaging and identity, installer or store
channel, service use, privilege requirements, signing, and update policy.
- Align existing domain questions with this deployment guidance when it is
  material: versions and editions, architecture, app model, service or
  desktop session, identity, ACLs, filesystem, registry, packaging, signing,
  updates, logging, and recovery. Do not repeat the core profile confirmation.

## Record in .grump

Record Windows answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Windows survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Windows
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a minimum Windows/edition/architecture change, app-model or
package-identity change, service-account or privilege change, COM/WinRT boundary
change, installer/signing change, or update/recovery redesign. Also refresh the
contribution when evidence contradicts saved doctrine or the user explicitly
requests a context refresh.
