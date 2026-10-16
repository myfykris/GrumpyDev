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
