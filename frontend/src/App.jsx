import { useState } from "react";

function App() {
  const [code, setCode] = useState("");
  const [result, setResult] = useState(null);

  const analyzeCode = async () => {
    const response = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code }),
    });

    const data = await response.json();
    setResult(data.analysis);
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>AI Code Review Assistant</h1>

      <textarea
        rows="12"
        cols="80"
        placeholder="Paste your Python code here..."
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />

      <br />
      <br />

      <button onClick={analyzeCode}>Analyze Code</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Score: {result.score}</h2>

          <h3>Issues:</h3>
          <ul>
            {result.issues.map((issue, index) => (
              <li key={index}>
                Line {issue.line} — {issue.message}
              </li>
            ))}
          </ul>

          <h3>AI Explanation:</h3>
          <pre>{result.ai_explanation}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
