tel_num = input('Input a telephone number, using the format XXX-XXX-XXXX: ')

for ch in tel_num:
    if ch == 'A' or ch == 'B' or ch == 'C':
        tel_num = tel_num.replace(ch, '2')
    elif ch == 'D' or ch == 'E' or ch == 'F':
        tel_num = tel_num.replace(ch, '3')
    elif ch == 'G' or ch == 'H' or ch == 'I':
        tel_num = tel_num.replace(ch, '4')
    elif ch == 'J' or ch == 'K' or ch == 'L':
        tel_num = tel_num.replace(ch, '5')
    elif ch == 'M' or ch == 'N' or ch == 'O':
        tel_num = tel_num.replace(ch, '6')
    elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
        tel_num = tel_num.replace(ch, '7')
    elif ch == 'T' or ch == 'U' or ch == 'V':
        tel_num = tel_num.replace(ch, '8')
    elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'z':
        tel_num = tel_num.replace(ch, '9')

print ('The actual phone number is ' + tel_num)