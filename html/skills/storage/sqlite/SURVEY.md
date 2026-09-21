# SQLite survey contribution

## Applies when

Apply this contribution when an application embeds SQLite or shares a SQLite database
file.

## Inspect

- Establish the exact SQLite library version, build options, wrapper or driver
  version, filesystem, and process model.

## Ask when unresolved

- Which SQLite library version, build options, filesystem, process model,
  journal mode, and connection ownership apply?

- How are writer contention, busy handling, migrations, type affinity, backup,
  and file replacement coordinated?

- Which runtime or deployment differences are material for future reviews:
  Library version, process and connection topology, filesystem and mount, WAL
  behavior, write concurrency, packaging, backup, restore, encryption if used,
  and network-filesystem exclusions?

## Record

Map SQLite data guarantees to `Requirements`, accepted tradeoffs to `Accepted
decisions`, topology and recovery facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
