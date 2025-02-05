from tkinter import *
from datetime import date
root = Tk()
root.title("Getting Started with widgets")
root.geometry("400x300")
lbl = Label(root, text="Hey there", fg="white", bg="black")
name_label = Label(root, text="Full Name", bg="#3895D3")
name_entry = Entry(root)
def display():
    name = name_entry.get()
    Message = "Welcome to the Application! \nToday's date is:"
    greet = "Hello " + name + "!"
    text_box.insert(END, greet + "\n")
    text_box.insert(END, Message + "\n")
    text_box.insert(END, str(date.today()) + "\n")
text_box = Text(root, height=3)
btn = Button(root, text="Begin", command=display, height=1, bg="#1261A0")
lbl.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()