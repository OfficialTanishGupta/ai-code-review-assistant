import { useState } from "react";
import Editor from "@monaco-editor/react";

function App() {
  const [code, setCode] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeCode = async () => {
    setLoading(true);

    const response = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code }),
    });

    const data = await response.json();
    setResult(data.analysis);

    setLoading(false);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>AI Code Review Assistant</h1>

      {/* 🧠 Monaco Editor */}
      <Editor
        height="400px"
        language="python"
        theme="vs-dark"
        value={code}
        onChange={(value) => setCode(value)}
      />

      <br />

      <button onClick={analyzeCode}>Analyze Code</button>

      {loading && <p>Analyzing code... ⏳</p>}

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
