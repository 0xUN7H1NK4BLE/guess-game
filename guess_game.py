
import random
randomnumber=random.randint(1,100)
#print(randomnumber)
b=None
guesses=0
while (b!=randomnumber):
   b=int(input("please enter your guess number from 1 to 100: "))


   if int(randomnumber==b):
    print("finally, yours guess is right👏👏🌹")
    print(f"you gussed it right in {guesses} times")

   else:
    print('try again')
    if (randomnumber)>b:
       print("higher number please")
       guesses +=1
    elif (randomnumber<b):
     print("lower number please")
    guesses +=1

with open("hiscore.txt","r") as f:
   hiscore=int(f.read())

if (guesses<hiscore):
   print("you have just broken the high score!👍👍👌✨")
   with open("hiscore.txt","w") as f:
      f.write(str(guesses))