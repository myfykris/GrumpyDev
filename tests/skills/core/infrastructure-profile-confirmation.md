# Infrastructure profile confirmation behavior

The repository shows a production web process, a background worker, and one
database used by both. Their runtime configuration is mostly established, but
the evidence does not establish who operates production or the worker shutdown
contract.

Expected behavior:

- Apply the infrastructure gate and infer concise `DEP-###` profiles for the
  web process and worker.
- Represent the database once as an `INF-###` component referenced by both
  profiles.
- Put one concise profile confirmation first in the initial question batch.
- Include the already-known ownership and shutdown gaps in that same batch.
- Do not ask the user to repeat runtime facts established by repository
  evidence.
