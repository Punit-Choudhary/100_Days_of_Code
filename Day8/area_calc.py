# Area Calc

"""
You are painting a wall.
The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
Given a random height and width of wall,
calculate how many cans of paint you'll need to buy.

Formula to caclculate number of cans:
(wall_height x wall_width) / coverage per can

"""

import math

def paint_calc(height, width, coverage):
    number_of_cans = math.ceil((height * width) / coverage)
    print(f"You'll need {number_of_cans} cans of paint.")

wall_height = int(input("Enter Height of wall: "))
wall_width = int(input("Enter Width of wall: "))

coverage = 5

paint_calc(wall_height, wall_width, coverage)