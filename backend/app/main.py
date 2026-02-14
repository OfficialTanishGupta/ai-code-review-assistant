from fastapi import FastAPI
from pydantic import BaseModel
from app.analyzer import analyze_code

app = FastAPI()


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def home():
    return {"message": "AI Code Review Assistant Running"}


@app.post("/analyze")
def analyze(request: CodeRequest):
    result = analyze_code(request.code)
    return {"analysis": result}
