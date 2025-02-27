import tkinter as tk
from tkinter import messagebox
def check_password_strength():
    password = password_entry.get()
    length = len(password)
    if length == 0:
        strength_label.config(text="Enter a password", fg="black")
    elif length < 6:
        strength_label.config(text="Weak", fg="red")
    elif 6 <= length < 12:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)
check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack()
root.mainloop()