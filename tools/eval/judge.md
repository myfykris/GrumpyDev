# Judge prompt (one judge per scenario packet; Opus; blind)

Build the packet first: `python3 -I tools/eval/bin/packet.py <work> <name> <run1,run2,...>`
(it shuffles, relabels R1..Rn, scrubs arm-identifying text, and writes the map to
`<work>/maps/`, which judges must not read).

```text
You are grading <N> reviews of the same work against an answer key. Work read-only.

Read:
- Answer key: tools/eval/keys/<key>.md
- Reviews: <work>/judge/<name>-packet.md (R1 to R<N>)
- The reviewed project, to check claims: a fresh build of the scenario
  (`tools/eval/bin/mkruns.py <tmp> <scenario> plain <model> 0`), including git history.
"The project notes" in some reviews is a doctrine file not in that project: <one-line summary>.
Do not read any other path under the work directory (not maps/, runs/ or results/).

Score each review strictly by the key: every key item 1, 0.5 or 0 with a short reason;
every penalty as a count with quotes; other findings as VALID-MATERIAL, VALID-MINOR and
INVALID (list INVALID ones with a reason); signal-to-noise 1-5 (5 = every line useful to
the owner). Real flaws the key did not anticipate are valid findings, not penalties.

Write JSON to <work>/judge/<name>-scores.json:
{"R1": {"<item>": n, ..., "reasons": {...}, "<penalty>": n, "<penalty>_quotes": [...],
 "valid_material": n, "valid_minor": n, "invalid": n, "invalid_list": [], "snr": n,
 "notes": "..."}, ...}
Then return a compact table.
```
