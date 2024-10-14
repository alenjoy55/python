import tkinter

win=tkinter.Tk()
win.title("batch11")
win.maxsize(500,500)
win.minsize(300,300)
win.configure(bg="green")

def save():
    l2.config(text=el.get())
#Label
l1=tkinter.Label(win,text="welcome home page",bg="green",fg="white")
l1.pack()
#add textbox
el=tkinter.Entry(win,bg="black",fg="white")
el.pack()
#add button
bl=tkinter.Button(win,text="save",bg="white",activebackground="orange",fg="red",activeforeground="black",padx=5,pady=5,command=save)
bl.pack()
l2=tkinter.Label(win,bg="yellow",fg="black")
l2.pack()
win.mainloop()