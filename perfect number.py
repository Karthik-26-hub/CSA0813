n=int(input("enter the number:"))
factor=0
for i in range(1,n):
    if(n%i==0):
        factor+=i
if(n==factor):
    print("perfect number")
else:
    print("not perfect")
