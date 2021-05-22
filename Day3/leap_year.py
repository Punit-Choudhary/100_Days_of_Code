# Leap year finder

"""
Program to find if given year is Leap or not!
"""

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap")
        else:
            print("Not Leap")
    else:
        print("Leap")
else:
    print("Not Leap")