n1=1;
n2=100;
for i in range(n1,n2+1):
    if(i>1):
        count=0
        for j in range(1,i+1):
            if (i%j==0):
                count=count+1
        if(count==2):
            print(i)
