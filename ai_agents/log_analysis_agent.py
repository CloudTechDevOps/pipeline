
import os
from ai_provider import ask_ai

print("📄 Running AI Log Analysis Agent...")

if not os.path.exists("output.log"):
    print("❌ output.log not found.")
    exit()

with open("output.log", "r") as f:
    logs = f.read()

prompt = f"""
Analyze Flask website logs.

Find:
- errors
- warnings
- crash reasons
- deployment issues

Logs:
{logs[-3000:]}
"""

response = ask_ai(prompt)

print(response)

