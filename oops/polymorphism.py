# class bank:
#     def __init__(self):
#         print('add bank dtls')
# class user(bank):
#     def __init__(self):
#         print('add user dtls')
        
# d=user()

# class school:
#     def notes(self):
#         print('school notes')
# class std(school):
#     def notes(self):
#         print('std notes')

# a=std()
# a.notes()

# class school:
#     def notes(self,*sub):
#         print('school notes',sub)
# class std(school):
#     def notes(self):
#         super().notes('python','jango')
#         print('std notes')
        

# s=std()
# s.notes()

class school:
    def notes(self,*sub):
        print('school notes',sub)
class std(school):
    def notes(self,*sub):
        super().notes(sub)
        print('std notes')

s=std()
s.notes('python','web','jango')
        

