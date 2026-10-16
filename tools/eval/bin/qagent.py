"""Read-only tool-using agent loop against an OpenAI-compatible endpoint.
Usage: qagent.py <run_dir> <prompt_file> <out_result_md> <out_transcript_json>
Tools are confined to run_dir. Final assistant text (without <think> blocks) goes to out_result_md."""
import json, os, re, sys, time, urllib.request, pathlib
URL = "http://192.168.1.63:8000/v1/chat/completions"
MODEL = os.environ.get("QMODEL", "qwen3.6-35b")
MAX_TOKENS = int(os.environ.get("QMAX", "32768"))
# Qwen3.6 model card, thinking mode for general tasks. At temperature 0.2 it looped until the
# token cap; presence_penalty is the card's remedy for endless repetition.
SAMPLING = {"temperature": 1.0, "top_p": 0.95, "top_k": 20, "min_p": 0.0, "presence_penalty": 1.5}
URL = os.environ.get("QURL", URL)
MAX_TURNS = 80
CAP = 25000
run_dir, prompt_file, out_md, out_tr = sys.argv[1:5]
root = pathlib.Path(run_dir).resolve()

def safe(p):
    t = (root / (p or ".")).resolve()
    if t != root and root not in t.parents:
        raise ValueError("path escapes project: " + p)
    return t

def list_dir(path="."):
    t = safe(path)
    if not t.is_dir():
        return "not a directory: " + path
    rows = []
    for c in sorted(t.iterdir()):
        if c.name == ".git":
            continue
        rows.append(c.name + ("/" if c.is_dir() else f"  ({c.stat().st_size} bytes)"))
    return "\n".join(rows[:400]) or "(empty)"

def read_file(path, offset=1, limit=2000):
    t = safe(path)
    if not t.is_file():
        return "not a file: " + path
    lines = t.read_text(encoding="utf-8", errors="replace").splitlines()
    start = max(int(offset) - 1, 0)
    chunk = lines[start:start + int(limit)]
    out = "\n".join(f"{i + start + 1}\t{l}" for i, l in enumerate(chunk))
    if start + len(chunk) < len(lines):
        out += f"\n... ({len(lines) - start - len(chunk)} more lines; use offset)"
    return out

def grep(pattern, path="."):
    t = safe(path)
    rx = re.compile(pattern)
    hits = []
    files = [t] if t.is_file() else [p for p in t.rglob("*") if p.is_file() and ".git" not in p.parts]
    for f in files:
        r = f.resolve()
        if r != root and root not in r.parents:
            continue  # symlink pointing outside the project
        try:
            for i, l in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if rx.search(l):
                    hits.append(f"{f.relative_to(root)}:{i}: {l[:200]}")
                    if len(hits) >= 200:
                        return "\n".join(hits) + "\n(truncated at 200)"
        except Exception:
            pass
    return "\n".join(hits) or "no matches"

TOOLS = [
    {"type": "function", "function": {"name": "list_dir", "description": "List a directory in the project (relative path).", "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": []}}},
    {"type": "function", "function": {"name": "read_file", "description": "Read a project file with line numbers. Use offset and limit for long files.", "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "offset": {"type": "integer"}, "limit": {"type": "integer"}}, "required": ["path"]}}},
    {"type": "function", "function": {"name": "git", "description": "Read-only git in the project: status, diff, log or show, with arguments, e.g. 'diff' or 'log --oneline -20'.", "parameters": {"type": "object", "properties": {"args": {"type": "string"}}, "required": []}}},
    {"type": "function", "function": {"name": "grep", "description": "Search project files for a regular expression. Returns file:line matches.", "parameters": {"type": "object", "properties": {"pattern": {"type": "string"}, "path": {"type": "string"}}, "required": ["pattern"]}}},
]
GIT_OK = {"status", "diff", "log", "show"}
GIT_BAD = ("--output", "--exec", "--git-dir", "--work-tree", "--ext-diff", "--textconv", "-c", "-C", "-o")

def git(args=""):
    import shlex, subprocess
    a = shlex.split(args or "status")
    if not a or a[0] not in GIT_OK or any(x.startswith(GIT_BAD) for x in a[1:]):
        return "allowed: git status | diff | log | show, with read-only options"
    try:
        out = subprocess.run(["git", "-C", str(root), "--no-pager", *a], capture_output=True, text=True,
                             timeout=30).stdout
    except Exception as e:
        return f"error: {e}"
    return out[:CAP] or "(no output)"

DISPATCH = {"list_dir": list_dir, "read_file": read_file, "grep": grep, "git": git}

SYSTEM = ("You are a coding agent working in a project directory. Inspect the project with the tools "
          "list_dir, read_file, grep and git (read-only). Paths are relative to the project root. When you have finished, "
          "reply with your final answer as plain text and make no further tool call.")

def call(messages):
    body = {"model": MODEL, "messages": messages, "tools": TOOLS, "tool_choice": "auto",
            "max_tokens": MAX_TOKENS, **SAMPLING}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=3600) as r:
        return json.load(r)

prompt = open(prompt_file, encoding="utf-8").read()
messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}]
transcript, calls, usage_in, usage_out, final = [], 0, 0, 0, ""
t0 = time.time()
for turn in range(MAX_TURNS):
    try:
        resp = call(messages)
    except Exception as e:
        final = f"(stopped: request failed on turn {turn}: {e!r})"
        print(final, flush=True)
        break
    u = resp.get("usage", {})
    usage_in += u.get("prompt_tokens", 0); usage_out += u.get("completion_tokens", 0)
    msg = resp["choices"][0]["message"]
    messages.append({k: v for k, v in msg.items() if v is not None})
    transcript.append({"turn": turn, "finish": resp["choices"][0]["finish_reason"], "message": msg})
    print(f"turn {turn} finish={resp['choices'][0]['finish_reason']} calls={calls} out_tokens={usage_out} "
          f"seconds={round(time.time() - t0)}", flush=True)
    json.dump({"partial": True, "transcript": transcript}, open(out_tr, "w", encoding="utf-8"))
    tcs = msg.get("tool_calls") or []
    if not tcs:
        final = msg.get("content") or ""
        break
    for tc in tcs:
        calls += 1
        name = tc["function"]["name"]
        try:
            args = json.loads(tc["function"].get("arguments") or "{}")
            result = DISPATCH[name](**args)
        except Exception as e:
            result = f"error: {e}"
        result = result[:CAP]
        transcript.append({"tool": name, "args": tc["function"].get("arguments"), "result_chars": len(result)})
        messages.append({"role": "tool", "tool_call_id": tc["id"], "content": result})
else:
    final = "(stopped: turn limit reached without a final answer)"

final = re.sub(r"<think>.*?</think>", "", final, flags=re.S).strip()
open(out_md, "w", encoding="utf-8").write(final + "\n")
json.dump({"tool_calls": calls, "turns": turn + 1, "prompt_tokens": usage_in, "completion_tokens": usage_out,
           "seconds": round(time.time() - t0), "transcript": transcript}, open(out_tr, "w", encoding="utf-8"), indent=1)
print(f"done: turns={turn + 1} tool_calls={calls} prompt_tokens={usage_in} completion_tokens={usage_out} seconds={round(time.time() - t0)} final_chars={len(final)}")
