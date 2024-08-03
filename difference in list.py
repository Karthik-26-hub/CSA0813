a=[1,2,3,4,5]
b=[3,4,5,6,7]
c=set(a)-set(b)
d=set(b)-set(a)
print("elements in a but not in b:",c)
print("elements in b but not in  a:",d)
