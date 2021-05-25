# Average Height

"""
Formula to calculate average: Sum / Count
"""

student_heights = [180, 124, 165, 173, 189, 169, 146]

count = 0
total = 0

for height in student_heights:
    total += height
    count += 1

average = total / count

print(average)