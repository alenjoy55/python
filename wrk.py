emp=[]

def login():
   uname=input("enter uname")
   passw=input("enter passw")
   f=0
   if uname=='alen' and passw=='joy':
      f=1
      return f
   
def add_emp():
   id=int(input("enter emp id"))
   f1=0
   for i in emp:
      if i['id']==id:
         f1=1
         print('id exits')
         add_emp()
   if f1==0:
    name=input("enter emp name")
    age=int(input("enter emp age"))
    salary=int(input("enter emp salary"))
    place=input("enter emp place")
    dob=input("date of birth")
    emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob})
    print(emp)

def update():
   id=int(input("enter emp id"))
   f1=0
   for i in emp:
      if i['id']==id:
         f1=1
         name=input("enter emp name")
         age=int(input("enter emp age"))
         salary=int(input("enter emp salary"))
         place=input("enter emp place")
         dob=input("date of birth")
         i['name']=name
         i['age']=age
         i['salary']=salary
         i['place']=place
         i['dob']=dob
   if f1==0:
      print("invalid id")
def delete():
   id=int(input("enter emp id"))
   f1=0
   for i in emp:
      if i['id']==id:
         f1=1
         emp.remove(i)        
   if f1==0:
      print("invalid id")
def display():
   print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id','name','age','salary','place','dob'))
   for i in emp:
            print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'], i['name'], i['age'],i['salary'],i['place'],i['dob']))
            
         
      
while True:
   print('''
         1.login
         2.exit
    ''') 
   ch=int(input("enter ur choice"))
   if ch==1:
      f=login()
      if f==1:
        while True:
           print('''
                 1.add emp
                 2.update
                 3.delete
                 4.display
                 5.logout
                 ''')
           sub_ch=int(input("enter ur choice"))
           if sub_ch==1:
              add_emp()
           elif sub_ch==2:
              update()
           elif sub_ch==3:
              delete()
           elif sub_ch==4:
              display()
           elif sub_ch==5:
              break    
      elif f==0:
        print("invalid uname or passw")
              
           

   