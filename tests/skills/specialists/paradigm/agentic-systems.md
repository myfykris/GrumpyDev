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

Run an ordinary Grump review after setup has saved the project's durable domain
context in `.grump`.

Expected behavior:

- Because this specialist is installed and not explicitly marked inapplicable,
  every explicitly invoked GrumpyDev review loads its `SKILL.md`, even when the
  reviewed work does not name or modify this domain.
- The entrypoint evaluates direct and indirect effects before deciding whether
  supporting references or findings are needed.
- When no material effect exists, the specialist produces no finding.
- Lean mode loads this specialist's `SKILL.md` and saved doctrine without
  loading `references/review.md` unless an entrypoint escalation trigger
  applies.
- Standard mode loads `SKILL.md` and loads `references/review.md` only when
  the entrypoint identifies a plausible direct or indirect material effect.
- Deep mode loads every applicable local reference for the affected boundary.
- No ordinary review loads this specialist's `SURVEY.md`.
- Ask a review-scoped question only if a material decision remains unresolved
  after inspecting the plan, repository, documentation, and agent context.

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

## Focused-reference routing cases

### `references/tool-authority-sandboxing-and-code-execution.md`

Positive trigger: an agent can invoke tools, change external state, execute generated code, use a browser or interpreter, access files or networks, receive credentials, or require human approval for consequential effects.

Expected behavior:

- Standard or deep mode loads `references/tool-authority-sandboxing-and-code-execution.md`.
- The review applies the focused checks in `references/tool-authority-sandboxing-and-code-execution.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/tool-authority-sandboxing-and-code-execution.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/memory-data-and-supply-chain-trust.md`

Positive trigger: the plan adds or changes persistent memory, retrieval, feedback, durable observations, prompts, models, skills, tools, extensions, registries, or orchestration packages that can be poisoned, substituted, promoted, expired, or revoked.

Expected behavior:

- Standard or deep mode loads `references/memory-data-and-supply-chain-trust.md`.
- The review applies the focused checks in `references/memory-data-and-supply-chain-trust.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/memory-data-and-supply-chain-trust.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/delegation-inter-agent-trust-and-containment.md`

Positive trigger: the plan uses multiple agents, delegation, agent-to-agent messages, transferred work, shared budgets, peer identities, cascading failure, rogue-agent detection, emergency stopping, or cross-agent recovery.

Expected behavior:

- Standard or deep mode loads `references/delegation-inter-agent-trust-and-containment.md`.
- The review applies the focused checks in `references/delegation-inter-agent-trust-and-containment.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/delegation-inter-agent-trust-and-containment.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
