from tkinter import *
root = Tk()
root.title("Number Card")
root.geometry("300x300")
nums = [[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    root.columnconfigure(i, weight=1 ,minsize=75)
    root.rowconfigure(i, weight=1 ,minsize=50)
for i in range(4):
    for j in range(3):
        frame = Frame(master=root, relief=RAISED, borderwidth=1, bg="green")
        frame.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
        label = Label(master=frame, text=nums[i][j], bg="green", fg="white", font = ("Arial", 10))
        label.pack(expand=True, fill="both",padx=5, pady=5)
root.mainloop()