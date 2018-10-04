import random


class DiceRolling:
    def rolldie(self):
        return random.randint(1, 6)


roll1 = DiceRolling()
while ('y' == input('Do you want to roll a dice? y/n :')):
    print(roll1.rolldie())
