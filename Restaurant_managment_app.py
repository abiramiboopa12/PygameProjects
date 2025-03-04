from tkinter import *
from tkinter import ttk, messagebox
class Restaurant:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("600x500")
        self.menu_items = {
            "Pizza": 10, "Burger": 5, "Pasta": 8, "French Fries": 4,
            "Sandwich": 6, "Coke": 2, "Pepsi": 2, "Water": 1
        }
        self.exchange_rate = 82
        self.setup_ui()
    def setup_ui(self):
        title_label = ttk.Label(self.root, text="Restaurant Management App", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            ttk.Label(self.frame, text=f"{item} - ${price}", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
            quantity_var = IntVar(value=0)
            ttk.Entry(self.frame, textvariable=quantity_var, width=5).grid(row=i, column=1, padx=10)
            self.menu_quantities[item] = quantity_var
        self.total_label = ttk.Label(self.root, text="Total: $0", font=("Arial", 14, "bold"))
        self.total_label.pack(pady=10)
        self.calculate_button = ttk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack(pady=5)
        self.convert_button = ttk.Button(self.root, text="Convert to INR", command=self.convert_to_inr)
        self.convert_button.pack(pady=5)
    def calculate_total(self):
        total = sum(self.menu_items[item] * self.menu_quantities[item].get() for item in self.menu_items)
        self.total_label.config(text=f"Total: ${total}")
    def convert_to_inr(self):
        total_usd = sum(self.menu_items[item] * self.menu_quantities[item].get() for item in self.menu_items)
        total_inr = total_usd * self.exchange_rate
        messagebox.showinfo("Total in INR", f"Total Amount in INR: ₹{total_inr:.2f}")
if __name__ == "__main__":
    root = Tk()
    app = Restaurant(root)
    root.mainloop()