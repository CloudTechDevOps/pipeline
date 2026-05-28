import os
import re

from agent_guard import fail

print("Running Security Agent...")

secret_patterns = [
    r"(?i)\bpassword\b\s*[:=]\s*['\"][^'\"]{4,}['\"]",
    r"(?i)\bsecret\b\s*[:=]\s*['\"][^'\"]{8,}['\"]",
    r"(?i)\btoken\b\s*[:=]\s*['\"][^'\"]{8,}['\"]",
    r"(?i)\bapi[_-]?key\b\s*[:=]\s*['\"][^'\"]{8,}['\"]",
    r"(?i)\bmail\b\s*[:=]\s*['\"][^'\"]+@[^'\"]+['\"]",
    r"(?i)\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b",
]

scan_extensions = {".py", ".html", ".css", ".js", ".json", ".yml", ".yaml", ".env"}
skip_dirs = {".git", "__pycache__", ".venv", "venv", "node_modules"}
issues = []

for root, dirs, files in os.walk("."):
    dirs[:] = [directory for directory in dirs if directory not in skip_dirs]

    for file_name in files:
        _, extension = os.path.splitext(file_name)

        if extension not in scan_extensions:
            continue

        path = os.path.join(root, file_name)

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        for pattern in secret_patterns:
            if re.search(pattern, content):
                issues.append(path)
                break

if issues:
    print("Possible hard-coded secret value found in:")
    for path in sorted(set(issues)):
        print(f"- {path}")
    fail("Security Agent found blocking condition(s).")

print("Security scan passed.")
