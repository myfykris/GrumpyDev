# MariaDB survey contribution

## Applicability

Apply this contribution when the project uses MariaDB or when its behavior
constrains a supported build, deployment, client, or operating environment.
Combine it with the `sql`, application framework, deployment, and recovery
skills. Deduplicate shared version, runtime, architecture, identity, data,
security, and deployment questions.

## Inspect before asking

Inspect server and compatibility settings, engines, schemas, migrations,
indexes, constraints, queries and plans, transaction boundaries, replication or
Galera configuration, backups, and restore runbooks, dependency declarations,
build and deployment files, CI workflows, runbooks, and project documentation.
Distinguish a committed project fact from a local-machine default or a transient
environment value. Do not access or mutate an external system merely to complete
setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- MariaDB version and distribution.
- Storage engines.
- SQL modes.
- Character sets and collations.
- Primary/replica or Galera topology.
- Isolation policy.
- Migration tooling.
- Backup, restore, and recovery objectives.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: product and version, engine, SQL modes,
  character settings, topology, Galera or replication, isolation, migration,
  backup, restore, failover, and hosting coverage.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later MariaDB reviews. Candidate subjects are: MariaDB version,
engine, SQL modes, character set and collation, topology, Galera or replication,
isolation, migration tooling, and backup or restore objectives.
- Align existing domain questions with this deployment guidance when it is
  material: product and version, engine, SQL modes, character
  settings, topology, Galera or replication, isolation, migration, backup,
  restore, failover, and hosting coverage. Do not repeat the core profile
  confirmation.

## Record in .grump

Record MariaDB answers in project technology, data, schema, consistency,
deployment, and recovery doctrine. Preserve source and scope. Record a material
unknown as unresolved doctrine instead of guessing.

Map existing MariaDB survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual query plans, one-off migration steps, current host or replica
identities, transient load readings, and copied data out of durable MariaDB
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a MariaDB major version or distribution change, MySQL-to-MariaDB
migration, engine/collation/SQL-mode change, replication or Galera redesign,
migration-tool change, or recovery-objective change. Also refresh the
contribution when evidence contradicts saved doctrine or the user explicitly
requests a context refresh.
