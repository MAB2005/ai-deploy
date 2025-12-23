from fastapi import FastAPI
from backend.ai_engine import ask_ai
app=FastAPI()
@app.get("/ask")
def ask(q:str):
    return {"reply":ask_ai(q)}
