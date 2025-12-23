import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages=[{"role":"system","content":"You are a highly intelligent assistant."}]
def ask_ai(t):
    messages.append({"role":"user","content":t})
    r=client.chat.completions.create(model="gpt-4.1-mini",messages=messages)
    a=r.choices[0].message.content
    messages.append({"role":"assistant","content":a})
    return a
