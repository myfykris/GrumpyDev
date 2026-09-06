---
name: llm-applications
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review LLM application engineering work for model contracts, prompt and context management, structured output, retrieval, evaluation, safety, privacy, cost, observability, and fallback behavior."
---

# LLM applications GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `application-security`,
`data-privacy`, `dependency-supply-chain`, and `observability` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read model providers and versions, system prompts, templates, context assembly, tools, output
  schemas, and sampling settings.

- Trace user, retrieved, tool, and system data through trust labels, token budgets, truncation,
  storage, logging, and model calls.

Watch especially for prompts hardcoded without version control, model upgrades
treated as compatible, retrieval without tenant filters, citations invented
rather than traced, structured output accepted without semantic validation,
sensitive or hidden context treated as safe because the user cannot normally see
it, retrieved content trusted as instructions, poisoned knowledge entering
indexes, unbounded model work, and no formal evaluation suite.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-tenant retrieval, secret disclosure, unvalidated high-impact output, or
  unauthorized tool use as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/retrieval-data-and-poisoning.md):
  Read when the reviewed work directly or indirectly changes RAG, vector indexes,
  embeddings, chunking, ranking,
  citations, tenant filtering, training or fine-tuning data, feedback, memory,
  ingestion, provenance, deletion propagation, or poisoning controls.
- [Focused rules](references/tools-output-and-authority.md):
  Read when the reviewed work directly or indirectly lets model output invoke
  tools, render active content, produce code, SQL, shell, templates, files,
  messages, or arguments, influence permissions or money, persist state, or
  cause any external effect.
- [Focused rules](references/evaluations-budgets-and-fallbacks.md):
  Read when the reviewed work directly or indirectly changes model or prompt versions,
  evaluation thresholds, token or
  cost budgets, truncation, rate limits, retries, fallback models, provider regions,
  traces, observability, privacy retention, outage behavior, or rollback.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State model and prompt versions, context trust and hidden-data model, output validation, action
authority, retrieval isolation and provenance, evaluation results, privacy, consumption bounds,
and fallback policy.
