n=1221
sumofdigits = 0
while (n>0):
    digit=n%10  
    sumofdigits += digit 
    n=n//10 
print("The sum of the digits is: ",sumofdigits)
