from agent_guard import fail_if_matches
from ai_provider import ask_ai
import re

print("Running AI Code Review Agent...")

with open("app.py", "r", encoding="utf-8") as f:
    code = f.read()

prompt = f"""
You are a senior DevSecOps reviewer.

Review this Flask application code.

Check for:
- critical security vulnerabilities
- exposed secrets or credentials
- dangerous deployment risks
- remote code execution risks
- SQL injection
- command injection

IMPORTANT:
- Ignore low-risk recommendations
- Ignore coding style suggestions
- Ignore performance suggestions unless critical
- Ignore Flask dev server warnings unless debug=True exists
- Use FAIL only for real production-blocking issues

Return response in this format only:

PIPELINE_STATUS: PASS or FAIL

Risk Level: LOW/MEDIUM/HIGH/CRITICAL

Summary:
<short summary>

Issues:
- <issue>

Code:
{code}
"""

response = ask_ai(prompt)

print(response)

response_lower = response.lower()

# Hard blocking conditions
blocking_patterns = [
    r"(?m)^pipeline_status\s*:\s*fail\b",
    r"risk level\s*:\s*(high|critical)",
    r"severity\s*:\s*(high|critical)",
    r"\bdeployment should not proceed\b",
    r"\bdo not deploy\b",
    r"\bremote code execution\b",
    r"\bsql injection\b",
    r"\bcommand injection\b",
    r"\bhardcoded secret\b",
    r"\bexposed credential\b",
]

# Prevent false positives
safe_patterns = [
    r"debug=true",
]

# If AI says FAIL but no actual critical issue exists -> convert to PASS
critical_match = any(
    re.search(pattern, response_lower)
    for pattern in blocking_patterns
)

safe_match = any(
    re.search(pattern, code.lower())
    for pattern in safe_patterns
)

if critical_match and not safe_match:
    fail_if_matches(
        "AI Code Review Agent",
        response,
        blocking_patterns
    )
else:
    print("No blocking issues detected.")

