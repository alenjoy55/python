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
        con.execute("insert into employee(id,name,position,salary)values(?,?,?,?)",(id,name,position,salary))
        con.commit()
    elif choice==2:
        data=con.execute("select * from employee")
        print('_'*60)
        print('{:<10}{:<10}{:<10}{:<10}'.format('emp id','name','position','salary'))
        print('_'*60)
        for i in data:
            print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    elif choice==3:
        while True:
            print('''
                1.update id
                2.update name
                3.update position
                4.update salary
            ''')
            sub_ch=int(input("enter choice"))
            # if sub_ch==1:

            # elif sub_ch==2:
            #     name=input("target name: ")
            #     nname=input("enter new name: ")
            #     con.execute("update ")