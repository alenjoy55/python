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
l=[1,5,8,10,11]
s=0
for i in l:
    if i%2==0:
        print(i)
        s+=i
print("sum =",s)
"""8
  10
  sum=18"""



