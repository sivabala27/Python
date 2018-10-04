import random

class GuessNumber:
    def checkRandom(self,ran,userInput):
        if ran==userInput:
            print("It's correct!!!\nBye.")
            return True
        elif ran>userInput:
            print("You have entered a smaller number.")
            return False
        elif ran<userInput:
            print("You have entered a larger number.")
            return False
    def getInput(self):
        return int(input('Enter a number between 1 and 100:'))
print("Guess the random between 1 and 100")
ran = random.randint(1, 100)
count=1
chance=GuessNumber()
while(count<6):
    print("Attempt #",count)
    userInput =chance.getInput()
    if(chance.checkRandom(ran,userInput)==True):
        break
    elif count==5:
        print("The Number is :", ran, '\nTry Next time')
    count+=1

