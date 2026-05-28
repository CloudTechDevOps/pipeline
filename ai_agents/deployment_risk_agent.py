
from ai_provider import ask_ai

print("🧠 Running Deployment Risk Agent...")

prompt = """
Analyze deployment risk for this Flask website.

Check:
- deployment stability
- dependency risks
- production risks
- downtime risks

Return:
- risk level
- recommendations
"""

response = ask_ai(prompt)

print(response)

