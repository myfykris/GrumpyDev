"""Write each subagent's final report to <dir>/results/<run>.md and usage to <dir>/usage.tsv.
Reads the durable transcripts in ~/.claude/projects/<project>/<session>/subagents/.
Usage: collect.py <dir with agents.tsv> <subagents_dir>"""
import json, os, sys
D, S = sys.argv[1], sys.argv[2]
usage = []
for line in open(os.path.join(D, "agents.tsv")):
    if not line.strip():
        continue
    run, agent = line.rstrip("\n").split("\t")[:2]
    if agent == "ERROR":
        continue
    p = os.path.join(S, f"agent-{agent}.jsonl")
    last, tools, model, out_tok, first_ts, last_ts = None, 0, None, 0, None, None
    if not os.path.exists(p):
        print(run, "NO_TRANSCRIPT"); continue
    for l in open(p, encoding="utf-8"):
        try:
            d = json.loads(l)
        except Exception:
            continue
        ts = d.get("timestamp")
        if ts:
            first_ts = first_ts or ts; last_ts = ts
        m = d.get("message")
        if not isinstance(m, dict) or m.get("role") != "assistant" or not isinstance(m.get("content"), list):
            continue
        model = m.get("model") or model
        out_tok += (m.get("usage") or {}).get("output_tokens", 0)
        txt = "".join(b.get("text", "") for b in m["content"] if isinstance(b, dict) and b.get("type") == "text")
        for b in m["content"]:
            if isinstance(b, dict) and b.get("type") == "tool_use":
                tools += 1
                if "andback" in str(b.get("name", "")):
                    inp = b.get("input", {})
                    txt = next((inp[k] for k in ("report", "message", "text", "content", "result", "summary")
                                if isinstance(inp.get(k), str)), txt)
        if txt.strip():
            last = txt
    if last is None:
        print(run, "NO_TEXT"); continue
    os.makedirs(os.path.join(D, "results"), exist_ok=True)
    open(os.path.join(D, "results", run + ".md"), "w", encoding="utf-8").write(last)
    usage.append(f"{run}\t{model}\t{tools}\t{out_tok}\t{first_ts}\t{last_ts}\t{len(last)}")
    print(run, model, len(last), "chars,", tools, "tool calls")
with open(os.path.join(D, "usage.tsv"), "w") as f:
    f.write("run\tmodel\ttool_calls\toutput_tokens\tstart\tend\treport_chars\n" + "\n".join(usage) + "\n")
