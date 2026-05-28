
import re
from agent_guard import fail_if_matches
from ai_provider import ask_ai

print("Running AI Code Review Agent...")

with open("app.py", "r", encoding="utf-8") as f:
    code = f.read()

prompt = f"""
You are a DevSecOps reviewer.

IMPORTANT RULES:
- Only mark FAIL if a REAL, CONFIRMED, EXPLOITABLE vulnerability exists.
- Do NOT mark FAIL for mentions, examples, or explanations.
- Do NOT mark FAIL for generic security advice.

Return EXACT format:

PIPELINE_STATUS: PASS or FAIL
Risk: LOW/MEDIUM/HIGH/CRITICAL
Finding: <only if real issue exists else "NONE">

Code:
{code}
"""

response = ask_ai(prompt)
print(response)

# ONLY trust explicit FAIL line
strict_fail_pattern = r"(?m)^PIPELINE_STATUS:\s*FAIL\s*$"

if re.search(strict_fail_pattern, response):
    fail_if_matches("AI Code Review Agent", response, [strict_fail_pattern])
else:
    print("✅ Pipeline passed (no confirmed critical issues)")

