# Windows survey contribution

## Applies when

Apply this contribution when the project uses Windows or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect supported Windows versions and architectures, manifests, services,
  users and service accounts, ACLs, registry use, files, COM/WinRT registration,
  package identity, installers, signatures, updates, event logs, dumps, and
  recovery runbooks.

## Ask when unresolved

- Which of these durable facts materially change future reviews: Windows
  versions and editions, architectures, app model, packaging and identity,
  installer or store channel, service use, privilege requirements, signing, and
  update policy?

- Which runtime or deployment differences are material for future reviews:
  versions and editions, architecture, app model, service or desktop session,
  identity, ACLs, filesystem, registry, packaging, signing, updates, logging,
  and recovery?

## Record

Map durable Windows requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
