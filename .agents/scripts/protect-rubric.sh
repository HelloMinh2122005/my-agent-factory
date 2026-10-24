#!/usr/bin/env bash
# Antigravity PreToolUse hook to protect evaluation-rubric.md against automated tampering

python3 -c "
import sys, json

try:
    data = json.load(sys.stdin)
    tool_call = data.get('toolCall', {})
    args = tool_call.get('args', {})
    target_file = args.get('TargetFile', '')

    if 'evaluation-rubric.md' in target_file:
        res = {
            'decision': 'deny',
            'reason': 'Security Violation: evaluation-rubric.md is immutable. Automated agents are strictly prohibited from modifying the evaluation rubric.'
        }
    else:
        res = {
            'decision': 'allow'
        }
    print(json.dumps(res))
except Exception as e:
    # Fail-safe: allow if parsing error occurs
    print(json.dumps({'decision': 'allow'}))
"
