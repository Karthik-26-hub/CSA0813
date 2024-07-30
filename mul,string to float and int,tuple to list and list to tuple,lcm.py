#multiplication
def mul(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
a=int(input("enter the number: "))
mul(a)

#string to float
def flt(n):
    n=float(n)
    return n
b=str(input("enter the number: "))
print("float: ",flt(b))

#string to ineger
def integr(n):
    n=int(n)
    return n
c=str(input("enter the number: "))
print("integer: ",integr(c))

#list to tuple
def tupl(n):
    n=tuple(n)
    return n
d=["hello",12.1,100,"welcome"]
print("tuple: ",tupl(d))

#tuple to list
def lis(n):
    n=list(n)
    return n
d=("hello",12.1,100,"welcome")
print("list: ",lis(d))

#sum of digits
def sumn(n):
  total=0
  for i in range (1,n+1):
    total+=i
  return total
n=10
print(sumn(n))

#Lcm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return (a * b) // gcd(a, b)
a=12
b=15
print(f"The LCM of {a} and {b} is {lcm(a,b)}")
