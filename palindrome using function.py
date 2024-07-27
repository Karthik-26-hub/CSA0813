def palin(s,n):
 if(n==s):
  return "palindrome"
 else:
  return "not palindrome"
a='madam'
n=a[::-1]
print(n)
print("given string:",palin(a,n))
