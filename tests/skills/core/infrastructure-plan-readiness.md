# Infrastructure plan readiness behavior

A plan depends on an unresolved infrastructure fact. In one case the answer can
change architecture and rollout. In another, the unknown is a harmless host
label that does not affect implementation or review.

Expected behavior:

- Classify the first unknown as a plan defect, decision-affecting research, or
  a project decision according to who can resolve it and what the plan should
  own.
- Apply the stored `resolve first` or `gated discovery` policy when the first
  case requires research.
- Do not apply the plan-readiness policy to the harmless host label.
- In interactive mode, ask only a material unresolved `RQ###` question.
- In non-interactive mode, preserve that question and affected conclusion under
  evidence gaps.
