import random
import array
maxlen=12
digit=['0','1','2','3','4','5','6','7','8','9']
uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbol=['!','@','#','$','%','^','&','*','(',')','_','+',':','>','<','~','?','|',';','(',')',',','.','/','\',']
combinedlist=digit+uppercase+lowercase+symbol
randomdig=random.choice(digit)
randomlower=random.choice(lowercase)
randomupper=random.choice(uppercase)
randomsymbol=random.choice(symbol)
temp=randomdig+randomlower+randomupper+randomsymbol
for x in range(maxlen-4):
        temp=temp+random.choice(combinedlist)
        templist=array.array('u',temp)
        random.shuffle(templist)
password=""
for x in templist:
        password=password+x
print(password)
