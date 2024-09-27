
# class Bank:
#     def __init__(a,min):
#         a.balance=min
#     def deposit(b,amount):
#         b.balance+=amount
#         print('amount added..... ',amount)
#     def withdraw(self,amount):
#         self.balance-=amount
#         print('withdraw.....',amount)
#     def display(self):
#         print('display',self.balance)

# user=Bank(400)
# user.deposit(1000)
# user.withdraw(500)
# user.display()
# user.deposit(7000)
# user.display()

#positional argument
# class Demo:
#     def __init__(self,a):
#         print(a)
# ob=Demo(30)

# class arg:
#     def __init__(self,name,age):
#         print(name,age)

# obj=arg('alen',20)

#keyword argument
# class arg:
#     def __init__(self,name,age):
#         print(name,age)

# obj=arg(name='alen',age=20)

#default argument
class Demo:
    def __init__(self,name,age):
        print(name,age)
obj=Demo('alen',22)