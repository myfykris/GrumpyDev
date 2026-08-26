---
name: llm-applications
description: Review LLM application plans for model contracts, prompt and context management, structured output, retrieval, evaluation, safety, privacy, cost, observability, and fallback behavior. Use when application behavior depends on a generative model.
---

# LLM applications plan review

Apply this guidance alongside the core GrumpyDev review and the `application-security`,
`data-privacy`, `dependency-supply-chain`, and `observability` skills.

## Inspect evidence

- Read model providers and versions, system prompts, templates, context assembly, tools, output
  schemas, and sampling settings.
- Trace user, retrieved, tool, and system data through trust labels, token budgets, truncation,
  storage, logging, and model calls.
- Inspect retrieval indexes, chunking, ranking, citations, freshness, tenant filters, embedding
  versions, and deletion propagation.
- Review evaluations, golden cases, adversarial cases, fallback models, retries, rate limits,
  cost controls, and incident switches.

## Establish the operating model

Establish the project target: Model providers and versions, reasoning and effort policy, prompt
sources and versioning, context and truncation policy, output schemas, retrieval and embedding
stack, data classifications, retention, evaluations, safety controls, fallback behavior,
budgets, and observability.

Model output is untrusted probabilistic data, even when structured. The application must
validate it before it affects permissions, money, persistence, code execution, or external
systems.

## Challenge the plan

### Recurring traps

Watch especially for prompts hardcoded without version control, model upgrades treated as
compatible, retrieval without tenant filters, citations invented rather than traced, structured
output accepted without semantic validation, sensitive or hidden context treated as safe because
the user cannot normally see it, retrieved content trusted as instructions, poisoned knowledge
entering indexes, unbounded model work, and no formal evaluation suite.

- Version prompts, models, tools, schemas, retrieval settings, and safety policy together so
  behavior can be reproduced and compared.
- Treat direct, indirect, multilingual, encoded, and multimodal prompt injection as an
  architectural trust-boundary problem. Label external content, keep it separate from control
  instructions, constrain resulting authority, and do not claim that filtering or retrieval alone
  solves injection.
- Do not place credentials in prompts or treat a system prompt, hidden context, refusal rule, or
  model instruction as a secret or enforceable security control. Enforce permissions and data
  boundaries outside the model.
- Validate structure, semantics, authorization, provenance, and allowed values before consuming
  model output. Apply the exact downstream safety rule for HTML, Markdown, URLs, SQL, shell,
  source code, templates, files, messages, and tool arguments.
- Separate model recommendation from application authority. Give the model only the minimum
  data and capabilities needed, require approval before high-impact effects, and reauthorize each
  action outside the model.
- Enforce tenant and document authorization before retrieval and again before presenting or
  acting on retrieved content.
- Establish provenance, review, trust labels, ingestion validation, change control, deletion,
  and incident removal for training, fine-tuning, retrieval, feedback, memory, model, adapter,
  embedding, and prompt data. Detect poisoning and unexpected behavior rather than trusting a
  successful ingest.
- Scope vector indexes, caches, and retrieval filters by tenant and authorization. Cover hidden
  text, metadata, chunk overlap, embedding inversion or leakage, stale permissions, and deletion
  propagation.
- Define token and context budgets, truncation priority, rate limits, retries, fallback models,
  timeout, cost, and degradation. Bound recursive calls, oversized context, expensive output,
  model extraction attempts, and per-user or tenant consumption.
- Create evaluations for correctness, groundedness, refusal, injection resistance, privacy,
  hidden-context disclosure, poisoned data, unsafe output, excessive agency, bias, latency, cost,
  and failure recovery.
- Redact and minimize prompts, responses, traces, feedback, and evaluation data according to
  explicit retention and access policy.

## Verify the claims

- Run pinned evaluation sets across model, prompt, retrieval, and tool changes with documented
  thresholds and regressions.
- Exercise injection, conflicting instructions, missing context, stale retrieval, malformed
  output, hidden-context extraction, poisoned documents, cross-tenant retrieval, unsafe Markdown
  or code, provider outage, recursive work, timeout, and quota.
- Inspect production traces for provenance, privacy, cost, model identity, prompt version,
  latency, and safe failure without storing secrets.
- Red-team the complete path from user and retrieved input through model output to rendering,
  persistence, retrieval, tools, and external effects. A model-only benchmark does not prove the
  application boundary.

## Ask when evidence is missing

- Which models, versions, effort settings, prompts, schemas, retrieval, data classes, and
  provider regions apply?
- How are injection, hidden context, data and model poisoning, output validation, agency,
  retrieval isolation, evaluations, privacy, citations, consumption, observability, fallbacks,
  and rollback handled?

## Calibrate findings

- Treat cross-tenant retrieval, secret disclosure, unvalidated high-impact output, or
  unauthorized tool use as critical.
- Downgrade when versions, trust labels, validations, evaluation thresholds, privacy, budgets,
  and failure paths are proven.

## Add to the verdict

State model and prompt versions, context trust and hidden-data model, output validation, action
authority, retrieval isolation and provenance, evaluation results, privacy, consumption bounds,
and fallback policy.
