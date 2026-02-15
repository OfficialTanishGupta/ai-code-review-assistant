from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from pydantic import BaseModel
from app.analyzer import analyze_code

app = FastAPI(
    title="AI Code Review Assistant",
    description="Static analysis + local LLM powered code reviewer",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def home():
    return {"message": "AI Code Review Assistant Running"}


@app.post("/analyze")
def analyze(request: CodeRequest):
    result = analyze_code(request.code)
    return {"analysis": result}
