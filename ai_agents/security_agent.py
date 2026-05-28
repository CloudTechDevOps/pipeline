
import os

print("🔐 Running Security Agent...")

danger_keywords = [
    "password",
    "secret",
    "token",
    "api_key"
]

issues_found = False

for root, dirs, files in os.walk("."):

    for file in files:

        if file.endswith(".py"):

            path = os.path.join(root, file)

            with open(path, "r", errors="ignore") as f:

                content = f.read().lower()

                for keyword in danger_keywords:

                    if keyword in content:
                        print(f"⚠️ Possible secret in: {path}")
                        issues_found = True

if not issues_found:
    print("✅ Security scan passed.")

