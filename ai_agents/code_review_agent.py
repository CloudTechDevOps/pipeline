from agent_guard import fail_if_matches
from ai_provider import ask_ai

print("Running AI Code Review Agent...")

with open("app.py", "r", encoding="utf-8") as f:
    code = f.read()

prompt = f"""
Review this Flask website code.

Check:
- security issues
- coding standards
- performance problems
- deployment risks

Return this exact gate line:
PIPELINE_STATUS: PASS or FAIL

Use FAIL only for a critical/high-risk issue that should block deployment.

Code:
{code}
"""

response = ask_ai(prompt)

print(response)

blocking_patterns = [
    r"(?m)^pipeline_status\s*:\s*fail\b",
    r"risk level\s*:\s*(high|critical)",
    r"severity\s*:\s*(high|critical)",
    r"\bdeployment should not proceed\b",
    r"\bdo not deploy\b",
]

fail_if_matches("AI Code Review Agent", response, blocking_patterns)
