#for loop syntax
# for iter_var in iterable

#sample programs
# for i in range(9):
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(1,100,1):
#     print(i)

#Sum of numbers

# start=int(input("starting value"))
# end=int(input("ending value"))
# sum=0
# for i in range(start,end):
#     sum+=i
# print(sum)

#sum of even numbers
# a=int(input("starting value : "))
# e=int(input("enter ending value : "))
# sum=0
# for i in range(sum,e+1):
#     if i%2==0:
#         print(i)
#         sum+=1
# print("sum of even no = ",sum)

#sum of odd numbers
# a=int(input("starting value : "))
# e=int(input("ending value : "))
# sum=0
# for i in range(sum,e+1):
#     if i%2!=0:
#         print(i)
#         sum+=1
# print("sum of odd no = ",sum)

#multiplication
# p=int(input("enter multiplication"))
# e=int(input("last value"))
# i=1
# for i in range(i,e+1,i+1):
#  print(i,'*',p,'=',i*p)

#sum of numbers
# f=int(input("enter first number : "))
# e=int(input("enter last number : "))
# i=0
# sum=0
# sum1=0
# sum2=0
# for i in range(f,e+1):
#     sum=sum+i
#     if i%2==0:
#         sum1=sum1+i
#     else:
#         sum2=sum2+i
#     i+=1
#     print("sum of numbers =",sum)
#     print("sum1 of numbers =",sum1)
#     print("sum2 of numbers =",sum2)

#Factorial number
# a=int(input("enter number : "))
# i=1
# f=1
# for i in range(i,a+1):
#     f*=i
# print("factorial of number : ",f)

#sum of digits
# a=int(input("enter a number : "))
# r=0
# for i in range(a):
#     a+=i
# print('sum of digits = ',r)

#string
# s=input("enter a string : ")
# for i in s:
#     print(i)

#Reverse of string
# s=input("enter a string : ")
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
