import tkinter as tk
from tkinter import messagebox
def red():
    root = tk.Tk()
    root.title("Red")
    root.geometry("600x400")
    root.configure(bg="red")
    label = tk.Label(root, text="This is Red", bg="red", fg="white")
    label.pack(pady=50)
    root.mainloop()
def pink():
    root = tk.Tk()
    root.title("Pink")
    root.geometry("600x400")
    root.configure(bg="pink")
    label = tk.Label(root, text="This is Pink", bg="pink", fg="black")
    label.pack(pady=50)
    root.mainloop()
def blue():
    root = tk.Tk()
    root.title("Blue")
    root.geometry("600x400")
    root.configure(bg="blue")
    label = tk.Label(root, text="This is Blue", bg="blue", fg="white")
    label.pack(pady=50)
    root.mainloop()
def green():
    root = tk.Tk()
    root.title("Green")
    root.geometry("600x400")
    root.configure(bg="green")
    label = tk.Label(root, text="This is Green", bg="green", fg="white")
    label.pack(pady=50)
    root.mainloop()
def none_of_the_above():
    root = tk.Tk()
    root.title("None of the Above")
    root.geometry("600x400")
    label = tk.Label(root, text="None of the Above")
    label.pack(pady=50)
    root.mainloop()
def main():
    def on_select(choice):
        root.destroy()
        if choice == "red":
            red()
        elif choice == "pink":
            pink()
        elif choice == "blue":
            blue()
        elif choice == "green":
            green()
        elif choice == "none_of_the_above":
            none_of_the_above()
        else:
            messagebox.showerror("Error", "Invalid choice")
    root = tk.Tk()
    root.title("Choose a colour")
    root.geometry("600x400")
    label = tk.Label(root, text="Choose a colour:")
    label.pack(pady=10)
    timer_button = tk.Button(root, text="Red", command=lambda: on_select("red"))
    timer_button.pack(pady=5)
    clock_button = tk.Button(root, text="Pink", command=lambda: on_select("pink"))
    clock_button.pack(pady=5)
    stopwatch_button = tk.Button(root, text="Blue", command=lambda: on_select("blue"))
    stopwatch_button.pack(pady=5)
    game_button = tk.Button(root, text="Green", command=lambda: on_select("green"))
    game_button.pack(pady=5)
    none_button = tk.Button(root, text="None of the Above", command=lambda: on_select("none_of_the_above"))
    none_button.pack(pady=5)
    root.mainloop()
if __name__ == "__main__":
    main()