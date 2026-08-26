# Shared infrastructure behavior

Three execution profiles use the same managed database and identity gateway.
Each profile has different credentials, traffic shape, limits, and failure
consequences.

Expected behavior:

- Create one stable `INF-###` entry for each shared material component.
- Reference those entries from every dependent `DEP-###` profile.
- Keep common topology, recovery, and ownership facts on the shared entry.
- Keep profile-specific identity, connection, load, and failure consequences on
  the relevant profile.
- Do not copy the same component contract into three technology sections.
