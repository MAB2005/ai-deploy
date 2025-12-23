from backend.ai_engine import ask_ai
while True:
    q=input("You: ")
    if q=="exit":
        break
    print("AI:",ask_ai(q))
