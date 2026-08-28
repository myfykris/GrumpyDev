# Agentic memory, data, and supply-chain trust

Read this reference when the reviewed work directly or indirectly adds or changes
persistent memory, retrieval,
feedback, durable observations, prompts, models, skills, tools, extensions, registries,
or orchestration packages that can be poisoned, substituted, promoted, expired, or
revoked.

## Review requirements

- Treat models, prompts, skills, tools, extensions, agent registries, memory sources, and
  orchestration packages as a supply chain. Pin approved identities and versions, review changes,
  define disable and rollback controls, and detect capability or description drift.

- Give persistent memory explicit provenance, trust, tenant, expiry, deletion, and promotion
  rules. Quarantine untrusted observations, prevent one result from becoming durable policy, and
  require review before memory can expand future authority.
