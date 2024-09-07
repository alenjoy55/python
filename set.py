# s=set()
#output
'''empty set'''

# s1={1,2,3,4,5,2}
# print(type(s1))
#output
'''{1, 2, 3, 4, 5}'''

# l=[1,2,3,2,3,4,4,5]
# s=set(l)
# l=list(s)
# print(l)
#output
'''[1, 2, 3, 4, 5]'''

# s={1,2,3,4,5}
# s1={1,2,3,}
# print(s.difference(s1))
# s.add(0)
# print(s)
# s.discard(3)
# print(s)
# s.remove(2)
# print(s)
# s.pop()
# print(s)
# s.update({6,7,8,9})
# print(s)
# print(s.intersection(s1))
# print(s.union(s1))
# print(s.isdisjoint(s1))
# print(s.issubset(s1))
# print(s.issuperset(s1))
# print(s.symmetric_difference(s1))

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.difference_update(s1)
# print(s)
# s.intersection_update(s1)
# print(s)
# s.symmetric_difference_update(s1)
# print(s)

#prgm
#limit
php=set()
l=int(input("enter a limit in php: "))
for i in range (l):
    name=input("enter a name: ")
    php.add(name)
print(php)
python=set()
l=int(input("enter a limit in python: "))
for i in range (l):
    name=input("enter a name: ")
    python.add(name)
print(python)
java=set()
l=int(input("enter a limit in java: "))
for i in range(l):
 name=input("enter a name: ")
 java.add(name)
print(java)

# a=php.intersection(python)
# a.intersection(java)
# print("common ",a)

# a=(python.difference(php))
# a.difference(java)
# print("python students: ",a)





