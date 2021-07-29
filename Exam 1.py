letter = input("Enter a captial letter to find its associated number. ")

if letter == "A" or letter == "B" or letter ==  "C":
    number = 2
elif letter == "D" or letter == "E" or letter == "F":
    number = 3
elif letter == "G" or letter == "H" or letter == "I":
    number = 4
elif letter == "J" or letter == "K" or letter == "L":
    number = 5
elif letter == "M" or letter == "N" or letter == "O":
    number = 6
elif letter == "P" or letter == "Q" or letter == "R" or letter == "S":
    number = 7
elif letter == "T" or letter == "U" or letter == "V":
    number = 8
else:
    number = 9

print("The letter", letter, "is associated with the number", number, "on the phone.")
