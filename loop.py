# i=1
# while i<=10:
#     print(i)
#     i+=1



# i=int(input("enter starting value : "))
# b=int(input("enter a ending value : "))
# while i<=b:
#     print(i)
#     i+=2


# a=1
# e=int(input("enter a limit : "))
# while a<=e:
#     print("alen")
#     a+=1


# i=int(input("enter starting value : "))
# e=int(input("enter ending value : "))
# sum=0
# while i<=e:
#     sum=sum+i
#     i+=1
# print("sum =",sum)

#even number print 

# i=int(input("enter starting value : "))
# e=int(input("enter ending value : "))
# while i<=e:
#     if i%2==0:
#         print(i)
#     i+=1

# odd numbers
# i=int(input("enter starting number : "))
# e=int(input("enter ending number : "))
# while i<=e:
#     if i%2!=0:
#         print(i)
#     i+=1

# sum of even numbers

# i=int(input("enter starting value :"))
# e=int(input("enter ending value : "))
# sum=0
# while i<=e:
#     if i%2==0:
#         sum=sum+i
#     i+=1
# print("sum of even =",sum)

# Sum of odd number
# i=int(input("enter starting value : "))
# e=int(input("enter ending values : "))
# sum=0
# while i<=e:
#     if i%2!=0:
#         sum=sum+i
#     i+=1
# print('sum of odd =',sum)

# Multiplication table
# p=int(input("enter multiplication"))
# i=1
# while i<=10:
#     print(i,'*',p,'=',i*p)
#     i+=1

#sum of numbers
# i=int(input("enter starting value : "))
# e=int(input("enter ending value : "))
# sum=0
# sum1=0
# sum2=0
# while i<=e:
#     sum=sum+i
#     if i%2==0:
#         sum1=sum1+i
#     else:
#          sum2=sum2+i
#     i+=1
#     print(sum)
#     print(sum1)
#     print(sum2)

#factorial number
# i=int(input("enter number : "))
# b=1
# f=1
# while b<=i:
#     f*=b
#     b+=1
# print(f)

#reverse number

# a=int(input("enter number : "))
# r=0
# while a>0:
#     d=a%10
#     r=r*10+d
#     a//=10
#     print('reverse = ',r)

#sum of digits 
# a=int(input("enter a number : "))
# r=0
# while a>0:
#     d=a%10
#     r=r+d
#     a//=10
# print('sum of digit = ',r)

#String
# a=input("enter a string : ")
# l=len(a)
# i=0
# while i<l:
#     print(a[i])
#     i+=1
    
#Reverse of string
a=input("enter a string : ")
l=len(a)
i=0
r=''
while i<l:
    r=a[i]+r
    i+=1
print(r)
