---
name: gd-llm-applications
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review LLM application engineering work for model contracts, prompt and context management, structured output, retrieval, evaluation, safety, privacy, cost, observability, and fallback behavior."
---

# LLM applications GrumpyDev review

## Quick checks

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

- Assess cross-tenant retrieval, secret disclosure, unvalidated high-impact output, or
  unauthorized tool use under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the LLM applications
specialist.

- [Focused rules](references/retrieval-data-and-poisoning.md):
  Read when the work changes RAG, vector indexes,
  embeddings, chunking, ranking,
  citations, tenant filtering, training or fine-tuning data, feedback, memory,
  ingestion, provenance, deletion propagation, or poisoning controls.
- [Focused rules](references/tools-output-and-authority.md):
  Read when the work lets model output invoke
  tools, render active content, produce code, SQL, shell, templates, files,
  messages, or arguments, influence permissions or money, persist state, or
  cause any external effect.
- [Focused rules](references/evaluations-budgets-and-fallbacks.md):
  Read when the work changes model or prompt versions,
  evaluation thresholds, token or
  cost budgets, truncation, rate limits, retries, fallback models, provider regions,
  traces, observability, privacy retention, outage behavior, or rollback.

## Verdict context

State model and prompt versions, context trust and hidden-data model, output validation, action
authority, retrieval isolation and provenance, evaluation results, privacy, consumption bounds,
and fallback policy.
