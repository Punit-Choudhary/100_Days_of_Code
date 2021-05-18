# Tip Calculator project

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
partition = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
print(f"Each person should pay: ${(bill / partition) * (tip_percentage  + 100) / 100}")
