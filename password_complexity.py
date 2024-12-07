import re
import tkinter as tk
from tkinter import messagebox

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."
    return "Password is valid!"

def check_password():
    password = entry.get()
    result = validate_password(password)
    messagebox.showinfo("Validation Result", result)

#main application window
root = tk.Tk()
root.title("Password Validator")

# Create a label and entry for password input
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show='*', width=30)
entry.pack(pady=10)

#button
validate_button = tk.Button(root, text="Validate Password", command=check_password)
validate_button.pack(pady=20)

# Start GUI loop
root.mainloop()