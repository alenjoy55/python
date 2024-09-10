def number():
    num1=int(input('enter a number: '))
    num2=int(input('enter a number: '))
    return num1,num2
def add():
    num1,num2=number()
    print(num1+num2)
def sub():
    num1,num2=number()
    print(num1-num2)
def div():
    num1,num2=number()
    print(num1/num2)
def mul():
    num1,num2=number()
    print(num1*num2)
def mod():
    num1,num2=number()
    print(num1%num2)
while True:
    # a=int(input("enter a first no: "))
    # b=int(input("enter a second no: "))
    print('''1.addition
          2.subtraction
          3.division
          4.multiplication
          5.modulus
          6.exit''')
    choice=int(input("enter a choice: "))
    if choice==1:
        add()
        # sum=a+b
        # print(sum)
    elif choice==2:
        sub()
        # sub=a-b
        # print(sub)
    elif choice==3:
        div()
        # div=a/b
        # print(div)
    elif choice==4:
        mul()
        # mul=a*b
        # print(mul)
    elif choice==5:
        mod()
        # mod=a%b
        # print(mod)
    elif choice==6:
       break
    else:
        print("invalid choice: ")
        
