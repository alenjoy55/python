# import sqlite3
# a=sqlite3.connect('python/database/batch11.db')
# try:
#     a.execute("create table std(roll_no int,name text,age int,mark real)")
# except:
#     print("table exists")

# a.execute("insert into std(roll_no,name,age,mark)values(1,'alen',22,65),")
# a.execute("insert into std(roll_no,name,age,mark)values(3,'ibin',24,80),")
# a.commit()

#single std data insertion
# roll=int(input("enter roll no: "))
# name=input("enter  name: ")
# age=int(input("enter age: "))
# mark=float(input("enter mark: "))
# a.execute("insert into std(roll_no,name,age,mark)values(?,?,?,?)",(roll,name,age,mark))
# a.commit()

#multiple std data insertion
# r=int(input("enter the limit: "))
# for i in range(r):
#     roll=int(input("enter roll_no: "))
#     name=input("enter name: ")
#     age=int(input("enter age: "))
#     mark=float(input("enter mark: "))
#     a.execute("insert into std(roll_no,name,age,mark)values(?,?,?,?)",(roll,name,age,mark))
#     a.commit()

    
# data=a.execute("select * from std")
# print('_'*50)
# print('{:<10}{:<10}{:<10}{:<10}'.format('roll','name','age','mark'))
# print('_'*50)
# for i in data:
#     print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))

#filteration database
# data=a.execute("select * from std where roll_no=10")
# for i in data:
#     print(i)

#userinput
# roll=int(input("enter a roll no: "))
# data=a.execute("select * from std where roll_no=?",(roll,))
# print('_'*50)
# print('{:<10}{:<10}{:<10}{:<10}'.format('roll','name','age','mark'))
# print('_'*50)
# for i in data:
#         print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))

#update name
# nname=input("enter new name: ")
# name=input("enter old name: ")
# a.execute("update std set name=? where name=?",(nname,name,))
# a.commit()

#delete 
# roll=int(input("enter a roll_no"))
# a.execute("delete from std where roll_no=?",(roll,))
# a.commit()