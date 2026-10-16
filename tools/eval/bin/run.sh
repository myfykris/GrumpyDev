#!/usr/bin/env bash
# Run one arm on one scenario.
# Usage: run.sh <work_dir> <scenario> <arm> <model> <rep>
#   model: sonnet | haiku | opus or a full id such as claude-sonnet-4-5 (claude CLI, needs a valid
#   login) or a local model id
#   (OpenAI-compatible endpoint in $QURL, default http://192.168.1.63:8000/v1/chat/completions).
# Writes <work_dir>/results/<run>.md and <work_dir>/usage/<run>.json (or .log for local models).
set -euo pipefail
bin="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
work="$1"; scen="$2"; arm="$3"; model="$4"; rep="$5"
mkdir -p "$work/results" "$work/usage" "$work/prompts"
work="$(cd "$work" && pwd)"
case "$model" in
  sonnet|haiku|opus|claude-*) ;;
  *) case "$scen" in impl|xs1)
       echo "$scen needs file writes; the local agent is read-only" >&2; exit 2 ;; esac ;;
esac
dir="$(python3 -I "$bin/mkruns.py" "$work" "$scen" "$arm" "$model" "$rep" "${@:6}")"
run="$(basename "$dir")"
python3 -I "$bin/prompt.py" "$dir" > "$work/prompts/$run.txt"
case "$model" in
  sonnet|haiku|opus|claude-*)
    tools="Read,Grep,Glob,Bash(git log:*),Bash(git show:*),Bash(git diff:*),Bash(git status:*),Bash(ls:*),Bash(wc:*),Write(.grumpydev/**),Edit(.grumpydev/**)"
    [ "$scen" = impl ] && tools="Read,Grep,Glob,Write,Edit,Bash(ls:*),Bash(php -l:*)"
    (cd "$dir" && claude -p "$(cat "$work/prompts/$run.txt")" --model "$model" --output-format json \
        --allowedTools "$tools") > "$work/usage/$run.json"
    python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1]))["result"])' "$work/usage/$run.json" \
        > "$work/results/$run.md" ;;
  *)
    QMODEL="$model" python3 -I "$bin/qagent.py" "$dir" "$work/prompts/$run.txt" "$work/results/$run.md" \
        "$work/usage/$run.json" > "$work/usage/$run.log" 2>&1 ;;
esac
echo "$run"
