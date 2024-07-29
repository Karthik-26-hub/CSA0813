a=int(input("enter the number:"))
count=0
n=2
while(count<a):
    dcount=0
    for i in range(1,n+1):
      if(n%i==0):
        dcount=dcount+1
    if(dcount==2):
      print(n)
      count+=1
    n+=1
