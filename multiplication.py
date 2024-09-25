f=open('python/multi.txt2','a')
no=int(input("enter a number: "))
# i=1
# for i in range(1,10+1):
#    c= print(i,'*',no,'=',i*no)
#    f.write(str(i)+'*'+'*'+str(no)+'='+str(i*no)+'\n')
for i in range(1,11):
    for j in range(1,no+1):
        f.write(str(i)+'*'+str(j)+'='+str(i*j)+'\t')
    f.write('\n')
   
   

    










