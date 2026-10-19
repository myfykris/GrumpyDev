# GrumpyDev test results (October 15, 2026)

## Setup

- Arms: GrumpyDev (this skill plus `.grump`), a strong plain review prompt
  ("plain"), and, on the original four scenarios, the old GrumpyDev with its
  specialist skills (commit e275a2c, "old").
- Models: Claude Sonnet 5.5 and Haiku 5.5, 3 runs per cell. One local model,
  qwen3.6-35b, 1 or 2 runs per cell.
- Judging: Opus 5.5 judges graded blind packets (arm names and paths removed)
  against the answer keys in `keys/`, checking every claim against the project.
  Each packet holds all arms for one scenario and model, so arms are compared
  within one judge.
- Scenarios are described in `README.md`. Key scores are out of the item count
  shown. "Tokens" is the GrumpyDev cost per review relative to the plain prompt.

Rows marked "rerun" are for the published skill without its last change (the
re-review count check). The cross-session Haiku row is for a version with that
check plus an owner-rule change that was tested and not adopted. Other rows are
for the first draft, which also printed a "Touched" list and a longer "Not
checked" section, and had shorter command and ledger sections.

## Results

| Scenario | Model | GrumpyDev key | Plain key | Tokens | Notes |
|---|---|---|---|---|---|
| s1 flawed plan (/7) | Sonnet | 7.00 | 7.00 | 1.26x | rerun; SNR 5.00 vs 4.00 |
| s1 flawed plan (/7) | Haiku | 7.00 | 7.00 | 1.31x | rerun; SNR 4.67 vs 3.67 |
| s2 sound plan | Sonnet | calibrated 1/3 | 0/3 | 1.25x | rerun; invalid 1.33 vs 0.67 |
| s2 sound plan | Haiku | calibrated 0/3 | 0/3 | 1.28x | rerun; invalid 0.33 vs 3.00 |
| s3 subtle traps (/10) | Sonnet | 9.83 | 9.33 | 1.08x | |
| s3 subtle traps (/10) | Haiku | 8.33 | 8.83 | 1.31x | |
| s5 buggy diff (/8) | Sonnet | 8.00 | 8.00 | 1.19x | |
| s5 buggy diff (/8) | Haiku | 8.00 | 7.67 | 1.21x | |
| pin: PHP 8 code, PHP 7.4 production (/5) | Sonnet | 5.00 | 3.83 | 1.14x | |
| pin (/5) | Haiku | 5.00 | 2.33 | 1.37x | |
| upgrade: plan needs PHP 8 (/5) | Sonnet | 5.00 | 2.83 | 1.18x | plain proposed upgrades |
| upgrade (/5) | Haiku | 5.00 | 1.17 | 1.37x | |
| research deferrals (/8) | Sonnet | 8.00 | 8.00 | 1.24x | rerun; spike called a blocker 0 vs 7 times |
| research deferrals (/8) | Haiku | 8.00 | 8.00 | 1.36x | rerun |
| boundaries plan (/7) | Sonnet | 7.00 | 5.50 | 1.30x | |
| boundaries plan (/7) | Haiku | 6.67 | 5.33 | 1.42x | |
| project audit (/13) | Sonnet | 12.83 | 12.50 | 1.21x | rerun |
| project audit (/13) | Haiku | 12.33 | 11.67 | 1.17x | rerun |
| touched units (/8) | Sonnet | 6.83 | 2.67 | 1.44x | rerun |
| touched units (/8) | Haiku | 3.83 | 2.17 | 1.20x | rerun |
| cross-session re-review (/11) | Sonnet | 11.00 | 10.67 | 1.41x | every earlier issue tracked 3/3 |
| cross-session re-review (/11) | Haiku | 10.83 | 10.83 | 1.55x | every earlier issue tracked 2/3 |
| same-session re-review (/11) | Sonnet | 11.00 | - | - | every earlier issue tracked 3/3 |
| same-session re-review (/11) | Haiku | 10.67 | - | - | every earlier issue tracked 3/3 |

SNR is the judge's signal-to-noise score (1-5). "Calibrated" means an approving
verdict on a plan written to be sound, with no invalid material finding.

## What it shows

- **Generic plan and diff reviews:** GrumpyDev and a strong plain prompt find
  the same defects (s1, s3, s5, research). GrumpyDev's output is cleaner:
  in the reruns its SNR was equal or higher than plain's in 8 of 10 cells.
