rainfall = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

index = 0

for n in rainfall:
    print('Enter the rainfall for ', months[index], ':', sep='')
    rainfall[index] = float(input())
    while rainfall[index] < 0:
        print("Rainfall can't be negative. Enter a positive amount:")
        rainfall[index] = float(input())
    index += 1

month_max = rainfall.index(max(rainfall))
month_min = rainfall.index(min(rainfall))

print('The total rainfall for the year is', sum(rainfall))
print('The average monthly rainfall for the year is', sum(rainfall)/12)
print('The highest rainfall of the year was in', months[month_max])
print('The lowest rainfall of the year was in', months[month_min])

