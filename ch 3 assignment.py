weight = float(input("How much do you weigh in lbs? "))
height = float(input("How tall are you in inches? "))

BMI = weight * (703/height**2)

if BMI < 18.5:
    print("Your BMI is ", format(BMI, '.2f'),". You are underweight.", sep='')
elif BMI > 25:
    print("Your BMI is ", format(BMI, '.2f'),". You are overweight.", sep='')
else:
    print("Your BMI is ", format(BMI, '.2f'),". You are a healthy weight.", sep='')