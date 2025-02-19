import tkinter as tk
def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches is equal to {cm:.2f} centimeters")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
window = tk.Tk()
window.title("Height : Inches to Centimeters Converter")
window.geometry("300x200")
entry = tk.Entry(window, width=10)
entry.pack(pady=20)
convert_button = tk.Button(window, text="Convert", command=convert_to_cm)
convert_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()