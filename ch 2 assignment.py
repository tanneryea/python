desiredCookies = int(input('How many cookies do you want to make? '))
batchSize = desiredCookies / 48
sugar = batchSize * 1.5
butter = batchSize
flour = batchSize * 2.75
print ("You need", format(sugar, '.2f'), "cups of sugar,", format(butter, '.2f'), 
"cups of butter, and", format(flour, '.2f'), "cups of flour.")