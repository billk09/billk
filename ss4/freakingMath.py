from random import *

a=randrange(10)
b=randrange(10)

correct = a + b
wrongNumber = [-1,0,1]
chosenNumber= choice(wrongNumber)

incorrect = correct + chosenNumber

print(a,"+",b,"=",incorrect)
userInput = input("True or False (T/F)")
if incorrect != correct :
    if userInput.lower()== 't':
        print("You lose")
    elif userInput.lower() == 'f':
        print("you wi")
else:
    if userInput.lower()== 't':
        print("You win")
    elif userInput.lower() == 'f':
        print("you lose")


#userInput = input("True or False (T/F):")

#if correct != incorrect:
  #  if userInput.lower()=="t":
    #    print("You lose")
  #  else:
        print('You win')#