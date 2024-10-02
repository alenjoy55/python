#SINGLE INHERITANCE
# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')
# class novavi(syn):
#     def web_dev(self):
#         print('web_dev')
#     def network(self):
#         print('network')

# # a=novavi()
# # a.network()
# # a.php()

# std=syn()
# std.python()

# class parent:
#     def shop(self):
#         print('shop')
#     def car(self):
#         print('car')
#     def phone(self):
#         print('phone')
# class child(parent):
#     def bike(self):
#         print('bike')

# a=parent()
# a.car()
# b=child()
# b.phone()
# b.bike()

#multiple inheritance
# class father:
#     def shop(self):
#         print('shop')
#     def car(self):
#         print('car')
# class mother:
#     def kitchen(self):
#         print('kitchen')
#     def dance(self):
#         print('dance')
# class chlid(father,mother):
#     def bike(self):
#         print('bike')

# a=father()
# a.shop()

# b=mother()
# b.dance()

# varun=chlid()
# varun.dance()
# varun.shop()
# varun.bike()

# class emp:
#     def emp_salary(self):
#         print('salary')
#     def emp_role(self):
#         print('job_role')
# class customer:
#     def cus_name(self):
#         print('cus_name')
#     def cus_mob(self):
#         print('cus_mob')
# class manager(emp,customer):
#     def manager_mob(self):
#         print('tour')
# arun=manager()
# arun.emp_salary()
# arun.cus_mob()

#multilevel inheritance
# class cu:
#     def exam_notification(self):
#         print('exam_notification')
#     def results(self):
#         print('results')
# class clg(cu):
#     def notes(self):
#         print('notes')
#     def class_room(self):
#         print('class_room')
#     def lib(self):
#         print('library')
# class student(clg):
#     def id_card(self):
#         print('id_card')
    
# amal=student()
# amal.exam_notification()
# amal.results()
# amal.notes()
# amal.id_card()

#hiearchial 
# class school:
#     def exam_not(self):
#         print('exam_not')
#     def result(self):
#         print('result')
# class class1(school):
#     def notes(self):
#         print('notes')
#     def subjects(self):
#         print('subjects')
# class class2(school):
#     def notes(self):
#         print('notes')
#     def subjects(self):
#         print('subjects')
# varun=class1()
# varun.exam_not()
# varun.result()
# varun.notes()
# varun.subjects()

# arun=class2()
# arun.exam_not()
# arun.result()
# arun.notes()
# arun.subjects()

#HYBRID INHERITANCE
# class synnefo:
#     def php(self):
#         print('php')
#     def python(self):
#         print('python')
#     def reg(self):
#         print('register')
# class teacher(synnefo):
#     def notes(self):
#         print('notes')
#     def attendence(self):
#         print('attendence')
# class nonteach(synnefo):
#     def enquiry(self):
#         print('enquiry')
#     def office(self):
#         print('office')
# class student(teacher):
#     def labs(self):
#         print('labs')
#     def exam(self):
#         print('exam')
#     def note_collection(self):
#         print('notes_collection')

# arun=student()
# arun.attendence()
# arun.exam()
# arun.note_collection()

# a=nonteach()
# a.enquiry()
# a.office()


# b=teacher()
# b.attendence()
# b.notes()
# b.python()

class clg():
    def m_tech(self):
        print('m_tech')
    def msc(self):
        print('msc')
    def reg(self):
        print('reg')
class mangement(clg):
    def exam_notifi(self):
        print('exam_notifi')
    def results(self):
        print('results')
class chairman(clg):
    def clg_profit(self):
        print('clg_profit')
    def staff_dtls(self):
        print('staff_details')
    def account_dtls(self):
        print('account_dtls')
class teacher(mangement):
    def notes(self):
        print('notes')
    def syllabus(self):
        print('syllabus')
    def attendence(self):
        print('attendence')
class non_teacher(mangement):
    def enquiry(self):
        print('enquiry')
    def admission_pro(self):
        print('addmission_pro')
class student(teacher):
    def notes_collection(self):
        print('notes_collection')
    def labs(self):
        print('labs')
    def identity_card(self):
        print('identity_card')

s=student()
s.reg()
s.m_tech()
s.attendence()
s.syllabus()
s.identity_card()
s.labs()
s.notes_collection()
s.exam_notifi()
s.results

a=teacher()
a.reg()
a.m_tech()
a.syllabus()
a.attendence()
a.exam_notifi()
a.results()

n=non_teacher()
n.enquiry()
n.admission_pro()

m=mangement()
m.exam_notifi()
m.results()

c=chairman()
c.account_dtls()
c.clg_profit()
c.staff_dtls()