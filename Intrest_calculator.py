import tkinter as tk
from tkinter import messagebox
def calculate_simple_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        simple_interest = (p * t * r) / 100
        simple_interest_label.config(text=f"Simple Interest: {simple_interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
def calculate_compound_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        compound_interest = p * (1 + r / 100) ** t - p
        compound_interest_label.config(text=f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
root = tk.Tk()
root.title("Interest Calculator")
principal_label = tk.Label(root, text="Principal Amount:")
principal_label.grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)
time_label = tk.Label(root, text="Time Period (years):")
time_label.grid(row=1, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1)
rate_label = tk.Label(root, text="Rate of Interest (%):")
rate_label.grid(row=2, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1)
simple_interest_button = tk.Button(root, text="Calculate Simple Interest", command=calculate_simple_interest)
simple_interest_button.grid(row=3, column=0, columnspan=2)
compound_interest_button = tk.Button(root, text="Calculate Compound Interest", command=calculate_compound_interest)
compound_interest_button.grid(row=4, column=0, columnspan=2)
simple_interest_label = tk.Label(root, text="Simple Interest: ")
simple_interest_label.grid(row=5, column=0, columnspan=2)
compound_interest_label = tk.Label(root, text="Compound Interest: ")
compound_interest_label.grid(row=6, column=0, columnspan=2)
root.mainloop()
import tkinter as tk
from tkinter import messagebox
def calculate_simple_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        simple_interest = (p * t * r) / 100
        simple_interest_label.config(text=f"Simple Interest: {simple_interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
def calculate_compound_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        compound_interest = p * (1 + r / 100) ** t - p
        compound_interest_label.config(text=f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
root = tk.Tk()
root.title("Interest Calculator")
principal_label = tk.Label(root, text="Principal Amount:")
principal_label.grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)
time_label = tk.Label(root, text="Time Period (years):")
time_label.grid(row=1, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1)
rate_label = tk.Label(root, text="Rate of Interest (%):")
rate_label.grid(row=2, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1)
simple_interest_button = tk.Button(root, text="Calculate Simple Interest", command=calculate_simple_interest)
simple_interest_button.grid(row=3, column=0, columnspan=2)
compound_interest_button = tk.Button(root, text="Calculate Compound Interest", command=calculate_compound_interest)
compound_interest_button.grid(row=4, column=0, columnspan=2)
simple_interest_label = tk.Label(root, text="Simple Interest: ")
simple_interest_label.grid(row=5, column=0, columnspan=2)
compound_interest_label = tk.Label(root, text="Compound Interest: ")
compound_interest_label.grid(row=6, column=0, columnspan=2)
root.mainloop()