# GrumpyDev review preferences

Read before interpreting a stored preference or its missing, invalid, or
conflicting-value fallback, including during setup and authorized doctrine
changes. This defines behavior, not project facts or permission to start work.

## Managed review preferences

GrumpyDev may generate, recognize, and act on only these exact fields under
`## Review preferences`:

| Field | Allowed stored values | Behavior when missing, invalid, or conflicting |
| --- | --- | --- |
| `Doctrine format` | `compact`, `detailed` | `compact` |
| `Plan addenda` | `allowed`, `chat only` | `chat only` |
| `Plan execution rules` | `allowed`, `disabled` | `disabled` |
| `Finding tables` | `preferred`, `disabled` | `preferred` |
| `Status icons` | `enabled`, `disabled` | `enabled` |
| `Review questions` | `interactive`, `non-interactive` | Ask the first material question with an option to continue without Q&A |
| `Confirmed doctrine updates` | `allowed`, `propose only` | `propose only` |
| `Decision-affecting research` | `resolve first`, `gated discovery` | `gated discovery` |
| `Research execution` | `automatic`, `ask first`, `report only` | `ask first` |

Store a field only after an explicit answer that applies to future GrumpyDev
work in this project. The installation survey establishes that scope. A
current-turn choice outside the survey controls only that operation unless the
user explicitly makes it project-wide. Never store `unresolved`, infer a
preference from silence, or turn one permitted action into standing permission.

`Plan execution rules: allowed` authorizes adding execution rules to local
implementation plans after `APPROVE` or `APPROVE WITH CONCERNS`, without asking
again. `disabled` authorizes no automatic insertion. This is separate from
`Plan addenda`, which controls saving review results, and never authorizes
implementation. Ask this preference during the survey, not during reviews.

When `Review questions` is missing, the first material review question must say
that the user may answer it or reply `continue without Q&A`. That reply makes
only the current review non-interactive. It suppresses later substantive review
questions and moves remaining material unknowns to `Evidence gaps`. It does not
create a stored preference.

Unknown human-authored preference fields are non-operative. Point them out when
they appear intended to control GrumpyDev, but do not guess at their meaning.

## Values that are not review preferences

Do not store these as managed preference fields:

- whether `.grump` and `.grumpydev/` were added to `.gitignore`;
- acceptance of execution rules for one plan;
- answers scoped to one review;
- permission for one research action;
- installation, update, or removal state; or
- permission to publish, deploy, access production, use secrets, spend money,
  or perform another external action.

The repository's actual `.gitignore` is the result of the setup choice.
Execution rules belong in the plan's GrumpyDev addendum. A promoted durable
review answer belongs in the relevant doctrine section, not in preferences.
