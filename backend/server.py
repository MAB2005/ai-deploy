from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.ai_engine import ask_ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ask")
def ask(q: str):
    return {"reply": ask_ai(q)}
