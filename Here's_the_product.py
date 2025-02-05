from tkinter import *
def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
root = Tk()
root.title("Product Calculator")
root.geometry("400x200")
label_num1 = Label(root, text="Enter first number:", bg="#3895D3")
label_num2 = Label(root, text="Enter second number:", bg="#3895D3")
entry_num1 = Entry(root)
entry_num2 = Entry(root)
calculate_button = Button(root, text="Calculate", command=calculate_product, bg="#1261A0")
result_label = Label(root, text="", bg="#3895D3")
label_num1.pack(pady=5)
entry_num1.pack(pady=5)
label_num2.pack(pady=5)
entry_num2.pack(pady=5)
calculate_button.pack(pady=10)
result_label.pack(pady=10)
root.mainloop()