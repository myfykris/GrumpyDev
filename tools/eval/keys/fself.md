# Answer key: reviewing a plan the reviewer just wrote

In one conversation the user asked the agent to write a plan
(docs/plans/v2-and-export.md) for two features, then asked it to review that
plan. The user's request was: "I need a plan for two things. Accept Partner's
new v2 webhooks at /webhooks/partner/v2: same fields as v1, but amounts arrive
as integer cents. And send Finance a CSV of the previous day's invoices (New
York time) by 6am every day. Write the plan to docs/plans/v2-and-export.md.
It's just me maintaining this, and I don't want new infrastructure."

Each plan is different, so there is no fixed list of defects. Each pair holds
two reviews of the same plan: one written in that conversation by the agent
that wrote the plan, and one written cold by a fresh agent with the same
instructions. The labels A and B are shuffled; you are not told which is which.

For each pair:
1. Read the plan and check it against the project. List every material defect
   in it (a wrong result, data loss, duplicates, a security hole, an outage, a
   broken rollout or rollback, or work that cannot succeed as written), each
   with one line of evidence. Include defects neither review found.
2. For each review, mark which listed defects it reports (1, 0.5 if partial,
   0) and record its verdict.
3. Count each review's INVALID findings and score its signal-to-noise 1-5.
