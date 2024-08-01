import array
sum=0
l=[6,7,8,9,5]
a=array.array('i',[])
a.fromlist(l)
for i in a:
    sum=sum+i
print(sum)
