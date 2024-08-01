def anagram(a,b):
    n=sorted(a)
    m=sorted(b)
    if(m==n):
        return "it is anagram"
    else:
        return "not anagram"
a=str(input("enter the a:"))
b=str(input("enter the b:"))
print(anagram(a,b))
