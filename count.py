f=open('python/alen.txt','r')
l=f.readlines()
f.seek(0)
letter=0
cap=0
small=0
word=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             letter+=1
# print(letter)


#To find cap and small letters:
# for i in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#         if i!=' ':
#             if i.isupper():
#                 cap+=1
#             letter+=1
# print('Total letters',letter)
# print('capital letters',cap)
# print('small letters',letter-cap)

#Count with word
# for i in range(len(l)):
#     a=f.readline().strip()
#     s=a.split()
#     for i in s:
#         if i!='':
#             word+=1
#     for i in a:
#         if i!=' ':
#             if i.isupper():
#                 cap+=1
#             letter+=1
# print('Total letters',letter)
# print('capital letters',cap)
# print('small letters',letter-cap)
# print('Total word',word)
# print('number of lines',len(l))




