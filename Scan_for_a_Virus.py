from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('200x200')
def msg():
    messagebox.showwarning("alert","This is a warning message")
Button = Button(root,text="Scan for a Virus",command=msg)   
Button.place(x=40,y=80)
root.mainloop()