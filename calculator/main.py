
import add as add
from sub import sub
from multi import multi
from div import div
from mod import mod
import num

while True:
    print('''
        1.add
        2.sub
        3.multi
        4.div
        5.mod
        6.exit
    ''')
    choice=int(input("enter your choice: "))
    if choice==1:
        a,b=num.num()
        add.add(a,b)
    elif choice==2:
        a,b=num.num()
        sub(a,b)
    elif choice==3:
        a,b=num.num()
        multi(a,b)
    elif choice==4:
        a,b=num.num()
        div(a,b)
    elif choice==5:
        a,b=num.num()
        mod(a,b)
    elif choice==6:
        break
    else:
        print("invalid ")
        
