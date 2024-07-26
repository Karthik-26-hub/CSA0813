n=12234
reversen=0
while(n!=0):
    digit=n%10
    reversen=reversen*10+digit
    n=n//10
print(reversen)
