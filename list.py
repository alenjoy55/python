#Sample prgm
# l=[10,11,10,'abc',5.8]
# for i in l:
#     print(i)
"""10
   11
   10
   abc
   5.8"""

# l=[10,11,12,'abc',11]
# if 10 in l:
#     print('yes')
# else:
#     print('invalid')
"YES"

# l=[10,11,12,'abc',11]
# print(l[3])
#  """abc"""

# l=[10,11,12,'abc',11]
# print(l[2])
#12

#Adding methods
# l=[10,11,12,'abc',11]
# l.append('add')
# print(l)
# l.extend(['a','b','c'])
# print(l)
# l.insert(0,'hai')
# print(l)
"""[10, 11, 12, 'abc', 11, 'add']
[10, 11, 12, 'abc', 11, 'add', 'a', 'b', 'c']
['hai', 10, 11, 12, 'abc', 11, 'add', 'a', 'b', 'c']
"""
#Deleting method
# l=[10,11,12,'abc',11]
# l.clear()
"""[]"""
# l.pop()
"""10 11 12 abc"""
# l.pop(2)
"""10 11 12 11"""
# l.remove(10)
# print(l)
"""11 12 abc 11"""

# l=[2,3,4,5,7,8,9,10]
# l.sort()
# print(l)
# l.reverse()
# print(l)
"""[2,3,4,5,7,8,9,10]
   [10,9,8,7,5,4,3,2,1]"""
# l1=l.copy()
# l.pop(4)
# print(l)
# print(l1)
"""[2,3,4,5,7,8,9,10]
   [2,3,4,5,8,9,10]"""
# print(l.index(2))
"""0"""
# l=[1,5,8,10,11]
# s=0
# for i in l:
#     if i%2==0:
#         print(i)
#         s+=i
# print("sum =",s)
"""8
  10
  sum=18"""
#Reverse of string
# l=['alen','welcome','home']
# # for i in l:
# #     print(i[::-1])
"""nela
   emoclew
   emoh"""
# l=[1,10,5.8,'abc',2]
# s=0
# for i in l:
#     if (type(i))==int or type(i)==float:
#         s+=i
# print(s)
"""18.8"""
# l=[5,8,5,1,2,3,8,5]
# a=[]
# for i in l:
#     if i not in a:
#         a.append(i)
# print(a)
"""[5,8,1,2,3]"""

#limit 
# names=[]
# limit=int(input("enter a limit : "))
# for i in range(limit):
#     name=input("enter a names : ")
#     names.append(name)
# print(names)    
"""
enter a limit5
enter a names : alma
enter a names : sreehari
enter a names : deepak
enter a names : ibin
enter a names : alen
['alma,'sreehari','deepak','ibin','alen']
"""
# std=[]
# limit=int(input("enter a limit : "))
# for i in range(limit):
#     name=input("enter a name : ")
#     age=int(input("enter age : "))
#     mark=int(input("enter mark : "))
#     std.append([name,age,mark])
# print(std)
"""
enter a limit : 3
enter a name : deepak
enter age : 22
enter mark : 65
enter a name : ibin
enter age : 22
enter mark : 66
enter a name : alen
enter age : 22
enter mark : 67
[['deepak', 22, 65], ['ibin', 22, 66], ['alen', 22, 67]]
"""
#choice program
# std=[]
# while True:
#     print("""
#    1.add std
#    2.view std
#    3.udate std
#    4.delete std
#    5.search
#    6.exit
#  """)
#     choice=int(input("enter your choice : "))
#     if choice==1:
#         name=input("enter a name : ")
#         age=int(input("enter age : "))
#         mark=int(input("enter mark : "))
#         std.append([name,age,mark])
#     elif choice==2:
#         print('{:<10}{:<5}{:<5}'.format('name','age','mark'))
#         print('_'*5)
#         for i in std:
#             print('{:<10}{:<5}{:<5}'.format(i[0],i[1],i[2]))
#     elif choice==3:
#         name=input("enter name")
#         f=0
#         for i in std:
#             if i[0]==name:
#                 mark=int(input("enter a new mark"))
#                 i[2]=mark
#                 f=1
#         if f==0:
#          print("invalid name")
#     elif choice==4:
#         name=input("enter name")
#         f=0
#         for i in std:
#             if i[0]==name:
#                 std.remove(i)
#                 f=1
#         if f==0:
#          print('invaild name')
#     elif choice==5:
#         name=input("enter name")
#         f=0
#         for i in std:
#             if i[0]==name:
#                 print(i)
#                 f=1
#     elif choice==6:
#         break
#     else:
#         print("invalid choice")

                

        
#output
"""
enter your choice : 1
enter a name : alen
enter age : 22
enter mark : 65

   1.add std
   2.view std
   3.udate std
   4.delete std
 
enter your choice : 1
enter a name : deepak
enter age : 22
enter mark : 66

   1.add std
   2.view std
   3.udate std
   4.delete std
 
enter your choice : 2
name      age  mark 
__________
alen      22   65   
deepak    22   66   

   1.add std
   2.view std
   3.udate std
   4.delete std

   #deleting
   name      age  mark 
   _____
"""
#employee details choice
ems=[]
while True:
    print("""
   1.registration id
   2.view ems
   3.udate ems
   4.delete ems
   5.search
   6.add task
 """)
    choice=int(input("enter your choice : "))
    if choice==1:
        ems_name=input("enter a name : ")
        ems_id=int(input("enter age : "))
        age=int(input("enter mark : "))
        salary=int(input("enter salary : "))
        position=input("enter position : ")
        experience=int(input("enter experience : "))
        ems.append([ems_name,ems_id,age,salary,position,experience])
    elif choice==2:
       print('{:<10}{:<5}{:<5}'.format('name','id','age','salary','position','experience'))
       print('_'*5)
       for i in ems:
            print('{:<10}{:<5}{:<5}{:<5}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif choice==3:
        ems_name=input("enter the employee name : ")
        f=0
        for i in ems:
            if i[0]==ems_name:
                
        




    


