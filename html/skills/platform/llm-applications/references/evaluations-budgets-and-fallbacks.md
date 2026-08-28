# LLM evaluations, budgets, and fallbacks

Read this reference when the reviewed work directly or indirectly changes model or
prompt versions, evaluation
thresholds, token or cost budgets, truncation, rate limits, retries, fallback models,
provider regions, traces, observability, privacy retention, outage behavior, or
rollback.

## Review requirements

- Version prompts, models, tools, schemas, retrieval settings, and safety policy together so
  behavior can be reproduced and compared.

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

- Inspect production traces for provenance, privacy, cost, model identity, prompt version,
  latency, and safe failure without storing secrets.


## Ask when evidence is missing

- Which models, versions, effort settings, prompts, schemas, retrieval, data classes, and
  provider regions apply?

- How are injection, hidden context, data and model poisoning, output validation, agency,
  retrieval isolation, evaluations, privacy, citations, consumption, observability, fallbacks,
  and rollback handled?