- **Where the project rules apply, GrumpyDev finds more:**
  - With a production pin in `.grump`, it caught every PHP 8 construct and
    never proposed an upgrade. Plain reviews often treated production as
    unknown and proposed upgrades.
  - With the touched-units rule, it reports pre-existing problems in the code a
    plan touches: Sonnet 6.83 vs 2.67 of 8. Haiku still misses about half.
  - With the Boundaries section, it names bypassed owners and the missing owner
    that plain reviews miss (boundaries plan, 5.3-5.5 to 6.7-7.0 of 7).
- **Re-reviews:** with the ledger, every earlier issue gets a status. Sonnet
  tracked every issue correctly in 6 of 6 re-reviews; Haiku in 5 of 6.
  Finding the new defects in a revision needs no history: plain reviews of
  the revision scored about the same.
- **Cost:** 1.08x to 1.55x the plain prompt's tokens per review, higher for
  Haiku and for re-reviews, which read the ledger. The old GrumpyDev cost about 2x
  plain (161k-230k tokens), with key scores no better than plain's and SNR
  2-3.

## Targets set before testing

| Criterion | Result |
|---|---|
| Key score at least the old GrumpyDev's and within 2% of plain | Met in every cell except s3 Haiku: 8.33 vs plain 8.83 and old 8.67 (of 10). |
| SNR at least 4.5 | Not met in most cells. Reached in s1 Sonnet (5.00), s1 Haiku (4.67), research Sonnet (4.67). No arm reaches 4.5 on most scenarios with these judges. |
| Invalid findings no higher than plain | Not met on s2 Sonnet (1.33 vs 0.67), s3 Sonnet (0.33 vs 0) and research Haiku (0.67 vs 0.33); met elsewhere. |
| Tokens at most 1.3x plain | Not met in 9 of 22 cells, mostly Haiku and re-reviews. |
| Per-issue status on every re-review | Met: 12 of 12. |
| Cross-session: every earlier issue with the correct status | Sonnet 3/3; Haiku 2/3 with the final rule (1/3 before it). |
| s2 calibrated in 2 of 3 runs per model | Not met by any arm, including plain (0/6) and old (0/6). |
| Pin and upgrade: every PHP 8 use caught, no upgrade, no fix needing a newer version | Met on both models. Haiku 2 of 3 pin runs reported accepted known debt as fixes. |
| Implementation: code runs on the pinned version with the constraints block | Met, but also met without the block (0 PHP 8 constructs in 12 runs), so the test does not show the block's effect. |
| Research: blockers flagged, repo answers cited, NEEDS INFO with a discovery split, spike not a blocker, ledger rows close on the recorded decision | Blockers, citations and the discovery split met on both models (split 6 of 6, plain 0 of 6). Spike: Sonnet never called it a blocker; in the Haiku rerun every review of every arm rated it MEDIUM or higher. Ledger closing conditions were not checked. |
| Boundaries plan: at least plain, every planted defect, missing owner reported | At least plain on both. Every planted defect: Sonnet 3 of 3 runs, Haiku 1 of 3. Missing owner fully reported in 4 of 6 runs. |
| Audit: at least 12.5 of 13, ordered plan with ratchets, SNR 4.5, tokens 1.3x | Key: Sonnet 12.83, Haiku 12.33. Ordered plan with ratchets in 6 of 6 runs (plain 2 of 6 full). SNR 4.0. Tokens 1.21x and 1.17x. |
| Real-history audit fixture | Not run: no repository chosen yet. |

## Local model

qwen3.6-35b on vLLM, read-only tools, the model card's thinking-mode sampling
(temperature 1.0, presence_penalty 1.5; at temperature 0.2 it looped until the
token cap). Absolute scores are low for both arms. GrumpyDev vs plain, key:
s1 4.25 vs 4.25, s3 2.5 vs 1.0, s5 3.0 vs 1.5. On s2 neither was calibrated:
GrumpyDev approved but with three wrong findings, plain asked for revisions.
Invalid findings per review: 0-3 vs 3-9. GrumpyDev used 1.0x-5.3x the tokens;
the plain prompt read little of the project.

## Limits

- The fixtures and keys were written by the same author as the skill. The
  real-history audit fixture is still needed.
- 3 runs per cell. The same reviews judged in two packets differed by up to
  0.5 in key score and 1 point in SNR, and judges disagreed about whether
  "no owner named" rows on a sound plan are invalid. Compare arms within a
  packet, and treat differences under about 0.5 as noise.
