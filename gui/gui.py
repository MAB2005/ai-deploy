import tkinter as tk
from backend.ai_engine import ask_ai
def send():
    q=e.get()
    e.delete(0,tk.END)
    t.insert(tk.END,"You: "+q+"\n")
    t.insert(tk.END,"AI: "+ask_ai(q)+"\n\n")
r=tk.Tk()
t=tk.Text(r);t.pack()
e=tk.Entry(r);e.pack()
tk.Button(r,text="Send",command=send).pack()
r.mainloop()
