# 🤖 AI Code Review Assistant

An intelligent AI-powered code review assistant that analyzes Python code and automatically detects issues such as PEP8 violations, missing documentation, bad naming conventions, and potential improvements.
The system also generates AI explanations for detected issues, helping developers understand and fix their code faster.

This project demonstrates the use of static code analysis + AI explanations to simulate a lightweight automated code reviewer.

## 🚀 Features

### 🔍 Automatic Code Analysis

Detects common Python issues using pylint

### 🧠 AI-powered Explanation

Explains detected issues in human-readable form

### 🧾 PEP8 Style Checking

Finds naming, formatting, and style problems

### ⚡ Local AI Support

Can run using local LLMs (Ollama) without OpenAI API

#### 🖥 CLI-based Tool

Run code reviews directly from terminal

## 🧠 Example Issues Detected

Example Python code:

a = 5
b = 10
print(a+b)

Output:

Issues Found:
Line 1 — Constant name "a" doesn't conform to UPPER_CASE naming style
Line 2 — Constant name "b" doesn't conform to UPPER_CASE naming style
Line 3 — Final newline missing

AI Explanation:

Variables declared as constants should be written in uppercase
according to PEP8 conventions. Rename 'a' to 'A' and 'b' to 'B'.

## 🛠 Tech Stack

Python

Pylint – Static code analysis

Ollama (Local LLM) – AI explanation generation

Requests – API communication

## 📂 Project Structure
```text
ai-code-review-assistant/
├── src/
│   ├── analyzer.py        # Runs pylint analysis
│   ├── ai_explainer.py    # Generates AI explanation
│   └── reviewer.py        # Combines analysis + AI explanation
├── examples/
│   └── bad_code.py        # Sample code for testing
├── requirements.txt
└── README.md
```


## ⚙️ Installation

### Clone the repository:

git clone https://github.com/OfficialTanishGupta/ai-code-review-assistant.git
cd ai-code-review-assistant

### Install dependencies:

pip install -r requirements.txt

### Install pylint:

pip install pylint

### (Optional) Install Ollama for local AI:

https://ollama.com

### Run a local model:
ollama run llama3

#### ▶️ Usage
Run the code reviewer:

python src/reviewer.py examples/bad_code.py

Output will show:

Detected issues

## AI explanation of the problems

Future Improvements
Web interface using Streamlit
Support for multiple languages (JavaScript, Java)

## 🔧 Auto code fix suggestions

🔗 GitHub Pull Request integration

📊 Code quality score

🎯 Learning Objectives

This project demonstrates:

Static code analysis

AI-assisted developer tools

Local LLM integration

Building developer productivity tools

## 👨‍💻 Author

Tanish Gupta

AI/ML Engineer | Robotics Enthusiast | Software Developer

GitHub:
https://github.com/OfficialTanishGupta
