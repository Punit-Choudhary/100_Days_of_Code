# BMI Calculator

"""
BMI stands for Body Mass Index
Formula to calculate BMI : weight(kg) / height(m)^2
"""

weight = int(input("Enter your weight in kg: "))
height_cm = int(input("Enter your height in cm: "))
height = height_cm / 100

bmi = round(weight / height ** 2, 2)

print("Your BMI is {}".format(bmi))