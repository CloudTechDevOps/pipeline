from agent_guard import fail_if_matches
from ai_provider import ask_ai

print("Running Deployment Risk Agent...")

prompt = """
Analyze deployment risk for this Flask website.

Check:
- deployment stability
- dependency risks
- production risks
- downtime risks

Return:
- risk level
- PIPELINE_STATUS: PASS or FAIL
- recommendations

Use FAIL only when deployment should be blocked.
"""

response = ask_ai(prompt)

print(response)

blocking_patterns = [
    r"(?m)^pipeline_status\s*:\s*fail\b",
    r"risk level\s*:\s*high",
    r"risk level\s*:\s*critical",
    r"\bdowntime likely\b",
    r"\bdeployment should not proceed\b",
    r"\bdo not deploy\b",
    r"\brollback required\b",
]

fail_if_matches("Deployment Risk Agent", response, blocking_patterns)
