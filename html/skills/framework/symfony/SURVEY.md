# Symfony survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Symfony.

## Inspect

- Read bundle and framework configuration, service definitions, event
  subscribers, routes, security firewalls and voters, Doctrine mappings and
  migrations, Messenger, cache, and tests.

## Ask when unresolved

- Which PHP, Symfony, runtime, container, database, cache, and Messenger
  versions or transports apply?

- How do service scopes, security voters, validation, transactions, messages,
  retries, and migrations interact?

- Which runtime or deployment differences are material for future reviews: PHP
  SAPI and server, FPM pools, Messenger workers, scheduler, cache, sessions,
  files, proxy, compiled container, migrations, worker restart, and deployment?

## Record

Map durable Symfony version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
