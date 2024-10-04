import re
# a='9605118338'
# if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
#     print('vaild')
# else:
#     print('invalid')

a='alen292@gmail.com'
print(re.search('^[a-z].*@gmail.com$',a))