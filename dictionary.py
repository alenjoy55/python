# d={'name':'alen','age':22,'mark':20,}
# print(d)
# print(d['name'])
#output
'''{'name': 'alen', 'age': 22}
alen'''

#updation
# d['name']='akhil'
# print(d)
# d['place']='tsr'
# print(d)
#output
'''{'name': 'akhil', 'age': 22}
{'name': 'akhil', 'age': 22, 'place': 'tsr'}'''

#Duplicate value in dictionary
# d={'name':'alen','age':22,'mark':20,'age':23}
# print(d)
#output
'''{'name': 'alen', 'age': 23, 'mark': 20}'''

#dictionary in loop
# d={'name':'alen','age':22,'mark':20,}
# for i in d:
#     print(i)
#     print(d[i])
#     print(i,d[i])

#dictionary in membership operator
# if d['name']=='alen':
#     print('valid')
# else:
#     print('invalid')
#output
'''valid'''

# print(d.get('mark'))
#output 
'''20'''
# print(d.get('place'))
#output
'''none'''
# print(d.values())
#output
'''dict_values(['alen', 22, 20])'''
# print(d.keys())
#output
'''dict_keys(['name', 'age', 'mark'])'''
# print(d.items())
#output
'''dict_items([('name', 'alen'), ('age', 22), ('mark', 20)])'''
# d.pop('name')
# print(d)
#output
'''{'age': 22, 'mark': 20}'''
# d.popitem()
# print(d)
#output
'''{'name': 'alen', 'age': 22}'''
# d.update({'mark':56})
# print(d)
#output
'''{'name': 'alen', 'age': 22, 'mark': 56}'''
# d.clear()
# print(d)
#output
'''{}'''
#fromkeys method
# d={}
# l=['name','age','place','mark']
# d=d.fromkeys(l)
# print(d)
#output
'''{'name': None, 'age': None, 'place': None, 'mark': None}'''
#setdefault method
# d={}
# d.setdefault('age')
# print(d)
#output
'''{'age': None}'''
#choice program
std=[]
while True:
    print("""
        1.add std
        2.view std
        3.udate std
        4.delete std
        5.search
        6.exit
""")