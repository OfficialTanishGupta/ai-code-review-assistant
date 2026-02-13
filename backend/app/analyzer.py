import subprocess
import tempfile

def analyze_code(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
        temp.write(code.encode())
        temp.flush()

        result = subprocess.run(
            ["pylint", temp.name],
            capture_output=True,
            text=True
        )

    return result.stdout
