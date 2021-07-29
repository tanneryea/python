import random

total = 0
numTotal = 0

oFile = open('random.txt', 'w')
iFile = open('random.txt', 'r')

amount = int(input('How many numbers do you want to generate? '))

for x in range(amount):
    oFile.write(str(random.randint(1,500)) + '\n')

oFile.close()

line = iFile.readline()

while line != '':
    result = int(line)
    print(result)
    total += result
    numTotal += 1
    line = iFile.readline()

print('The total of the numbers is', total)
print('You generated', numTotal, 'random numbers.')

iFile.close()
    
