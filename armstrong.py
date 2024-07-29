n=int(input("enter the number:"))
armstrong=0
m=n
while(n!=0):
  r=n%10
  armstrong+=r**3
  n=n//10
if(armstrong==m):
    print("armstrong")
else:
    print("not armstrong")
