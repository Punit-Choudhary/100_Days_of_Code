# BMI Calculator 2.0

"""
BMI stands for Body Mass Index
Formula to calculate BMI : weight(kg) / height(m)^2

If BMI is:
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""

weight = int(input("Enter your weight in kg: "))
height_cm = int(input("Enter your height in cm: "))
height = height_cm / 100

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    interpretation = "are underweight."
elif bmi >= 18.5 and bmi < 25:
    interpretation = "have a normal weight."
elif bmi >= 25 and bmi < 30:
    interpretation = "are slightly overweight."
elif bmi >= 30 and bmi < 35:
    interpretation = "are obese."
else:
    interpretation = "are clinically obese."

print(f"Your bmi is {bmi}, and you {interpretation}")