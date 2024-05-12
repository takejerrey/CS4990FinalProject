import tkinter as tk
from tkinter import scrolledtext
import openai

API_KEY = 'MY_API_KEY_HERE'
openai.api_key = API_KEY
client = openai.OpenAI(api_key=API_KEY)
conversation = []

def send_message_to_ai():
  user_input = user_input_text.get("1.0", tk.END).strip()
  if user_input:
      try:
        
          conversation.append({"role": "user", "content": user_input})

    
          response = client.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=conversation
          )

         
          ai_text = response.choices[0].message.content
          conversation.append({"role": "assistant", "content": ai_text})

          
          display_conversation(ai_text)

          
          user_input_text.delete("1.0", tk.END)
      except Exception as e:
          
          display_conversation(f"Error: {str(e)}")
          user_input_text.delete("1.0", tk.END)

def display_conversation(text):
  conversation_history.config(state=tk.NORMAL)
  conversation_history.insert(tk.END, "AI: " + text + "\n\n")
  conversation_history.yview(tk.END)
  conversation_history.config(state=tk.DISABLED)

#Change this to whatever you want to set your campaign theme to
conversation.append({'role': 'system', 'content': 'You find yourself in a dark, mysterious forest. What will you do?'})


root = tk.Tk()
root.title("AI Dungeon Master")


input_frame = tk.Frame(root)
input_frame.pack(pady=20)


user_input_text = scrolledtext.ScrolledText(input_frame, height=3, width=50)
user_input_text.pack(side=tk.LEFT, padx=(0, 10))


send_button = tk.Button(input_frame, text="Send", command=send_message_to_ai)
send_button.pack(side=tk.RIGHT)


conversation_history = scrolledtext.ScrolledText(root, state=tk.DISABLED, height=35, width=100)
conversation_history.pack(padx=20, pady=(0, 20))


root.mainloop()
