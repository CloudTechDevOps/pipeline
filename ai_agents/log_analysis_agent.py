import os

from agent_guard import fail, fail_if_matches
from ai_provider import ask_ai

print("Running AI Log Analysis Agent...")

if not os.path.exists("output.log"):
    fail("output.log not found.")

with open("output.log", "r", encoding="utf-8", errors="ignore") as f:
    logs = f.read()

log_blocking_patterns = [
    r"\btraceback\b",
    r"\bexception\b",
    r"\berror\b",
    r"\bfailed\b",
    r"\bcrash\b",
    r"\baddress already in use\b",
]

fail_if_matches("Runtime Log Gate", logs[-3000:], log_blocking_patterns)

prompt = f"""
Analyze Flask website logs.

Find:
- errors
- warnings
- crash reasons
- deployment issues

Return this exact gate line:
PIPELINE_STATUS: PASS or FAIL

Use FAIL only when logs show a real runtime/deployment failure.

Logs:
{logs[-3000:]}
"""

response = ask_ai(prompt)

print(response)

ai_blocking_patterns = [
    r"(?m)^pipeline_status\s*:\s*fail\b",
    r"\bdeployment should not proceed\b",
    r"\bdo not deploy\b",
]

fail_if_matches("AI Log Analysis Agent", response, ai_blocking_patterns)
