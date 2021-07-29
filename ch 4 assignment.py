factor = int(input("Enter the factorial you want to calculate: "))
total = 1
while factor <= 0:
    print('Number must be a nonnegative integer.')
    factor = int(input("Enter the factorial you want to calculate: "))
for x in range (1,factor+1):
    total *= x
print ("The result is", total)