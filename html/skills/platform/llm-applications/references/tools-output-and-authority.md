# LLM tools, output, and authority

Read this reference when the reviewed work directly or indirectly lets model
output invoke tools, render active content, produce code, SQL, shell, templates,
files, messages, or arguments, influence permissions or money, persist state, or
cause any external effect.

## Review requirements

- Do not place credentials in prompts or treat a system prompt, hidden context, refusal rule, or
  model instruction as a secret or enforceable security control. Enforce permissions and data
  boundaries outside the model.

- Validate structure, semantics, authorization, provenance, and allowed values before consuming
  model output. Apply the exact downstream safety rule for HTML, Markdown, URLs, SQL, shell,
  source code, templates, files, messages, and tool arguments.

- Separate model recommendation from application authority. Give the model only the minimum
  data and capabilities needed, require approval before high-impact effects, and reauthorize each
  action outside the model.

## Verify the claims

- Red-team the complete path from user and retrieved input through model output to rendering,
  persistence, retrieval, tools, and external effects. A model-only benchmark does not prove the
  application boundary.
