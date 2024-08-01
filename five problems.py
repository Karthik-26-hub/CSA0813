#string to integer55
def integr(n):
    n=int(n)
    return n
a=str(input("enter the number: "))
print("integer: ",integr(a))

#removing duplicates
a=[1,2,3,2,1,4,5]
b=list(set(a))
print(b)

#average in list
a=[1,2,3,4,5]
b=sum(a)/5
print("average:",b)

#perfect square
def check(n):
    for i in range(1,n+1):
        if(i*i==n):
            print("perfect square")
            return
    print("not perfect squqre")
a=int(input("enter the number:"))
check(a)

#sum of even numbers
def check(n,sum):
    for i in n:
        if(i%2==0):
            sum=sum+i
    return sum
a=[1,2,3,4,5,6,7,8,9,10]
sum=0
print("sum: ",check(a,sum))
