num=[];
i=2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if(i%j==0):
            print(i,"不是质数,可以被",str(j),"整除")
    else:
        print(i,"是质数")
