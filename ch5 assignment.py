import random

def main():
    play = 'y'
    while play == 'y':
        print('Guess the random number!')
        number = random.randint(1,100)
        guessing(number)
        play = input("Would you like to play again? y/n ")

def guessing(number):
    correct = "n"
    while correct == 'n':
        answer = int(input('What is your guess? '))
        if answer < number:
            print("Too low, try again!")            
        elif answer > number:
            print("Too high, try again!")
        else:
            correct = 'y'
            print("Correct!")

main()