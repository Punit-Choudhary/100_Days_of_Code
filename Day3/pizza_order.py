# Pizza Order Program

"""
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""

size = input("Size of Pizza? ").lower()
pepperoni = input("Add Pepperoni? ").lower()
cheese = input("extra cheese? ").lower()

if size == 's':
    bill = 15
    pepperoni_price = 2
elif size == 'm':
    bill = 20
    pepperoni_price = 3
elif size == 'l':
    bill = 25
    pepperoni_price = 3
else:
    print(f"We don't have pizza of {size} size.")

if pepperoni == 'y':
    bill += pepperoni_price

if cheese == 'y':
    bill += 1

print(f"Your bill costs ${bill}")