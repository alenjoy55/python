import sqlite3
con=sqlite3.connect('python/database/emp.db')
try:
    con.execute("create table employee(id int,name text,position text,salary int)")
except:
    print("table exists")

while True:
    print('''
        1.add emp
        2.view emp
        3.update emp
        4.search emp
        5.delete emp
        6.exit
    ''')
    choice=int(input("enter your choice: "))
    if choice==1:
        id=int(input("enter id: "))
        name=input("enter name: ")
        position=input("enter postition: ")
        salary=int(input("enter salary: "))
        con.execute("insert into employee(id,name,position,salary)")
        con.commit()


