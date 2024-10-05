import sqlite3
a=sqlite3.connect('python/batch11.db')
try:
    a.execute("create table std(roll_no int,name text,age int,mark real)")
except:
    print("table exists")

# a.execute("insert into std(roll_no,name,age,mark)values(1,'alen',22,65),")
a.execute("insert into std(roll_no,name,age,mark)values(3,'ibin',24,80),")
a.commit()

