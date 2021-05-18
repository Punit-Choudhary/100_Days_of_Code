# Life in weeks

"""
https://waitbutwhy.com/2014/05/life-weeks.html

A program returns number of days,weeks and months
we have left if we live until 90 years old.
"""

age = int(input("What is your current age? "))

years_left = 90 - age

days = round(years_left * 365)
weeks = round(years_left * 52)
months = round(years_left * 12)

print(f"You have {days} days, {weeks} weeks and {months} months left.")