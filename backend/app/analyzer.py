import subprocess
import tempfile
import json
import requests
import re


# =====================================================
# AI EXPLANATION + IMPROVED CODE GENERATION
# =====================================================
def get_ai_explanation(code: str, issues: list):

    prompt = f"""
You are an expert senior software engineer.

Review the following Python code and detected issues.

CODE:
{code}

ISSUES:
{issues}

Provide:

1. Clear explanation of problems
2. Why they matter
3. A FULLY improved version of the code following best practices

Return STRICTLY in this format:

EXPLANATION:
...

IMPROVED_CODE:
# improved code here
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        return response.json().get("response", "")

    except Exception as e:
        return f"AI explanation failed: {str(e)}"


# =====================================================
# MAIN ANALYSIS FUNCTION
# =====================================================
def analyze_code(code: str):

    # Create temporary file for pylint
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
        temp.write(code.encode())
        temp.flush()
        temp_file = temp.name

    # ---------- Run pylint in JSON mode ----------
    result = subprocess.run(
        ["pylint", temp_file, "-f", "json"],
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

    # ---------- Extract pylint score ----------
    score_result = subprocess.run(
        ["pylint", temp_file],
        capture_output=True,
        text=True
    )

    score = None
    match = re.search(r"rated at ([\\d\\.]+)/10", score_result.stdout)

    if match:
        score = float(match.group(1))

    # ---------- AI explanation + improved code ----------
    ai_explanation = get_ai_explanation(code, issues)

    return {
        "score": score,
        "issues": issues,
        "ai_explanation": ai_explanation
    }
