from fastapi import FastAPI
from app.analyzer import analyze_code

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Code Review Assistant Running"}

@app.post("/analyze")
def analyze(code: str):
    result = analyze_code(code)
    return {"analysis": result}
