from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denominations Calculator")
root.geometry("500x500")
uplo = Image.open("mouse.png")
uplo = uplo.resize((500, 500), Image.ANTIALIAS)
image = ImageTk.PhotoImage(uplo)
label = Label(image=image)
lable.place(x=0, y=0)
lable2 = Label(root, text="Welcome to the denomination counter",bg = "olive green")
lable2.place(relx = 0.5, y=340 , anchor="center")
btn = Button(root, text="Let;'s get started ", command = Message ,bg = "olive green")
def message():
    mesgbox = messagebox.showinfo("Do youn want to calculate the denomination count")
    if mesgbox == "ok":
        topwin()
def topwin():
    top = Toplevel()
    top.title("Denomination Calcolator")
    top