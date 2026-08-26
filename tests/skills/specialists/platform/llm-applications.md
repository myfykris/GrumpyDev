# llm-applications behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which models, versions, effort settings, prompts, schemas, retrieval, data classes, and
  provider regions apply?
- How are injection, hidden context, data and model poisoning, output validation, agency,
  retrieval isolation, evaluations, privacy, citations, consumption, observability, fallbacks,
  and rollback handled?

Expected behavior:

- Ask only the unresolved questions that can change the verdict, severity, or required action.
- Apply the skill's domain-specific critical and lower-severity conditions.

## Resolved-evidence case

Review the same plan after repository evidence or explicit plan content resolves the material decisions.

Expected behavior:

- Ask zero questions that the evidence already answers.
- Downgrade or omit findings that the supplied evidence invalidates.

## Hidden-context and output case

Review a plan that stores credentials in a system prompt, trusts retrieved
documents as instructions, renders model Markdown, and executes structured tool
arguments because the model returned valid JSON.

Expected behavior:

- Reject the system prompt as a secret store or authorization control and treat
  retrieved content as a possible indirect or multimodal injection source.
- Require tenant and document authorization, provenance, poisoning controls,
  deletion propagation, and vector-store isolation.
- Validate model output for the exact Markdown, URL, tool, authorization, and
  effect context outside the model, with budgets and adversarial evaluation.

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

- model endpoints and regions, model and embedding versions, effort settings, prompt
  sources, retrieval stores, tool permissions, data retention, rate and cost limits, evaluation
  gates, observability, fallbacks, and kill switches.

Expected behavior:

- Use domain candidates to fill the applicable DEP-### profile without repeating core confirmation.
- Reference a shared INF-### component when profiles use the same infrastructure.
- Ask zero domain questions when current evidence already establishes the facts.