- Two key errors were found and fixed during judging: s1r2 F4 (the revised
  export window still has a DST error) and the s1r2 item names (they clashed
  with the review labels).
- s2 calibration fails for every arm and model. Reviewers rate real but minor
  issues (catch-all 4xx handling, rows stranded by a rollback) HIGH.

## Same-session priorities test (October 19, 2026)

The usual flow is to write a plan with the agent and then ask for the review in the
same conversation. This test ran that way: the user stated priorities in the first
message, and the review was requested in the second. Arms: plain prompt, the skill
without a priorities section, and the skill with the "Fit with the project" section
that is now published. Sonnet and Haiku, 3 runs each, blind Opus judges.

| Scenario | Model | Plain | Skill without | Skill with |
|---|---|---|---|---|
| Over-built plan for a one-person project: fit items (of 4) | Sonnet | 4.00 | 3.83 | 3.83 |
| Over-built plan: fit items (of 4) | Haiku | 4.00 | 2.33 | 3.83 |
| Flawed plan, "speed over polish": fixes sized to the deadline (of 1) | Sonnet | 1.00 | 0.67 | 1.00 |
| Flawed plan, "speed over polish": fixes sized to the deadline (of 1) | Haiku | 1.00 | 0.83 | 1.00 |
| Sound plan, "a few hours' delay is fine": delay issues rated by that (of 1) | Sonnet | 0.00 | 0.00 | 1.00 |
| Sound plan, "a few hours' delay is fine": delay issues rated by that (of 1) | Haiku | 0.00 | 0.00 | 0.00 |

- Without the section, the skill followed the user's stated priorities less than a
  plain prompt did. With it, it matched the plain prompt, and on the sound plan with
  Sonnet it rated delay-only issues by what the user said (3 of 3, against 0 of 3).
- No arm lowered the severity of a real bug because of a priority. Every review in
  every arm found both data-loss bugs in the over-built plan and kept the security,
  rollout and duplicate bugs in the flawed plan at HIGH.
- The sound plan was still not approved in most runs: 1 of 3 with the section on
  Sonnet, 0 everywhere else.
- Cost: the section did not change the tokens per review on average.

Reviewing a plan the agent just wrote: in a sixth scenario the agent wrote the plan
from a short brief and then reviewed it in the same conversation. A fresh agent then
reviewed the same plan with no history. Across 18 plans, the same-session review found
64.5 of 98 material defects (66%) and the fresh review 82.5 (84%). The gap appeared in
all six arm and model combinations, with or without GrumpyDev. Verdicts were about as
strict either way; the same-session review simply missed more.

## Running the review in a subagent

Tested this line at the top of "Before reviewing": "If you can start a subagent, run
the review in one. Give it the path of this file, the target, and everything the user
has said in this conversation about the project's goals, priorities and constraints,
in the user's words. Tell it to do the review itself, and show the user its review as
written." Same flow as above, on the over-built plan, the sound plan and the plan the
agent wrote itself. Sonnet and Haiku, 3 runs each, blind Opus judges.

- Whether agents follow the line could not be measured here. The reviewers in this
  harness are themselves subagents, and Claude Code tells a subagent to do its task
  rather than hand it to another subagent. Asked afterwards, reviewers said they saw
  the line and followed that rule instead. Sonnet never delegated (0 of 9). Haiku
  delegated in all 6 runs on the over-built and self-written plans and in none of the
  3 on the sound plan.
- When it delegated, the handoff worked: all 6 briefs quoted the user's statement
  word for word, and all 6 reviews reached the user unchanged. (In one run the agent
  started the subagent in the background and stopped before it finished; that review
  was scored as the subagent wrote it.)
- Priorities survived the handoff. On the over-built plan, Haiku's delegated reviews
  scored 3.67 of 4 on fit items, the same as reviews done in place, and found both
  data-loss bugs (one at half credit in one run).
- It did not close the self-review gap. On plans the agent had just written, Haiku's
  delegated reviews found 12 of 17 defects and fresh reviews of the same plans found
  14. A Sonnet repeat without delegation found 12.5 of 16 in the same session against
  13 fresh, so at 3 runs the gap itself is noisy.
- Cost: delegated reviews used 1.7x (self-written plan) to 2.7x (over-built plan) the
  tokens of a review done in place, and 3 to 5 times the uncached input, because the
  subagent reads the project again.

Not added to the skill: about twice the cost, and no measured gain.
