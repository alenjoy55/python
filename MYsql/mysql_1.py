import mysql.connector

con =mysql.connector.connect(host='localhost',user='alen11',password='alen',database='alendatas')
con.autocommit=True
cur =con.cursor()
# cur.execute('create database alendatas')
# cur.execute("create table std (roll_no int,name text,age int)")
# cur.execute("insert into std (roll_no,name,age) values(1,'albin',22)")

# roll=int(input("enter roll no: "))
# name=input("enter name: ")
# age=int(input("enter age: "))

# cur.execute('insert into std (roll_no,name,age) values(%s,%s,%s)',(roll,name,age))

# cur.execute("select * from std")
# data=cur.fetchall()
# for i in data:
#     print(i)

#update name
# name=input("enter new name: ")
# nname=input("enter old name: ")
# cur.execute("update std set name=%s where name=%s",(name,nname))

#delete 
# roll=int(input("enter roll no: "))
# cur.execute("delete from std where roll_no=%s ",(roll,))

#user input
# roll=int(input("enter roll no: "))
# data=cur.execute("select * from std where roll_no=%s",(roll,))
# print('_'*60)
# print('{:<10}{:<10}{:<10}'.format('roll','name','age'))
# print('_'*60)
# for i in cur:
#      print('{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2]))

