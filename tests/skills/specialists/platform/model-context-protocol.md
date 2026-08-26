# model-context-protocol behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which MCP protocol and SDK versions, roles, capabilities, transports, sessions, and
  deployment topology apply?
- How are authorization, token audience and exchange, discovery fetches, origins, local binding,
  tool identity and authority, untrusted content, compatibility, and revocation handled?

Expected behavior:

- Ask only the unresolved questions that can change the verdict, severity, or required action.
- Apply the skill's domain-specific critical and lower-severity conditions.

## Resolved-evidence case

Review the same plan after repository evidence or explicit plan content resolves the material decisions.

Expected behavior:

- Ask zero questions that the evidence already answers.
- Downgrade or omit findings that the supplied evidence invalidates.

## Token and metadata case

Review an MCP server plan that forwards the client's MCP access token to a
vendor API and fetches authorization metadata from a URL supplied during
discovery without destination restrictions.

Expected behavior:

- Treat access-token passthrough as a critical confused-deputy and credential
  boundary, and require a separate downstream token with issuer, audience,
  scope, storage, rotation, and revocation controls.
- Treat metadata and registration fetches as SSRF paths with scheme, host,
  redirect, DNS, address, response-size, and timeout restrictions.
- Bind approval to the exact server, tool, schema, arguments, scopes, target,
  and effect, and reconfirm material tool identity or capability drift.

## Evidence-resolved survey case

Run initial setup or an explicit re-survey after .grump, repository evidence, and project documentation establish every applicable durable fact.

Expected behavior:

- Load this specialist's SURVEY.md because this is a survey operation.
- Ask zero questions whose decisions are already supported by current evidence.
- Preserve concise doctrine with useful evidence references.

## Material survey-gap case

Run a survey when inspection leaves one durable fact unresolved and it can materially change future reviews in this domain.

Expected behavior:

- Ask only the unresolved durable question after pooling and deduplicating all contributions.
- Let the survey orchestrator assign its sequential question identifier.
- Record the answer or a deliberate unresolved state without inventing a default.

## Ordinary-review loading case

Run an ordinary Grump review after setup saved durable domain context in .grump.

Expected behavior:

- Load this specialist's SKILL.md and saved doctrine, but not SURVEY.md.
- Ask a plan-scoped question only when material evidence remains unresolved.

## Companion-overlap case

Run setup with this specialist and a companion proposing the same underlying decision.

Expected behavior:

- Pool contributions before numbering questions and ask one combined question.
- Preserve genuinely distinct choices and record one coherent project fact.

## Infrastructure-profile case

Run setup or re-survey with this domain boundary:

- MCP protocol and SDK versions, client and server topology, transports, bind
  addresses, origins, TLS, authorization metadata, token audiences, process environment,
  capability allowlists, timeouts, logs, and disable controls.

Expected behavior:

- Use domain candidates to fill the applicable DEP-### profile without repeating core confirmation.
- Reference a shared INF-### component when profiles use the same infrastructure.
- Ask zero domain questions when current evidence already establishes the facts.
