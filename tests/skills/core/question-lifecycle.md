# Review question lifecycle

Expected behavior:

- Survey setup questions use the continuous `Q###` sequence and may establish
  `.grump` policy.
- Live plan-review questions use `RQ###`, beginning at `RQ001` for each
  evaluation.
- Answered questions resume the review.
- Deferred or declined questions are not repeated without materially changed
  evidence.
- The post-review plan-rules offer uses the next `RQ###` identifier but
  does not delay or change the completed verdict.
- Required safety, approval, capability, and target-identification prompts are
  not suppressed by the plan interaction preference.
