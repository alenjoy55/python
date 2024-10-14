import tkinter

win=tkinter.Tk()
win.title("batch11")
win.maxsize(500,500)
win.minsize(300,300)
win.configure(bg="green")
    
def reg_form():
    win1=tkinter.Tk()
    win1.title("batch11")
    win1.maxsize(500,500)
    win1.minsize(300,300)
    win1.configure(bg="black")
    l1=tkinter.Label(win1,text="Login",bg="green",fg="white")
    l1.place(x=150,y=10)
    l2=tkinter.Label(win1,text="username",bg="green",fg="white")
    l2.place(x=80,y=40)
    el=tkinter.Entry(win1)
    el.place(x=200,y=40)
    l3=tkinter.Label(win1,text="password",bg="green",fg="white")
    l3.place(x=80,y=70)
    e2=tkinter.Entry(win1)
    e2.place(x=200,y=70)
    bl=tkinter.Button(win1,text="save",bg="white",activebackground="orange",fg="red",activeforeground="black",padx=10,pady=10)
    bl.place(x=150,y=100)
    b2=tkinter.Button(win1,text="register",bg="white",activebackground="orange",fg="red",activeforeground="black",padx=10,pady=10,command=save)
    b2.place(x=250,y=100)

    win1.mainloop()
def save():
    print(el.config(text=e2.get()))




l1=tkinter.Label(win,text="Login",bg="green",fg="white")
l1.place(x=150,y=10)
l2=tkinter.Label(win,text="username",bg="green",fg="white")
l2.place(x=80,y=40)
el=tkinter.Entry(win)
el.place(x=200,y=40)
l3=tkinter.Label(win,text="password",bg="green",fg="white")
l3.place(x=80,y=70)
e2=tkinter.Entry(win)
e2.place(x=200,y=70)
bl=tkinter.Button(win,text="save",bg="white",activebackground="orange",fg="red",activeforeground="black",padx=10,pady=10)
bl.place(x=150,y=100)
b2=tkinter.Button(win,text="register",bg="white",activebackground="orange",fg="red",activeforeground="black",padx=10,pady=10,command=reg_form)
b2.place(x=250,y=100)
win.mainloop()
