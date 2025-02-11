from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry('100x100')
def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\nThe button was clicked!") 
Button = Button(window,text="Click your keys!")
Button.pack()
Button.bind("<Button-1>", handle_click)
window.mainloop()