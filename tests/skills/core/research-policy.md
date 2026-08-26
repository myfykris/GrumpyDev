# Research policy behavior

## Unresolved decision-affecting research

An implementation plan leaves research open whose result can change a material
implementation decision.

Expected behavior:

- `resolve first` prevents approval of the implementation plan until the
  research is resolved and the resulting decision is reviewed.
- `gated discovery` can approve a bounded discovery-only plan, but not its
  dependent implementation.
- Missing policy defaults to gated discovery.
- Ordinary verification with specified outcomes and responses is not treated as
  decision-affecting research merely because it gathers evidence.

## Research execution

Expected behavior:

- `automatic` performs only safe, read-only research within existing
  permissions and then resumes the evaluation.
- `ask first` requires one deduplicated `RQ###` permission question.
- `report only` records the research and blocked decision as an evidence gap.
- Research permission never grants project mutation, external writes,
  production or secret access, spending, software installation, downloaded code
  execution, or state-changing experiments.
