a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=b**2-4*a*c
if(d==0):
 print("same and real roots")
elif(d>0):
 print("different real roots")
else:
 print("imaginary roots")
