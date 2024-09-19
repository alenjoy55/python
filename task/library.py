lb=[]
book=[]
def register():
        if len(lb)==0:
            id=101
        else:
            id=lb[-1]['id']+1
        email=input("enter your email: ")
        f=0
        for i in lb:
            if i['email_id']==email:
                f=1
                print("already existing!!!")
                register()
        if f==0:
            name=input("enter your name: ")
            place=input("enter your place: ")
            address=input("enter your address: ")
            mob=int(input("enter your mobile number: "))
            passw=input("set password: ")
            lb.append({'id':id,'name':name,'place':place,'address':address,'mob':mob,'email_id':email,'password':passw})
            print("registration successful!")
def login():
     uname=input("enter your username(email): ")
     passwrd=input("enter your password: ")
     f=0
     if uname=='admin' and passwrd=='admin':
          f=1
     user=''
     for i in lb:
         if uname==i['email_id'] and passwrd==i['password']:
              f=2
              user=i
     return f,user
def add():
    if len(book)==0:
          id=10
    else:
        id=book[-1]['b_id']+1
    bname=input("enter name of the book: ")
    stock=int(input("enter the book stock: "))
    price=int(input("enter the book price: "))
    book.append({'id':id,'book_name':bname,'stock':stock,'price':price})
def view_book():
     print('_'*40)
     print("{:<10}{:<15}{:<10}{:<10}")
     
     
while True:
    print('''
        1.register
        2.login
        3.exit
''')
    choice=int(input("enter your choice: "))
    if choice==1:
        register()
    elif choice==2:
         f,user=login()
         if f==1:
              while True:
                   print('''
                    1.add book
                    2.view book
                    3.update book
                    4.delete book
                    5.view users
                    ''')
                   sub_ch=int(input("enter your choice: "))
                   if sub_ch==1:
                        add()
                   elif sub_ch==2:
                        view_book()


         elif f==2:
                print("user login")
         else:
            print("invalid uname or password: ")
