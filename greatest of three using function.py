def greatest(a,b,c):
 if (a>b):
    if (a>c):
        print("Greatest is", a)
    else:
        print("Greatest is", c)
 else:
    if (b>c):
        print("Greatest is", b)
    else:
        print("Greatest is", c)
a=10
b=20
c=30
greatest(a,b,c)
