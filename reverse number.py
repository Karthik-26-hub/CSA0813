n=12121
m=n
reverse=0
while(n!=0):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if(m==reverse):
 print("palindrome")
else:
 print("not palindrome")
