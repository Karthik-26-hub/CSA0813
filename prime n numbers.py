n=9
m=100
count=0
for k in range(1,m):
 for i in range(1,n+1):
    if(n%i==0):
        count=count+1
 if(count==2):
        print("prime number")
 else:
        print("not prime number")
