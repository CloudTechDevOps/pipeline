
from ai_provider import ask_ai

print("🤖 Running AI Code Review Agent...")

with open("app.py", "r") as f:
    code = f.read()

prompt = f"""
Review this Flask website code.

Check:
- security issues
- coding standards
- performance problems
- deployment risks

Code:
{code}
"""

response = ask_ai(prompt)

print(response)

