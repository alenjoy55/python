import sqlite3
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
    def reg():
        con=sqlite3.connect("python/Tkinter/sample.db")
        # con.execute("create table user(uname text,password text)")
        con.execute("insert into user(uname,password)values(?,?)",(el.get(),e2.get()))
        con.commit()
        win1.destroy()


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
    bl=tkinter.Button(win1,text="save",bg="white",activebackground="orange",fg="red",activeforeground="black",padx=10,pady=10,command=reg)
    bl.place(x=150,y=100)
    win1.mainloop()
def Home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win2,text='Home page')
    l1.pack()
    b1=tkinter.Button(win2,text="Logout",bg="black",fg="white",command=win2.quit)
    b1.pack()
    win2.maxsize(800,800)
    win2.minsize(500,500)
    win2.configure(bg="red",)
    win2.mainloop()

def login():
    con=sqlite3.connect("python/Tkinter/sample.db")
    data=con.execute("select * from user where uname=? and password=?",(el.get(),e2.get()))
    f=0
    for i in data:
        f=1
        Home()
    if f==0:
        l4.config(text="invalid username or password")


def save():
    print("username",el.get())
    l2.config(text=el.get())
    print("password",e2.get())
    l3.config(text=e2.get())




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
bl=tkinter.Button(win,text="Login",bg="white",activebackground="orange",fg="red",activeforeground="black",padx=10,pady=10,command=login)
bl.place(x=150,y=100)
b2=tkinter.Button(win,text="register",bg="white",activebackground="orange",fg="red",activeforeground="black",padx=10,pady=10,command=reg_form)
b2.place(x=250,y=100)
l4=tkinter.Label(win)
l4.place(x=150,y=30)
win.mainloop()
