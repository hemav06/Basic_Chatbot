import tkinter as tk

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

def send():
    user_msg = entry.get()
    if user_msg:
        chat_log.insert(tk.END, f"You: {user_msg}\n")
        bot_response = get_bot_response(user_msg)
        chat_log.insert(tk.END, f"Bot: {bot_response}\n\n")
        entry.delete(0, tk.END)

        # Delay exit to allow response to appear
        if user_msg.lower().strip() == "bye":
            send_button.config(state="disabled")  # optional: disable button
            entry.config(state="disabled")
            root.after(1500, root.quit)  # quit after 1.5 seconds

# Create GUI window
root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("400x500")

chat_log = tk.Text(root, height=20, width=50, font=("Arial", 12))
chat_log.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send)
send_button.pack(pady=5)

root.bind('<Return>', lambda event=None: send())

root.mainloop()
