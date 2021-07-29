import random


def compChoice():
    number = random.randint (1,4)
    return number

def userChoice():
    number = int(input('Make a selection: 1 for Red, 2 for Green, 3 for Blue or 4 for Orange. '))
    while number <= 0 or number >=5:
        print ('That is not an acceptable number.')
        number = int(input('Make a selection: 1 for Red, 2 for Green, 3 for Blue or 4 for Orange. '))
    return number

def colorValue(number):
    if number == 1:
        color = 'Red'
    elif number == 2:
        color = 'Green'
    elif number == 3:
        color = 'Blue'
    else:
        color = 'Orange'
    return color

def matchCheck(user, computer):
    userAnswer = colorValue(user)
    computerAnswer = colorValue(computer)
    print('You entered ', userAnswer, ', the computer selected ', computerAnswer, '.', sep='')
    if userAnswer == computerAnswer:
        print('You got a match!')
        return 1
    else:
        print('You did not get a match!')
        return 0

def main():
    total = 0
    for x in range (10):
        computer = compChoice()
        user = userChoice()
        result = matchCheck (user, computer)
        if result == 1:
            total += 1
        else:
            total += 0
    print('You guessed correctly', total, 'times.')

main()
