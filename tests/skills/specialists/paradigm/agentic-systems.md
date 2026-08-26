# agentic-systems behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which agents, models, tools, authorities, approval points, budgets, memory, and delegation
  topology apply?
- How are goal hijack, tool misuse, identity, supply chain, code execution, memory poisoning,
  inter-agent trust, cascading failure, human approval, rogue behavior, audit, and recovery
  handled?

Expected behavior:

- Ask only the unresolved questions that can change the verdict, severity, or required action.
- Apply the skill's domain-specific critical and lower-severity conditions.

## Resolved-evidence case

Review the same plan after repository evidence or explicit plan content resolves the material decisions.

Expected behavior:

- Ask zero questions that the evidence already answers.
- Downgrade or omit findings that the supplied evidence invalidates.

## Memory and delegation case

Review a plan in which any tool result can become durable memory, a delegated
agent inherits the caller's credentials, generated code runs on the host, and a
human approves from a fluent one-line summary.

Expected behavior:

- Require provenance, tenant, expiry, quarantine, deletion, and explicit
  promotion rules before observations become durable memory or policy.
- Require separate least-privilege identities and reauthorization for delegated
  work and authenticated, typed, replay-resistant inter-agent messages.
- Require a code sandbox, bounded cascading failure, an independent emergency
  stop, and approval that exposes the actual target, data, permission, effect,
  and uncertainty.

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

- model providers and versions, effort settings, orchestration runtime, tool endpoints
  and permissions, memory stores, queues, sandboxes, budgets, evaluation gates, audit retention,
  and emergency disable controls.

Expected behavior:

- Use domain candidates to fill the applicable DEP-### profile without repeating core confirmation.
- Reference a shared INF-### component when profiles use the same infrastructure.
- Ask zero domain questions when current evidence already establishes the facts.
