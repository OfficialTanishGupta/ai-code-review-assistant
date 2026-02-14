import subprocess
import tempfile
import json
import requests


def get_ai_explanation(code: str, issues: list):
    prompt = f"""
You are a senior software engineer.

Review the following Python code and detected issues.

Code:
{code}

Issues:
{issues}

Explain:
1. What is wrong
2. Why it matters
3. How to improve it

Be clear and beginner friendly.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        return f"AI explanation failed: {str(e)}"


def analyze_code(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
        temp.write(code.encode())
        temp.flush()

        # Use JSON output from pylint
        result = subprocess.run(
            ["pylint", temp.name, "-f", "json"],
            capture_output=True,
            text=True
        )

    try:
        pylint_output = json.loads(result.stdout)
    except:
        pylint_output = []

    issues = []

    for item in pylint_output:
        issues.append({
            "type": item.get("type"),
            "line": item.get("line"),
            "message": item.get("message")
        })

    # Calculate score separately
    score_result = subprocess.run(
        ["pylint", temp.name],
        capture_output=True,
        text=True
    )

    score = None
    import re
    match = re.search(r"rated at ([\d\.]+)/10", score_result.stdout)
    if match:
        score = float(match.group(1))

    ai_explanation = get_ai_explanation(code, issues)

    return {
        "score": score,
        "issues": issues,
        "ai_explanation": ai_explanation
    }
