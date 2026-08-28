# LLM applications standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

- Treat direct, indirect, multilingual, encoded, and multimodal prompt injection as an
  architectural trust-boundary problem. Label external content, keep it separate from control
  instructions, constrain resulting authority, and do not claim that filtering or retrieval alone
  solves injection.
## Verify the claims

- Exercise injection, conflicting instructions, missing context, stale retrieval, malformed
  output, hidden-context extraction, poisoned documents, cross-tenant retrieval, unsafe Markdown
  or code, provider outage, recursive work, timeout, and quota.
## Ask when evidence is missing

- Ask which model and prompt versions, data classifications, provider regions,
  retention boundaries, and enforceable safety controls apply when project
  evidence does not establish them.

## Calibrate findings

- Downgrade when versions, trust labels, validations, evaluation thresholds, privacy, budgets,
  and failure paths are proven.
