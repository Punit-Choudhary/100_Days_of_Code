# Who's Paying

"""
A program that will select a random name from a list of names.
The selected person have to pay for everybody's food bill.

Important : Not allowed to use choice() function.
"""
import random

names = input("Enter names of people: ")
names_list = names.split(", ")

rnd_number = random.randint(0, len(names_list) - 1)
print(f"{names_list[rnd_number]} is going to buy the meal today!")