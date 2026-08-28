---
name: mariadb
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review MariaDB plans and other engineering artifacts for MySQL divergence, engines, types, collations, indexes, locking, isolation, replication, Galera, online DDL, SQL modes, migrations, query plans, and recovery. Project applicability: the project stores or queries data in MariaDB or depends on MariaDB topology or operations."
---

# MariaDB GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `sql`,
application framework, deployment, and recovery skills. Every installed
companion that remains applicable to the project participates; the reviewed
target does not select the roster. Verify behavior against the project's
declared targets; do not silently substitute the newest version, a development
default, or a neighboring product's semantics.

## Lean review

- Inspect server and compatibility settings, engines, schemas, migrations,
  indexes, constraints, queries and plans, transaction boundaries, replication
  or Galera configuration, backups, and restore runbooks.

- Compare repository declarations with the effective schema and operating
  topology where safely available. Model files and migration sources are
  evidence, not proof of current state.

Watch especially for MySQL compatibility assumed without version evidence,
Galera certification conflicts and retry behavior, auto-increment assumptions
across nodes, collation differences, online DDL that still locks, replication
formats changing effects, and failover promoting data that is not current.

Lean mode is insufficient when this material severity condition may apply:

- Treat data loss, prolonged blocking, split-brain writes, broken uniqueness
  after collation change, or an untested recovery path for critical data as
  critical or high according to blast radius and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/schema-locking-and-query-plans.md):
  Read when the reviewed work directly or indirectly changes MariaDB or MySQL
  compatibility, engines, types, JSON
  behavior, SQL modes, character sets, collations, indexes, query plans, isolation,
  record or gap locks, deadlock retries, DDL, online algorithms, table rebuilds,
  temporary space, migrations, or mixed application versions.
- [Focused rules](references/replication-galera-and-recovery.md):
  Read when the reviewed work directly or indirectly changes replication, Galera,
  quorum, flow control, conflict
  handling, state transfer, failover, fencing, read routing, rejoin, backup,
  point-in-time recovery, encryption, retention, restore, or server-setting recovery.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
MariaDB and MySQL divergence, storage engines, types, collations, indexes,
locking, isolation, replication, Galera, online DDL, SQL modes, migrations,
query plans, and recovery, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
