from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
def message():
    mesgbox = messagebox.askquestion("Denomination Calculator", "Do you want to calculate the denomination count?")
    if mesgbox == "yes":
        topwin()
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.geometry("500x500")
    top.config(bg="olive green")
    Label(top, text="Enter the total amount", bg="olive green").place(x=180, y=50)
    entry = Entry(top)
    entry.place(x=180, y=80)
    Label(top, text="Here are the number of notes for each denomination:", bg="olive green").place(x=140, y=120)
    Label(top, text="2000 notes: ", bg="olive green").place(x=180, y=150)
    Label(top, text="500 notes: ", bg="olive green").place(x=180, y=180)
    Label(top, text="100 notes: ", bg="olive green").place(x=180, y=210)
    t1 = Entry(top)
    t1.place(x=270, y=150)
    t2 = Entry(top)
    t2.place(x=270, y=180)
    t3 = Entry(top)
    t3.place(x=270, y=210)
    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    Button(top, text="Calculate", command=calculator, bg="olive green").place(x=240, y=250)
root = Tk()
root.title("Denominations Calculator")
root.geometry("500x500")
uplo = Image.open("mouse.png")
uplo = uplo.resize((500, 500), Image.LANCZOS)
image = ImageTk.PhotoImage(uplo)
label = Label(root, image=image)
label.place(x=0, y=0)
Label(root, text="Welcome to the denomination counter", bg="olive green").place(relx=0.5, y=340, anchor="center")
Button(root, text="Let's get started", command=message, bg="olive green").place(relx=0.5, y=380, anchor="center")
root.mainloop()