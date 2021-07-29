import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup


coin1 = Coin()

print('This side is up:', coin1.get_sideup())

coin1.toss()
print('This side is up:', coin1.get_sideup())