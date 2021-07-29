num_list = []

def calculate(num_list):
    print('The numbers in the list are:')
    for value in num_list:
        print(value)
    total = 0
    for value in num_list:
        total += value
    minimum = min(num_list)
    maximum = max(num_list)
    print('The total of the list is', total)
    print('The average of the list is', total/len(num_list))
    print('The highest value is', maximum, 'and its index is', num_list.index(maximum))
    print('The lowest value is', minimum, 'and its index is', num_list.index(minimum)) 


def main():
    entry = 0
    while entry < 10:
        number = int(input('Enter a value: '))
        num_list.append(number)
        entry += 1
    calculate(num_list)

main()
