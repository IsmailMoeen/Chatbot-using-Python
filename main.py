import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import google.generativeai as genai

api_key = "AIzaSyAHWzSbwv3BnMiuH35anM5glMDpVGO_jDI"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def send_message(event=None):
    user_input = entry.get().strip()
    if user_input.lower() in ['bye', 'quit']:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"You: {user_input}\nChatbot: Goodbye!\n")
        chat_log.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        return
    if user_input:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"You: {user_input}\n")
        response_text = get_response(user_input)
        chat_log.insert(tk.END, f"Chatbot: {response_text}\n")
        chat_log.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        chat_log.yview(tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a message.")

root = tk.Tk()
root.title("Chatbot")

root.geometry("400x600")
root.configure(bg='black')
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg='#1e1e1e', fg='white', font=('Arial', 12), bd=0, insertbackground='white')
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
frame = tk.Frame(root, bg='black')
frame.pack(padx=10, pady=(0, 10), fill=tk.X)
entry = tk.Entry(frame, bg='#333', fg='white', font=('Arial', 12), bd=0, insertbackground='white')
entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
entry.bind("<Return>", send_message)  
send_button = tk.Button(frame, text="Send", command=send_message, bg='#007bff', fg='white', font=('Arial', 12), bd=0, relief=tk.FLAT)
send_button.pack(side=tk.RIGHT, padx=5)
def create_rounded_button(root, text, command, color, hover_color):
    canvas = tk.Canvas(root, width=80, height=30, bd=0, highlightthickness=0)
    canvas.create_oval(0, 0, 30, 30, fill=color, outline='')
    canvas.create_oval(50, 0, 80, 30, fill=color, outline='')
    canvas.create_rectangle(30, 0, 50, 30, fill=color, outline='')
    canvas.create_text(40, 15, text=text, fill='white', font=('Arial', 12))
    canvas.pack(side=tk.RIGHT, padx=5)
root.mainloop()
